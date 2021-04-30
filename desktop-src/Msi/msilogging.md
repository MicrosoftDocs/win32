---
description: The MsiLogging property sets the default logging mode for the Windows Installer package.
ms.assetid: f5ae389e-bc27-465d-886b-4f4f41d49118
title: MsiLogging property
ms.topic: reference
ms.date: 05/31/2018
---

# MsiLogging property

The **MsiLogging** property sets the default logging mode for the Windows Installer package. If this optional property is present in the [Property table](property-table.md), the installer generates a log file named MSI\*.LOG. The full path to the log file is given by the value of the [**MsiLogFileLocation**](msilogfilelocation.md) property.

## Value

The value of this property should be a string of the following characters that specify the default logging mode.



| Value                                                                        | Meaning                                                                        |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <dl> <dt>I</dt> </dl> | Status messages.<br/>                                                    |
| <dl> <dt>w</dt> </dl> | Nonfatal warnings.<br/>                                                  |
| <dl> <dt>e</dt> </dl> | All error messages.<br/>                                                 |
| <dl> <dt>a</dt> </dl> | Start up of actions.<br/>                                                |
| <dl> <dt>r</dt> </dl> | Action-specific records.<br/>                                            |
| <dl> <dt>u</dt> </dl> | User requests.<br/>                                                      |
| <dl> <dt>c</dt> </dl> | Initial UI parameters.<br/>                                              |
| <dl> <dt>m</dt> </dl> | Out-of-memory or fatal exit information.<br/>                            |
| <dl> <dt>o</dt> </dl> | Out-of-disk-space messages.<br/>                                         |
| <dl> <dt>p</dt> </dl> | Terminal properties.<br/>                                                |
| <dl> <dt>v</dt> </dl> | Verbose output.<br/>                                                     |
| <dl> <dt>x</dt> </dl> | Extra debugging information. Only available on Windows Server 2003.<br/> |
| <dl> <dt>!</dt> </dl> | Flush each line to the log.<br/>                                         |



 

## Remarks

This property is available starting with Windows Installer 4.0.

You cannot use the "+" and "\*" values of the /L option in the value of the **MsiLogging** property.

The logging mode can be set using policy, a command-line option, or programmatically. This overrides the default logging mode. For more information about all the methods that are available for setting the logging mode, see [Normal Logging](normal-logging.md) in the [Windows Installer Logging](windows-installer-logging.md) section.

If the **MsiLogging** property is present in the [Property table](property-table.md), the default logging mode of the package can be modified by changing the value of this property using a [database transform](database-transforms.md). The default logging mode cannot be changed using a [Patch Package](patch-packages.md) (a .msp file.)

If the **MsiLogging** property has been set in the [Property table](property-table.md), the default logging mode for all users of the computer can be specified by setting both the [DisableLoggingFromPackage](disableloggingfrompackage.md) policy and [Logging](logging.md) policy. Setting both the DisableLoggingFromPackage policy and Logging policy will override the **MsiLogging** property for all packages.

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

 

 




