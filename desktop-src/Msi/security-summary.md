---
description: The Security Summary property conveys whether the package should be opened as read-only.
ms.assetid: f064b899-8123-49e1-b275-511186f49750
title: Security Summary property
ms.topic: reference
ms.date: 05/31/2018
---

# Security Summary property

The **Security Summary** property conveys whether the package should be opened as read-only. The database editing tool should not modify a read-only enforced database and should issue a warning at attempts to modify a read-only recommended database. The following values of this property are applicable to Windows Installer files.



| Value | Description           |
|-------|-----------------------|
| 0     | No restriction        |
| 2     | Read-only recommended |
| 4     | Read-only enforced    |



 

This property should be set to read-only recommended (2) for an installation database and to read-only enforced (4) for a transform or patch.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |



## See also

<dl> <dt>

[Summary Property Descriptions](summary-property-descriptions.md)
</dt> </dl>

 

 




