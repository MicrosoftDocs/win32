---
Description: On Windows 2000 and later operating systems, the installer sets the MsiNTSuiteSmallBusiness property to 1 if Microsoft Small Business Server is installed.
ms.assetid: 9ac578b9-316f-413c-aae0-4f414109583b
title: MsiNTSuiteSmallBusiness property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MsiNTSuiteSmallBusiness property

On Windows 2000 and later operating systems, the installer sets the **MsiNTSuiteSmallBusiness** property to 1 if Microsoft Small Business Server is installed. The installer sets this property to 1 only if the VER\_SUITE\_SMALLBUSINESS flag is set in the [**OSVERSIONINFOEX**](https://msdn.microsoft.com/4ab07a72-404d-459b-b061-b3b06b5db37e) structure. Otherwise the installer does not set this property.

## Requirements



|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




