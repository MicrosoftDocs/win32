---
title: User Must Change Password at Next Logon (LDAP Provider)
description: To force a user to change their password at next logon, set the pwdLastSet attribute to zero (0). To remove this requirement, set the pwdLastSet attribute to -1. The pwdLastSet attribute cannot be set to any other value except by the system.
ms.assetid: 0182151c-ddb7-4d08-98c6-c37e6e514cf0
ms.tgt_platform: multiple
keywords:
- User Must Change Password at Next Logon ADSI , LDAP provider
- LDAP provider ADSI , user management examples, User Must Change Password at Next Logon
ms.topic: article
ms.date: 05/31/2018
---

# User Must Change Password at Next Logon (LDAP Provider)

To force a user to change their password at next logon, set the **pwdLastSet** attribute to zero (0). To remove this requirement, set the **pwdLastSet** attribute to -1. The **pwdLastSet** attribute cannot be set to any other value except by the system.

The following code example shows how to set the "User must change password at next logon" option.


```VB
Dim usr as IADs

Set usr = GetObject("LDAP://CN=Jeff Smith,OU=Sales,DC=Fabrikam,DC=Com")
usr.Put "pwdLastSet", CLng(0)
usr.SetInfo
```



The following code example shows how to set the "User must change password at next logon" option.


```C++
/***************************************************************************

    SetUserMustChangePassword()

***************************************************************************/

HRESULT SetUserMustChangePassword(LPCWSTR pwszUserADsPath, 
                                  LPCWSTR pwszUsername, 
                                  LPCWSTR pwszPassword)
{
    IADs *pUser;
    HRESULT hr;

    hr = ADsOpenObject(pwszUserADsPath,
                        pwszUsername,
                        pwszPassword,
                        ADS_SECURE_AUTHENTICATION,
                        IID_IADs,
                        (void**)&pUser);

    if(SUCCEEDED(hr))
    {
        VARIANT var;
        VariantInit(&var);
        V_I4(&var) = 0;
        V_VT(&var) = VT_I4;
        hr = pUser->Put(CComBSTR("pwdLastSet"), var);
        hr = pUser->SetInfo();

        VariantClear(&var);
        pUser->Release();
    }

    return hr;
}
```



 

 




