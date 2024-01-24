---
title: Registering the Property Page COM Object in a Display Specifier
description: This topic shows how to register an extension DLL that contains an Active Directory property sheet with the Windows registry and Active Directory.
ms.assetid: e2d6142b-c2fe-4435-b4af-83f7cd45218b
ms.tgt_platform: multiple
keywords:
- Registering the Property Page COM Object in a Display Specifier Active Directory
- property page COM object Active Directory , registering in a display specifier
- display specifiers Active Directory , registering the property page COM object in
ms.topic: article
ms.date: 05/31/2018
---

# Registering the Property Page COM Object in a Display Specifier

When you use COM to create a property sheet extension DLL for Active Directory Domain Services, you must also register the extension with the Windows registry and Active Directory Domain Services. Registering the extension enables the Active Directory administrative MMC snap-ins and the Windows shell to recognize the extension.

## Registering in the Windows Registry

Like all COM servers, a property sheet extension must be registered in the Windows registry. The extension is registered under the following key.

```
HKEY_CLASSES_ROOT
   CLSID
      <clsid>
```

*&lt;clsid&gt;* is the string representation of the CLSID as produced by the [**StringFromCLSID**](/windows/win32/api/combaseapi/nf-combaseapi-stringfromclsid) function. Under the *&lt;clsid&gt;* key, there is an **InProcServer32** key that identifies the object as a 32-bit in-proc server. Under the **InProcServer32** key, the location of the DLL is specified in the default value and the threading model is specified in the **ThreadingModel** value. All property sheet extensions must use the "Apartment" threading model.

## Registering with Active Directory Domain Services

Property sheet extension registration is specific to one locale. If the property sheet extension applies to all locales, it must be registered in the object class [**displaySpecifier**](/windows/desktop/ADSchema/c-displayspecifier) object in all of the locale subcontainers in the Display Specifiers container. If the property sheet extension is localized for a certain locale, register it in the **displaySpecifier** object in that locale subcontainer. For more information about the Display Specifiers container and locales, see [Display Specifiers](display-specifiers.md) and [DisplaySpecifiers Container](displayspecifiers-container.md).

There are three display specifier attributes that a property sheet extension can be registered under. These are [**adminPropertyPages**](/windows/desktop/ADSchema/a-adminpropertypages), [**shellPropertyPages**](/windows/desktop/ADSchema/a-shellpropertypages), and [**adminMultiselectPropertyPages**](/windows/desktop/ADSchema/a-adminmultiselectpropertypages).

The [**adminPropertyPages**](/windows/desktop/ADSchema/a-adminpropertypages) attribute identifies administrative property pages to display in Active Directory administrative snap-ins. The property page appears when the user views properties for objects of the appropriate class in one of the Active Directory administrative MMC snap-ins.

The [**shellPropertyPages**](/windows/desktop/ADSchema/a-shellpropertypages) attribute identifies end-user property pages to display in the Windows shell. The property page appears when the user views the properties for objects of the appropriate class in the Windows Explorer. Beginning with the Windows Server 2003 operating systems, the Windows shell no longer displays objects from Active Directory Domain Services.

The [**adminMultiselectPropertyPages**](/windows/desktop/ADSchema/a-adminmultiselectpropertypages) is only available on the Windows Server 2003 operating systems. The property page appears when the user views properties for more than one object of the appropriate class in one of the Active Directory administrative MMC snap-ins.

All of these attributes are multi-valued.

The values for the [**adminPropertyPages**](/windows/desktop/ADSchema/a-adminpropertypages) and [**shellPropertyPages**](/windows/desktop/ADSchema/a-shellpropertypages) attributes require the following format.


```C++
<order number>,<clsid>,<optional data>
```



The values for the [**adminMultiselectPropertyPages**](/windows/desktop/ADSchema/a-adminmultiselectpropertypages) attribute require the following format.


```C++
<order number>,<clsid>
```



The "&lt;order number&gt;" is an unsigned number that represents the page position in the sheet. When a property sheet is displayed, the values are sorted using a comparison of each value's "&lt;order number&gt;". If more than one value has the same "&lt;order number&gt;", those property page COM objects are loaded in the order they are read from the Active Directory server. If possible, you should use a non-existing "&lt;order number&gt;"; that is, one not used by other values in the property. There is no prescribed starting position, and gaps are allowed in the "&lt;order number&gt;" sequence.

The "&lt;clsid&gt;" is the string representation of the CLSID as produced by the [**StringFromCLSID**](/windows/win32/api/combaseapi/nf-combaseapi-stringfromclsid) function.

The "&lt;optional data&gt;" is a string value that is not required. This value can be retrieved by the property page COM object using the [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) pointer passed to its [**IShellExtInit::Initialize**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishellextinit-initialize) method. The property page COM object obtains this data by calling [**IDataObject::GetData**](/windows/win32/api/objidl/nf-objidl-idataobject-getdata) with the [**CFSTR\_DSPROPERTYPAGEINFO**](cfstr-dspropertypageinfo.md) clipboard format. This provides an **HGLOBAL** that contains a [**DSPROPERTYPAGEINFO**](/windows/desktop/api/Dsclient/ns-dsclient-dspropertypageinfo) structure The **DSPROPERTYPAGEINFO** structure contains a Unicode string that contains the "&lt;optional data&gt;". The "&lt;optional data&gt;" is not allowed with the [**adminMultiselectPropertyPages**](/windows/desktop/ADSchema/a-adminmultiselectpropertypages) attribute. The following C/C++ code example shows how to retrieve the "&lt;optional data&gt;".


```C++
fe.cfFormat = RegisterClipboardFormat(CFSTR_DSPROPERTYPAGEINFO);
fe.ptd = NULL;
fe.dwAspect = DVASPECT_CONTENT;
fe.lindex = -1;
fe.tymed = TYMED_HGLOBAL;
hr = pDataObj->GetData(&fe, &stm);
if(SUCCEEDED(hr))
{
    DSPROPERTYPAGEINFO *pPageInfo;
    
    pPageInfo = (DSPROPERTYPAGEINFO*)GlobalLock(stm.hGlobal);
    if(pPageInfo)
    {
        LPWSTR  pwszData;

        pwszData = (LPWSTR)((LPBYTE)pPageInfo + pPageInfo->offsetString);
        pwszData = NULL;
        
        GlobalUnlock(stm.hGlobal);
    }

    ReleaseStgMedium(&stm);
}
```



A property sheet extension can implement more than one property page; one possible use of the "&lt;optional data&gt;" is to name the pages to display. This provides the flexibility of choosing to implement multiple COM objects, one for each page, or a single COM object to handle multiple pages.

The following code example is an example value that can be used for the [**adminPropertyPages**](/windows/desktop/ADSchema/a-adminpropertypages), [**shellPropertyPages**](/windows/desktop/ADSchema/a-shellpropertypages), or [**adminMultiselectPropertyPages**](/windows/desktop/ADSchema/a-adminmultiselectpropertypages) attributes.


```C++
1,{6dfe6485-a212-11d0-bcd5-00c04fd8d5b6}
```



> [!IMPORTANT]
> For the Windows shell, display specifier data is retrieved at user logon, and cached for the user session. For administrative snap-ins, the display specifier data is retrieved when the snap-in is loaded, and is cached for the lifetime of the process. For the Windows shell, this indicates that changes to display specifiers take effect after a user logs off and then logs on again. For the administrative snap-ins, changes take effect when the snap-in or console file is loaded.

 

## Adding a Value to the Property Sheet Extension Attributes

The following procedure describes how to register a property sheet extension under one of the property sheet extension attributes.

**Registering a property sheet extension under one of the property sheet extension attributes**

1.  Ensure that the extension does not already exist in the attribute values.
2.  Add the new value at the end of the property page ordering list. That is set the "&lt;order number&gt;" portion of the attribute value to the next value after the highest existing order number.
3.  The [**IADs::PutEx**](/windows/desktop/api/iads/nf-iads-iads-putex) method is used to add the new value to the attribute. The *lnControlCode* parameter must be set to **ADS\_PROPERTY\_APPEND** so that the new value is appended to the existing values and does not, therefore, overwrite the existing values. The [**IADs::SetInfo**](/windows/desktop/api/iads/nf-iads-iads-setinfo) method must be called afterward to commit the change to the directory.

Be aware that the same property sheet extension can be registered for more than one object class.

The [**IADs::PutEx**](/windows/desktop/api/iads/nf-iads-iads-putex) method is used to add the new value to the attribute. The *lnControlCode* parameter must be set to **ADS\_PROPERTY\_APPEND**, so that the new value is appended to the existing values and does not, therefore, overwrite the existing values. The [**IADs::SetInfo**](/windows/desktop/api/iads/nf-iads-iads-setinfo) method must be called after to commit the change to the directory.

The following code example adds a property sheet extension to the group class in the computer's default locale. Be aware that the **AddPropertyPageToDisplaySpecifier** function verifies the property sheet extension CLSID in the existing values, gets the highest order number, and adds the value for the property page using [**IADs::PutEx**](/windows/desktop/api/iads/nf-iads-iads-putex) with the **ADS\_PROPERTY\_APPEND** control code.


```C++
//  Add msvcrt.dll to the project.
//  Add activeds.lib to the project.
//  Add adsiid.lib to the project.

#include "stdafx.h"
#include <wchar.h>
#include <objbase.h>
#include <activeds.h>
#include "atlbase.h"

HRESULT AddPropertyPageToDisplaySpecifier(LPOLESTR szClassName, //  ldapDisplayName of the class.
                                          CLSID *pPropPageCLSID //  CLSID of property page COM object.
                                         );

HRESULT BindToDisplaySpecifiersContainerByLocale(LCID *locale,
                                                 IADsContainer **ppDispSpecCont
                                                 );

HRESULT GetDisplaySpecifier(IADsContainer *pContainer, LPOLESTR szDispSpec, IADs **ppObject);

//  Entry point for the application.
void wmain(int argc, wchar_t *argv[ ])
{

    wprintf(L"This program adds a sample property page to the display specifier for group class in the local computer's default locale.\n");

    // Initialize COM.
    CoInitialize(NULL);
    HRESULT hr = S_OK;

    //  Class ID for the sample property page.
    LPOLESTR szCLSID = L"{D9FCE809-8A10-11d2-A7E7-00C04F79DC0F}";
    LPOLESTR szClass = L"group";
    CLSID clsid;
    //  Convert to GUID.
    hr = CLSIDFromString(
        szCLSID,  //  Pointer to the string representation of the CLSID.
        &clsid    //  Pointer to the CLSID.
        );

    hr = AddPropertyPageToDisplaySpecifier(szClass, //  ldapDisplayName of the class.
                                           &clsid //  CLSID of property page COM object.
                                          );
    if (S_OK == hr)
        wprintf(L"Property page registered successfully\n");
    else if (S_FALSE == hr)
        wprintf(L"Property page was not added because it was already registered.\n");
    else
        wprintf(L"Property page was not added. HR: %x.\n");

    //  Uninitialize COM.
    CoUninitialize();
    return;
}

//  Adds a property page to Active Directory admin snap-ins.
HRESULT AddPropertyPageToDisplaySpecifier(LPOLESTR szClassName, //  ldapDisplayName of class.
                                          CLSID *pPropPageCLSID //  CLSID of property page COM object.
                                         )
{
    HRESULT hr = E_FAIL;
    IADsContainer *pContainer = NULL;
    LPOLESTR szDispSpec = new OLECHAR[MAX_PATH];
    IADs *pObject = NULL;
    VARIANT var;
    CComBSTR sbstrProperty = L"adminPropertyPages";
    LCID locale = NULL;
    //  Get the display specifier container using default system locale.
    //  When adding a property page COM object, specify the locale
    //  because the registration is locale-specific.
    //  This means if you created a property page
    //  for German, explicitly add it to the 407 container,
    //  so that it will be used when a computer is running with locale
    //  set to German and not the locale set on the
    //  computer where this application is running.
    hr = BindToDisplaySpecifiersContainerByLocale(&locale,
                                                  &pContainer
                                                 );
    //  Handle fail case where dispspec object
    //  is not found and give option to create one.

    if (SUCCEEDED(hr))
    {
        //  Bind to display specifier object for the specified class.
        //  Build the display specifier name.
#ifdef _MBCS
        wcscpy_s(szDispSpec, szClassName);
        wcscat_s(szDispSpec, L"-Display");
        hr = GetDisplaySpecifier(pContainer, szDispSpec, &pObject);
#endif _MBCS#endif _MBCS
        if (SUCCEEDED(hr))
        {
            //  Convert GUID to string.
            LPOLESTR szDSGUID = new WCHAR [39];
            ::StringFromGUID2(*pPropPageCLSID, szDSGUID, 39); 

            //  Get the adminPropertyPages property.
            hr = pObject->GetEx(sbstrProperty, &var);
            if (SUCCEEDED(hr))
            {
                LONG lstart, lend;
                SAFEARRAY *sa = V_ARRAY(&var);
                VARIANT varItem;
                //  Get the lower and upper bound.
                hr = SafeArrayGetLBound(sa, 1, &lstart);
                if (SUCCEEDED(hr))
                {
                    hr = SafeArrayGetUBound(sa, 1, &lend);
                }
                if (SUCCEEDED(hr))
                {
                    //  Iterate the values to verify if the prop page CLSID
                    //  is already registered.
                    VariantInit(&varItem);
                    BOOL bExists = FALSE;
                    UINT uiLastItem = 0;
                    UINT uiTemp = 0;
                    INT iOffset = 0;
                    LPOLESTR szMainStr = new OLECHAR[MAX_PATH];
                    LPOLESTR szItem = new OLECHAR[MAX_PATH];
                    LPOLESTR szStr = NULL;
                    for (long idx=lstart; idx <= lend; idx++)
                    {
                        hr = SafeArrayGetElement(sa, &idx, &varItem);
                        if (SUCCEEDED(hr))
                        {
#ifdef _MBCS
                            //  Verify that the specified CLSID is already registered.
                            wcscpy_s(szMainStr,varItem.bstrVal);
                            if (wcsstr(szMainStr,szDSGUID))
                                bExists = TRUE;
                            //  Get the index which is the number before the first comma.
                            szStr = wcschr(szMainStr, ',');
                            iOffset = (int)(szStr - szMainStr);
                            wcsncpy_s(szItem, szMainStr, iOffset);
                            szItem[iOffset]=0L;
                            uiTemp = _wtoi(szItem);
                            if (uiTemp > uiLastItem)
                                uiLastItem = uiTemp;
                            VariantClear(&varItem);
#endif _MBCS
                        }
                    }
                    //  If the CLSID is not registered, add it.
                    if (!bExists)
                    {
                        //  Build the value to add.
                        LPOLESTR szValue = new OLECHAR[MAX_PATH];
                        //  Next index to add at end of list.
#ifdef _MBCS
                        uiLastItem++;
                        _itow_s(uiLastItem, szValue, 10);   
                        wcscat_s(szValue,L",");
                        //  Add the class ID for the property page.
                        wcscat_s(szValue,szDSGUID);
                        wprintf(L"Value to add: %s\n", szValue);
#endif _MBCS

                        VARIANT varAdd;
                        //  Only one value to add
                        LPOLESTR pszAddStr[1];
                        pszAddStr[0]=szValue;
                        ADsBuildVarArrayStr(pszAddStr, 1, &varAdd);

                        hr = pObject->PutEx(ADS_PROPERTY_APPEND, sbstrProperty, varAdd);
                        if (SUCCEEDED(hr))
                        {
                            //  Commit the change.
                            hr = pObject->SetInfo();
                        }
                    }
                    else
                        hr = S_FALSE;
                }
            }
            VariantClear(&var);
        }
        if (pObject)
            pObject->Release();
    }

    return hr;
}

//  This function returns a pointer to the display specifier container 
//  for the specified locale.
//  If locale is NULL, use the default system locale and then return the locale in the locale param.
HRESULT BindToDisplaySpecifiersContainerByLocale(LCID *locale,
                                                 IADsContainer **ppDispSpecCont
                                                )
{
    HRESULT hr = E_FAIL;

    if ((!ppDispSpecCont)||(!locale))
        return E_POINTER;

    //  If no locale is specified, use the default system locale.
    if (!(*locale))
    {
        *locale = GetSystemDefaultLCID();
        if (!(*locale))
            return E_FAIL;
    }

    //  Verify that it is a valid locale.
    if (!IsValidLocale(*locale, LCID_SUPPORTED))
        return E_INVALIDARG;

    LPOLESTR szPath = new OLECHAR[MAX_PATH*2];
    IADs *pObj = NULL;
    VARIANT var;

    hr = ADsOpenObject(L"LDAP://rootDSE",
                       NULL,
                       NULL,
                       ADS_SECURE_AUTHENTICATION, // Use Secure Authentication.
                       IID_IADs,
                       (void**)&pObj);

    if (SUCCEEDED(hr))
    {
        //  Get the DN to the config container.
        hr = pObj->Get(CComBSTR("configurationNamingContext"), &var);
        if (SUCCEEDED(hr))
        {
#ifdef _MBCS
            //  Build the string to bind to the DisplaySpecifiers container.
            swprintf_s(szPath,L"LDAP://cn=%x,cn=DisplaySpecifiers,%s", *locale, var.bstrVal);
            //  Bind to the DisplaySpecifiers container.
            *ppDispSpecCont = NULL;
            hr = ADsOpenObject(szPath,
                               NULL,
                               NULL,
                               ADS_SECURE_AUTHENTICATION, // Use Secure Authentication.
                               IID_IADsContainer,
                               (void**)ppDispSpecCont);
#endif _MBCS

            if(FAILED(hr))
            {
                if (*ppDispSpecCont)
                {
                    (*ppDispSpecCont)->Release();
                    (*ppDispSpecCont) = NULL;
                }
            }
        }
    }
    //   Cleanup.
    VariantClear(&var);
    if (pObj)
        pObj->Release();

    return hr;
}

HRESULT GetDisplaySpecifier(IADsContainer *pContainer, LPOLESTR szDispSpec, IADs **ppObject)
{
    HRESULT hr = E_FAIL;
    CComBSTR sbstrDSPath;
    IDispatch *pDisp = NULL;

    if (!pContainer)
    {
        hr = E_POINTER;
        return hr;
    }

    //  Verify other pointers.
    //  Initialize the output pointer.
    (*ppObject) = NULL;

    //  Build relative path to the display specifier object.
    sbstrDSPath = "CN=";
    sbstrDSPath += szDispSpec;

    //  Use child object binding with IADsContainer::GetObject.
    hr = pContainer->GetObject(CComBSTR("displaySpecifier"),
        sbstrDSPath,
        &pDisp);
    if (SUCCEEDED(hr))
    {
        hr = pDisp->QueryInterface(IID_IADs, (void**)ppObject);
        if (FAILED(hr))
        {
            //  Clean up.
            if (*ppObject)
                (*ppObject)->Release();
        }
    }

    if (pDisp)
        pDisp->Release();

    return hr;

}
```



 

 
