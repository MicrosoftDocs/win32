---
description: The Date property is the current month, day, and year as a string of literal text in the format MM/DD/YYYY.
ms.assetid: 22c1f9b4-f6c9-4d57-8457-53bb045e2a4d
title: Date property
ms.topic: reference
ms.date: 05/31/2018
---

# Date property

The **Date** property is the current month, day, and year as a string of literal text in the format MM/DD/YYYY. For example, the date June 22, 2005 can represented as "06/22/2005". The format of the value depends upon the user's locale, and is the format obtained using [**GetDateFormat**](/windows/desktop/api/datetimeapi/nf-datetimeapi-getdateformata) with the DATE\_SHORTDATE option. The value of this property is set by the Windows Installer and not the package author.

## Remarks

Because this is a text string, it cannot be used in conditional expressions.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

