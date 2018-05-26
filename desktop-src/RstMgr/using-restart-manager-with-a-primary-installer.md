---
title: Using Restart Manager with a Primary Installer
description: The following procedure describes how to use the Restart Manager to shutdown and restart applications and services. When using the Restart Manager with a single installer, this installer is also the primary installer that controls the user interface.
ms.assetid: 8d2b4129-c595-4b11-9771-6dc953f4db40
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Restart Manager with a Primary Installer

The following procedure describes how to use the Restart Manager to shutdown and restart applications and services. When using the Restart Manager with a single installer, this installer is also the primary installer that controls the user interface.

**To use the Restart Manager with a primary installer**

1.  The installer calls the [**RmStartSession**](/windows/win32/RestartManager/nf-restartmanager-rmstartsession?branch=master) function to start the Restart Manager session and obtain a session handle and key.
2.  The installer calls the [**RmRegisterResources**](/windows/win32/RestartManager/nf-restartmanager-rmregisterresources?branch=master) function to register resources. The Restart Manager can only use registered resources to determine which applications and services must be shut down and restarted. All resources that can be affected by the installation should be registered with the session. Resources can be identified by filename, service short name, or an [**RM\_UNIQUE\_PROCESS**](/windows/win32/RestartManager/ns-restartmanager-_rm_unique_process?branch=master) structure.
3.  The installer calls the [**RmGetList**](/windows/win32/RestartManager/nf-restartmanager-rmgetlist?branch=master) function to obtain an array of [**RM\_PROCESS\_INFO**](/windows/win32/RestartManager/ns-restartmanager-_rm_process_info?branch=master) structures that lists all applications and services that must be shut down and restarted.

    If the value of the *lpdwRebootReason* parameter that is returned by the [**RmGetList**](/windows/win32/RestartManager/nf-restartmanager-rmgetlist?branch=master) function is nonzero, the Restart Manager is unable to free a registered resource by the shutdown of an application or service. In this case, a system shutdown and restart is required to continue the installation. The installer should prompt the user for an action, stop programs or services, or schedule a system shutdown and restart.

    If the value of the *lpdwRebootReason* parameter that is returned by the [**RmGetList**](/windows/win32/RestartManager/nf-restartmanager-rmgetlist?branch=master) function is zero, the installer should call the [**RmShutdown**](/windows/win32/RestartManager/nf-restartmanager-rmshutdown?branch=master) function. This shuts down the services and applications that are using registered resources. The installer should then perform system modifications that are required to complete the installation. Finally, the installer should call the [**RmRestart**](/windows/win32/RestartManager/nf-restartmanager-rmrestart?branch=master) function so that the Restart Manager can restart the applications it has shut down and that have been registered for a restart.

4.  The installer can use the [**RmAddFilter**](/windows/win32/RestartManager/nf-restartmanager-rmaddfilter?branch=master) function to prevent specified applications and services from being shutdown or restarted by Restart Manager operations. The [**RmGetFilterList**](/windows/win32/RestartManager/nf-restartmanager-rmgetfilterlist?branch=master) function returns a list of the applications and services to be filtered from shutdown and restart. The [**RmRemoveFilter**](/windows/win32/RestartManager/nf-restartmanager-rmremovefilter?branch=master) function removes a filter.
5.  The installer calls the [**RmEndSession**](/windows/win32/RestartManager/nf-restartmanager-rmendsession?branch=master) function to close the Restart Manager session.

For an example code snippet that shows starting and using a Restart Manager session by using a primary installer and then joining a secondary installer to the existing session, see [Using Restart Manager with a Secondary Installer](using-restart-manager-with-a-secondary-installer.md).

 

 




