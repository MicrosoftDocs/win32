---
description: The PATCHNEWPACKAGECODE property updates the Revision Number Summary property of an administrative image during patching.
ms.assetid: 5ca0058a-b4eb-48df-89eb-fbc7da7224e8
title: PATCHNEWPACKAGECODE property
ms.topic: reference
ms.date: 05/31/2018
---

# PATCHNEWPACKAGECODE property

The **PATCHNEWPACKAGECODE** property updates the [**Revision Number Summary**](revision-number-summary.md) property of an administrative image during patching. This property is only set by a transform in a .msp file. The .msp file must include a transform that adds this property to the [Property table](property-table.md) and sets its value. The installer then writes the value of **PATCHNEWPACKAGECODE** to the **Revision Number Summary** property.

## Remarks

The **PATCHNEWPACKAGECODE**, [**PATCHNEWSUMMARYCOMMENTS**](patchnewsummarycomments.md), and [**PATCHNEWSUMMARYSUBJECT**](patchnewsummarysubject.md) properties are used to update the summary information when a patch is installed to an administrative image.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




