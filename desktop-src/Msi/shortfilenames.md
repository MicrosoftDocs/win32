---
description: Setting the SHORTFILENAMES property causes short file names to be used for the names of target files, rather than long file names. It does not affect the file names the installer looks for at the source.
ms.assetid: b330f9c3-3297-45cf-915c-5fbb291b8afb
title: SHORTFILENAMES property
ms.topic: reference
ms.date: 05/31/2018
---

# SHORTFILENAMES property

Setting the **SHORTFILENAMES** property causes short file names to be used for the names of target files, rather than long file names. It does not affect the file names the installer looks for at the source.

## Default Value

Long names are used by the installer if the **SHORTFILENAMES** property is not set and the target volume supports long names. Short names are used by the installer if the target volume does not support long names.

## Remarks

When the **SHORTFILENAMES** property is set, the installer creates folders and installs files using short file names from any short\|long pairs listed in the [File table](file-table.md) or [Directory table](directory-table.md).

Applications can use the [**GetShortPathName**](/windows/win32/api/fileapi/nf-fileapi-getshortpathnamew) function to retrieve the short path form of a specified file path.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 
