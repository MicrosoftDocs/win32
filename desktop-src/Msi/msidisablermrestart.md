---
Description: The MSIDISABLERMRESTART property determines how applications or services that are currently using files affected by an update should be shut down and restarted to enable the installation of the update.
ms.assetid: 45c804bf-6d15-416a-b106-d8bb3f4c547d
title: MSIDISABLERMRESTART property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSIDISABLERMRESTART property

The **MSIDISABLERMRESTART** property determines how applications or services that are currently using files affected by an update should be shut down and restarted to enable the installation of the update.

## Value



| Value                                                                        | Meaning                                                                                                                                                                                      |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | All system services that were shut down to install the update are restarted. All applications that registered themselves with the [Restart Manager](https://msdn.microsoft.com/en-us/library/Cc948910(v=VS.85).aspx) are restarted.<br/> |
| <dl> <dt>1</dt> </dl> | Processes that were shut down using the [Restart Manager](https://msdn.microsoft.com/en-us/library/Cc948910(v=VS.85).aspx) while installing the update will not be restarted after the update is applied.<br/>                           |



 

## Remarks

The **MSIDISABLERMRESTART** Property is ignored if the [Restart Manager](https://msdn.microsoft.com/en-us/library/Cc948910(v=VS.85).aspx) is unavailable or disabled.

## Requirements



|                    |                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum service pack required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[Not Supported in Windows Installer 3.1 and earlier versions](not-supported-in-windows-installer-version-3-1.md)
</dt> </dl>

 

 




