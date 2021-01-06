---
description: The Win32\_OSRecoveryConfiguration&\#8194;WMI class represents the types of information that will be gathered from memory when the operating system fails. This includes boot failures and system crashes.
ms.assetid: 0c8a2aeb-2fd9-44b7-8f91-d19afb8d2de6
ms.tgt_platform: multiple
title: Win32_OSRecoveryConfiguration class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_OSRecoveryConfiguration
- Win32_OSRecoveryConfiguration.Caption
- Win32_OSRecoveryConfiguration.Description
- Win32_OSRecoveryConfiguration.SettingID
- Win32_OSRecoveryConfiguration.AutoReboot
- Win32_OSRecoveryConfiguration.DebugFilePath
- Win32_OSRecoveryConfiguration.DebugInfoType
- Win32_OSRecoveryConfiguration.ExpandedDebugFilePath
- Win32_OSRecoveryConfiguration.ExpandedMiniDumpDirectory
- Win32_OSRecoveryConfiguration.KernelDumpOnly
- Win32_OSRecoveryConfiguration.MiniDumpDirectory
- Win32_OSRecoveryConfiguration.Name
- Win32_OSRecoveryConfiguration.OverwriteExistingDebugFile
- Win32_OSRecoveryConfiguration.SendAdminAlert
- Win32_OSRecoveryConfiguration.WriteDebugInfo
- Win32_OSRecoveryConfiguration.WriteToSystemLog
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_OSRecoveryConfiguration class

The **Win32\_OSRecoveryConfiguration** [WMI class](../wmisdk/retrieving-a-class.md) represents the types of information that will be gathered from memory when the operating system fails. This includes boot failures and system crashes.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), SupportsUpdate, UUID("{8502C4E8-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_OSRecoveryConfiguration : CIM_Setting
{
  string  Caption;
  string  Description;
  string  SettingID;
  boolean AutoReboot;
  string  DebugFilePath;
  uint32  DebugInfoType;
  string  ExpandedDebugFilePath;
  string  ExpandedMiniDumpDirectory;
  boolean KernelDumpOnly;
  string  MiniDumpDirectory;
  string  Name;
  boolean OverwriteExistingDebugFile;
  boolean SendAdminAlert;
  boolean WriteDebugInfo;
  boolean WriteToSystemLog;
};
```

## Members

The **Win32\_OSRecoveryConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_OSRecoveryConfiguration** class has these properties.

<dl> <dt>

**AutoReboot**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|SYSTEM\\\\CurrentControlSet\\\\Control\\\\CrashControl\|AutoReboot")
</dt> </dl>

System will automatically reboot during a recovery operation.

</dd> <dt>

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

**DebugFilePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|SYSTEM\\\\CurrentControlSet\\\\Control\\\\CrashControl\|DumpFile")
</dt> </dl>

Full path to the debug file. A debug file is created with the memory state of the computer after a computer failure.

Example: "C:\\Windows\\Memory.dmp"

</dd> <dt>

**DebugInfoType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Type of debugging information written to the log file.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (0)


</dt> <dd></dd> <dt>

<span id="Complete_memory_dump"></span><span id="complete_memory_dump"></span><span id="COMPLETE_MEMORY_DUMP"></span>

**Complete memory dump** (1)


</dt> <dd></dd> <dt>

<span id="Kernel_memory_dump"></span><span id="kernel_memory_dump"></span><span id="KERNEL_MEMORY_DUMP"></span>

**Kernel memory dump** (2)


</dt> <dd></dd> <dt>

<span id="Small_memory_dump"></span><span id="small_memory_dump"></span><span id="SMALL_MEMORY_DUMP"></span>

**Small memory dump** (3)


</dt> <dd></dd> </dl>

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

**ExpandedDebugFilePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Expanded version of the **DebugFilePath** property.

Example: "C:\\Windows\\Memory.dmp"

</dd> <dt>

**ExpandedMiniDumpDirectory**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Expanded version of the **MiniDumpDirectory** property.

Example: "C:\\Windows\\MiniDump"

</dd> <dt>

**KernelDumpOnly**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**DEPRECATED**](../wmisdk/standard-wmi-qualifiers.md), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|SYSTEM\\\\CurrentControlSet\\\\Control\\\\CrashControl\|KernelDumpOnly")
</dt> </dl>

Only kernel debug information will be written to the debug log file. If **TRUE**, then only the state of the kernel is written to a file in the event of a system failure. If **FALSE**, the system will try to log the state of the memory, and any devices that can provide information about the system when it failed.

</dd> <dt>

**MiniDumpDirectory**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|SYSTEM\\\\CurrentControlSet\\\\Control\\\\CrashControl\|MiniDumpDir")
</dt> </dl>

Directory where small memory dump files will be recorded and accumulated.

Example: "%systemRoot%\\MiniDump"

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](../wmisdk/key-qualifier.md), [**MaxLen**](../wmisdk/standard-qualifiers.md) (256), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI")
</dt> </dl>

Identifying name for this instance of the **Win32\_OSRecoveryConfiguration** class.

</dd> <dt>

**OverwriteExistingDebugFile**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|SYSTEM\\\\CurrentControlSet\\\\Control\\\\CrashControl\|Overwrite")
</dt> </dl>

New debug file will overwrite an existing one.

</dd> <dt>

**SendAdminAlert**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|SYSTEM\\\\CurrentControlSet\\\\Control\\\\CrashControl\|SendAlert")
</dt> </dl>

Alert message will be sent to the system administrator in the event of an operating system failure.

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

**WriteDebugInfo**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**DEPRECATED**](../wmisdk/standard-wmi-qualifiers.md), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|SYSTEM\\\\CurrentControlSet\\\\Control\\\\CrashControl\|CrashDumpEnabled")
</dt> </dl>

Debugging information is to be written to a log file.

</dd> <dt>

**WriteToSystemLog**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|SYSTEM\\\\CurrentControlSet\\\\Control\\\\CrashControl\|LogEvent")
</dt> </dl>

Events will be written to a system log.

</dd> </dl>

## Remarks

The **Win32\_OSRecoveryConfiguration** class is derived from [**CIM\_Setting**](cim-setting.md).

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

 

 
