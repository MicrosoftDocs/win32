---
description: The Win32\_StartupCommand&\#8194;WMI class represents a command that runs automatically when a user logs onto the computer system.
ms.assetid: 7184ade8-fcc9-47b3-af04-8054b2fca937
ms.tgt_platform: multiple
title: Win32_StartupCommand class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_StartupCommand
- Win32_StartupCommand.Caption
- Win32_StartupCommand.Description
- Win32_StartupCommand.SettingID
- Win32_StartupCommand.Command
- Win32_StartupCommand.Location
- Win32_StartupCommand.Name
- Win32_StartupCommand.User
- Win32_StartupCommand.UserSID
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_StartupCommand class

The **Win32\_StartupCommand** [WMI class](../wmisdk/retrieving-a-class.md) represents a command that runs automatically when a user logs onto the computer system.

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

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (64)
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

Qualifiers: [**key**](../wmisdk/key-qualifier.md), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run")
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

Qualifiers: [**key**](../wmisdk/key-qualifier.md), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|\\\\SOFTWARE\\\\MICROSOFT\\\\WINDOWS\\\\CURRENTVERSION\\\\Windows")
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

Qualifiers: [**key**](../wmisdk/key-qualifier.md), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|File Structures\|[**WIN32\_FIND\_DATA**](/windows/win32/api/minwinbase/ns-minwinbase-win32_find_dataa)\|cFileName")
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

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (256)
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

Qualifiers: [**key**](../wmisdk/key-qualifier.md), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI")
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

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI")
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

The calling process that uses this class must have the **SE\_RESTORE\_NAME** privilege on the computer in which the registry resides. For example, if you enumerate this class on the local computer, the account under which your application runs must have this privilege. For more information, see [Executing Privileged Operations](../wmisdk/executing-privileged-operations.md).

You can change the registry values where **Win32\_StartupCommand** obtains data by calling the WMI [System Registry Provider](/previous-versions/windows/desktop/regprov/system-registry-provider) methods in script or in C++. For more information, see [Modifying the System Registry](../wmisdk/modifying-the-system-registry.md).

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



| Requirement | Value |
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

[Operating System Classes](./operating-system-classes.md)
</dt> </dl>

 

 
