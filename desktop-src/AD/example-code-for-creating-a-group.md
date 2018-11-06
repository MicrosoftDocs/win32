---
title: Example Code for Creating a Group
description: This topic includes a code example code that creates a group.
ms.assetid: f6bba6fc-fec2-4dd9-b7f2-da7782a6caa5
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory , creating a group
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Creating a Group

The following C++ code example contains a function that creates a group with only the essential properties explicitly set (**cn**, **sAMAccountType**, **groupType**) and containing no members.


```C++
/////////////////////////////////////////////////////////////////////
/*  CreateSimpleGroup()   - Function for creating a basic group
    
    Parameters
 
      IDirectoryObject *pDirObject  -   Parent Directory Object 
                                        for the new group
      LPWSTR pwCommonName           -   Common Name for the new group
      IADs ** ppObjRet              -   Pointer to the Pointer which 
                                        will receive the new Group
      int iGroupType                -   Bitflags for new group:
                                       
                              ADS_GROUP_TYPE_GLOBAL_GROUP, 
                              ADS_GROUP_TYPE_DOMAIN_LOCAL_GROUP, 
                              ADS_GROUP_TYPE_UNIVERSAL_GROUP, 
                              ADS_GROUP_TYPE_SECURITY_ENABLED 
*/

HRESULT CreateSimpleGroup(IDirectoryObject *pDirObject, 
                          LPWSTR pwCommonName,
                          LPWSTR pwSamAcctName,
                          IADs *ppObjRet,
                          int iGroupType)
{
    if(!pDirObject)
        return E_INVALIDARG;
 
// Verify that the group type is Universal Security
// if true, ensure that domain is in native mode.
    if(((iGroupType & ADS_GROUP_TYPE_UNIVERSAL_GROUP) == 
                      ADS_GROUP_TYPE_UNIVERSAL_GROUP)
       &&((iGroupType & ADS_GROUP_TYPE_SECURITY_ENABLED) == 
                        ADS_GROUP_TYPE_SECURITY_ENABLED))
    {
        // Verify that the domain that contains the container
        // is in mixed mode.
        hr = CheckDomainModeOfObject(pDirObject, &bIsMixed);
 
        if (SUCCEEDED(hr))
        {
            if (bIsMixed)
                return E_INVALIDARG;
        }
        else
        {
            return hr;
        }
    }
 
    // SamAccountName cannot be larger than 20 characters.
    if (wcslen(pwSamAcctName) >20)
    {
        return E_FAIL;
    }
 
    HRESULT    hr;
    
    /* 
        ADSVALUE is used to specify attribute data for calling 
        IDirectoryObject::CreateDSObject()
        When Creating a new group, the required attributes are : 
        objectClass,sAMAccountName and groupType.
 
        In this function the "objectClass" is set to "group". 
        The  "sAMAccountName" is the Windows NT 4.0 name.
        In Windows 2000/Windows NT 4 mixed-mode environment, 
        this attribute is exposed to the Windows NT 4 computers. 
        Therefore, this name must be globally unique throughout
        the network and cannot exceed 20 characters in length.
    */
    ADSVALUE   sAMValue;
    ADSVALUE   classValue;
    ADSVALUE   groupType;
 
    LPDISPATCH pDisp;
    WCHAR       *pwCommonNameFull;
    
    // Build an Array of ADS_ATTR_INFO structures
    // Be aware that the sAMAccountName and groupType entries
    // contain a pointer to the respective ADSVALUE 
    // structures defined previously.
    ADS_ATTR_INFO  attrInfo[] = 
    {  
       {L"objectClass", ADS_ATTR_UPDATE, 
                        ADSTYPE_CASE_IGNORE_STRING, &classValue, 1},
       {L"sAMAccountName", ADS_ATTR_UPDATE, 
                           ADSTYPE_CASE_IGNORE_STRING, &sAMValue, 1},
       {L"groupType", ADS_ATTR_UPDATE, 
                      ADSTYPE_CASE_IGNORE_STRING, &groupType, 1}
    };
 
    // Get the size of the array. 
    DWORD dwAttrs = sizeof(attrInfo)/sizeof(ADS_ATTR_INFO); 
 
    /*
        For ADSVALUES, the dwType member and 
        the data value member (in this case "CaseIgnoreString")
        must be set.
    */
 
    // To create a group, this parameter must be set to "group".
    classValue.dwType = ADSTYPE_CASE_IGNORE_STRING;
    classValue.CaseIgnoreString = L"group";
 
    // Set sAMAccountName to the name passed to this function
    sAMValue.dwType=ADSTYPE_CASE_IGNORE_STRING;
    sAMValue.CaseIgnoreString = pwSamAcctName;
 
    // Set the groupType to the group type passed to this function
    groupType.dwType=ADSTYPE_INTEGER;
    groupType.Integer =  iGroupType;

    // Allocate a buffer to hold the full common name string
    pwCommonNameFull = new WCHAR[wcslen(pwCommonName)+4];

    // Be aware that CN is limited to 64 characters.
    // Take the passed commonname and prefix a 'CN=' to conform 
    // to the format that  IDirectoryObject::CreateDSObject() requires
    swprintf_s(pwCommonNameFull,L"CN=%s",pwCommonName);
 
    // Create the new group.
    hr = pDirObject->CreateDSObject( pwCommonNameFull,  attrInfo, 
                                dwAttrs, &pDisp );
    if (SUCCEEDED(hr))
    {
        // Query the new group for an IADs to be returned 
        // from this function.
        hr = pDisp->QueryInterface(IID_IADs,(void**) ppObjRet);
 
        pDisp->Release();
        pDisp = NULL;
    }
    return hr;
}
 
 
HRESULT GetDomainMode(IADs *pDomain, BOOL *bIsMixed)
{
HRESULT hr = E_FAIL;
VARIANT var;
if (pDomain)
{
    VariantClear(&var);
    // Get the ntMixedDomain attribute
    hr = pDomain->Get(CComBSTR("ntMixedDomain"), &var);
    if (SUCCEEDED(hr))
    {
        // Type should be VT_I4.
        if (var.vt==VT_I4)
        {
            // Zero (0) indicates native mode.
            if (var.lVal == 0)
                *bIsMixed = FALSE;
            // One (1) indicates mixed mode.
            else if (var.lVal == 1)
                *bIsMixed = TRUE;
            else
                hr=E_FAIL;
        }
    }
    VariantClear(&var);
}
return hr;
 
}
 
 
HRESULT CheckDomainModeOfObject(IDirectoryObject *pDirObject, 
                                BOOL *bIsMixed)
{
    HRESULT hr = E_FAIL;
    IADs *pDomain = NULL;
    VARIANT VarTest;
    WCHAR *pFound = NULL;
    int iLen;
    WCHAR *pDomainPath = new WCHAR[MAX_PATH*2];
 
    // Verify that the domain that contains the container 
    // is in mixed mode
    WCHAR *pVal = NULL;
    pVal = GetDirectoryObjectAttrib(pDirObject,L"canonicalName");
 
    if (pVal)
    {
        // Parse the canonical name for the DNS name of the domain
        pFound = wcschr(pVal,'/');
        // Bind to the domain using the dns name, 
        // get defaultnamingcontext, 
        if (pFound)
        {
            iLen = pFound - pVal;
            wcscpy_s(pDomainPath, L"LDAP://");
            wcsncat_s(pDomainPath, pVal,iLen);
            wcscat_s(pDomainPath, L"/rootDSE");
            wprintf(L"DNS Name: %s\n", pDomainPath);
            VariantClear(&VarTest);
            hr = ADsOpenObject(pDomainPath,
                            NULL,
                            NULL,
                            ADS_SECURE_AUTHENTICATION, // Use Secure 
                                                       // Authentication
                            IID_IADs,
                            (void**)&pDomain);
            if (SUCCEEDED(hr))
            {
                hr = pDomain->Get(CComBSTR("defaultNamingContext"), 
                                  &VarTest);
                if (SUCCEEDED(hr))
                {
                    wcscpy_s(pDomainPath, L"LDAP://");
                     wcsncat_s(pDomainPath, pVal,iLen);
                    wcscat_s(pDomainPath, L"/");
                    wcscat_s(pDomainPath, VarTest.bstrVal);
                    VariantClear(&VarTest);
                    if (pDomain)
                        pDomain->Release();
                    if (SUCCEEDED(hr))
                    {
                        hr = ADsOpenObject(pDomainPath,
                                        NULL,
                                        NULL,
                                        ADS_SECURE_AUTHENTICATION,
                                        IID_IADs,
                                        (void**)&pDomain);
                        if (SUCCEEDED(hr))
                        {
                            hr = GetDomainMode(pDomain, bIsMixed);
                        }
                    }
                }
            }
            if (pDomain)
                pDomain->Release();
        }
    }
    return hr;
}
 
 
////////////////////////////////////////////////////////////////////
/*
    GetDirectoryObjectAttrib()  -   Returns the value of the attribute
                                    named in pAttrName from the 
                                    IDirectoryObject passed.
    Parameters
 
        IDirectoryObject *pDirObject  - Object from which to retrieve 
                                        an attribute value
        LPWSTR pAttrName              - Name of attribute to retrieve
*/
WCHAR * GetDirectoryObjectAttrib(IDirectoryObject *pDirObject,
                                 LPWSTR pAttrName)
{
    HRESULT   hr;
    ADS_ATTR_INFO   *pAttrInfo=NULL;
    DWORD   dwReturn;
    static WCHAR pwReturn[1024];
 
    pwReturn[0] = 0l;
 
    hr = pDirObject->GetObjectAttributes( &pAttrName, 
                                          1, 
                                          &pAttrInfo, 
                                          &dwReturn ); 
    if ( SUCCEEDED(hr) )
    {
        for(DWORD idx=0; idx < dwReturn;idx++, pAttrInfo++ )   
        {
            if ( (_wcsicmp(pAttrInfo->pszAttrName,pAttrName) == 0 ) &&
                 (pAttrInfo->dwADsType == ADSTYPE_CASE_IGNORE_STRING))
            {
                wcscpy_s(pwReturn,
                       pAttrInfo->pADsValues->CaseIgnoreString);
                break;
            }
        }
        FreeADsMem( pAttrInfo );
    }    
    return pwReturn;
}
```



The following Visual Basic code example creates a group with only the essential properties explicitly set (**cn**, **sAMAccountType**, **groupType**) and containing no members.


```VB
'////////////////////////////////////////////////////////////////////
'    CreateSimpleGroup()   - Function for creating a basic group
'
'    Parameters
'
'        oDirObject As IDirectoryObject   -   Parent Directory Object
'                                             for the new group
'        ByVal sCommonName As String      -   Common Name for
'                                             the new group
'        ByVal sSAMAcctName As String     -   Pointer to the Pointer 
'                                             which will receive
'                                             the new Group
'        oDirObjectRet As IDirectoryObject  - New object returned
'        ByVal iGroupType As Long           - Bitflags for new group:
'                                          
'                          ADS_GROUP_TYPE_GLOBAL_GROUP,
'                          ADS_GROUP_TYPE_DOMAIN_LOCAL_GROUP,
'                          ADS_GROUP_TYPE_UNIVERSAL_GROUP,
'                          ADS_GROUP_TYPE_SECURITY_ENABLED

Sub CreateSimpleGroup(oDirObject As IDirectoryObject,
                      ByVal sCommonName As String, 
                      ByVal sSAMAcctName As String,
                      oDirObjectRet As IDirectoryObject,
                      ByVal iGroupType As Long)

    On Error GoTo CleanUp
    
    If Len(sSAMAcctName) > 20 Then
        MsgBox "SamAccountName CANNOT be bigger than 20 characters"
        Exit Sub
    End If
 
    Dim sGroupType As String
    Dim oNewObject As IADs
    Dim oIadsContDirObj As IADsContainer
    Set oIadsContDirObj = oDirObject
 
    ' Get the string value for the group type.
    sGroupType = Str(iGroupType)
    
    ' Get a New group object.
    Set oNewObject = oIadsContDirObj.Create("group", 
                                            "CN=" & sCommonName)
 
    ' Put the required attributes.
    oNewObject.Put "sAMAccountName", sSAMAcctName
    oNewObject.Put "GroupType", iGroupType
 
    ' Commit the new group.
    oNewObject.SetInfo
 
    ' Print group vitals.
    DisplayMessage ">>> Created new GROUP with a groupeType of " & Str(iGroupType)
    PrintIADSObject oNewObject
 
    Set oDirObjectRet = oNewObject
    Set oNewObject = Nothing
    Set oIadsContDirObj = Nothing
    Exit Sub

CleanUp:
    Set oNewObject = Nothing
    Set oIadsContDirObj = Nothing
    Set oDirObjectRet = Nothing
    
End Sub
```



 

 




