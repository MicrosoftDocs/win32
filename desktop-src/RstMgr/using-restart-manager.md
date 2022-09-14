---
title: Using Restart Manager
description: The following sections describe using the Restart Manager API.
ms.assetid: 78448d5e-20f6-45b6-b833-7d7791e5e4c6
keywords:
- Restart Manager Restart Mgr , using
ms.topic: article
ms.date: 05/31/2018
---

# Using Restart Manager

The following sections describe using the Restart Manager API. Your applications and services should also follow the [Guidelines for Applications and Services](guidelines-for-applications-and-services.md).

## Using the Microsoft Windows Installer

The [Microsoft Windows Installer](/windows/desktop/Msi/windows-installer-portal) Version 4.0 is the application installation service of Windows Vista or Windows Server 2008. Applications that use the Windows Installer version 4.0 for installation and servicing automatically use the Restart Manager to reduce system restarts. Custom installers can also be designed to call the Restart Manager API to shut down and restart applications and services directly to avoid requiring a system restart. In cases where a system restart is unavoidable, installers can use the [**InitiateShutdown**](/windows/desktop/api/winreg/nf-winreg-initiateshutdowna) or [**ExitWindowsEx**](/windows/desktop/api/winuser/nf-winuser-exitwindowsex) function to schedule it in such a way that it minimizes the disruption to the user. Interactive Windows Installer packages should implement a user interface that includes a [MsiRMFilesInUse](/windows/desktop/Msi/msirmfilesinuse-dialog) dialog box. For more information, see [Using Windows Installer with Restart Manager](/windows/desktop/Msi/using-windows-installer-with-restart-manager) in the Windows Installer SDK documentation.

## Using the Restart Manager API with Custom Installers

Custom installers, or a Windows Installer package that contains custom actions that cause a system restart, can use the Restart Manager API to shut down and restart applications and services.

-   All operations that are performed using the Restart Manager API must be associated with a session. A maximum of 64 Restart Manager sessions per user session can be open on the system at the same time. The primary installer starts and ends the Restart Manager session. For more information about using Restart Manager with a single installer, see [Using Restart Manager with a Primary Installer](using-restart-manager-with-a-primary-installer.md).
-   If necessary for the installation, one or more secondary installers can be joined to the Restart Manager session and can run either in-process or out-of-process of the primary installer. Secondary installers require that the session key be provided by the primary installer to join a session. For more information and an example of using secondary installers, see [Using Restart Manager with a Secondary Installer](using-restart-manager-with-a-secondary-installer.md).
-   Interactive installers should implement a user interface that includes an [MsiRMFilesInUse](/windows/desktop/Msi/msirmfilesinuse-dialog) dialog box that can ask users to close applications and services. For more information, see [Using Windows Installer with Restart Manager](/windows/desktop/Msi/using-windows-installer-with-restart-manager) in the Windows Installer SDK documentation.
-   Installers can call the Restart Manager API to change, cancel, and get the status of the current Restart Manager operation. For more information, see the following topics: [Getting the Status of a Restart Manager Operation](getting-the-status-of-a-restart-manager-operation.md) and [Canceling the Current Restart Manager Operation](canceling-the-current-restart-manager-operation.md).
-   Installers should not disable file system redirection before calling the Restart Manager API. Some 32-bit installers run on 64-bit Windows may be unable to register a file in the %windir%\\system32 directory.

 

 