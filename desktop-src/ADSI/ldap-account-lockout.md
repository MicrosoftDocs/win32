---
title: Account Lockout (LDAP Provider)
description: When the number of failed logon attempts is exceeded, the user account is locked out for a time period specified by the lockoutDuration attribute.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: bf86f6ac-8209-4306-8736-99ce53c93617
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Account Lockout (LDAP Provider) ADSI
- Account Lockout ADSI , LDAP provider
- LDAP provider ADSI , user management examples, Account Lockout
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Account Lockout (LDAP Provider)

When the number of failed logon attempts is exceeded, the user account is locked out for a time period specified by the [**lockoutDuration**](https://msdn.microsoft.com/library/ms676840) attribute. The [**IADsUser.IsAccountLocked**](iadsuser-property-methods.md) property appears to be the property to use to read and modify the lockout state of a user account, but the LDAP ADSI provider does not accurately support the **IsAccountLocked** property. To obtain and set accurate account lockout data, use the WinNT provider. For more information about using the **IsAccountLocked** property with the WinNT provider, see [Account Lockout (WinNT Provider)](winnt-account-lockout.md).

 

 




