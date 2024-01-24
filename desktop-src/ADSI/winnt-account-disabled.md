---
title: Account Disabled (WinNT Provider)
description: When using the WinNT provider, an account can be enabled or disabled using the IADsUser.AccountDisabled property.
ms.assetid: a3d855cc-5e3d-49c2-b61e-3b35064002ea
ms.tgt_platform: multiple
keywords:
- Account Disabled (WinNT Provider)
- Account Disabled ADSI , WinNT provider
- WinNT provider ADSI , user management examples, Account Disabled
ms.topic: article
ms.date: 05/31/2018
---

# Account Disabled (WinNT Provider)

When using the WinNT provider, an account can be enabled or disabled using the [**IADsUser.AccountDisabled**](iadsuser-property-methods.md) property.

## Example 1

The following code example shows how to disable an account using Visual Basic with ADSI.


```VB
Dim usr as IADsUser
On Error GoTo Cleanup

Set usr = GetObject("WinNT://Fabrikam/JeffSmith")
usr.AccountDisabled = TRUE ' Disable the account.
usr.SetInfo

Cleanup:
    If (Err.Number<>0) Then
        MsgBox("An error has occurred. " & Err.Number)
    End If
    Set usr = Nothing
```



## Example 2

The following code example shows how to disable an account using C++ with ADSI.


```C++
IADsUser *pUser;

HRESULT hr = S_OK;
LPWSTR adsPath;
adsPath=L"WinNT://Fabrikam/JeffSmith";
hr = ADsGetObject(adsPath, IID_IADsUser, (void**)&pUser);

hr = pUser->put_AccountDisabled(TRUE);
hr = pUser->SetInfo();
```



 

 




