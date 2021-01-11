---
description: The Win32\_WMISetting singleton WMI class contains the operational parameters for the WMI service. This class can only have one instance, which always exists for each Windows system and cannot be deleted. Additional instances cannot be created.
ms.assetid: d33cd4f3-969b-46ce-baff-466f1a464906
ms.tgt_platform: multiple
title: Win32_WMISetting class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_WMISetting
- Win32_WMISetting.Caption
- Win32_WMISetting.Description
- Win32_WMISetting.SettingID
- Win32_WMISetting.ASPScriptDefaultNamespace
- Win32_WMISetting.ASPScriptEnabled
- Win32_WMISetting.AutorecoverMofs
- Win32_WMISetting.AutoStartWin9X
- Win32_WMISetting.BackupInterval
- Win32_WMISetting.BackupLastTime
- Win32_WMISetting.BuildVersion
- Win32_WMISetting.DatabaseDirectory
- Win32_WMISetting.DatabaseMaxSize
- Win32_WMISetting.EnableAnonWin9xConnections
- Win32_WMISetting.EnableEvents
- Win32_WMISetting.EnableStartupHeapPreallocation
- Win32_WMISetting.HighThresholdOnClientObjects
- Win32_WMISetting.HighThresholdOnEvents
- Win32_WMISetting.InstallationDirectory
- Win32_WMISetting.LastStartupHeapPreallocation
- Win32_WMISetting.LoggingDirectory
- Win32_WMISetting.LoggingLevel
- Win32_WMISetting.LowThresholdOnClientObjects
- Win32_WMISetting.LowThresholdOnEvents
- Win32_WMISetting.MaxLogFileSize
- Win32_WMISetting.MaxWaitOnClientObjects
- Win32_WMISetting.MaxWaitOnEvents
- Win32_WMISetting.MofSelfInstallDirectory
api_type: 
- DllExport
api_location: 
- Wbemcore.dll
---

# Win32\_WMISetting class

The **Win32\_WMISetting** singleton [WMI class](../wmisdk/retrieving-a-class.md) contains the operational parameters for the WMI service. This class can only have one instance, which always exists for each Windows system and cannot be deleted. Additional instances cannot be created.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Singleton, Dynamic, Provider("WBEMCORE"), UUID("{A83EF166-CA8D-11d2-B33D-00104BCC4B4A}"), AMENDMENT]
class Win32_WMISetting : CIM_Setting
{
  string   Caption;
  string   Description;
  string   SettingID;
  string   ASPScriptDefaultNamespace = "\\\\root\\cimv2";
  boolean  ASPScriptEnabled;
  string   AutorecoverMofs[];
  uint32   AutoStartWin9X;
  uint32   BackupInterval;
  datetime BackupLastTime;
  string   BuildVersion;
  string   DatabaseDirectory;
  uint32   DatabaseMaxSize;
  boolean  EnableAnonWin9xConnections;
  boolean  EnableEvents;
  boolean  EnableStartupHeapPreallocation;
  uint32   HighThresholdOnClientObjects;
  uint32   HighThresholdOnEvents;
  string   InstallationDirectory;
  uint32   LastStartupHeapPreallocation;
  string   LoggingDirectory;
  uint32   LoggingLevel;
  uint32   LowThresholdOnClientObjects;
  uint32   LowThresholdOnEvents;
  uint32   MaxLogFileSize;
  uint32   MaxWaitOnClientObjects;
  uint32   MaxWaitOnEvents;
  string   MofSelfInstallDirectory;
};
```

## Members

The **Win32\_WMISetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_WMISetting** class has these properties.

<dl> <dt>

**ASPScriptDefaultNamespace**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\WBEM\\\\scripting\|Default Namespace")
</dt> </dl>

Default script namespace. This property contains the namespace used by calls from the Scripting API for WMI if none is specified by the caller.

This property reflects the value in the registry key.

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**WBEM**\\    **scripting\|Default Namespace**

Example: root\\cimv2

For an example script that uses this property, see the Remarks section.

</dd> <dt>

**ASPScriptEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\WBEM\\\\scripting\|Enable for ASP")
</dt> </dl>

If **True**, WMI scripting can be used on Active Server Pages (ASP). This property is valid on systems running unsupported versions of Windows only. For supported Windows systems, WMI scripting is always allowed on ASP.

</dd> <dt>

**AutorecoverMofs**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\WBEM\\\\CIMOM\|Autorecover MOFs")
</dt> </dl>

List of fully qualified MOF file names used to initialize or recover the WMI repository. The list determines the order in which MOF files are compiled.

This property reflects the value in the registry key.

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**WBEM**\\    **CIMOM\|Autorecover MOFs**

</dd> <dt>

**AutoStartWin9X**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\WBEM\\\\CIMOM\|AutostartWin9X")
</dt> </dl>

Not supported.

<dt>

<span id="Don_t_start"></span><span id="don_t_start"></span><span id="DON_T_START"></span>

**Don't start** (0)


</dt> <dd></dd> <dt>

<span id="Autostart"></span><span id="autostart"></span><span id="AUTOSTART"></span>

**Autostart** (1)


</dt> <dd></dd> <dt>

<span id="Start_on_reboot"></span><span id="start_on_reboot"></span><span id="START_ON_REBOOT"></span>

**Start on reboot** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**BackupInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\WBEM\\\\CIMOM\|Backup Interval Threshold"), [**Units**](../wmisdk/standard-qualifiers.md) ("minutes")
</dt> </dl>

Not supported. Instead, backup the WMI repository manually.

</dd> <dt>

**BackupLastTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Time Functions\|GetTimeZoneInformation")
</dt> </dl>

Date and time the last backup was performed.

</dd> <dt>

**BuildVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\WBEM\|Build")
</dt> </dl>

Version information for the currently installed WMI service.

Length of time that elapses between backups of the WMI database.

This property reflects the value in the registry key.

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**WBEM\|Build**

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

**DatabaseDirectory**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\WBEM\\\\CIMOM\|Repository Directory")
</dt> </dl>

Directory path that contains the WMI repository.

</dd> <dt>

**DatabaseMaxSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\WBEM\\\\CIMOM\|Max DB Size"), [**Units**](../wmisdk/standard-qualifiers.md) ("kilobytes")
</dt> </dl>

Maximum size of the WMI repository.

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

**EnableAnonWin9xConnections**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\WBEM\\\\CIMOM\|EnableAnonConnections")
</dt> </dl>

Not supported.

</dd> <dt>

**EnableEvents**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\WBEM\\\\CIMOM\|EnableEvents")
</dt> </dl>

If **True**, the WMI event subsystem should be enabled.

This property reflects the value in the registry key.

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**WBEM\|CIMOM\|EnableEvents**

</dd> <dt>

**EnableStartupHeapPreallocation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\WBEM\\\\CIMOM\|EnableStartupHeapPreallocation")
</dt> </dl>

If **True**, WMI creates a pre-allocated heap with the size of the **LastStartupHeapPreallocation** value when WMI is initialized.

</dd> <dt>

**HighThresholdOnClientObjects**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\WBEM\\\\CIMOM\|High Threshold On Client Objects"), [**Units**](../wmisdk/standard-qualifiers.md) ("objects per second")
</dt> </dl>

Maximum rate at which provider-created objects can be delivered to clients. To accommodate speed differentials between providers and clients, WMI holds objects in queues before delivering them to consumers. For more efficiency, consumers must collect the objects at a pace that matches the provider. If the memory held by uncollected objects reaches **LowThresholdOnObjects**, then WMI slows down the addition of new objects into the queue. If uncollected events continue to accumulate and the maximum wait to deliver events in **MaxWaitOnClientObjects** is reached while the memory used is at the value in **HighThresholdOnClientObjects**, then WMI accepts no more objects from providers and returns **WBEM\_E\_OUT\_OF\_MEMORY** to the clients.

</dd> <dt>

**HighThresholdOnEvents**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\WBEM\\\\CIMOM\|High Threshold On Events"), [**Units**](../wmisdk/standard-qualifiers.md) ("events per second")
</dt> </dl>

Maximum rate at which events are to be delivered to clients. To accommodate speed differentials between providers and clients, WMI queues events before delivering them to consumers. For more efficiency, consumers must collect the events at a pace that matches the provider. If the memory held by uncollected events reaches **LowThresholdOnObjects**, then WMI slows down the addition of new events into the queue. If uncollected events continue to accumulate and the maximum wait to deliver events in **MaxWaitOnEvents** is reached while the memory used is at the value in **HighThresholdOnEvents**, WMI accepts no more events from providers and returns **WBEM\_E\_OUT\_OF\_MEMORY** to the clients.

> [!Note]  
> Throttling is only done for Permanent Event consumers, so temporary consumers should not expect throttling when events get backed up in the WMI internal event queue.

 

This property reflects the value in the registry key.

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**WBEM**\\    **CIMOM\|High Threshold On Client Objects (B)**

</dd> <dt>

**InstallationDirectory**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\WBEM\|Installation Directory")
</dt> </dl>

Directory path where the WMI software has been installed. The default location is \\System32\\Wbem.

This property reflects the value in the registry key.

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**WBEM\|Installation Directory**

</dd> <dt>

**LastStartupHeapPreallocation**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\WBEM\\\\CIMOM\|LastStartupHeapPreallocation"), [**Units**](../wmisdk/standard-qualifiers.md) ("bytes")
</dt> </dl>

Size of the pre-allocated heap created by WMI during initialization.

This property reflects the value in the registry key.

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**WBEM\|CIMOM\|LastStartupHeapPreallocation**

</dd> <dt>

**LoggingDirectory**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\WBEM\\\\CIMOM\|Logging Directory")
</dt> </dl>

Directory path that contains the location of the WMI system log files.

This property reflects the value in the registry key.

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**WBEM\|CIMOM\|Logging Directory**

</dd> <dt>

**LoggingLevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\WBEM\\\\CIMOM\|Logging")
</dt> </dl>

Enabling of event logging and the verbosity level of logging used.

This property reflects the value in the registry key.

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**WBEM\|CIMOM\|Logging**

<dt>

<span id="Off"></span><span id="off"></span><span id="OFF"></span>

**Off** (0)


</dt> <dd></dd> <dt>

<span id="Error_logging"></span><span id="error_logging"></span><span id="ERROR_LOGGING"></span>

**Error logging** (1)


</dt> <dd></dd> <dt>

<span id="Verbose_Error_logging"></span><span id="verbose_error_logging"></span><span id="VERBOSE_ERROR_LOGGING"></span>

**Verbose Error logging** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**LowThresholdOnClientObjects**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\WBEM\\\\CIMOM\|Low Threshold On Client Objects"), [**Units**](../wmisdk/standard-qualifiers.md) ("objects per second")
</dt> </dl>

Rate at which WMI starts to slow the creation of new objects created for clients. To accommodate speed differentials between providers and clients, WMI holds objects in queues before delivering them to consumers. For more efficiency, consumers must collect the objects at a pace that matches the provider. If the rate of requests for objects reaches **LowThresholdOnClientObjects**, then WMI gradually slows down the creation of new objects to match the client's rate of use. This slowdown starts when the rate at which objects are being created exceeds the value of this property. See **HighThresholdOnClientObjects**.

This property reflects the registry value.

**KEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**WBEM**\\    **CIMOM\|High Threshold On Client Objects (B)**

</dd> <dt>

**LowThresholdOnEvents**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\WBEM\\\\CIMOM\|Low Threshold On Events"), [**Units**](../wmisdk/standard-qualifiers.md) ("events per second")
</dt> </dl>

Rate at which WMI starts to slow the delivery of new events. To accommodate speed differentials between providers and clients, WMI queues events before delivering them to consumers. For more efficiency, consumers must collect the objects at a pace that matches the provider. If the queue grows out of control, WMI throttles—slows down—the delivery of events gradually to align with the client rate. This slowdown starts when the rate at which events are generated exceeds the value of this property. See **HighThresholdOnEvents**.

> [!Note]  
> Throttling is only done for permanent event consumers, so temporary consumers should not expect throttling when events get backed up in the WMI internal event queue.

 

This property reflects the registry value.

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**WBEM**\\    **CIMOM\|High Threshold On Client Objects {B}**

</dd> <dt>

**MaxLogFileSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\WBEM\\\\CIMOM\|Log File Max Size"), [**Units**](../wmisdk/standard-qualifiers.md) ("bytes")
</dt> </dl>

Maximum size of the log files produced by the WMI service.

This property reflects the value in the registry key.

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**WBEM\|CIMOM\|Log File Max Size**

</dd> <dt>

**MaxWaitOnClientObjects**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\WBEM\\\\CIMOM\|Max Wait On Events"), [**Units**](../wmisdk/standard-qualifiers.md) ("milliseconds")
</dt> </dl>

Amount of time a newly created object waits to be used by the client before it is discarded and an error value is returned. This property interacts with the **LowThresholdOnClientObjects** and **HighThresholdOnClientObjects** properties to throttle—slow down—the delivery of objects to consumers when the consumer is receiving the objects too slowly.

</dd> <dt>

**MaxWaitOnEvents**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\WBEM\\\\CIMOM\|Max Wait On Events"), [**Units**](../wmisdk/standard-qualifiers.md) ("milliseconds")
</dt> </dl>

Amount of time for which an event sent to a client is queued before being discarded. This property interacts0 with **LowThresholdOnEvents** and **HighThresholdOnEvents** to throttle—slow down—the delivery of objects to consumers when the consumer is receiving the objects too slowly.

This property reflects the registry value.

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**WBEM**\\    **CIMOM\|Max Wait On Events (ms)**

</dd> <dt>

**MofSelfInstallDirectory**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|Software\\\\Microsoft\\\\WBEM\|MOF Self-Install Directory")
</dt> </dl>

Directory path for applications that install MOF files to the WMI repository. WMI automatically compiles any MOF files placed in this directory and, depending on its success, moves the MOF to a subdirectory labeled good or bad. If the \# [pragma autorecover](../wmisdk/pragma-autorecover.md) command is included, the fully qualified file name is added to the **AutorecoverMofs** list used when WMI is initializing or recovering the repository. The list determines the order in which MOFs are compiled.

This property reflects the value in the registry key.

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**WBEM\|CIMOM\|MOF Self=Install Directory**

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

</dd> </dl>

## Remarks

The **Win32\_WMISetting** class is derived from [**CIM\_Setting**](cim-setting.md). Only one instance of this class can exist on a computer.

Knowing how WMI is configured on a computer can be very useful when you are debugging scripts or troubleshooting problems with the WMI service itself. For example, many WMI scripts are written under the assumption that root\\cimv2 is the default namespace on the target computer. As a result, script writers who need to access a class in "Root\\CIMv2" often fail to include the namespace in the GetObject moniker, as shown in the following code sample:

`Set colServices = GetObject("winmgmts:").ExecQuery ("SELECT * FROM Win32_Service")`

If root\\cimv2 is not the default namespace on the target computer, this script will fail. To prevent this from happening, the namespace root\\cimv2 must be included in the moniker, as shown in the following code sample:

`Set colServices = GetObject("winmgmts:root\cimv2").ExecQuery("SELECT * FROM Win32_Service")`

If the default namespace on the target computer is different from the namespace assumed by a script, the script will fail. On top of that, the user will be presented with the somewhat misleading error message "Invalid class." In truth, the failure is not because the class is invalid but because the class cannot be found in the default namespace. This is a difficult problem to troubleshoot, because you are likely to investigate possible problems with the class rather than problems with the namespace that was (or, in this case, was not) specified.

You can use the **Win32\_WMISetting** class to determine how WMI has been configured on a computer. Configuration details such as the default namespace or the WMI build number can be useful in troubleshooting script problems. These settings also provide important administrative information such as how, or even whether, WMI errors are logged on a computer and which WMI providers will automatically be reloaded if you need to rebuild the WMI repository.

## Examples

The [Modify WMI Settings](https://Gallery.TechNet.Microsoft.Com/aa80d174-3592-4fed-9c50-11f34e541445) VBScript code example on the TechNet Gallery uses the **Win32\_WMISetting** class to configure the WMI backup interval and logging level.

The [List the Default Namespace](https://Gallery.TechNet.Microsoft.Com/3fc69acd-ead0-4dd1-9ea1-e15a7331cfa0) VBScript code example on the TechNet Gallery uses the **Win32\_WMISetting** class to retrieve and display the current WMI "Default namespace for scripting" setting.

The [Modify the Default WMI Namespace](https://Gallery.TechNet.Microsoft.Com/6dbb20e6-036d-43a2-ad6d-58325ada6a19) VBScript code example on the TechNet Gallery uses the **ASPScriptDefaultNamespace** property to set the WMI "Default namespace for scripting" setting to "root\\cimv2".

The [List All the WMI Settings](https://Gallery.TechNet.Microsoft.Com/29c04301-e9b2-46d1-8714-2dbb51014c92) VBSCript code example uses a number of properties on **Win32\_WMISetting** to return a list of WMI settings configured on a computer.

The [List WMI Setting Information](https://Gallery.TechNet.Microsoft.Com/0427cfde-4cd9-4a3d-9140-3bb622a1df5d) JavaScript code example uses a number of properties on **Win32\_WMISetting** to return a list of WMI settings configured on a computer.

The [List WMI Setting Information](https://Gallery.TechNet.Microsoft.Com/370e7fbe-ea3c-4290-8a56-1e38519f518d) Python code example uses a number of properties on **Win32\_WMISetting** to return a list of WMI settings configured on a computer.

The [List WMI Setting Information](https://Gallery.TechNet.Microsoft.Com/9309e4c5-2ca6-4662-9451-f1342d5171d2) Object REXX code example uses a number of properties on **Win32\_WMISetting** to return a list of WMI settings configured on a computer.

The following VBScript code example shows how to obtain the version of WMI running on the local computer. The "Win32\_WMISetting=@" indicates the single instance of the class. For more information, see WMI versions.


```VB
set objWMIService = GetObject("winmgmts:{impersonationLevel=Impersonate}!/Root/CIMv2")

set objWMISetting = objWMIService.Get("Win32_WMISetting=@")

WScript.Echo  objWMISetting.BuildVersion
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemcore.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Setting**](cim-setting.md)
</dt> <dt>

[WMI Service Management Classes](./wmi-service-management-classes.md)
</dt> </dl>

 

 
