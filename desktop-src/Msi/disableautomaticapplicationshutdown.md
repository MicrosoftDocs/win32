---
description: If this per-machine system policy is set to 1 (one), Windows Installer does not interact with Restart Manager, but it will use the FilesInUse Dialog.If this per-machine system policy is set to 2 (two), Windows Installer uses the FilesInUse Dialog.
ms.assetid: a59de5bb-e0a1-459d-83e6-afaf81298123
title: DisableAutomaticApplicationShutdown
ms.topic: article
ms.date: 05/31/2018
---

# DisableAutomaticApplicationShutdown

If this per-machine system policy is set to 1 (one), Windows Installer does not interact with [Restart Manager](/windows/desktop/RstMgr/restart-manager-portal), but it will use the [FilesInUse Dialog](filesinuse-dialog.md).

If this per-machine system policy is set to 2 (two), Windows Installer uses the [FilesInUse Dialog](filesinuse-dialog.md). This setting disables attempts by the [Restart Manager](/windows/desktop/RstMgr/restart-manager-portal) to mitigate restarts when installing a Windows Installer package that has not been authored to use the Restart Manager. The installer still uses the Restart Manager to detect files in use by applications.

The DisableAutomaticApplicationShutdown policy is available beginning with Windows Installer version 4.0 on Windows Vista.

## Registry Key

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**

## Data Type

**REG\_DWORD**

## Related topics

<dl> <dt>

[**MSIRESTARTMANAGERCONTROL**](msirestartmanagercontrol.md)
</dt> <dt>

[Not Supported in Windows Installer 3.1 and earlier versions](not-supported-in-windows-installer-version-3-1.md)
</dt> </dl>

 

 
