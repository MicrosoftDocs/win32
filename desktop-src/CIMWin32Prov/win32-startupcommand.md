---
Description: The Win32\_StartupCommand&\#8194;WMI class represents a command that runs automatically when a user logs onto the computer system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7184ade8-fcc9-47b3-af04-8054b2fca937
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_StartupCommand class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_StartupCommand class

The **Win32\_StartupCommand** [WMI class](https://msdn.microsoft.com/cfe4bcca-692e-45cd-a840-93ebfe4ae267) represents a command that runs automatically when a user logs onto the computer system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), Privileges("SeRestorePrivilege"), UUID("{8502C50A-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_StartupCommand : CIM_Setting
{
  string Caption;
  string Description;
  string SettingID;
  string Command;
  string Location;
  string Name;
  string User;
  string UserSID;
};
```

## Members

The **Win32\_StartupCommand** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_StartupCommand** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) (64)
</dt> </dl>

Short textual description of the current object.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**Command**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/838d295f-e812-4e46-99a4-d2714a0ae8dc), [**MappingStrings**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32Registry\|SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run")
</dt> </dl>

Command run by the startup command.

WMI obtains this data from the registry key

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**Windows**\\**CurrentVersion**\\**Run**

Example: "C:\\Windows\\notepad.exe myfile.txt"

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the current object.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**Location**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/838d295f-e812-4e46-99a4-d2714a0ae8dc), [**MappingStrings**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32Registry\|\\\\SOFTWARE\\\\MICROSOFT\\\\WINDOWS\\\\CURRENTVERSION\\\\Windows")
</dt> </dl>

Path where the startup command resides on the disk file system.

For example: HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run

<dt>

<span id="Startup"></span><span id="startup"></span><span id="STARTUP"></span>

**Startup** ("Startup")


</dt> <dd></dd> <dt>

<span id="Common_Startup"></span><span id="common_startup"></span><span id="COMMON_STARTUP"></span>

**Common Startup** ("Common Startup")


</dt> <dd></dd> <dt>

<span id="HKLM__SOFTWARE__Microsoft__Windows__CurrentVersion__Run"></span><span id="hklm__software__microsoft__windows__currentversion__run"></span><span id="HKLM__SOFTWARE__MICROSOFT__WINDOWS__CURRENTVERSION__RUN"></span>

**HKLM\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run** ("HKLM\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run")


</dt> <dd></dd> <dt>

<span id="HKLM__SOFTWARE__Microsoft__Windows__CurrentVersion__RunServices"></span><span id="hklm__software__microsoft__windows__currentversion__runservices"></span><span id="HKLM__SOFTWARE__MICROSOFT__WINDOWS__CURRENTVERSION__RUNSERVICES"></span>

**HKLM\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\RunServices** ("HKLM\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\RunServices")


</dt> <dd></dd> </dl>

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/838d295f-e812-4e46-99a4-d2714a0ae8dc), [**MappingStrings**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("Win32API\|File Structures\|[**WIN32\_FIND\_DATA**](https://msdn.microsoft.com/eb700d84-0ba5-4af8-a619-2d2544560dbc)\|cFileName")
</dt> </dl>

File name of the startup command.

Example: "FindFast"

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) (256)
</dt> </dl>

Identifier by which the current object is known.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**User**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/838d295f-e812-4e46-99a4-d2714a0ae8dc), [**MappingStrings**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("WMI")
</dt> </dl>

User name for whom this startup command will run.

Example: "mydomain\\myname"

</dd> <dt>

**UserSID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/671ea769-f68d-4788-96f5-c4f86ab3b00e) ("WMI")
</dt> </dl>

The UserSID property indicates the SID of the user for whom this startup command will run. That User property may be empty but UserSID still has a value if the user name can't be resolved (like in the case of a deleted user). The property is helpful to distinguish between commands associated w/ two different users with unresolved names. It may be NULL when the command is associated with items not actually identifying a user like All Users.

Example:S-1-5-21-1579938362-1064596589-3161144252-1006

</dd> </dl>

## Remarks

The **Win32\_StartupCommand** class is derived from [**CIM\_Setting**](cim-setting.md).

Computer startup does not end after the operating system has been loaded. Instead, the Windows operating system can be configured so that startup commands are run each time Windows starts. Startup commands are stored in the registry or as part of the user profile and are used to automatically start specified scripts or applications each time Windows is loaded.

In most cases, autostart programs are useful; they ensure that certain applications, such as antivirus tools, are automatically started and run each time Windows is loaded. However, autostart programs also can be responsible for problems such as:

-   Computers that take an exceptionally long time to start. This might be the result of a large number of applications that must be started each time Windows starts.
-   Applications that are represented in the Taskbar or in Task Manager, even though the user did not start them. Although these applications do not necessarily cause problems, they can result in help desk calls from users who are confused as to where these programs came from and why they are running.
-   Computers experiencing problems even when they seem idle. These problems are often traced to startup commands that are running when no one is aware that they are running.

Identifying the applications and scripts that automatically run at startup is an important but difficult administrative task, because startup commands can be stored in many different locations:

-   HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run
-   HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce
-   HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run
-   HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce
-   HKU\\ProgID\\Software\\Microsoft\\Windows\\CurrentVersion\\Run
-   systemdrive\\Documents and Settings\\All Users\\Start Menu\\Programs\\Startup
-   systemdrive\\Documents and Settings\\username\\Start Menu\\Programs\\Startup

You can use the WMI Win32\_StartupCommand class to enumerate autostart programs regardless of where the information is stored.

The calling process that uses this class must have the **SE\_RESTORE\_NAME** privilege on the computer in which the registry resides. For example, if you enumerate this class on the local computer, the account under which your application runs must have this privilege. For more information, see [Executing Privileged Operations](https://msdn.microsoft.com/11bb8723-f329-4083-8219-2256ce44a5e3).

You can change the registry values where **Win32\_StartupCommand** obtains data by calling the WMI [System Registry Provider](https://msdn.microsoft.com/39323619-82db-45d3-b20e-4ba1d4c11388) methods in script or in C++. For more information, see [Modifying the System Registry](https://msdn.microsoft.com/e16a5d4c-46a0-4798-894d-0af4cfa18f22).

## Examples

The following VBScript enumerates the startup commands on a computer.


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:" _
 & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colStartupCommands = objWMIService.ExecQuery _
 ("SELECT * FROM Win32_StartupCommand")
For Each objStartupCommand in colStartupCommands
 Wscript.Echo "Command: " & objStartupCommand.Command
 Wscript.Echo "Description: " & objStartupCommand.Description
 Wscript.Echo "Location: " & objStartupCommand.Location
 Wscript.Echo "Name: " & objStartupCommand.Name
 Wscript.Echo "SettingID: " & objStartupCommand.SettingID
 Wscript.Echo "User: " & objStartupCommand.User
Next
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Setting**](cim-setting.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/windows/desktop/D0756D8C-A3D3-4C75-96A3-8C7F05300B39)
</dt> </dl>

 

 




