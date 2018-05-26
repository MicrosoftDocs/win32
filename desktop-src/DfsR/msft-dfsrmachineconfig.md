---
title: MSFT\_DfsrMachineConfig class
description: This class provides service-wide settings on the local computer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 95ba9c5c-759c-4f91-860c-76a64b56ded2
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DfsrMachineConfig class Distributed File System Replication
- MSFT_DfsrMachineConfig class Distributed File System Replication , described
topic_type:
- apiref
api_name:
- MSFT_DfsrMachineConfig
- MSFT_DfsrMachineConfig.LastChangeNumber
- MSFT_DfsrMachineConfig.LastChangeTime
- MSFT_DfsrMachineConfig.LastChangeSource
- MSFT_DfsrMachineConfig.Description
- MSFT_DfsrMachineConfig.EnableDebugLog
- MSFT_DfsrMachineConfig.DebugLogFilePath
- MSFT_DfsrMachineConfig.MaxDebugLogFiles
- MSFT_DfsrMachineConfig.DebugLogSeverity
- MSFT_DfsrMachineConfig.MaxDebugLogMessages
- MSFT_DfsrMachineConfig.DsPollingIntervalInMin
- MSFT_DfsrMachineConfig.EnableLightDSPolling
- MSFT_DfsrMachineConfig.RpcPortAssignment
- MSFT_DfsrMachineConfig.ReghostingRateInMin
- MSFT_DfsrMachineConfig.RootLowWatermarkPercent
- MSFT_DfsrMachineConfig.RootHighWatermarkPercent
- MSFT_DfsrMachineConfig.StagingLowWatermarkPercent
- MSFT_DfsrMachineConfig.StagingHighWatermarkPercent
- MSFT_DfsrMachineConfig.ConflictLowWatermarkPercent
- MSFT_DfsrMachineConfig.ConflictHighWatermarkPercent
- MSFT_DfsrMachineConfig.MaxOfflineTimeInDays
- MSFT_DfsrMachineConfig.Identifier
- MSFT_DfsrMachineConfig.StopReplicationOnAutoRecovery
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_DfsrMachineConfig class

This class provides service-wide settings on the local computer.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DfsrWMIV2"), AMENDMENT]
class MSFT_DfsrMachineConfig
{
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
  string   Identifier;
  boolean  StopReplicationOnAutoRecovery;
};
```

## Members

The **MSFT\_DfsrMachineConfig** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_DfsrMachineConfig** class has these properties.

<dl> <dt>

**ConflictHighWatermarkPercent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("80"), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) ("100"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Conflict High Watermark Percentage")
</dt> </dl>

The conflict cleanup process starts when the size of the Conflict and Deleted folder hits its high watermark. Every replicated folder defines the maximum size of its Conflict and Deleted folder.

</dd> <dt>

**ConflictLowWatermarkPercent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("10"), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) ("80"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Conflict Low Watermark Percentage")
</dt> </dl>

The conflict cleanup process stops when the size of the Conflict and Deleted folder hits its low watermark. Every replicated folder defines the maximum size of its Conflict and Deleted folder.

</dd> <dt>

**DebugLogFilePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (2600), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Debug Log File Path")
</dt> </dl>

The full path of the debug log files.

</dd> <dt>

**DebugLogSeverity**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("1"), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) ("5"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Debug Log Severity")
</dt> </dl>

The level of detail in the debug log files.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Description")
</dt> </dl>

The user-defined description of the current settings.

</dd> <dt>

**DsPollingIntervalInMin**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("1"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Active Directory Domain Services Polling Interval In Minutes")
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

**Identifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Identifier for DFSR machine config")
</dt> </dl>

Identifier for DFSR machine config

</dd> <dt>

**LastChangeNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("1"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Change Number")
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

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("1"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Maximum Debug Log Files")
</dt> </dl>

The maximum number of debug log files to be generated. If the number of debug log files exceeds this value, DFSR will delete the oldest debug log file.

</dd> <dt>

**MaxDebugLogMessages**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("1000"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Maximum Debug Log Messages")
</dt> </dl>

The maximum number of log entries in each debug log file.

</dd> <dt>

**MaxOfflineTimeInDays**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("0"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Max Offline Time In Days")
</dt> </dl>

The maximum number of days a replicated folder can be disconnected from other partners before it is put into an error state.

</dd> <dt>

**ReghostingRateInMin**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("60"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Reghosting Rate In Minutes")
</dt> </dl>

Reserved for system use.

</dd> <dt>

**RootHighWatermarkPercent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("40"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Root High Watermark Percentage")
</dt> </dl>

Reserved for system use.

</dd> <dt>

**RootLowWatermarkPercent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("10"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Root Low Watermark Percentage")
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

**StagingHighWatermarkPercent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("80"), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) ("100"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Staging High Watermark Percentage")
</dt> </dl>

The staging cleanup process starts when the size of the staging folder hits its high watermark. Every replicated folder defines the maximum size of its staging folder.

</dd> <dt>

**StagingLowWatermarkPercent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("10"), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) ("80"), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Staging Low Watermark Percentage")
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
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                        |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dfsr<br/>                                                |
| MOF<br/>                      | <dl> <dt>Dfsrwmiv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[DFSR WMI Classes](dfsr-wmi-classes.md)
</dt> </dl>

 

 





