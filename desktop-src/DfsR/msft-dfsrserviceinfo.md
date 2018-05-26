---
title: MSFT\_DfsrServiceInfo class
description: This class is a DFS Replication monitoring provider class. This is a singleton class that has provider-specific settings in addition to computer-wide service configuration parameters and methods.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ae614a6f-d715-4d4e-8b2e-f17975425381
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DfsrServiceInfo class Distributed File System Replication
- MSFT_DfsrServiceInfo class Distributed File System Replication , described
topic_type:
- apiref
api_name:
- MSFT_DfsrServiceInfo
- MSFT_DfsrServiceInfo.Identifier
- MSFT_DfsrServiceInfo.ProviderVersion
- MSFT_DfsrServiceInfo.ServiceStartTime
- MSFT_DfsrServiceInfo.LastDsPollTime
- MSFT_DfsrServiceInfo.State
- MSFT_DfsrServiceInfo.LastErrorCode
- MSFT_DfsrServiceInfo.LastErrorMessageId
api_location:
- DfsRWmiV2.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_DfsrServiceInfo class

This class is a DFS Replication monitoring provider class. This is a singleton class that has provider-specific settings in addition to computer-wide service configuration parameters and methods.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DfsrWMIV2"), AMENDMENT]
class MSFT_DfsrServiceInfo
{
  string   Identifier;
  string   ProviderVersion;
  datetime ServiceStartTime;
  datetime LastDsPollTime;
  uint8    State;
  uint32   LastErrorCode;
  uint32   LastErrorMessageId;
};
```

## Members

The **MSFT\_DfsrServiceInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_DfsrServiceInfo** class has these properties.

<dl> <dt>

**Identifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Identifier for DFSR service info class")
</dt> </dl>

The identifier for the **MSFT\_DfsrServiceInfo** class.

</dd> <dt>

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



 (0)


</dt> <dd></dd> </dl>

</dd> <dt>

**LastErrorMessageId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](https://msdn.microsoft.com/library/aa393650) ("Last Error Message ID")
</dt> </dl>

The event log message ID that corresponds to the last error code.

<dt>



 (0)


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

The current service state.

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

 

 





