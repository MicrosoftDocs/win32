---
title: Password Never Expires (LDAP Provider)
description: To enable the password never expires option using the LDAP provider, set the ADS\_UF\_DONT\_EXPIRE\_PASSWD flag on the user userAccountControl attribute.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: b8d7e7fe-c846-45c4-9c5f-770530453836
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Password Never Expires ADSI ,LDAP provider
- LDAP provider ADSI ,user management examples,Password Never Expires
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Password Never Expires (LDAP Provider)

To enable the password never expires option using the LDAP provider, set the [**ADS\_UF\_DONT\_EXPIRE\_PASSWD**](/windows/desktop/api/Iads/ne-iads-ads_user_flag) flag on the user [**userAccountControl**](https://msdn.microsoft.com/library/ms680832) attribute.


```VB
Const ADS_UF_DONT_EXPIRE_PASSWD = &amp;H10000

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
VariantInit(&amp;var);

HRESULT hr = S_OK;
LPWSTR adsPath = L"LDAP://serv1/cn=Jeff Smith,cn=Users,dc=Fabrikam,dc=com";
hr = ADsGetObject(adsPath, IID_IADsUser, (void**)&amp;pUser);

hr = pUser->Get(_bstr_t("userAccountControl"), &amp;var);

V_I4(&amp;var) |= ADS_UF_DONT_EXPIRE_PASSWD;
hr = pUser->Put(_bstr_t("userAccountControl"), var);

hr = pUser->SetInfo();
VariantClear(&amp;var);
hr = pUser->Release();
```



 

 




