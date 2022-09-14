---
title: Account Expiration (WinNT Provider)
description: When using the WinNT provider, the account expiration date can be set using the IADsUser.AccountExpirationDate property.
ms.assetid: 1d887a33-a3ae-4c61-88fa-2764a6bbf6bf
ms.tgt_platform: multiple
keywords:
- Account Expiration ADSI , WinNT provider
- WinNT provider ADSI , user management examples, Account Expiration
ms.topic: article
ms.date: 05/31/2018
---

# Account Expiration (WinNT Provider)

When using the WinNT provider, the account expiration date can be set using the [**IADsUser.AccountExpirationDate**](iadsuser-property-methods.md) property.

To set the account expiration date, set the [**IADsUser.AccountExpirationDate**](iadsuser-property-methods.md) property to the desired date value. To set the account expiration date to never expire, set this property to "January 1, 1970".

## Example 1

The following code example shows how to set the account expiration date using Visual Basic with ADSI.


```VB
Dim usr As IADsUser

Set usr = GetObject("WinNT://Fabrikam/JeffSmith")
usr.AccountExpirationDate = "05/06/1998"
usr.SetInfo
 
' Set the account to never expire.
usr.AccountExpirationDate = "01/01/1970"
usr.SetInfo
```



## Example 2

The following code example shows how to set the account expiration date using C++ with ADSI.


```C++
void SetUserAccountExpirationDate(IADsUser *pUser, DATE date)
{
   if(!pUser) return;

   HRESULT hr = S_OK;
   hr = pUser->put_AccountExpirationDate(date); // Set the account to expires on date.
   
   hr = pUser->SetInfo();
   hr = pUser->Release();
   return;
}
```



 

 




