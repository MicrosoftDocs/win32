---
title: DfsrMachineConfig class
description: This class provides service-wide settings on the local computer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1b5d2542-77a5-4d0b-895c-92a3ccad6cbd
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DfsrMachineConfig class Distributed File System Replication
- DfsrMachineConfig class Distributed File System Replication , described
topic_type:
- apiref
api_name:
- DfsrMachineConfig
- DfsrMachineConfig.Caption
- DfsrMachineConfig.SettingID
- DfsrMachineConfig.LastChangeNumber
- DfsrMachineConfig.LastChangeTime
- DfsrMachineConfig.LastChangeSource
- DfsrMachineConfig.Description
- DfsrMachineConfig.EnableDebugLog
- DfsrMachineConfig.DebugLogFilePath
- DfsrMachineConfig.MaxDebugLogFiles
- DfsrMachineConfig.DebugLogSeverity
- DfsrMachineConfig.MaxDebugLogMessages
- DfsrMachineConfig.DsPollingIntervalInMin
- DfsrMachineConfig.EnableLightDSPolling
- DfsrMachineConfig.RpcPortAssignment
- DfsrMachineConfig.ReghostingRateInMin
- DfsrMachineConfig.RootLowWatermarkPercent
- DfsrMachineConfig.RootHighWatermarkPercent
- DfsrMachineConfig.StagingLowWatermarkPercent
- DfsrMachineConfig.StagingHighWatermarkPercent
- DfsrMachineConfig.ConflictLowWatermarkPercent
- DfsrMachineConfig.ConflictHighWatermarkPercent
- DfsrMachineConfig.MaxOfflineTimeInDays
- DfsrMachineConfig.StopReplicationOnAutoRecovery
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DfsrMachineConfig class

This class provides service-wide settings on the local computer.

## Syntax

``` syntax
[Dynamic, Provider("DfsrConfigProv"), Singleton]
class DfsrMachineConfig : CIM_Setting
{
  string   Caption;
  string   SettingID;
  uint32   LastChangeNumber;
  datetime LastChangeTime;
  string   LastChangeSource;
  string   Description;
  boolean  EnableDebugLog;
  string   DebugLogFilePath;
  uint32   MaxDebugLogFiles;
  uint32   DebugLogSeverity;
  uint32   MaxDebugLogMessages;
  uint32   DsPollingIntervalInMin;
  boolean  EnableLightDSPolling;
  uint32   RpcPortAssignment;
  uint32   ReghostingRateInMin;
  uint32   RootLowWatermarkPercent;
  uint32   RootHighWatermarkPercent;
  uint32   StagingLowWatermarkPercent;
  uint32   StagingHighWatermarkPercent;
  uint32   ConflictLowWatermarkPercent;
  uint32   ConflictHighWatermarkPercent;
  uint32   MaxOfflineTimeInDays;
  boolean  StopReplicationOnAutoRecovery;
};
```

## Members

The **DfsrMachineConfig** class has these types of members:

-   [Properties](#properties)

### Properties

The **DfsrMachineConfig** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

Short textual description of the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object.

This property is inherited from [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461).

</dd> <dt>

**ConflictHighWatermarkPercent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Conflict High Watermark Percentage"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (80), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (100)
</dt> </dl>

The conflict cleanup process starts when the size of the Conflict and Deleted folder hits its high watermark. Every replicated folder defines the maximum size of its Conflict and Deleted folder.

</dd> <dt>

**ConflictLowWatermarkPercent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Conflict Low Watermark Percentage"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (10), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (80)
</dt> </dl>

The conflict cleanup process stops when the size of the Conflict and Deleted folder hits its low watermark. Every replicated folder defines the maximum size of its Conflict and Deleted folder.

</dd> <dt>

**DebugLogFilePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Debug Log File Path"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (2600)
</dt> </dl>

The full path of the debug log files.

</dd> <dt>

**DebugLogSeverity**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Debug Log Severity"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (5)
</dt> </dl>

The level of detail in the debug log files.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user-defined description of the current settings.

</dd> <dt>

**DsPollingIntervalInMin**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Active Directory Domain Services Polling Interval In Minutes"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The number of minutes between the end of one Active Directory Domain Services polling cycle and the start of another.

</dd> <dt>

**EnableDebugLog**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Enable Debug Log")
</dt> </dl>

Enables or disables the generation of debug logs.

</dd> <dt>

**EnableLightDSPolling**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Enable Light Active Directory Domain Services Polling")
</dt> </dl>

Enables or disables a lightweight check for membership configuration changes in the Active Directory Domain Services. This periodic check speeds up the service response to certain types of configuration changes. If any change are detected, a full poll follows. Lightweight polling does not interfere with the normal polling cycles.

</dd> <dt>

**LastChangeNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Change Number"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The configuration sequence number. This value is incremented each time the computer configuration changes.

</dd> <dt>

**LastChangeSource**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Change Source")
</dt> </dl>

Information about the originator of the last configuration change. This is the name of the user who submitted the change.

</dd> <dt>

**LastChangeTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Change Time")
</dt> </dl>

The time stamp of the last configuration change.

</dd> <dt>

**MaxDebugLogFiles**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Maximum Debug Log Files"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The maximum number of debug log files to be generated. If the number of debug log files exceeds this value, DFSR will delete the oldest debug log file.

</dd> <dt>

**MaxDebugLogMessages**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Maximum Debug Log Messages"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1000)
</dt> </dl>

The maximum number of log entries in each debug log file.

</dd> <dt>

**MaxOfflineTimeInDays**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Max Offline Time In Days"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (0)
</dt> </dl>

The maximum number of days a replicated folder can be disconnected from other partners before it is put into an error state.

</dd> <dt>

**ReghostingRateInMin**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Reghosting Rate In Minutes"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (60)
</dt> </dl>

Reserved for system use.

</dd> <dt>

**RootHighWatermarkPercent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Root High Watermark Percentage"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (40)
</dt> </dl>

Reserved for system use.

</dd> <dt>

**RootLowWatermarkPercent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Root Low Watermark Percentage"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

Reserved for system use.

</dd> <dt>

**RpcPortAssignment**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("RPC Port Assignment")
</dt> </dl>

The user-specified RPC port assignment. The default is 0, which indicates any available port. Changes to this value do not take effect until the next time the service starts.

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

Identifier by which the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object is known.

This property is inherited from [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461).

</dd> <dt>

**StagingHighWatermarkPercent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Staging High Watermark Percentage"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (80), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (100)
</dt> </dl>

The staging cleanup process starts when the size of the staging folder hits its high watermark. Every replicated folder defines the maximum size of its staging folder.

</dd> <dt>

**StagingLowWatermarkPercent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Staging Low Watermark Percentage"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (10), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (80)
</dt> </dl>

The staging cleanup process stops when the size of the staging folder hits its low watermark. Every replicated folder defines the maximum size of its staging folder.

</dd> <dt>

**StopReplicationOnAutoRecovery**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Stop Replication on Auto Recovery")
</dt> </dl>

Enables Stop Replication on Auto Recovery feature.

</dd> </dl>

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                     |
| Namespace<br/>                | Root\\MicrosoftDfs<br/>                                                            |
| MOF<br/>                      | <dl> <dt>DfsRProvs.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461)
</dt> <dt>

[DFSR WMI Classes](dfsr-wmi-classes.md)
</dt> </dl>

 

 





