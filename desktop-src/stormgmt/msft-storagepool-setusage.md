---
title: SetUsage method of the MSFT\_StoragePool class
description: Sets or changes the intended usage for the storage pool object.
ms.assetid: CC133913-C19A-4565-8D91-45679B7C709A
keywords:
- SetUsage method Windows Storage Management API
- SetUsage method Windows Storage Management API , MSFT_StoragePool class
- MSFT_StoragePool class Windows Storage Management API , SetUsage method
topic_type:
- apiref
api_name:
- MSFT_StoragePool.SetUsage
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SetUsage method of the MSFT\_StoragePool class

Sets or changes the intended usage for the storage pool object.

## Syntax


```mof
UInt32 SetUsage(
  [in]  UInt16 Usage,
  [in]  String OtherUsageDescription,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*Usage* \[in\]
</dt> <dd>

The new usage for the storage pool. This parameter is required and cannot be NULL.

<dl> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="Unrestricted"></span><span id="unrestricted"></span><span id="UNRESTRICTED"></span>**Unrestricted** (2)
</dt> <dt>

<span id="Reserved_for_ComputerSystem__the_block_server_"></span><span id="reserved_for_computersystem__the_block_server_"></span><span id="RESERVED_FOR_COMPUTERSYSTEM__THE_BLOCK_SERVER_"></span>**Reserved for ComputerSystem (the block server)** (3)
</dt> <dt>

<span id="Reserved_as_a_Delta_Replica_Container"></span><span id="reserved_as_a_delta_replica_container"></span><span id="RESERVED_AS_A_DELTA_REPLICA_CONTAINER"></span>**Reserved as a Delta Replica Container** (4)
</dt> <dt>

<span id="Reserved_by_Migration_Services"></span><span id="reserved_by_migration_services"></span><span id="RESERVED_BY_MIGRATION_SERVICES"></span>**Reserved by Migration Services** (5)
</dt> <dt>

<span id="Reserved_for_Local_Replication_Services"></span><span id="reserved_for_local_replication_services"></span><span id="RESERVED_FOR_LOCAL_REPLICATION_SERVICES"></span>**Reserved for Local Replication Services** (6)
</dt> <dt>

<span id="Reserved_for_Remote_Replication_Services"></span><span id="reserved_for_remote_replication_services"></span><span id="RESERVED_FOR_REMOTE_REPLICATION_SERVICES"></span>**Reserved for Remote Replication Services** (7)
</dt> <dt>

<span id="Reserved_for_Sparing"></span><span id="reserved_for_sparing"></span><span id="RESERVED_FOR_SPARING"></span>**Reserved for Sparing** (8)
</dt> </dl> </dd> <dt>

*OtherUsageDescription* \[in\]
</dt> <dd>

If *Usage* is set to **Other**, this parameter is the string representation of a vendor defined usage for this storage pool. This parameter must not be set if *Usage* is not **Other**.

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

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cannot connect to the storage provider.** (46000)
</dt> <dt>

**The storage provider cannot connect to the storage subsystem.** (46001)
</dt> <dt>

**This operation is not supported on primordial storage pools.** (48000)
</dt> <dt>

**The storage pool could not complete the operation because its health or operational status does not permit it.** (48006)
</dt> <dt>

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
</dt> </dl>

## Remarks

Not all storage pools may allow this method. Those that do not will cause this method to return **Not Supported**.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StoragePool**](msft-storagepool.md)
</dt> </dl>

 

 





