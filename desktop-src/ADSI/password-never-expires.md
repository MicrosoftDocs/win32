---
title: Password Never Expires (LDAP Provider)
description: To enable the password never expires option using the LDAP provider, set the ADS\_UF\_DONT\_EXPIRE\_PASSWD flag on the user userAccountControl attribute.
ms.assetid: b8d7e7fe-c846-45c4-9c5f-770530453836
ms.tgt_platform: multiple
keywords:
- Password Never Expires ADSI ,LDAP provider
- LDAP provider ADSI ,user management examples,Password Never Expires
ms.topic: article
ms.date: 05/31/2018
---

# Password Never Expires (LDAP Provider)

To enable the password never expires option using the LDAP provider, set the [**ADS\_UF\_DONT\_EXPIRE\_PASSWD**](/windows/win32/api/iads/ne-iads-ads_user_flag_enum) flag on the user [**userAccountControl**](/windows/desktop/ADSchema/a-useraccountcontrol) attribute.


```VB
Const ADS_UF_DONT_EXPIRE_PASSWD = &H10000

Set usr = GetObject("LDAP://CN=jeffsmith,OU=Sales,DC=Fabrikam,DC=Com")
flag = usr.Get("userAccountControl")
newFlag = flag Or ADS_UF_DONT_EXPIRE_PASSWD
usr.Put "userAccountControl", newFlag
usr.SetInfo
```




```C++
#include <activeds.h>

IADsUser *pUser;
VARIANT var;
VariantInit(&var);

HRESULT hr = S_OK;
LPWSTR adsPath = L"LDAP://serv1/cn=Jeff Smith,cn=Users,dc=Fabrikam,dc=com";
hr = ADsGetObject(adsPath, IID_IADsUser, (void**)&pUser);

hr = pUser->Get(_bstr_t("userAccountControl"), &var);

V_I4(&var) |= ADS_UF_DONT_EXPIRE_PASSWD;
hr = pUser->Put(_bstr_t("userAccountControl"), var);

hr = pUser->SetInfo();
VariantClear(&var);
hr = pUser->Release();
```



 

 