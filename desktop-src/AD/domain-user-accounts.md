---
title: Using a Domain User Account as a Service Logon Account
description: A domain user account enables the service to take full advantage of the service security features of Windows and Microsoft Active Directory Domain Services.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 03c486fd-faec-450c-9348-314680eb73cb
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using a Domain User Account as a Service Logon Account

A domain user account enables the service to take full advantage of the service security features of Windows and Microsoft Active Directory Domain Services. The service has whatever local and network access is granted to the account, or to any groups of which the account is a member. The service can support Kerberos mutual authentication.

> [!Note]  
> The following documentation is for computer programmers. If you are an end-user looking for information about an error message involving domain user accounts, see the [Microsoft community forums](http://answers.microsoft.com). For information about managing domain user accounts, see [TechNet](https://technet.microsoft.com/library/cc754217.aspx).

 

The advantage of using a domain user account is that the service's actions are limited by the access rights and privileges associated with the account. Unlike a LocalSystem service, bugs in a user-account service cannot damage the system. If the service is compromised by a security attack, the damage is limited to the operations that the system allows the user account to perform. At the same time, clients running at varying privilege levels can connect to the service, which enables the service to impersonate a client to perform sensitive operations.

Be aware that a service's user account should not be a member of any administrators groups, that is local, domain, or enterprise. If your service needs local administrative privileges, run under the LocalSystem account. For operations that require domain administrative privileges, perform them by impersonating the security context of a client application.

A service instance that uses a domain user account requires periodic administrative action to maintain the account password. The service control manager (SCM) on the host computer of a service instance caches the account password for use in logging on the service. So when you change the account password, you must also update the cached password on the host computer where the service is installed. For more information and a code example, see [Changing the Password on a Service's User Account](changing-the-password-on-a-serviceampaposs-user-account.md). You could avoid the regular maintenance by leaving the password unchanged, but that would increase the likelihood of a password attack on the service account. Be aware that even though the SCM stores the password in a secure portion of the registry, it is nevertheless subject to attack.

A domain user account has two name formats that programmers must handle for various operations: the distinguished name of the user object in the directory and the "<domain&gt;\\<username&gt;" format used by the local service control manager. For more information and a code example that converts from one format to the other, see [Converting Domain Account Name Formats](converting-domain-account-name-formats.md).

 

 




