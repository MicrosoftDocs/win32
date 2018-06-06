---
Description: The MSIRESTARTMANAGERCONTROL Property specifies whether the Windows Installer package uses the Restart Manager or FilesInUse Dialog functionality.
ms.assetid: fefff18b-892a-440e-9f57-d23aeb99af74
title: MSIRESTARTMANAGERCONTROL property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSIRESTARTMANAGERCONTROL property

The **MSIRESTARTMANAGERCONTROL** Property specifies whether the Windows Installer package uses the [Restart Manager](https://www.bing.com/search?q=Restart+Manager) or [FilesInUse Dialog](filesinuse-dialog.md) functionality.

## Value



| Value                                                                                        | Meaning                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl>                 | This is the default value if the property is not set. Windows Installer always attempts to use the [Restart Manager](https://www.bing.com/search?q=Restart+Manager) on Windows Vista.<br/>                                                                                                                                                                                                       |
| <dl> <dt>"Disable"</dt> </dl>         | Disables interaction of the package with the [Restart Manager](https://www.bing.com/search?q=Restart+Manager). Windows Installer uses the [FilesInUse Dialog](filesinuse-dialog.md). <br/>                                                                                                                                                                                                      |
| <dl> <dt>"DisableShutdown"</dt> </dl> | Windows Installer uses the [FilesInUse Dialog](filesinuse-dialog.md). This setting disables attempts by the [Restart Manager](https://www.bing.com/search?q=Restart+Manager) to mitigate restarts when installing a Windows Installer package that has not been authored to use the Restart Manager. The installer still uses the Restart Manager to detect files in use by applications. <br/> |



 

## Remarks

The **MSIRESTARTMANAGERCONTROL** Property is ignored if the [Restart Manager](https://www.bing.com/search?q=Restart+Manager) is unavailable or disabled.

The value of this property can be modified using customization transforms or upgrades. Changing the value of this property from custom actions has no effect.

## Requirements



|                    |                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum service pack required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[DisableAutomaticApplicationShutdown](disableautomaticapplicationshutdown.md)
</dt> <dt>

[Not Supported in Windows Installer 3.1 and earlier versions](not-supported-in-windows-installer-version-3-1.md)
</dt> </dl>

 

 




