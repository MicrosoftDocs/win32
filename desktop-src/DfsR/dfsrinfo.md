---
title: DfsrInfo class
description: The DFSR monitoring provider class. This singleton class has provider-specific settings in addition to computer-wide service properties and methods.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8197c9f1-3882-4483-a985-59e9ba41164a
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DfsrInfo class Distributed File System Replication
- DfsrInfo class Distributed File System Replication , described
topic_type:
- apiref
api_name:
- DfsrInfo
- DfsrInfo.ProviderVersion
- DfsrInfo.ServiceStartTime
- DfsrInfo.LastDsPollTime
- DfsrInfo.State
- DfsrInfo.LastErrorCode
- DfsrInfo.LastErrorMessageId
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DfsrInfo class

The DFSR monitoring provider class. This singleton class has provider-specific settings in addition to computer-wide service properties and methods.

## Syntax

``` syntax
[Dynamic, Provider("DfsrMonitorProv"), Singleton]
class DfsrInfo
{
  string   ProviderVersion;
  datetime ServiceStartTime;
  datetime LastDsPollTime;
  uint8    State;
  uint32   LastErrorCode;
  uint32   LastErrorMessageId;
};
```

## Members

The **DfsrInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **DfsrInfo** class has these properties.

<dl> <dt>

**LastDsPollTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Active Directory Domain Services Poll Time")
</dt> </dl>

The last time there was an attempt to poll the Active Directory Domain Services; it does not matter whether the attempt succeeded.

</dd> <dt>

**LastErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Error Code")
</dt> </dl>

The last error code.

<dt>

<span id="DFSR_E_DS_POLLING_FAILED"></span><span id="dfsr_e_ds_polling_failed"></span>

<span id="DFSR_E_DS_POLLING_FAILED"></span><span id="dfsr_e_ds_polling_failed"></span>**DFSR\_E\_DS\_POLLING\_FAILED**


</dt> <dd>

Could not connect to the Active Directory.

</dd> </dl>

</dd> <dt>

**LastErrorMessageId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Error Message ID")
</dt> </dl>

Event log message identifier that corresponds to the last error code.

<dt>

<span id="Success"></span><span id="success"></span><span id="SUCCESS"></span>

**Success** (0)


</dt> <dd></dd> </dl>

</dd> <dt>

**ProviderVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("DFS Replication Monitoring Provider Version")
</dt> </dl>

The current version of the provider.

</dd> <dt>

**ServiceStartTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Service Start Time")
</dt> </dl>

The time stamp of the last service start.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("State")
</dt> </dl>

The current state of the DFSR service.

<dt>

<span id="Service_Starting"></span><span id="service_starting"></span><span id="SERVICE_STARTING"></span>

**Service Starting** (0)


</dt> <dd></dd> <dt>

<span id="Service_Running"></span><span id="service_running"></span><span id="SERVICE_RUNNING"></span>

**Service Running** (1)


</dt> <dd></dd> <dt>

<span id="Service_Degraded"></span><span id="service_degraded"></span><span id="SERVICE_DEGRADED"></span>

**Service Degraded** (2)


</dt> <dd></dd> <dt>

<span id="Service_Shutting_Down"></span><span id="service_shutting_down"></span><span id="SERVICE_SHUTTING_DOWN"></span>

**Service Shutting Down** (3)


</dt> <dd></dd> </dl>

</dd> </dl>

## Remarks

The following state diagram illustrates the transitions between the service states.

![dfsr service state diagram](images/service-state.png)

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

[DFSR WMI Classes](dfsr-wmi-classes.md)
</dt> </dl>

 

 





