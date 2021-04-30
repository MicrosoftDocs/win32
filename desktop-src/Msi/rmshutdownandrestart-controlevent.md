---
description: Notifies the Windows Installer to use the Restart Manager to shutdown all applications that have files in use and to restart them at the end of the installation.
ms.assetid: bfa19cc8-4cf7-42ed-9e94-acaeca8d707a
title: RmShutdownAndRestart ControlEvent
ms.topic: article
ms.date: 05/31/2018
---

# RmShutdownAndRestart ControlEvent

This event notifies the Windows Installer to use the [Restart Manager](../rstmgr/restart-manager-portal.md) to shutdown all applications that have files in use and to restart them at the end of the installation.

This ControlEvent has no effect if any of the following are true.

-   The operating system running the installation is not Windows Vista or Windows Server 2008.
-   Interactions with the [Restart Manager](../rstmgr/restart-manager-portal.md) have been disabled by the [**MSIRESTARTMANAGERCONTROL**](msirestartmanagercontrol.md) property or the [DisableAutomaticApplicationShutdown](disableautomaticapplicationshutdown.md) policy.
-   There is currently no open [Restart Manager](../rstmgr/restart-manager-portal.md) session.
-   Any calls from the Windows Installer to the [Restart Manager](../rstmgr/restart-manager-portal.md) returns a failure.

## Typical Use

The RMShutdownAndRestart control event is published only by a [PushButton](pushbutton-control.md) control on the [MsiRMFilesInUse Dialog](msirmfilesinuse-dialog.md) box.

 

 
