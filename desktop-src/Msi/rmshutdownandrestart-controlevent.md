---
Description: Notifies the Windows Installer to use the Restart Manager to shutdown all applications that have files in use and to restart them at the end of the installation.
ms.assetid: bfa19cc8-4cf7-42ed-9e94-acaeca8d707a
title: RmShutdownAndRestart ControlEvent
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RmShutdownAndRestart ControlEvent

This event notifies the Windows Installer to use the [Restart Manager](rstmgr.portal) to shutdown all applications that have files in use and to restart them at the end of the installation.

This ControlEvent has no effect if any of the following are true.

-   The operating system running the installation is not Windows Vista or Windows Server 2008.
-   Interactions with the [Restart Manager](rstmgr.portal) have been disabled by the [**MSIRESTARTMANAGERCONTROL**](msirestartmanagercontrol.md) property or the [DisableAutomaticApplicationShutdown](disableautomaticapplicationshutdown.md) policy.
-   There is currently no open [Restart Manager](rstmgr.portal) session.
-   Any calls from the Windows Installer to the [Restart Manager](rstmgr.portal) returns a failure.

## Typical Use

The RMShutdownAndRestart control event is published only by a [PushButton](pushbutton-control.md) control on the [MsiRMFilesInUse Dialog](msirmfilesinuse-dialog.md) box.

 

 



