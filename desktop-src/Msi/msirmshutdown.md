---
description: The MSIRMSHUTDOWN property determines how applications or services that are currently using files affected by an update should be shut down to enable the installation of the update.
ms.assetid: 6763a490-8d1a-42d2-a8cb-0743b7ba6866
title: MSIRMSHUTDOWN property
ms.topic: reference
ms.date: 05/31/2018
---

# MSIRMSHUTDOWN property

The **MSIRMSHUTDOWN** property determines how applications or services that are currently using files affected by an update should be shut down to enable the installation of the update.

## Value



| Value                                                                        | Meaning                                                                                                                                                                                                                                                                 |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | Processes or services that are currently using files affected by the update are shut down.<br/>                                                                                                                                                                   |
| <dl> <dt>1</dt> </dl> | Processes or services that are currently using files affected by the update, and that do not respond to the [Restart Manager](../rstmgr/restart-manager-portal.md), are forced to shut down.<br/>                                                                                       |
| <dl> <dt>2</dt> </dl> | Processes or services that are currently using files affected by the update are shut down only if they have all been registered for a restart. If any process or service has not been registered for a restart, then no processes or services are shut down.<br/> |



 

## Remarks

The **MSIRMSHUTDOWN** property is ignored if the [Restart Manager](../rstmgr/restart-manager-portal.md) is unavailable or disabled.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum service pack required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[Not Supported in Windows Installer 3.1 and earlier versions](not-supported-in-windows-installer-version-3-1.md)
</dt> </dl>

 

 
