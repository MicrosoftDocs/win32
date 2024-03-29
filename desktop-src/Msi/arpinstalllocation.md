---
description: The ARPINSTALLLOCATION property is the full path to the application's primary folder.
ms.assetid: f4635241-ac18-4bc5-b043-c6e42c0b456e
title: ARPINSTALLLOCATION property
ms.topic: reference
ms.date: 05/31/2018
---

# ARPINSTALLLOCATION property

The **ARPINSTALLLOCATION** property is the full path to the application's primary folder.

## Remarks

This property enables application backup and restore; in that scenario, it's used to associate **Start** menu shortcuts (based on their targets pointing into this location) with the product that created them. That can be done statically, or via a custom action.

## Requirements
| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.|

## See also

* [Properties](properties.md)
