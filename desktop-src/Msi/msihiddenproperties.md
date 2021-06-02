---
description: The MsiHiddenProperties property may be used to prevent the installer from displaying passwords or other confidential information in the log file.
ms.assetid: 7d5eb9cf-04a5-41bd-9ca9-f30af45ab0a5
title: MsiHiddenProperties property
ms.topic: reference
ms.date: 05/31/2018
---

# MsiHiddenProperties property

The **MsiHiddenProperties** property may be used to prevent the installer from displaying passwords or other confidential information in the log file. To prevent a property from being written into the log file, set the value of the **MsiHiddenProperties** property to the name of the property you wish to hide. You can hide multiple properties by specifying a string of property names delimited by semicolons (;).

> [!Note]  
> When the [Debug](debug.md) policy is set to a value of 7, the installer will write information entered on a command line into the log. This makes public properties entered on a command line visible even if the property is included in the **MsiHiddenProperties** property. This can make confidential information entered on a command line visible in the log. For more information, see [Preventing Confidential Information from Being Written into the Log File](preventing-confidential-information-from-being-written-into-the-log-file.md).

 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




