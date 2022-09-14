---
title: Account Disabled (LDAP Provider)
description: To disable a user account, set the AccountDisabled property to TRUE in the IADsUser interface. This is similar to the WinNT provider. The following code examples show how to disable a user account.
ms.assetid: 7911baa4-4178-47a9-80eb-11dc608a0ea3
ms.tgt_platform: multiple
keywords:
- Account Disabled ADSI ,LDAP provider
- LDAP provider ADSI ,user management examples,Account Disabled
ms.topic: article
ms.date: 05/31/2018
---

# Account Disabled (LDAP Provider)

To disable a user account, set the AccountDisabled property to **TRUE** in the [**IADsUser**](/windows/desktop/api/Iads/nn-iads-iadsuser) interface. This is similar to the WinNT provider. The following code examples show how to disable a user account.

## Example 1


```VB
Dim usr As IADsUser
On Error GoTo Cleanup

Set usr = GetObject("LDAP:// CN=JeffSmith, OU=Sales, DC=Fabrikam, DC=Com")
usr.AccountDisabled = TRUE ' Disable the account.
usr.SetInfo

Cleanup:
    If (Err.Number<>0) Then
        MsgBox("An error has occurred. " & Err.Number)
    End If

    Set usr = Nothing
```



## Example 2


```C++
IADsUser *pUser = NULL;

HRESULT hr = S_OK;
LPWSTR adsPath;
adsPath=L"LDAP://serv1/cn=Jeff Smith,cn=Users, dc=Fabrikam, dc=com";
hr = ADsGetObject(adsPath,IID_IADsUser,(void**)&pUser);

if(FAILED(hr)){return;}

hr = pUser->put_AccountDisabled(true);
hr = pUser->SetInfo();
```



 

 




