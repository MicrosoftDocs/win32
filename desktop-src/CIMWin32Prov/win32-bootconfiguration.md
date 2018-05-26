---
Description: The Win32\_BootConfiguration WMI class represents the boot configuration of a computer system running Windows.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c2db28dd-3feb-44bb-a532-c91cab980ba3
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_BootConfiguration class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_BootConfiguration class

The **Win32\_BootConfiguration** [WMI class](https://msdn.microsoft.com/library/aa393244) represents the boot configuration of a computer system running Windows.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C4E2-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_BootConfiguration : CIM_Setting
{
  string Caption;
  string Description;
  string SettingID;
  string BootDirectory;
  string ConfigurationPath;
  string LastDrive;
  string Name;
  string ScratchDirectory;
  string TempDirectory;
};
```

## Members

The **Win32\_BootConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_BootConfiguration** class has these properties.

<dl> <dt>

**BootDirectory**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Win32API\|Process and Thread Functions\|[**GetEnvironmentVariable**](https://msdn.microsoft.com/library/windows/desktop/ms683188)\|WinBootDir")
</dt> </dl>

Path to the system files required for booting the system.

Example: "C:\\Windows"

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

Short textual description of the current object.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**ConfigurationPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Win32API\|Process and Thread Functions\|[**GetEnvironmentVariable**](https://msdn.microsoft.com/library/windows/desktop/ms683188)\|WinBootDir")
</dt> </dl>

Path to the configuration files. This value may be similar to the value in the **BootDirectory** property.

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

**LastDrive**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Win32API\|File Functions\|GetDriveType")
</dt> </dl>

Last drive letter to which a physical drive is assigned.

Example: "E:"

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("WMI")
</dt> </dl>

Name of the boot configuration. It is an identifier for the boot configuration.

</dd> <dt>

**ScratchDirectory**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Win32API\|File Functions\|GetTempPath")
</dt> </dl>

Directory where temporary files can reside during boot time.

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

Identifier by which the current object is known.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**TempDirectory**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("Win32API\|File Functions\|GetTempPath")
</dt> </dl>

Directory where temporary files are stored.

Example: "C:\\TEMP"

</dd> </dl>

## Remarks

The **Win32\_BootConfiguration** class is derived from [**CIM\_Setting**](cim-setting.md).

## Examples

The [List the Boot Configuration Properties of a Computer](https://Gallery.TechNet.Microsoft.Com/55c35de3-bb6a-47f0-89f9-d2c49ab4cf19) Perl sample returns boot configuration information for a computer.

The following VBScript sample returns boot configuration information for a computer.


```VB
On Error Resume Next 
 
strComputer = "." 
Set objWMIService = GetObject("winmgmts:" _ 
    & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2") 
 
Set colItems = objWMIService.ExecQuery("Select * from Win32_BootConfiguration") 
 
For Each objItem in colItems 
    Wscript.Echo "Boot Directory: " & objItem.BootDirectory 
    Wscript.Echo "Configuration Path: " & objItem.ConfigurationPath 
    Wscript.Echo "Description: " & objItem.Description 
    Wscript.Echo "Last Drive: " & objItem.LastDrive 
    Wscript.Echo "Name: " & objItem.Name 
    Wscript.Echo "Scratch Directory: " & objItem.ScratchDirectory 
    Wscript.Echo "Setting ID: " & objItem.SettingID 
    Wscript.Echo "Temp Directory: " & objItem.TempDirectory 
Next 
```



The following code sample demonstrates the use of the **Win32\_BootConfiguration** WMI class.


```PowerShell
# Get Boot configuration from WMI

$boot = Get-WMIObject Win32_BootConfiguration

# Display information

"Boot Directory     : {0}" -f $boot.bootdirectory
"Caption            : {0}" -f $boot.caption
"Description        : {0}" -f $boot.description
"Last Drive         : {0}" -f $boot.lastdrive
"Scratch Directory  : {0}" -f $boot.scratchdirectory
"Temp Directory     : {0}" -f $boot.tempdirectory

```



The previous code sample creates the following output:

``` syntax
Boot Directory     : \WINDOWS
Caption            : \Device\Harddisk0\Partition1
Description        : \Device\Harddisk0\Partition1
Last Drive         : K:
Scratch Directory  : C:\WINDOWS\system32\config\systemprofile\Local Settings\Temp
Temp Directory     : C:\WINDOWS\system32\config\systemprofile\Local Settings\Temp
```

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Setting**](cim-setting.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> </dl>

 

 




