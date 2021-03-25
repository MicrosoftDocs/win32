---
description: The EnableLog method of the Installer object enables logging of the selected message type for all subsequent installation sessions in the current process space.
ms.assetid: eb384587-0870-4812-866c-b483c1dfa841
title: Installer.EnableLog method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.EnableLog
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.EnableLog method

The **EnableLog** method of the [**Installer**](installer-object.md) object enables logging of the selected message type for all subsequent installation sessions in the current process space.

## Syntax


```JScript
Installer.EnableLog(
  logMode,
  logFile
)
```



## Parameters

<dl> <dt>

*logMode* 
</dt> <dd>

A required string that contains letters representing the message types to log. The string can be a combination of the following values.



| Value | Description                                                                                            |
|-------|--------------------------------------------------------------------------------------------------------|
| I     | Information-only messages.                                                                             |
| w     | Non-fatal warning messages.                                                                            |
| e     | Error messages that may be fatal errors.                                                               |
| f     | List of files in use that need to be replaced.                                                         |
| a     | Start of action notification.                                                                          |
| r     | Action data record containing content specific to action.                                              |
| u     | User request messages.                                                                                 |
| c     | UI initialization parameters.                                                                          |
| m     | Out-of-memory message.                                                                                 |
| v     | Sends large amounts of information to log file not generally useful to users. May be used for support. |
| p     | Dump property table; "property = value" at engine termination                                          |
| \+    | Append to existing log file.                                                                           |
| !     | Flush each line to the log file.                                                                       |
| x     | Extra debugging information. This option only available with Windows Server 2003.                      |
| o     | Out-of-disk-space messages.                                                                            |



 

</dd> <dt>

*logFile* 
</dt> <dd>

Required string containing the path to the log file to be created. Use an empty string ("") to turn off logging.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The path to the logfile location must already exist when using this method. The Installer does not create the directory structure for the logfile.

The logging options set using **EnableLog** override any existing Windows Installer logging policy settings.

Logging overwrites an existing log file by default. You must use the '+' letter in the logging mode to append to an existing log file.

The '!' option is not recommended because it can significantly slow installation. This option may be useful when debugging an installation.

The following sample script turns on verbose logging for an installation. At the end of the installation, the generated log file will be at c:\\temp\\install.log.


```VB
    Dim Installer
    Set Installer = CreateObject("WindowsInstaller.Installer")
    Installer.EnableLog "voicewarmup", "c:\temp\install.log"
    Installer.InstallProduct "\\server\share\products\sample\sample.msi"
```



## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[Windows Installer Logging](windows-installer-logging.md)
</dt> </dl>

 

 




