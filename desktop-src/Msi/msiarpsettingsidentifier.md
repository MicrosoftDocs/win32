---
description: The MSIARPSETTINGSIDENTIFIER property contains a semi-colon delimited list of the registry locations where the application stores a user's settings and preferences.
ms.assetid: 524ba004-d3a2-4619-8c98-362761a3ae7a
title: MSIARPSETTINGSIDENTIFIER property
ms.topic: reference
ms.date: 05/31/2018
---

# MSIARPSETTINGSIDENTIFIER property

The **MSIARPSETTINGSIDENTIFIER** property contains a semi-colon delimited list of the registry locations where the application stores a user's settings and preferences. During an operating system upgrade, setup can use this information to improve the experience of users who are migrating applications.

The value of the **MSIARPSETTINGSIDENTIFIER** property is literal text that contains the list of registry locations where the application stores its settings. The value can specify multiple possible registry locations. Separate multiple registry locations by using semi-colons. Application settings are typically stored in the **HKCU** or **HKLM** registry hives in the form: *Company\\Application\\Version*. The following example is a possible value for the **MSIARPSETTINGSIDENTIFIER** property.

*MyCompany\\AppSuite\\1.0;MyCompany\\App1\\1.0;MyCompany\\App2\\1.0*

This property is optional and can be set in the [Property](property-table.md) table. If this property appears in the Property table, the value must not be set to **NULL**.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer 4.5 on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[Not Supported in Windows Installer 3.1 and earlier versions](not-supported-in-windows-installer-version-3-1.md)
</dt> </dl>

 

 




