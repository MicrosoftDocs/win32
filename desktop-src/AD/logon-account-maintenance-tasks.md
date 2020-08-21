---
title: Logon Account Maintenance Tasks
description: This topic describes issues that pertain to logon account maintenance tasks.
ms.assetid: 528be433-58ef-400b-ba9a-d114f3f94ec6
ms.tgt_platform: multiple
keywords:
- Logon Account Maintenance Tasks AD
ms.topic: article
ms.date: 05/31/2018
---

# Logon Account Maintenance Tasks

This topic describes issues that pertain to logon account maintenance tasks.

There are two primary issues that concern logon account maintenance tasks:

-   Updating the account password for a service instance that runs under a user account. For more information, see [Changing the Password on a Service's User Account](changing-the-password-on-a-serviceampaposs-user-account.md).
-   Handling changes to the logon account of a service instance.

The latter is a rare case, but can happen. The system provides the Computer Management administrative tool that enables change to a service logon account. In addition, other applications can use the [**ChangeServiceConfig**](/windows/desktop/api/winsvc/nf-winsvc-changeserviceconfiga) function to specify a new logon account for an installed service. By default, local administrator privileges are required to change a service account. If this did happen, it could affect your service in two ways:

-   If you have registered service principal names (SPNs), they will be registered on the wrong account.
-   If you set ACEs to grant access to the service, they would now grant access to the wrong account.

One approach is to have the service installer store the registered SPNs for each service instance in the registry on the host computer. You could use the same registry key under HKEY\_LOCAL\_MACHINE that you used to store the binding string for the service SCP. When the service starts, it calls the [**QueryServiceConfig**](/windows/desktop/api/winsvc/nf-winsvc-queryserviceconfiga) function to determine its logon account and then queries the Active Directory server to determine whether the SPNs are registered on the directory object for that account. If the SPNs are not registered, or are registered on the wrong account, the service refuses to start and displays a message saying that a domain administrator must run the service's configuration program to update the logon account settings. Be aware that this reconfiguration must be completed by an administrator because the service account should not have access to update its own SPN. Also be aware that SPNs must be removed from the old account, otherwise the SPNs will be useless for authentication because they are not unique in the forest.

 

 