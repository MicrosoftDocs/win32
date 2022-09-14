---
description: The Time property is the current time in hours, minutes, and seconds as a string of literal text in the format HH:MM:SS using a 24 hour clock.
ms.assetid: 6f487e46-e178-4d41-b6fa-7c16aa1c46fd
title: Time property
ms.topic: reference
ms.date: 05/31/2018
---

# Time property

The **Time** property is the current time in hours, minutes, and seconds as a string of literal text in the format HH:MM:SS using a 24 hour clock. For example, the time 6:57 p.m. is represented by "18:57:00". The format of the value depends upon the user's locale, and is the format obtained using [**GetTimeFormat**](/windows/win32/api/datetimeapi/nf-datetimeapi-gettimeformata) function with the TIME\_FORCE24HOURFORMAT \| TIME\_NOTIMEMARKER option. The value of this property is set by the Windows Installer and not the package author.

## Remarks

Because this is a text string, it cannot be used in conditional expressions.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 
