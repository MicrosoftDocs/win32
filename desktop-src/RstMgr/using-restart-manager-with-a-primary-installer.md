---
title: Using Restart Manager with a Primary Installer
description: The following procedure describes how to use the Restart Manager to shutdown and restart applications and services. When using the Restart Manager with a single installer, this installer is also the primary installer that controls the user interface.
ms.assetid: '8d2b4129-c595-4b11-9771-6dc953f4db40'
---

# Using Restart Manager with a Primary Installer

The following procedure describes how to use the Restart Manager to shutdown and restart applications and services. When using the Restart Manager with a single installer, this installer is also the primary installer that controls the user interface.

**To use the Restart Manager with a primary installer**

1.  The installer calls the [**RmStartSession**](rmstartsession.md) function to start the Restart Manager session and obtain a session handle and key.
2.  The installer calls the [**RmRegisterResources**](rmregisterresources.md) function to register resources. The Restart Manager can only use registered resources to determine which applications and services must be shut down and restarted. All resources that can be affected by the installation should be registered with the session. Resources can be identified by filename, service short name, or an [**RM\_UNIQUE\_PROCESS**](rm-unique-process.md) structure.
3.  The installer calls the [**RmGetList**](rmgetlist.md) function to obtain an array of [**RM\_PROCESS\_INFO**](rm-process-info.md) structures that lists all applications and services that must be shut down and restarted.

    If the value of the *lpdwRebootReason* parameter that is returned by the [**RmGetList**](rmgetlist.md) function is nonzero, the Restart Manager is unable to free a registered resource by the shutdown of an application or service. In this case, a system shutdown and restart is required to continue the installation. The installer should prompt the user for an action, stop programs or services, or schedule a system shutdown and restart.

    If the value of the *lpdwRebootReason* parameter that is returned by the [**RmGetList**](rmgetlist.md) function is zero, the installer should call the [**RmShutdown**](rmshutdown.md) function. This shuts down the services and applications that are using registered resources. The installer should then perform system modifications that are required to complete the installation. Finally, the installer should call the [**RmRestart**](rmrestart.md) function so that the Restart Manager can restart the applications it has shut down and that have been registered for a restart.

4.  The installer can use the [**RmAddFilter**](rmaddfilter.md) function to prevent specified applications and services from being shutdown or restarted by Restart Manager operations. The [**RmGetFilterList**](rmgetfilterlist.md) function returns a list of the applications and services to be filtered from shutdown and restart. The [**RmRemoveFilter**](rmremovefilter.md) function removes a filter.
5.  The installer calls the [**RmEndSession**](rmendsession.md) function to close the Restart Manager session.

For an example code snippet that shows starting and using a Restart Manager session by using a primary installer and then joining a secondary installer to the existing session, see [Using Restart Manager with a Secondary Installer](using-restart-manager-with-a-secondary-installer.md).

 

 




