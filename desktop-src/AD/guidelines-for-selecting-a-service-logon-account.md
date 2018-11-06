---
title: Guidelines for Selecting a Service Logon Account
description: A Win32-based service can run in the security context of a local user account, a domain user account, or the LocalSystem account.
ms.assetid: aa2b93c7-335f-4e03-9198-fe2b396e296e
ms.tgt_platform: multiple
keywords:
- Guidelines for Selecting a Service Logon Account AD
ms.topic: article
ms.date: 05/31/2018
---

# Guidelines for Selecting a Service Logon Account

A Win32-based service can run in the security context of a local user account, a domain user account, or the LocalSystem account. To decide which account to use, an administrator should install the service with the minimum set of permissions required to perform the service operations. In a typical directory-enabled service, this means the service installer should create a domain user account for the service and grant that account the specific access rights and privileges required by the service at run time. A service should only run under the LocalSystem account if the service requires administrative privileges or must act as part of the operating system on the local computer.

Be aware that the service installer should, by default, set up the service to run under a domain user account. To run the service under the LocalSystem account, the service installer should query the administrator for permission to do so.

For more information about descriptions, advantages, and disadvantages of each account type, see:

-   [Local User Accounts](local-user-accounts.md).
-   [Domain User Accounts](domain-user-accounts.md).
-   [The LocalSystem Account](the-localsystem-account.md).

 

 




