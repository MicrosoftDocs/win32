---
description: The CostingComplete property indicates whether the installer has completed disk space costing.
ms.assetid: 23688f1e-3ae8-4cd9-824c-36077cc7838f
title: CostingComplete property
ms.topic: reference
ms.date: 05/31/2018
---

# CostingComplete property

The **CostingComplete** property indicates whether the installer has completed disk space costing. This property can be used to author a dialog box triggered if costing has not been completed. The property is set dynamically during disk space costing and is set to 1 as soon as the costing is complete. This property is initialized to 0 by the [CostFinalize action](costfinalize-action.md).

## Remarks

For an example of how to author a "Please wait . . . " dialog box that pops up during disk space costing, see the section [Authoring a Conditional "Please wait . . ." Message Box](authoring-a-conditional-please-wait-------message-box.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




