---
Description: The installer sets the TempFolder property to the full path to the Temp folder.Authors should not need to set the TempFolder property.
ms.assetid: 841dd1b3-249c-49e1-b462-82da65b4b023
title: TempFolder property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TempFolder property

The installer sets the **TempFolder** property to the full path to the Temp folder.

Authors should not need to set the **TempFolder** property. Windows Installer uses the [**GetTempPath**](https://msdn.microsoft.com/en-us/library/Aa364992(v=VS.85).aspx) function to retrieve the path of the directory designated for temporary files and to set this property.

## Remarks

A common value for this property is C:\\Temp.

## Requirements



|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




