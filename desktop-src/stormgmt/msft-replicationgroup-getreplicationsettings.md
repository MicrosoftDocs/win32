---
title: GetReplicationSettings method of the MSFT\_ReplicationGroup class
description: Returns the replication settings for this replication group.
ms.assetid: '6A4144F4-C432-439C-B0F1-DAB8E8636ECC'
keywords: ["GetReplicationSettings method Windows Storage Management API", "GetReplicationSettings method Windows Storage Management API , MSFT_ReplicationGroup class", "MSFT_ReplicationGroup class Windows Storage Management API , GetReplicationSettings method"]
topic_type:
- apiref
api_name:
- MSFT_ReplicationGroup.GetReplicationSettings
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
---

# GetReplicationSettings method of the MSFT\_ReplicationGroup class

Returns the replication settings for this replication group.

## Syntax


```mof
UInt32 GetReplicationSettings(
  [out] String ReplicationSettings,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*ReplicationSettings* \[out\]
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
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_ReplicationGroup**](msft-replicationgroup.md)
</dt> </dl>

 

 





