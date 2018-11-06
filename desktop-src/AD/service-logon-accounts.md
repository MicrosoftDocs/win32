---
title: Service Logon Accounts
description: A service, like any process, has a primary security identity that determines the granted access rights and privileges for local and network resources.
ms.assetid: c2345967-8415-4cc0-96d3-12c48e74028e
ms.tgt_platform: multiple
keywords:
- Active Directory,using,service logon
ms.topic: article
ms.date: 05/31/2018
---

# Service Logon Accounts

A service, like any process, has a primary security identity that determines the granted access rights and privileges for local and network resources. This security identity, or security context, also determines the potential the service has for damaging local and network resources.

The security context for a Microsoft Win32 service is determined by the logon account that is used to start the service. This section discusses programming issues and best practices relating to the service logon account used by Win32 services, with a focus on directory-enabled services. This section includes the following topics:

-   [About Service Logon Accounts](about-service-logon-accounts.md)—An overview of service logon accounts and security context programming issues for a Win32 service.
-   [Guidelines for Selecting a Service Logon Account](guidelines-for-selecting-a-service-logon-account.md) for a Win32 service.
-   [Setting up a Service's User Account](setting-up-a-serviceampaposs-user-account.md).
-   [Installing a Service on a Host Computer](installing-a-service-on-a-host-computer.md) and specifying the service logon account.
-   [Granting Logon as Service Right on the Host Computer](granting-logon-as-service-right-on-the-host-computer.md)—Granting the service's user account the logon as a service right on the host computer.
-   [Testing Whether Running on a Domain Controller](testing-whether-running-on-a-domain-controller.md)—Detecting at installation time whether the service instance is being installed on a domain controller.
-   [Granting Access Rights to the Service Logon Account](granting-access-rights-to-the-service-logon-account.md)—Setting and maintaining ACEs and group memberships to ensure that the system will grant the running service access to the necessary local and network resources.
-   [Changing the Password on a Service's User Account](changing-the-password-on-a-serviceampaposs-user-account.md)—Changing the password on a service's user account, and at the same time updating the password registered with the service control manager on each host server on which the service is installed.
-   [Mutual Authentication Using Kerberos](mutual-authentication-using-kerberos.md)—Maintaining service principal name (SPN) registration on the directory object associated with the logon account of each instance of your service. SPNs enable clients to authenticate a service using Kerberos mutual authentication.
-   [Converting Domain Account Name Formats](converting-domain-account-name-formats.md)—For example, converting a distinguished name to *Domain***\\***UserName* format, and vice versa.

 

 




