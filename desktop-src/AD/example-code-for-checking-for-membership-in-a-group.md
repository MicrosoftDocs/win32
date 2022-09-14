---
title: Example Code for Checking for Membership in a Group
description: The following code example verifies absolute membership of an object by recursively verifying that an object is a member of a group or any groups nested in that group.
ms.assetid: 4b6ef607-8d2e-4209-be61-498302749f7c
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory , checking for membership in a group
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Checking for Membership in a Group

The following code example verifies absolute membership of an object by recursively verifying that an object is a member of a group or any groups nested in that group.


```C++
/////////////////////////////////////////////////////////////////////
/*  RecursiveIsMember()         

    - Recursively scans the members of passed IADsGroup pointer
      and any groups that belong to the passed pointer - for 
      membership of Passed group.
      Returns TRUE if the member is found in the passed group,
      or if the passed member is a member of any group which is
      a member of the passed group.

    Parameters
 
        IADsGroup * pADsGroup       - Group from which to 
                                      verify members.
        LPWSTR      pwszMember      - LDAP path for object 
                                      to verify membership.
        BOOL        bVerbose        - IF TRUE, will output verbose 
                                      data for the scan.
 
    OPTIONAL Parameters
 
       LPOLESTR  pwszUser           - User Name and Password, if the 
                                      parameters are not passed, 
       LPOLESTER pwszPassword       - binding will use ADsGetObject; 
                                      if the parameters are specified, 
                                      ADsOpenObject is used, passing 
                                      user name and password.
*/
 
BOOL RecursiveIsMember(IADsGroup * pADsGroup,
                       LPWSTR pwszMemberGUID,
                       LPWSTR pwszMemberPath, 
                       BOOL bVerbose, 
                       LPOLESTR  pwszUser, 
                       LPOLESTR pwszPassword)
{
    HRESULT        hr                = S_OK;  // COM Result Code
    IADsMembers *  pADsMembers       = NULL;  // Pointer to Members 
                                              // of the IADsGroup
    BOOL           fContinue         = TRUE;  // Looping Variable
    IEnumVARIANT * pEnumVariant      = NULL;  // Pointer to the Enum
                                              //  variant
    IUnknown *     pUnknown          = NULL;  // IUnknown for getting
                                              // the ENUM initially
    VARIANT        VariantArray[FETCH_NUM];   // Variant array for temp
                                              // holding returned data
    ULONG          ulElementsFetched = NULL;  // Number of elements 
                                              // retrieved
    BSTR           bsGroupPath       = NULL;
    BOOL           bRet              = FALSE;

    if(!IADsGroup || !pwszMemberGUID || !pwszMemberPath)
    {
        return FALSE;
    }
 
    // Get the path of the object passed in
    hr = pADsGroup->get_ADsPath(&bsGroupPath);
 
    if (!SUCCEEDED(hr))
        return hr;
 
    if (bVerbose)
    {
        WCHAR pwszOutput[2048];
        swprintf_s(pwszOutput,
                 L"Checking the Group: %s\n\n for the member: %s\n\n",
                 bsGroupPath,
                 pwszMemberPath);
        PrintBanner(pwszOutput);
    }
 
    // Get an interface pointer to the IADsCollection of members
    hr = pADsGroup->Members(&pADsMembers);
 
    if (SUCCEEDED(hr))
    {
      // Query the IADsCollection of members for a new ENUM 
      // Interface. Be aware that the enum comes back as an 
      // IUnknown *
      hr = pADsMembers->get__NewEnum(&pUnknown);
 
      if (SUCCEEDED(hr))
      {
        // Call the QueryInterface method for the 
        // IUnknown * for an IEnumVARIANT interface.
        hr = pUnknown->QueryInterface(IID_IEnumVARIANT,
                                      (void **)&pEnumVariant);
 
        if (SUCCEEDED(hr))
        {
          // While no hit errors or end of data...
          while (fContinue) 
          {
             ulElementsFetched = 0;
             // Get a "batch" number of group members-number 
             // of rows specified by FETCH_NUM
             hr = ADsEnumerateNext(pEnumVariant, 
                                   FETCH_NUM,
                                   VariantArray,
                                   &ulElementsFetched);
 
             if (ulElementsFetched )
             {
               // Loop through the current batch,
               // printing the path for each member.
               for (ULONG i = 0; i < ulElementsFetched; i++ ) 
               {
                  // Pointer for holding dispatch of element:
                  IDispatch * pDispatch         = NULL; 
                  
                  // Holds path of object:
                  BSTR        bstrCurrentPath   = NULL; 

                  // Holds the GUID of object:
                  BSTR        bstrGuidCurrent   = NULL; 

                  // Holds the current object:
                  IDirectoryObject * pIDOCurrent = NULL;          
 
                  // Get the dispatch pointer for the variant
                  pDispatch = VariantArray[i].pdispVal;
                  assert(HAS_BIT_STYLE(VariantArray[i].vt,
                         VT_DISPATCH));
 
                  // Get the IADs interface for the
                  // "member" of this group
                  hr = pDispatch->QueryInterface(IID_IDirectoryObject,
                                                (VOID **) &pIDOCurrent);
 
                  if (SUCCEEDED(hr))
                  {
                    // Get the GUID for the current object
                    hr = GetObjectGuid(pIDOCurrent,bstrGuidCurrent);
 
                    if (FAILED(hr))
                        return hr;
 
                    IADs * pIADsCurrent = NULL;

                    // Get the IADs Interface for 
                    // the current object
                    hr = pIDOCurrent->QueryInterface(IID_IADs,
                                                     (void**)&pIADsCurrent);
                    if (FAILED(hr))
                         return hr;
 
                    // Get the ADsPath property for this member
                    hr = pIADsCurrent->get_ADsPath(&bstrCurrentPath);

                    if (SUCCEEDED(hr))
                    {
                      if (bVerbose)
                        wprintf(L"Comparing:\n%s\nWITH:\n%s\n\n",
                                bstrGuidCurrent,
                                pwszMemberGUID);
                                    
                      // Verify that the member of this group is 
                      // Equal to passed.
                      if (_wcsicmp(bstrGuidCurrent,
                                   pwszMemberGUID)==0)
                      {
                         if (bVerbose)
                             wprintf(L"Object: %s is a member of %s\n\n",
                                     pwszMemberPath,
                                     bstrGuidCurrent);   
 
                         bRet = TRUE;
                         break;
                       }
                       else // Otherwise, bind to this and
                            // verify that it is a group.
                       {    // If is it a group then the call to 
                            // the QueryInterface method to 
                            // IADsGroup succeeds.
                                        
                         IADsGroup * pIADsGroupAsMember = NULL;
                                        
                         if (pwszUser)
                           hr = ADsOpenObject(bstrCurrentPath,
                                              pwszUser, 
                                              pwszPassword, 
                                              ADS_SECURE_AUTHENTICATION,
                                              IID_IADsGroup, 
                                              (void**) &pIADsGroupAsMember);
                         else
                           hr = ADsGetObject(bstrCurrentPath,
                                             IID_IADsGroup,
                                             (void **)&pIADsGroupAsMember);
 
                         // If bind was completed, then this is a group.
                         if (SUCCEEDED(hr))
                         {
                           // Recursively call this group to 
                           // verify this group.
                           BOOL bRetRecurse;
                           bRetRecurse = 
                             RecursiveIsMember(pIADsGroupAsMember,
                                               pwszMemberGUID,
                                               pwszMemberPath,
                                               bVerbose,
                                               pwszUser,
                                               pwszPassword );
                                           
                           if (bRetRecurse)
                           {
                              bRet = TRUE;
                              break;
                           }
                           pIADsGroupAsMember->Release();
                           pIADsGroupAsMember = NULL;
                         }
                       }
                       SysFreeString(bstrCurrentPath);
                       bstrCurrentPath = NULL;
 
                       SysFreeString(bstrGuidCurrent);
                       bstrGuidCurrent = NULL;
                     }
                     // Release.
                     pIDOCurrent->Release();
                     pIDOCurrent = NULL;
                     if (pIADsCurrent)
                     {
                        pIADsCurrent->Release();
                        pIADsCurrent = NULL;
                     }
                   }
                 }
                 // Clear the variant array.
                 memset(VariantArray, 0, sizeof(VARIANT)*FETCH_NUM);
               }
               else
               fContinue = FALSE;
             }
             pEnumVariant->Release();
             pEnumVariant = NULL;
           }
           pUnknown->Release();
           pUnknown = NULL;
       }
       pADsMembers ->Release();
       pADsMembers  = NULL;
    }
 
    // Free the group path if retrieved.
    if (bsGroupPath)
    {
      SysFreeString(bsGroupPath);
      bsGroupPath = NULL;
    }
    return bRet;
}
//////////////////////////////////////////////////////////////////////
/*  GetObjectGuid()    - Gets the GUID, in string form, from 
                         the passed Directory Object.
                         Returns S_OK on success.
 
    Parameters
 
        IDirectoryObject * pDO    - Directory Object from where 
                                    GUID is retrieved.
        BSTR             & bsGuid - Returned GUID            
*/
 
HRESULT GetObjectGuid(IDirectoryObject * pDO,BSTR &bsGuid)
{
 
    GUID *pObjectGUID   = NULL;
    PADS_ATTR_INFO      pAttributeEntries;

    // Get the GUID for the object:
    LPWSTR              pAttributeName = L"objectGUID";  
    DWORD               dwAttributesReturned = 0;
    HRESULT             hr;

    if(!pDO)
    {
      return E_FAIL;
    }

    hr = pDO->GetObjectAttributes(&pAttributeName, // objectGUID
                                  1,               // Only objectGUID
                                  &pAttributeEntries, // Returned 
                                                      // attributes
                                  &dwAttributesReturned // Number of 
                                                        // attributes 
                                                        // returned
                                  );
 
    if (SUCCEEDED(hr) && dwAttributesReturned>0)
    {
        // Verify that the right type was retrieved--
        // objectGUID is ADSTYPE_OCTET_STRING
        if (pAttributeEntries->dwADsType == ADSTYPE_OCTET_STRING)
        {
            // Get COM converted string version of the GUID
            // lpvalue should be LPBYTE. Should be able to 
            // cast it to pointer to the GUID.
            pObjectGUID = 
             (GUID*)(pAttributeEntries->pADsValues[0].OctetString.lpValue);
            
            // OLE str to fit a GUID
            
            LPOLESTR szGUID = new WCHAR [64];
            szGUID[0]=NULL;
            // Convert GUID to string.
            ::StringFromGUID2(*pObjectGUID, szGUID, 39); 
            bsGuid = SysAllocString(szGUID);
            
            delete [] szGUID;
         }
    }
 
    return hr;
 
}
//////////////////////////////////////////////////////////////////
/*  PrintBanner()   -       Prints a banner to the screen.
 
    Parameters
 
                LPOLESTR pwszBanner   - String to print
*/
void PrintBanner(LPOLESTR pwszBanner)
{
    _putws(L"");
    _putws(L"////////////////////////////////////////////////////");
    wprintf(L"\t");
    _putws(pwszBanner);
    _putws(L"////////////////////////////////////////////////////\n");
}
```



 

 




