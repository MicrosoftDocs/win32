---
title: Example Code for Creating a Container Object
description: The following code example creates two objects.
ms.assetid: bd9a8d62-c8e8-4ee5-86d8-bda5ddeb6e2c
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory , creating a container object
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Creating a Container Object

The following code example creates two objects. First, a container object and, second, a sub-container object. A value for the sub-container object is added to the [**otherWellKnownObjects**](/windows/desktop/ADSchema/a-otherwellknownobjects) property of the container object. The code example binds to the sub-container object using the WKGUID binding and displays its ADsPath. It then renames the sub-container object and binds again using the same WKGUID binding.


```C++
#define _WIN32_WINNT 0x0501

#include "resource.h"
#include <atlbase.h>
#include <atlcom.h>
#pragma comment(lib, "Activeds.lib")
#pragma comment(lib, "adsiid.Lib")
#include <atlenc.h>
#include <activeds.h>
#include <stdio.h>

void wmain( int argc, wchar_t *argv[ ])
        HRESULT hr = S_OK;
                CComPtr<IADs> pObject ;
                CComPtr<IADsContainer> pDomain ;
                IDispatch *pDisp = NULL;

                CComPtr<IADsContainer> pNewContainer ;
                CComPtr<IADs> pIADsObject, pNewObject,  pTestWKO1, pTestWKO2;

                CComVariant vartest, var;
                CComBSTR bstr, szNewContainerDN (MAX_PATH), 
                               szPath(MAX_PATH), 
                               szRelPath(MAX_PATH);
                // Names of the container and child object.
                CComBSTR szContainer ( L"MyWKOTestContainer"), 
                         szNewObject ( L"MyWKOTestObject"), 
                         szNewObjectRenameRDN ( L"cn=ObjectwithNEWNAME");


        // Get rootDSE and the domain container DN.
        hr = ADsGetObject(L"LDAP://rootDSE", IID_IADs, (void**)&pObject);
        if (FAILED(hr))
        {
                wprintf(L"Not Found. Cannot bind to the domain.\n");
                return hr;
        }

        hr = pObject->Get(CComBSTR(L"defaultNamingContext"),&var);
        if (SUCCEEDED(hr))
        {
    // Build the ADsPath to the domain.
    szPath = L"LDAP://";
    szPath.AppendBSTR(var.bstrVal);
    var.Clear();
    // Bind to the current domain.
    hr = ADsGetObject(szPath, IID_IADsContainer, (void**)&pDomain);
    if (SUCCEEDED(hr))
    {
      // Create the container.
      szRelPath = L"cn=";
      szRelPath += szContainer;
      hr = pDomain->Create(CComBSTR(L"container"), 
                              // ldapDisplayName of the class
                              // of the object to create.
                           szRelPath, // Relative path in RDN=value format.
                            &pDisp); // Return an IDispatch pointer to new object.
      if (SUCCEEDED(hr))
      {
        // Call the QueryInterface method for an IADs interface.
        hr = pDisp->QueryInterface(&pIADsObject);
                pDisp->Release();
        // Commit the new object to the directory.
        hr = pIADsObject->SetInfo();
        // Call the QueryInterface method for an IADsContainer interface.
        hr = pDisp->QueryInterface(&pNewContainer);
        if (SUCCEEDED(hr))
        {
          // Create the new container object in the container.
                  szRelPath = L"cn=";
          szRelPath += szNewObject;
                  hr = pNewContainer->Create(CComBSTR(L"container"), 
                                             szRelPath,
                                             &pDisp);
          if (SUCCEEDED(hr))
          {
            // Get the DN of the new container object.
            hr = pIADsObject->Get(CComBSTR(L"distinguishedName"), &var);
            if (SUCCEEDED(hr))
            {
              szNewContainerDN = var.bstrVal;
              var.Clear();
              wprintf(L"Created new container with DN: %s\n",szNewContainerDN);
              hr = pDisp->QueryInterface(&pNewObject);
                                pDisp->Release();
              if (SUCCEEDED(hr))
              {
                // Commit the new object to the directory.
                hr = pNewObject->SetInfo();
                // Get the DN for the new object.
                hr = pNewObject->Get(CComBSTR(L"distinguishedName"), &var);
                if (SUCCEEDED(hr))
                {
                  wprintf(L"Created new child object with DN: %s\n",var.bstrVal);
                  // Use LDAP API to set the otherWellKnownObjects property.
                  wprintf(L"Call AddValueToOtherWKOProperty with:\n");
                  wprintf(L"szContainer DN: %s\n",szNewContainerDN);


                  wprintf(L"pWKOGUID (bindable string format): %s\n",
                            MyWKOTestObjectGUID);
                  wprintf(L"szWKOObjectDN: %s\n",var.bstrVal);
                  hr = AddValueToOtherWKOProperty(
                          pNewObject, 
                          szNewContainerDN, // DN for container whose 
                                            // otherWellKnownObjects 
                                            // property to modify.
                          MyWKOTestObjectGUID, // WKO GUID for the well-known object
                          var.bstrVal // DN of the well-known object.
                                   );
                  wprintf(L"AddValueToOtherWKOProperty returned: %x\n",hr);
                  if (SUCCEEDED(hr))
                  {
                     // Bind using WKGUID binding.
                     // Build the ADsPath to the well-known object.
                     szPath = L"LDAP://<WKGUID=";
                     szPath += MyWKOTestObjectGUID;
                     szPath += L",";
                     szPath += szNewContainerDN;
                     szPath += L">";
                     wprintf(L"Bind with the following WKGUID binding string: %s\n",
                             szPath);
                     hr = ADsGetObject(szPath,IID_IADs, (void**)&pTestWKO1);
                     if (SUCCEEDED(hr))
                     {
                         hr = pTestWKO1->Get(CComBSTR(L"distinguishedName"),
                                                      &vartest);
                          if (SUCCEEDED(hr))
                          {
                              wprintf(L"Successfully bound to object. DN: %s\n",
                                      vartest.bstrVal);
                              vartest.Clear();
                          }
                      }
                      else
                          wprintf(L"Binding failed with hr: %x\n",hr);

                      // Bind again using the DN to get a regular ADsPath.
                      szPath = L"LDAP://";
                      szPath += var.bstrVal;
                      hr = ADsGetObject(szPath, IID_IADs, (void**)&pTestWKO1);
                      hr = pTestWKO1->get_ADsPath(&bstr);
                      // Rename the WKO object.
                      hr = pNewContainer->MoveHere(bstr, szNewObjectRenameRDN,NULL);
                      pTestWKO1.Release();
                      // Bind again using WKGUID binding.
                      // Build the ADsPath to the well-known object.
                      szPath = L"LDAP://<WKGUID=";
                      szPath += MyWKOTestObjectGUID;
                      szPath += L",";
                      szPath += szNewContainerDN;
                      szPath += L">";
                      wprintf( 
                       L"Bind AGAIN with the following WKGUID binding string: %s\n",
                       szPath
                      );
                      hr = ADsGetObject(szPath, IID_IADs, (void**)&pTestWKO2);
                      if (SUCCEEDED(hr))
                      {
                          hr = pTestWKO2->Get(CComBSTR(L"distinguishedName"),
                                              &vartest);
                          if (SUCCEEDED(hr))
                          {
                              wprintf(L"Successfully bound to object. ");
                              wprintf(L"Be aware that the DN reflects the rename.");
                              wprintf(L" DN: %s\n",vartest.bstrVal);
                              vartest.Clear();
                          }
                      }
                      else
                          wprintf(L"Binding failed with hr: %x\n",hr);
                  }

                }
              }
            }
          }
        }

        // Offer user the option to delete test containers.
        wprintf(L"Delete the test container and object (Y/N):");
                CComBSTR pszBuffer(MAX_PATH * 2);
        _getws_s(pszBuffer, MAX_PATH * 2);
        if (pszBuffer == L"Y" )
        {
            // Delete the object.
            // Delete the container.
            hr = pNewContainer->Delete(CComBSTR(L"container"), 
                                       szNewObjectRenameRDN);
            if (SUCCEEDED(hr))
            {
              wprintf(L"Test object successfully deleted.\n");
              szRelPath = L"cn=";
              szRelPath += szContainer;
              // Delete the container.
              hr = pDomain->Delete(CComBSTR(L"container"), szRelPath);
              if (SUCCEEDED(hr))
                wprintf(L"Test container and its contents successfully deleted.\n");
              else
                wprintf(L"Failed to delete test container. hr: %x\n",hr);
            }
            else
              wprintf(L"Failed to delete test container. hr: %x\n",hr);
        }
                hr = S_FALSE;

      }
    }
}

}


// converts hexadecimal string to a octet encoded byte 
array STDMETHODIMP ConvertHexGuidToArray(PCWSTR hexGuid, LPSAFEARRAY *sa) throw() {

        if (hexGuid == NULL) return E_INVALIDARG;

        int hexLen = (int)wcslen(hexGuid);
        HRESULT hr = S_OK;
        CTempBuffer<CHAR> sHex(hexLen);
        int loopLen = hexLen;
        // make ansi
        while(loopLen-- != 0)
                sHex[loopLen] = (CHAR) hexGuid[loopLen];
        SAFEARRAY *temp= SafeArrayCreateVector(VT_UI1, 0, hexLen / 2);
        if (temp == NULL)
                hr = E_OUTOFMEMORY;
        PBYTE dst ;
        if (hr == S_OK) hr = SafeArrayAccessData(temp, (void**)&dst);
        int dstLen = hexLen /2;
        if (hr == S_OK)
        {
                AtlHexDecode(sHex, hexLen, dst, &dstLen );
                hr = SafeArrayUnaccessData(temp);
                *sa = temp;
        }

        return hr;

}

HRESULT AddValueToOtherWKOProperty(IADs *pads, 
                                   LPOLESTR szContainerDN, 
                                     // DN for container 
                                     // whose otherWellKnownObjects 
                                     // property to modify.
                                   PCWSTR pWKOGUID, // WKO GUID for the WKO.
                                   BSTR szWKOObjectDN // DN of the WKO.
                                   )
{
        HRESULT hr = E_FAIL;

        CComPtr<IADsDNWithBinary> pdnWithBin;
        CComBSTR retGuid;
        pdnWithBin.CoCreateInstance(CLSID_DNWithBinary);

        CComVariant v;
        v.vt = VT_UI1 | VT_ARRAY;
        ConvertHexGuidToArray(pWKOGUID, &v.parray);
        hr = pdnWithBin->put_DNString(szWKOObjectDN);
        hr = pdnWithBin->put_BinaryValue(v);
        v.Clear();
        v.vt = VT_DISPATCH;
        pdnWithBin.QueryInterface(&v.pdispVal);

        SAFEARRAY *psa = SafeArrayCreateVector(VT_VARIANT, 0, 1);
        VARIANT *varray = (VARIANT*)psa->pvData;
        VariantCopy(&varray[0] ,&v);
        CComVariant v2;
        v2.vt = VT_VARIANT | VT_ARRAY;
        v2.parray = psa;
        hr = pads->PutEx(ADS_PROPERTY_APPEND, 
                         CComBSTR(L"otherWellKnownObjects"), 
                         v2);

        return hr;
}
```



 

 