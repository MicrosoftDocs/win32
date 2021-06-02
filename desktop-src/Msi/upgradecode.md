---
description: The UpgradeCode property is a GUID representing a related set of products. The UpgradeCode is used in the Upgrade Table to search for related versions of the product that are already installed.This property is used by the RegisterProduct action.
ms.assetid: 6cdee5d8-8aa0-4fad-9338-152ee33b8077
title: UpgradeCode property
ms.topic: reference
ms.date: 05/31/2018
---

# UpgradeCode property

The **UpgradeCode** property is a GUID representing a related set of products. The **UpgradeCode** is used in the [Upgrade Table](upgrade-table.md) to search for related versions of the product that are already installed.

This property is used by the [RegisterProduct action](registerproduct-action.md).

## Remarks

It is strongly recommended that authors of installation packages specify an **UpgradeCode** for their application.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[Patching and Upgrades](patching-and-upgrades.md)
</dt> <dt>

[Preparing an Application for Future Major Upgrades](preparing-an-application-for-future-major-upgrades.md)
</dt> </dl>

 

 




