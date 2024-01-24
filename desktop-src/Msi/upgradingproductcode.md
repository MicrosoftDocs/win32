---
description: The UPGRADINGPRODUCTCODE property is set by Windows Installer when an upgrade removes an application.
ms.assetid: 903e4c22-e7ae-47bd-989b-d8c922de8d1a
title: UPGRADINGPRODUCTCODE property
ms.topic: reference
ms.date: 05/31/2018
---

# UPGRADINGPRODUCTCODE property

The **UPGRADINGPRODUCTCODE** property is set by Windows Installer when an upgrade removes an application. The installer sets this property when it runs the [RemoveExistingProducts action](removeexistingproducts-action.md). This property is not set by removing an application using the Add or Remove Programs in Control Panel. An application determines whether it is being removed by an upgrade or the Add or Remove Programs by checking **UPGRADINGPRODUCTCODE**.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




