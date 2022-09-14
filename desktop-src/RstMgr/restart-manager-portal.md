---
title: Restart Manager
description: Write custom installers to eliminate system restarts that are required to complete updating a file in use. Shut down and restart all but critical system services from programs.
ms.assetid: 44b7975a-0093-4c8f-9a14-2a6bfd7a68a5
keywords:
- Restart Manager Restart Mgr
ms.topic: article
ms.date: 05/31/2018
---

# Restart Manager

## Purpose

The Restart Manager API can eliminate or reduce the number of system restarts that are required to complete an installation or update. The primary reason software updates require a system restart during an installation or update is that some of the files that are being updated are currently being used by a running application or service. The Restart Manager enables all but the [critical system services](critical-system-services.md) to be shut down and restarted. This frees files that are in use and allows installation operations to complete.

## Where applicable

The Restart Manager DLL exports a public C interface that can be loaded by standard or custom installers. The installer can use the Restart Manager to register files that should be replaced during the installation of an application or update. Then during a subsequent update or installation, the installer can use the Restart Manager to determine which files cannot be updated because they are currently in use. Restart Manager can shut down and restart the non-critical services or applications that are currently using those files. Installers can direct the Restart Manager to shut down and restart applications or services based on the file in use, the process ID (PID), or the short-name of a Windows service.

Restart Manager is intended for the development of desktop style applications.

## Developer audience

This documentation is intended for developers of installation applications who want to take advantage of the installer capabilities in Windows Vista or Windows Server 2008. Applications that use the [Windows Installer](/windows/desktop/Msi/windows-installer-portal) version 4.0 for installation and servicing automatically use the Restart Manager to reduce system restarts. Custom installers can also be designed to call the Restart Manager API to shut down and restart applications and services. In cases where a system restart is unavoidable, installers can use the Restart Manager API to schedule restarts in such a way that it minimizes the disruption of the user's work flow.

## Run-time requirements

The Restart Manager API is available beginning with Windows Vista and Windows Server 2008. Restart Manager consists of a single DLL that applications can load to access the Restart Manager API.

## In this section



| Topic                                                                 | Description                                                     |
|-----------------------------------------------------------------------|-----------------------------------------------------------------|
| [About Restart Manager](about-restart-manager.md)<br/>         | Overview topics that describe the Restart Manager.<br/>   |
| [Using Restart Manager](using-restart-manager.md)<br/>         | Overview topics about using the Restart Manager API.<br/> |
| [Restart Manager Reference](restart-manager-reference.md)<br/> | Reference topics for the Restart Manager API.<br/>        |



 

 

