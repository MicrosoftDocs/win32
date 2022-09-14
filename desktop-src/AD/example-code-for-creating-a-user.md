---
title: Example Code for Creating a User
description: This topic includes code examples that create a user in a domain controlled by Active Directory Domain Services.
ms.assetid: a2e1be50-0936-4e6b-a712-637156f63be6
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory , creating a user
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Creating a User

This topic includes code examples that create a user in a domain controlled by Active Directory Domain Services.


```VB
Const ADS_UF_SCRIPT = &H1
Const ADS_UF_ACCOUNTDISABLE = &H2
Const ADS_UF_HOMEDIR_REQUIRED = &H8
Const ADS_UF_LOCKOUT = &H10
Const ADS_UF_PASSWD_NOTREQD = &H20
Const ADS_UF_PASSWD_CANT_CHANGE = &H40
Const ADS_UF_ENCRYPTED_TEXT_PASSWORD_ALLOWED = &H80
Const ADS_UF_TEMP_DUPLICATE_ACCOUNT = &H100
Const ADS_UF_NORMAL_ACCOUNT = &H200
Const ADS_UF_INTERDOMAIN_TRUST_ACCOUNT = &H800
Const ADS_UF_WORKSTATION_TRUST_ACCOUNT = &H1000
Const ADS_UF_SERVER_TRUST_ACCOUNT = &H2000
Const ADS_UF_DONT_EXPIRE_PASSWD = &H10000
Const ADS_UF_MNS_LOGON_ACCOUNT = &H20000
Const ADS_UF_SMARTCARD_REQUIRED = &H40000
Const ADS_UF_TRUSTED_FOR_DELEGATION = &H80000
Const ADS_UF_NOT_DELEGATED = &H100000
Const ADS_UF_USE_DES_KEY_ONLY = &H200000
Const ADS_UF_DONT_REQUIRE_PREAUTH = &H400000
Const ADS_UF_PASSWORD_EXPIRED = &H800000
Const ADS_UF_TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION = &H1000000

Public Sub CreateUser(strName As String, 
                      strSAMAccountName As String,
                      strInitialPassword As String)
    Dim objRootDSE As IADs
    Dim objUsers As IADsContainer
    Dim objNewUser As IADsUser

    On Error Resume Next
    
    ' Bind to the rootDSE object.
    Set objRootDSE = GetObject("LDAP://rootDSE")
    If (Err.Number <> 0) Then
        Exit Sub
    End If
    
    ' Bind to the Users folder in the domain.
    Set objUsers = GetObject("LDAP://CN=Users," & 
                             objRootDSE.Get("defaultNamingContext"))
    If (Err.Number <> 0) Then
        Exit Sub
    End If
    
    ' Create the user object.
    Set objNewUser = objUsers.Create("user", "CN=" + strName)
    If (Err.Number <> 0) Then
        Exit Sub
    End If
    
    ' Set the sAMAccountName property.
    objNewUser.Put "sAMAccountName", strSAMAccountName
    If (Err.Number <> 0) Then
        Exit Sub
    End If
    
    ' Commit the new user.
    objNewUser.SetInfo
    If (Err.Number <> 0) Then
        Exit Sub
    End If

    ' Set the initial password. This must be performed after
    ' SetInfo is called because the user object must
    ' already exist on the server.
    objNewUser.SetPassword strInitialPassword
    If (Err.Number <> 0) Then
        Exit Sub
    End If
    
    ' Set the pwdLastSet property to zero, which forces the
    ' user to change their password at next log on.
    objNewUser.Put "pwdLastSet", 0
    If (Err.Number <> 0) Then
        Exit Sub
    End If
    
    ' To enable the user account, remove the
    ' ADS_UF_ACCOUNTDISABLE flag from the userAccountControl
    ' property. Also, remove the ADS_UF_PASSWD_NOTREQD and
    ' ADS_UF_DONT_EXPIRE_PASSWD flags from the
    ' userAccountControl property.
    userActCtrl = objNewUser.Get("userAccountControl")
    userActCtrl = userActCtrl And Not (ADS_UF_ACCOUNTDISABLE + 
                                       ADS_UF_PASSWD_NOTREQD + 
                                       ADS_UF_DONT_EXPIRE_PASSWD)
    objNewUser.Put "userAccountControl", userActCtrl
    If (Err.Number <> 0) Then
        Exit Sub
    End If
    
    ' Commit the updated properties.
    objNewUser.SetInfo
End Sub
```




```C++
//*******************************************************************
//
//  CreateUserFromADs()
//
//*******************************************************************

HRESULT CreateUserFromADs(LPCWSTR pwszContainerDN,
                          LPCWSTR pwszName, 
                          LPCWSTR pwszSAMAccountName, 
                          LPCWSTR pwszInitialPassword)
{
    HRESULT hr;

    //  Build the DN of the container.
    CComBSTR sbstrADsPath = "LDAP://";
    sbstrADsPath += pwszContainerDN;

    IADsContainer *pUsers = NULL;

    // Bind to the container.
    hr = ADsGetObject(sbstrADsPath, 
                      IID_IADsContainer, 
                      (LPVOID*)&pUsers);
    if(SUCCEEDED(hr))
    {
        IDispatch *pDisp = NULL;
        
        CComBSTR sbstrName = "CN=";
        sbstrName += pwszName;
        
        // Create the new object in the User folder.
        hr = pUsers->Create(CComBSTR("user"), sbstrName, &pDisp);

        if(SUCCEEDED(hr))
        { 
            IADsUser *padsUser = NULL;

            // Get the IADs interface.
            hr = pDisp->QueryInterface(IID_IADsUser,
                                       (void**) &padsUser);

            if(SUCCEEDED(hr))
            { 
                CComBSTR sbstrProp;
                /*
                The sAMAccountName property is required on operating system 
                versions prior to Windows Server 2003.
                The Windows Server 2003 operating system will create a 
                sAMAccountName value if one is not specified.
                */
                CComVariant svar;
                svar = pwszSAMAccountName;
                sbstrProp = "sAMAccountName";
                hr = padsUser->Put(sbstrProp, svar);

                /*
                Commit the new user to persistent memory. 
                The user does not exist until this is called.
                */
                hr = padsUser->SetInfo();

                /*
                Set the initial password. This must be done after 
                SetInfo is called because the user object must 
                already exist on the server.
                */
                hr = padsUser->SetPassword(CComBSTR(pwszInitialPassword));

                /*
                Set the pwdLastSet property to zero, which forces the 
                user to change the password the next time they log on.
                */
                sbstrProp = "pwdLastSet";
                svar = 0;
                hr = padsUser->Put(sbstrProp, svar);

                /*
                Enable the user account by removing the 
                ADS_UF_ACCOUNTDISABLE flag from the userAccountControl 
                property. Also, remove the ADS_UF_PASSWD_NOTREQD and 
                ADS_UF_DONT_EXPIRE_PASSWD flags from the 
                userAccountControl property.
                */
                svar.Clear();
                sbstrProp = "userAccountControl";
                hr = padsUser->Get(sbstrProp, &svar);
                if(SUCCEEDED(hr))
                {
                    svar = svar.lVal & ~(ADS_UF_ACCOUNTDISABLE | 
                        ADS_UF_PASSWD_NOTREQD | 
                        ADS_UF_DONT_EXPIRE_PASSWD);

                    hr = padsUser->Put(sbstrProp, svar);
                    hr = padsUser->SetInfo();
                }
                
                hr = padsUser->put_AccountDisabled(VARIANT_FALSE);
                hr = padsUser->SetInfo();

                padsUser->Release();
            }

            pDisp->Release();
        }

        pUsers->Release();
    }

    return hr;
}
```




```C++
//*******************************************************************
//
//  CreateUserFromDirObject()
//
//*******************************************************************

HRESULT CreateUserFromDirObject(LPCWSTR pwszContainerDN,
                                LPCWSTR pwszName, 
                                LPCWSTR pwszSAMAccountName, 
                                LPCWSTR pwszInitialPassword)
{
    HRESULT hr;

    //  Build the DN of the container.
    CComBSTR sbstrADsPath = "LDAP://";
    sbstrADsPath += pwszContainerDN;

    IDirectoryObject *pdoUsers = NULL;

    // Bind to the container.
    hr = ADsGetObject(sbstrADsPath, 
                      IID_IDirectoryObject,
                      (LPVOID*)&pdoUsers);
    if(SUCCEEDED(hr))
    {
        IDispatch *pDisp;
        ADS_ATTR_INFO rgAttrInfo[3];
        
        // Setup the objectClass property.
        ADSVALUE classValue;
        classValue.dwType = ADSTYPE_CASE_IGNORE_STRING;
        classValue.CaseIgnoreString = L"User";
        rgAttrInfo[0].pszAttrName = L"objectClass";
        rgAttrInfo[0].dwControlCode = ADS_ATTR_UPDATE;
        rgAttrInfo[0].dwADsType = ADSTYPE_CASE_IGNORE_STRING;
        rgAttrInfo[0].pADsValues = &classValue;
        rgAttrInfo[0].dwNumValues = 1;

        /*
        The sAMAccountName property is required on operating system versions 
        prior to Windows Server 2003. 
        The Windows Server 2003 operating system will create a 
        sAMAccountName value if one is not specified.
        */
        ADSVALUE sAMValue;
        sAMValue.dwType = ADSTYPE_CASE_IGNORE_STRING;
        sAMValue.CaseIgnoreString = 
           (ADS_CASE_IGNORE_STRING)pwszSAMAccountName;
        rgAttrInfo[1].pszAttrName = L"sAMAccountName";
        rgAttrInfo[1].dwControlCode = ADS_ATTR_UPDATE;
        rgAttrInfo[1].dwADsType = ADSTYPE_CASE_IGNORE_STRING;
        rgAttrInfo[1].pADsValues = &sAMValue;
        rgAttrInfo[1].dwNumValues = 1;

        /*
        Set the initial userAccountControl attribute so that
        the user is created as an enabled account and a
        password is required.
        */
        ADSVALUE userAccountControlValue;
        userAccountControlValue.dwType = ADSTYPE_INTEGER;
        userAccountControlValue.Integer = ADS_UF_NORMAL_ACCOUNT;
        rgAttrInfo[2].pszAttrName = L"userAccountControl";
        rgAttrInfo[2].dwControlCode = ADS_ATTR_UPDATE;
        rgAttrInfo[2].dwADsType = ADSTYPE_INTEGER;
        rgAttrInfo[2].pADsValues = &userAccountControlValue;
        rgAttrInfo[2].dwNumValues = 1;

        CComBSTR sbstrName = "CN=";
        sbstrName += pwszName;

        /*
        Create the object in the Users container with the specified 
        property values.
        */
        hr = pdoUsers->CreateDSObject(
              sbstrName,  
              rgAttrInfo, 
              sizeof(rgAttrInfo)/sizeof(ADS_ATTR_INFO), 
              &pDisp
             );

        if(SUCCEEDED(hr))
        {
            IDirectoryObject *pdoNewUser;

            hr = pDisp->QueryInterface(IID_IDirectoryObject, 
                                       (LPVOID*)&pdoNewUser);
            if(SUCCEEDED(hr))
            {
                ADSVALUE adsValue;
                DWORD dw;
                
                /*
                Set the initial password.
                */
                IADsUser *padsUser;
                hr = pdoNewUser->QueryInterface(IID_IADsUser, 
                                                (LPVOID*)&padsUser);
                if(SUCCEEDED(hr))
                {
                  hr = 
                   padsUser->SetPassword(CComBSTR(pwszInitialPassword));
                  padsUser->Release();
                }
                
                /*
                Set the pwdLastSet property to zero, which forces the 
                user to change their password at next log on.
                */
                adsValue.dwType = ADSTYPE_LARGE_INTEGER;
                adsValue.LargeInteger.LowPart = 0;
                adsValue.LargeInteger.HighPart = 0;
                rgAttrInfo[0].pszAttrName = L"pwdLastSet";
                rgAttrInfo[0].dwControlCode = ADS_ATTR_UPDATE;
                rgAttrInfo[0].dwADsType = ADSTYPE_LARGE_INTEGER;
                rgAttrInfo[0].pADsValues = &adsValue;
                rgAttrInfo[0].dwNumValues = 1;
                hr = pdoNewUser->SetObjectAttributes(rgAttrInfo,
                                                     1,
                                                     &dw);

                pdoNewUser->Release();
            }
            
            pDisp->Release();
        }
        
        pdoUsers->Release();
    }

    return hr;
}
```



 

 




