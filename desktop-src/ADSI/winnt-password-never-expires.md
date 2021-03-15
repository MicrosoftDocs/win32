---
title: Password Never Expires (WinNT Provider)
description: To enable this option using the WinNT ADSI provider, set the ADS\_UF\_DONT\_EXPIRE\_PASSWD (0x10000) flag on the UserFlags attribute.Note  For Windows 2000 and later, use the LDAP ADSI provider for user management operations as shown.
ms.assetid: 9e38b31c-399b-447f-bceb-36c599b2714e
ms.tgt_platform: multiple
keywords:
- Password Never Expires (WinNT Provider)
- Password Never Expires ADSI , WinNT provider
- WinNT provider ADSI , user management examples, Password Never Expires
ms.topic: article
ms.date: 05/31/2018
---

# Password Never Expires (WinNT Provider)

To enable this option using the WinNT ADSI provider, set the **ADS\_UF\_DONT\_EXPIRE\_PASSWD** (0x10000) flag on the **UserFlags** attribute.

> [!Note]  
> For Windows 2000 and later, use the LDAP ADSI provider for user management operations as shown. For more information, see [Password Never Expires (LDAP Provider)](password-never-expires.md).

 

## Example 1

The following code example shows how to set the password never expires option using Visual Basic with ADSI.


```VB
Const ADS_UF_DONT_EXPIRE_PASSWD = &H10000
Dim usr as IADs

Set usr = GetObject("WinNT://Fabrikam/JeffSmith")
oldFlags = usr.Get("UserFlags")
newFlags = oldFlags Or ADS_UF_DONT_EXPIRE_PASSWD
usr.Put "UserFlags", newFlags
usr.SetInfo
```



## Example 2

The following code example shows how to set the password never expires option using C++ with ADSI.


```C++
#include <activeds.h>

IADsUser *pUser = NULL;
VARIANT var;
VariantInit(&var);

HRESULT hr = S_OK;
LPWSTR adsPath;
adsPath = L"WinNT://Fabrikam/JeffSmith";
hr = ADsGetObject(adsPath,IID_IADsUser, (void**)&pUser);

CComBSTR sbstrUserFlags = "UserFlags";
hr = pUser->Get(sbstrUserFlags, &var);

V_I4(&var) |= ADS_UF_DONT_EXPIRE_PASSWD;
hr = pUser->Put(sbstrUserFlags, var);

hr = pUser->SetInfo();

VariantClear(&var);

pUser->Release();
```



 

 




