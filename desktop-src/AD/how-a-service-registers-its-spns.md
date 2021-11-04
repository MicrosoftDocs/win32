---
title: How a Service Registers its SPNs
description: Before a client can use an SPN to authenticate an instance of a service, the SPN must be registered on the user or computer account that the service instance will use to log on.
ms.assetid: 39712c1f-3a9a-4c98-a1cb-879ab0b4cb63
ms.tgt_platform: multiple
keywords:
- How a Service Registers its SPNs AD
- service principal name AD , how a service registers its SPNs
ms.topic: article
ms.date: 05/31/2018
---

# How a Service Registers its SPNs

Before a client can use an SPN to authenticate an instance of a service, the SPN must be registered on the user or computer account that the service instance will use to log on. Typically, SPN registration is done by a service installation program running with domain administrator privileges.

The service installer that installs a service instance on a host computer typically performs the following procedure.

**To register SPNs for a service instance**

1.  Call the [**DsGetSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsgetspna) function to create one or more unique SPNs for the service instance. For more information, see [Name Formats for Unique SPNs](name-formats-for-unique-spns.md).
2.  Call the [**DsWriteAccountSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dswriteaccountspna) function to register the names on the service's logon account.

[**DsWriteAccountSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dswriteaccountspna) registers SPNs as a property of a user or computer account object in the directory. **user** and **computer** objects have a **servicePrincipalName** attribute, which is a multi-valued attribute for storing all the SPNs associated with a user or computer account. If the service runs under a user account, the SPNs are stored in the **servicePrincipalName** attribute of that account. If the service runs in the LocalSystem account, the SPNs are stored in the **servicePrincipalName** attribute of the account of the service's host computer. The **DsWriteAccountSpn** caller must specify the distinguished name of the account object under which the SPNs are stored.

To ensure that registered SPNs are secure, the **servicePrincipalName** attribute cannot be written directly; it can only be written by calling [**DsWriteAccountSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dswriteaccountspna). The caller must have write-access to the **servicePrincipalName** attribute of the target account. Typically, write access is granted by default only to domain administrators. However, there is a special case in which the system allows a service running under the LocalSystem account to register its own SPNs on the computer account of the service's host. In this case, the SPN being written must have the form "<service class>/&lt;host&gt;" and "&lt;host&gt;" must be the DNS name of the local computer.

[**DsWriteAccountSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dswriteaccountspna) can also remove SPNs from an account. An operation parameter indicates whether the SPNs are to be added to the account, removed from the account, or used to completely replace all current SPNs for the account. When a service instance is uninstalled, remove any SPNs registered for that instance.

For more information and a code example that registers or unregisters a service's SPNs, see [Registering the SPNs for a Service](registering-the-spns-for-a-service.md).

Host-based services that use the simple SPN format "<service class>/&lt;host&gt;", have the option of using the [**DsServerRegisterSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsserverregisterspna) function, which both creates and registers SPNs for a service instance. **DsServerRegisterSpn** is a helper function that calls [**DsGetSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsgetspna) and [**DsWriteAccountSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dswriteaccountspna).

For more information, see [Service Logon Accounts](service-logon-accounts.md).

 

 




