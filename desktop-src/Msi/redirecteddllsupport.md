---
description: The installer sets the RedirectedDLLSupport property if the system platform performing the installation supports Isolated Components.
ms.assetid: 703489c4-cac4-442c-bd96-d3927491a864
title: RedirectedDLLSupport property
ms.topic: reference
ms.date: 05/31/2018
---

# RedirectedDLLSupport property

The installer sets the **RedirectedDLLSupport** property if the system platform performing the installation supports [Isolated Components](isolated-components.md).

The installer sets the **RedirectedDLLSupport** property to a value of 1 if the system performing the installation supports [Isolated Components](isolated-components.md) based on .LOCAL files. The installer sets the **RedirectedDLLSupport** property to a value of 2 if the system that performs the installation supports isolation using either .LOCAL files or Win32 side-by-side assemblies.

The **RedirectedDLLSupport** property can be used to condition the [IsolateComponents action](isolatecomponents-action.md) in the [InstallUISequence table](installuisequence-table.md) or [InstallExecuteSequence table](installexecutesequence-table.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




