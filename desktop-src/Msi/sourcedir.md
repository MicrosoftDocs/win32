---
Description: The SourceDir property is the root directory that contains the source cabinet file or the source file tree of the installation package. This value is used for directory resolution.
ms.assetid: 79c7c5eb-b212-4dbf-943a-00ebd6037ce1
title: SourceDir property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SourceDir property

The **SourceDir** property is the root directory that contains the source cabinet file or the source file tree of the installation package. This value is used for directory resolution.

## Default Value

The directory that contains the installation package.

## Remarks

The [ResolveSource action](resolvesource-action.md) must be called before using the **SourceDir** property in any expression or attempting to retrieve the value of **SourceDir** with [**MsiGetProperty**](/windows/desktop/api/Msiquery/nf-msiquery-msigetpropertya). The ResolveSource action should not be run while the source is unavailable, such as when uninstalling an application, because this can cause an unintended prompt for the source media.

## Requirements



|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




