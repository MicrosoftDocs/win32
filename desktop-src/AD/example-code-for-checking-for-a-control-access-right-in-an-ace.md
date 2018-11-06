---
title: Example Code for Checking for a Control Access Right in an ACE
description: The following C++ code example verifies a specified control access right in an ACE in the ACL of the specified object.
ms.assetid: 03a96c99-eefb-4de5-a4ab-526eca7875cc
ms.tgt_platform: multiple
keywords:
- Example Code for Checking for a Control Access Right in an ACE AD
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Checking for a Control Access Right in an ACE

The following C++ code example verifies a specified control access right in an ACE in the ACL of the specified object.


```C++
/***********************************************************

    ReadExtendedRight()

    DESCRIPTION: ReadExtendedRight verifies the specified control
    access right for the specified object. If an ACE with that control
    access right exists, it displays (using wprintf) the trustee and 
    ACE type for the control access right.
     
    FLOW: Get the security descriptor of an object, get the ACL, 
    enumerate the ACEs, check for control access rights ACEs,
    verify the specified right, and display the trustee and ACE
    type.

    The pszRightsGUID UNICODE string should be a string that
    contains the rightsGUID property value of the control access
    right and the string should have the same format as the COM
    Library function StringFromGUID2. 
    
    For example:
    LPCWSTR pszRightsGUID = L"{8186e976-4d8a-11d2-95dd-0000f875b660}";
    The pfExists parameter specifies a BOOL that will receive
    TRUE if an ACE with the specified right exists; otherwise, FALSE.
 
********************************************************************/

HRESULT ReadExtendedRight(IADs *pObject,
                          LPCWSTR pszRightsGUID,
                          BOOL *pfExists)
 
{
    if(!pObject || !pszRightsGUID)
    {
        return E_INVALIDARG;
    }
    
    HRESULT hr = E_FAIL;
    BOOL fExists = FALSE;
    CComVariant svar;
     
    // Get the nTSecurityDescriptor.
    hr = pObject->Get(CComBSTR("nTSecurityDescriptor"), &svar);
    if(SUCCEEDED(hr) && (VT_DISPATCH == svar.vt))
    {
      CComPtr<IADsSecurityDescriptor> spSD;
        
      // Call the QueryInterface method for the 
      // IADsSecurityDescriptor pointer.
      hr = svar.pdispVal->QueryInterface(IID_IADsSecurityDescriptor,
                                         (void**)&spSD);
        if (SUCCEEDED(hr))
        {
          CComPtr<IDispatch> spDisp;

          // Get the DACL.
          hr = spSD->get_DiscretionaryAcl(&spDisp);
          if (SUCCEEDED(hr))
          {
            CComPtr<IADsAccessControlList> spACL;

            // Call the QueryInterface method for the
            // IADsAccessControlList interface.
            hr = spDisp->QueryInterface(IID_IADsAccessControlList,
                                        (void**)&spACL);
            if (SUCCEEDED(hr))
            {
              CComPtr<IUnknown> spUnk;
              // Enumerate the ACEs in the ACL.
              hr = spACL->get__NewEnum(&spUnk);
              if (SUCCEEDED(hr))
              {
                CComPtr<IEnumVARIANT> spEnum;
                hr = spUnk->QueryInterface(IID_IEnumVARIANT,
                                           (void**) &spEnum);
                if (SUCCEEDED(hr))
                {
                   CComVariant svarACE;
                   ULONG lFetch;
                   hr = spEnum->Next(1, &svarACE, &lFetch);
                   // Loop to read all ACEs on the object.
                   while(S_OK == hr)
                   {
                     // Verify that 1 item is returned and 
                     // returned item is an IDispatch pointer.
                     if ((lFetch == 1) && 
                         (VT_DISPATCH == svarACE.vt))
                     {
                        CComPtr<IADsAccessControlEntry> spACE;
                        // Call the QueryInterface method for 
                        // IADsAccessControlEntry to use to 
                        // read the ACE.
                        hr = 
                          svarACE.pdispVal->QueryInterface(IID_IADsAccessControlEntry,
                                                           (void**)&spACE);
                        if (SUCCEEDED(hr))
                        {
                          long lAccessMask;
                          hr = spACE->get_AccessMask(&lAccessMask);
                          // Verify the control access 
                          // right flag as an ACE for
                          // a control access right.
                          if (lAccessMask & 
                              ADS_RIGHT_DS_CONTROL_ACCESS)
                          {
                            long lTypeFlag;
                            spACE->get_Flags(&lTypeFlag);
                            // Verify that this ACE 
                            // applies to an object.
                            if (lTypeFlag & 
                                ADS_FLAG_OBJECT_TYPE_PRESENT)
                            {
                               CComBSTR sbstrObjectType;
                               // Get the object type 
                               // GUID and print it.
                               spACE->get_ObjectType(&sbstrObjectType);
                               if ( _wcsicmp(sbstrObjectType,
                                             pszRightsGUID) == 0 )
                               {
                                 long lAceType;
                                 CComBSTR sbstrTrustee;
                                            
                                 fExists = TRUE;

                                 wprintf(L"\nObjectType: %S\n", 
                                         sbstrObjectType);

                                 spACE->get_AceType(&lAceType);
                                 if (lAceType == 
                                      ADS_ACETYPE_ACCESS_ALLOWED_OBJECT)
                                 {
                                    wprintf(L"ACE Type: ADS_ACETYPE_ACCESS_ALLOWED_OBJECT\n");
                                 }
                                 else if (lAceType == ADS_ACETYPE_ACCESS_DENIED_OBJECT)
                                 {
                                    wprintf(L"ACE Type: ADS_ACETYPE_ACCESS_DENIED_OBJECT\n");
                                 }

                                 // Get the trustee, who the 
                                 // right applies to, and print it.
                                 spACE->get_Trustee(&sbstrTrustee);
                                 wprintf(L"Trustee: %S\n", sbstrTrustee);
                               }
                             }
                           }
                         }
                       }

                       // Get the next ACE.
                       hr = spEnum->Next(1, &svarACE, &lFetch);
                     }// End of While loop.
                   }
                 }
               }
             }
        }
    }
    
    *pfExists = fExists;

    return hr;
}
```



 

 




