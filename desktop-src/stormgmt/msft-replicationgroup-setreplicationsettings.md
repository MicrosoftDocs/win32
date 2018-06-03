---
title: SetReplicationSettings method of the MSFT\_ReplicationGroup class
description: Specifies the replication settings for this replication group.
ms.assetid: D7D6E175-A067-4EAF-99A6-0A394D3679AD
keywords:
- SetReplicationSettings method Windows Storage Management API
- SetReplicationSettings method Windows Storage Management API , MSFT_ReplicationGroup class
- MSFT_ReplicationGroup class Windows Storage Management API , SetReplicationSettings method
topic_type:
- apiref
api_name:
- MSFT_ReplicationGroup.SetReplicationSettings
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetReplicationSettings method of the MSFT\_ReplicationGroup class

Specifies the replication settings for this replication group.

## Syntax


```mof
UInt32 SetReplicationSettings(
  [in]  String ReplicationSettings,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*ReplicationSettings* \[in\]
</dt> <dd>

A string that contains an embedded [**MSFT\_ReplicationSettings**](msft-replicationsettings.md) object specifying the replication settings.

</dd> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**Object Not Found** (8)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cache out of date** (40003)
</dt> <dt>

**The operation is not supported while the cluster is being upgraded.** (40009)
</dt> <dt>

**Cannot connect to the storage provider.** (46000)
</dt> <dt>

**The storage provider cannot connect to the storage subsystem.** (46001)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_ReplicationGroup**](msft-replicationgroup.md)
</dt> </dl>

 

 





