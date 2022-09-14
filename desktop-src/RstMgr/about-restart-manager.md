---
title: About Restart Manager
description: The primary reason software installation and updates require a system restart is that some of the files that are being updated are currently being used by a running application or service.
ms.assetid: 9a1166d7-a0e1-4948-9077-278c84afccac
keywords:
- Restart Manager Restart Mgr , about
ms.topic: article
ms.date: 05/31/2018
---

# About Restart Manager

The primary reason software installation and updates require a system restart is that some of the files that are being updated are currently being used by a running application or service. Restart Manager enables all but the critical applications and services to be shut down and restarted . This frees the files that are in use and allows installation operations to complete. It can also eliminate or reduce the number of system restarts that are required to complete an installation or update.

The Restart Manager stops applications in the following order, and after the applications have been updated, restarts applications that have been registered for restart in the reverse order.

1.  GUI applications
2.  Console applications
3.  Windows services
4.  Windows explorer

Restart Manager shuts down application or services only if the caller has permission to do so. Note that shutdown across sessions is not supported.

Applications that use the [Windows Installer](/windows/desktop/Msi/windows-installer-portal) version 4.0 for installation and servicing automatically use the Restart Manager to reduce system restarts. Custom installers can also be designed to call the Restart Manager API to shut down and restart applications and services. In cases where a system restart is unavoidable, installers can use the Restart Manager API to schedule restarts in such a way that it minimizes the disruption of the user's work flow.

For information about using the Restart Manager API during installation and updates, see [Using Restart Manager](using-restart-manager.md).

Critical system services cannot be stopped and restarted by the Restart Manager without a system restart. For more information about identifying critical system services, see [Critical System Services](critical-system-services.md).

Your applications and services should be prepared to be shut down by the Restart Manager and save user data and state information that are needed for a clean restart. For more information about how to prepare your applications and services to work with the Restart Manager, see [Guidelines for Applications and Services](guidelines-for-applications-and-services.md).

For reference information about the enumerations, structures, and functions of the Restart Manager API, see the [Restart Manager Reference](restart-manager-reference.md) section

 

 