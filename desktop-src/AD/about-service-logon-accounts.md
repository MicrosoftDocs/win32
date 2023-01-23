---
title: About Service Logon Accounts
description: When a Win32-based service starts, it logs on to the local computer.
ms.assetid: 637ad0c0-118f-43e8-9d21-a93f6886f546
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# About Service Logon Accounts

When a Win32-based service starts, it logs on to the local computer. It can log on as:

-   A local or domain user account.
-   The LocalSystem account.

The logon account determines the security identity of the service at run time, that is, the service's primary security context. The security context determines the service's ability to access local and network resources. For example, a service running in the security context of a local user account cannot access network resources. Conversely, a service running in the security context of the LocalSystem account on a Windows 2000 domain controller (DC), would have unrestricted access to the DC. For more information, and a discussion of the benefits and limitations between user accounts and LocalSystem, see [Security Contexts and Active Directory Domain Services](security-contexts-and-active-directory-domain-services.md).

Ultimately, administrators on the system where the service is installed have control over the service's logon account. For security reasons, some administrators may not allow you to install your service under the LocalSystem account. Your service must be able to run under a domain user account. As a programmer, you can exercise some control over your service's logon account. Your service installer specifies the service's logon account when it calls the [**CreateService**](/windows/desktop/api/winsvc/nf-winsvc-createservicea) function to install the service on a host computer. Your installer can suggest a default logon account, but it should allow an administrator to specify the actual account.

Your installer can also perform the following tasks relating to your service's logon account:

-   Installation. If installing your service to run under a user account, the account must exist before you call [**CreateService**](/windows/desktop/api/winsvc/nf-winsvc-createservicea). You can use an existing account or create one as part of the host-computer installer. For more information, see [Setting up a Service's User Account](setting-up-a-serviceampaposs-user-account.md).
-   Authentication. If you want clients to use Kerberos mutual authentication, register the SPNs on the service's logon account. If the service runs under the LocalSystem account, the service's logon account is the computer account of the host computer. For more information, see [Service Principal Names](service-principal-names.md).
-   Grant Access. Ensure that the service at run time has the access rights and privileges that it requires to perform its tasks. This can require setting access-control entries (ACEs) in the security descriptors of various resources, that is directory objects, file shares, and so on, to allow the necessary access rights to the user or computer account. For more information, see [Granting Access Rights to the Service Logon Account](granting-access-rights-to-the-service-logon-account.md).
-   Set Privileges. Assign privileges to the specified logon account, such as the right to logon as a service to the host computer. For more information, see [Granting Logon as Service Right on the Host Computer](granting-logon-as-service-right-on-the-host-computer.md).

After a service is installed, there are maintenance tasks that relate to your service logon account. For more information, see [Logon Account Maintenance Tasks](logon-account-maintenance-tasks.md).

-   Password maintenance. For a service that runs under a user account, you must periodically change the password and keep the password in sync with the password used by one or more local service control managers to start the service.
-   SPN maintenance. If a service logon account changes, remove the SPNs registered on the old account and register them on the new account. Be aware that when a service is installed, a domain administrator can change the account under which your service runs; use Win32 functions or the user interface of the Computer Management administrative tool.
-   ACE maintenance. If a service logon account changes, you need to update ACEs and group memberships to ensure that the service can still access the necessary resources.

 

 