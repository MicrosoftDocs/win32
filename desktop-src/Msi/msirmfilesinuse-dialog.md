---
description: The MsiRMFilesInUse Dialog box can be authored to display a list of processes that are currently running files that need to be overwritten or deleted by the installation.
ms.assetid: e8d93310-388e-4a08-9bce-04c31c33a665
title: MsiRMFilesInUse Dialog
ms.topic: article
ms.date: 05/31/2018
---

# MsiRMFilesInUse Dialog

The MsiRMFilesInUse Dialog box can be authored to display a list of processes that are currently running files that need to be overwritten or deleted by the installation. The user can select between options to "Automatically close applications and restart them" or "Do not close applications. (A reboot will be required.)" If the user selects the "Automatically close applications and restart them" option, a push button control on this dialog box can be authored to publish the RMShutdownAndRestart control event and the [Restart Manager](../rstmgr/restart-manager-portal.md) can close the applications and restart them at the end of the installation. This can eliminate or reduce the need to restart the computer. For more information, see [System Reboots](system-reboots.md).

The **MsiRMFilesInUse** dialog box is displayed during an installation only if all the following are true. When any of these are false, the Windows Installer ignores the **MsiRMFilesInUse** dialog box.

-   A Windows Installer version that is not earlier than version 4.0 and an operating system that is not earlier than Windows Vista or Windows Server 2008 is running the installation.
-   The Full UI [user interface level](user-interface-levels.md) is used.
-   Interactions with the [Restart Manager](../rstmgr/restart-manager-portal.md) have not been disabled by the [**MSIRESTARTMANAGERCONTROL**](msirestartmanagercontrol.md) property or the [DisableAutomaticApplicationShutdown](disableautomaticapplicationshutdown.md) policy.
-   The **MsiRMFilesInUse** dialog box is present in the installation package.
-   All calls from the Windows Installer to the [Restart Manager](../rstmgr/restart-manager-portal.md) are successful.

This dialog box will be created as required by the [InstallValidate action](installvalidate-action.md).

 

 
