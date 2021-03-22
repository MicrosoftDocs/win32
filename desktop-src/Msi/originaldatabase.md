---
description: The Windows Installer sets the OriginalDatabase property to the path of the installation database used to launch the installation.
ms.assetid: 985c70a4-1575-4226-a8c2-a7a21f7a0dbd
title: OriginalDatabase property
ms.topic: reference
ms.date: 05/31/2018
---

# OriginalDatabase property

The Windows Installer sets the **OriginalDatabase** property to the path of the installation database used to launch the installation. If the installation is launched from a command line, the value depends on whether the recache package option (the -v flag) is present in the [**REINSTALLMODE**](reinstallmode.md) property.



| Installation Method                                                                                                                                                                                  | OriginalDatabase Value                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| Any installation launched by invoking the path of the installation package (.msi file).                                                                                                              | Path to the installation package (.msi file). |
| Installation launched from a command line. The installation is not launched from a package path. The recache option (-v flag) is present in the [**REINSTALLMODE**](reinstallmode.md) property.     | Path to the database on the source.           |
| Installation launched from a command line. The installation is not launched from a package path. The recache option (-v flag) is not present in the [**REINSTALLMODE**](reinstallmode.md) property. | Path to the cached database.                  |



 

## Remarks

During a first time installation, a custom action sequenced before the [ResolveSource action](resolvesource-action.md) can use the **OriginalDatabase** property to determine the location of the installation source.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




