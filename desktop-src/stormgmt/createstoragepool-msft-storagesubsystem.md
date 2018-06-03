---
title: CreateStoragePool method of the MSFT\_StorageSubSystem class
description: Creates a storage pool from available physical disks contained within a common primordial pool.
ms.assetid: 3fa2f78f-be75-42c0-baba-b08f4959af8c
keywords:
- CreateStoragePool method Windows Storage Management API
- CreateStoragePool method Windows Storage Management API , MSFT_StorageSubSystem class
- MSFT_StorageSubSystem class Windows Storage Management API , CreateStoragePool method
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystem.CreateStoragePool
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

# CreateStoragePool method of the MSFT\_StorageSubSystem class

Creates a storage pool from available physical disks contained within a common primordial pool.

A physical disk is available for storage pool creation if the **CanPool** property of its [**MSFT\_PhysicalDisk**](msft-physicaldisk.md) object is **TRUE**.

Storage pool creation is only available when the **SupportsStoragePoolCreation** property of the storage subsystem's [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) object is **TRUE**.

## Syntax


```mof
UInt32 CreateStoragePool(
  [in]  String              FriendlyName,
  [in]  UInt16              Usage,
  [in]  String              OtherUsageDescription,
  [in]  String              PhysicalDisks[],
  [in]  String              ResiliencySettingNameDefault,
  [in]  UInt16              ProvisioningTypeDefault,
  [in]  UInt64              LogicalSectorSizeDefault,
  [in]  Boolean             EnclosureAwareDefault,
  [in]  UInt64              WriteCacheSizeDefault,
  [in]  Boolean             AutoWriteCacheSize,
  [in]  Boolean             RunAsJob,
  [out] String              CreatedStoragePool,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

<dl> <dt>

*FriendlyName* \[in\]
</dt> <dd>

Specifies the friendly name for the new storage pool.

Friendly names are expected to be descriptive, but they are not required to be unique. Note that some storage subsystems do not allow setting a friendly name during pool creation.

If a subsystem doesn't support this, storage pool creation should still succeed. However, the pool may have a different name assigned to it.

This parameter is required and cannot be NULL.

</dd> <dt>

*Usage* \[in\]
</dt> <dd>

Specifies the intended usage for the storage pool.

You can specify a predefined description or a custom description. To specify a predefined description, use a value other than **Other**.

To specify a custom description, use **Other** and specify a non-NULL value for the *OtherUsageDescription* parameter.

<dl> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="Unrestricted"></span><span id="unrestricted"></span><span id="UNRESTRICTED"></span>**Unrestricted** (2)
</dt> <dt>

<span id="Reserved_for_ComputerSystem__the_block_server_"></span><span id="reserved_for_computersystem__the_block_server_"></span><span id="RESERVED_FOR_COMPUTERSYSTEM__THE_BLOCK_SERVER_"></span>**Reserved for ComputerSystem (the block server)** (3)
</dt> <dt>

<span id="Reserved_as_a_Delta_Replica_Container"></span><span id="reserved_as_a_delta_replica_container"></span><span id="RESERVED_AS_A_DELTA_REPLICA_CONTAINER"></span>**Reserved as a Delta Replica Container** (4)
</dt> <dt>

<span id="Reserved_for_Migration_Services"></span><span id="reserved_for_migration_services"></span><span id="RESERVED_FOR_MIGRATION_SERVICES"></span>**Reserved for Migration Services** (5)
</dt> <dt>

<span id="Reserved_for_Local_Replication_Services"></span><span id="reserved_for_local_replication_services"></span><span id="RESERVED_FOR_LOCAL_REPLICATION_SERVICES"></span>**Reserved for Local Replication Services** (6)
</dt> <dt>

<span id="Reserved_for_Remote_Replication_Services"></span><span id="reserved_for_remote_replication_services"></span><span id="RESERVED_FOR_REMOTE_REPLICATION_SERVICES"></span>**Reserved for Remote Replication Services** (7)
</dt> <dt>

<span id="Reserved_for_Sparing"></span><span id="reserved_for_sparing"></span><span id="RESERVED_FOR_SPARING"></span>**Reserved for Sparing** (8)
</dt> </dl> </dd> <dt>

*OtherUsageDescription* \[in\]
</dt> <dd>

Allows a user to set a custom usage type for the new [**MSFT\_StoragePool**](msft-storagepool.md) object. This parameter can only be specified if the *Usage* parameter is set to **Other**.

</dd> <dt>

*PhysicalDisks* \[in\]
</dt> <dd>

An array of strings, each of which contains an embedded instance of the [**MSFT\_PhysicalDisk**](msft-physicaldisk.md) class.

This parameter is used to specify an array of [**MSFT\_PhysicalDisk**](msft-physicaldisk.md) objects that will be used as the backing data storage for the newly created storage pool. The physical disks must come from a primordial pool in the subsystem in which you are creating this pool. All of the physical disks must come from the same primordial pool.

This parameter is required and cannot be NULL.

</dd> <dt>

*ResiliencySettingNameDefault* \[in\]
</dt> <dd>

The desired resiliency setting to be used by default when creating a new virtual disk in this storage pool. If the subsystem's **SupportsMultipleResiliencySettingsPerStoragePool** property is set to **FALSE**, this parameter also acts as a hint to the storage management provider on which resiliency setting should be inherited by this storage pool. If no value is given, the storage management provider is responsible for choosing the most appropriate resiliency setting.

</dd> <dt>

*ProvisioningTypeDefault* \[in\]
</dt> <dd>

The desired provisioning type to be used by default when creating a new virtual disk on this storage pool. If this parameter is zero, the default provisioning type is inherited from the primordial pool.

<dl> <dt>

<span id="Thin"></span><span id="thin"></span><span id="THIN"></span>**Thin** (1)
</dt> <dt>

<span id="Fixed"></span><span id="fixed"></span><span id="FIXED"></span>**Fixed** (2)
</dt> </dl> </dd> <dt>

*LogicalSectorSizeDefault* \[in\]
</dt> <dd>

The default logical sector size, in bytes. This is useful when a storage pool may contain a mix of 512-byte emulated and either 4K-byte native or 512-byte native physical disks.

</dd> <dt>

*EnclosureAwareDefault* \[in\]
</dt> <dd>

The default allocation policy for virtual disks created in an enclosure aware storage pool. For example, an enclosure-aware subsystem could balance each data copy of the virtual disk across multiple physical enclosures such that each enclosure contains a full data copy of the virtual disk.

</dd> <dt>

*WriteCacheSizeDefault* \[in\]
</dt> <dd>

The default size of the write cache for virtual disk creation.

</dd> <dt>

*AutoWriteCacheSize* \[in\]
</dt> <dd>

If **TRUE**, the provider should pick up the auto write cache size.

</dd> <dt>

*RunAsJob* \[in\]
</dt> <dd>

If **TRUE**, this method uses the *CreatedStorageJob* parameter when the request is taking a long time to service. If a storage job has been created to track the operation, this method will return **Method Parameters Checked - Job Started**.

> [!Note]  
> Even if *RunAsJob* is **TRUE**, this method can still return a result if it has finished in sufficient time.

 

If **FALSE** or **NULL**, this method will follow default WMI asynchronous behavior as determined by the client's method for invocation. In other words, it is synchronous unless requested otherwise.

</dd> <dt>

*CreatedStoragePool* \[out\]
</dt> <dd>

If the storage pool is successfully created, this parameter receives a string that contains an embedded [**MSFT\_StoragePool**](msft-storagepool.md) object.

</dd> <dt>

*CreatedStorageJob* \[out\]
</dt> <dd>

If *RunAsJob* is set to **TRUE** and this method takes a long time to execute, this parameter receives a reference to the storage job object that is used to track the long-running operation.

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

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cache out of date** (40003)
</dt> <dt>

**An unexpected I/O error has occurred** (40004)
</dt> <dt>

**The request failed due to a fatal device hardware error.** (40007)
</dt> <dt>

**Cannot connect to the storage provider.** (46000)
</dt> <dt>

**The storage provider cannot connect to the storage subsystem.** (46001)
</dt> <dt>

**Failover clustering could not be enabled for this storage object.** (46008)
</dt> <dt>

**No resiliency setting with that name exists.** (49000)
</dt> <dt>

**The value for WriteCacheSize is outside of the supported range of values.** (50005)
</dt> <dt>

**One of the physical disks specified is not supported by this operation.** (51000)
</dt> <dt>

**Not enough physical disks were specified to successfully complete the operation.** (51001)
</dt> <dt>

**One of the physical disks specified is already in use.** (51002)
</dt> <dt>

**One of the physical disks specified uses a sector size that is not supported by this storage pool.** (51003)
</dt> <dt>

**One or more physical disks are not connected to the nodes on which the pool is being created.** (51005)
</dt> </dl>

## Remarks

Subsystems that don't support storage pools should implement this method as follows:

-   The **SupportsAutomaticStoragePoolSelection** property of the [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) object should be set to **TRUE**.
-   The **SupportsStoragePoolCreation**, **SupportsStoragePoolModification**, and **SupportsStoragePoolDeletion** properties of the [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) object should be set to **FALSE**.
-   The [**MSFT\_VirtualDisk**](msft-virtualdisk.md) object should be created in the subsystem by calling [**MSFT\_StorageSubSystem.CreateVirtualDisk**](msft-storagesubsystem-createvirtualdisk.md). Support for this method is mandatory in this case.
-   Support for the [**MSFT\_StoragePool**](msft-storagepool.md) and [**MSFT\_ResiliencySetting**](msft-resiliencysetting.md) classes is not required.
-   Support for the [**MSFT\_StoragePool.CreateVirtualDisk**](createvirtualdisk-msft-storagepool.md) method is not required.

Subsystems that support storage pools but don't allow storage pool selection (administrator selection of the pool in which the virtual disk is created), creation, modification, or deletion should implement this method as follows:

-   The **SupportsAutomaticStoragePoolSelection** property of the [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) object should be set to **TRUE**.
-   The **SupportsStoragePoolCreation**, **SupportsStoragePoolModification**, and **SupportsStoragePoolDeletion** properties of the [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) object should be set to **FALSE**.
-   The [**MSFT\_VirtualDisk**](msft-virtualdisk.md) object should be created in the subsystem by calling [**MSFT\_StorageSubSystem.CreateVirtualDisk**](msft-storagesubsystem-createvirtualdisk.md). Support for this method is mandatory in this case.
-   The storage pool in which the [**MSFT\_VirtualDisk**](msft-virtualdisk.md) object will be created needs to be automatically selected by the SMP.
-   Support for the [**MSFT\_StoragePool**](msft-storagepool.md) and [**MSFT\_ResiliencySetting**](msft-resiliencysetting.md) classes is not required.
-   Support for the [**MSFT\_StoragePool.CreateVirtualDisk**](createvirtualdisk-msft-storagepool.md) method is not required.

Subsystems that support storage pools and storage pool selection but do not support storage pool creation, modification, or deletion should implement this method as follows:

-   The **SupportsAutomaticStoragePoolSelection** property of the [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) object should be set to **TRUE** only if the [**MSFT\_StoragePool.CreateVirtualDisk**](createvirtualdisk-msft-storagepool.md) method is implemented.
-   The **SupportsStoragePoolCreation**, **SupportsStoragePoolModification**, and **SupportsStoragePoolDeletion** properties of the [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) object should be set to **FALSE**.
-   The [**MSFT\_VirtualDisk**](msft-virtualdisk.md) object should be created in the subsystem by calling [**MSFT\_StorageSubSystem.CreateVirtualDisk**](msft-storagesubsystem-createvirtualdisk.md). Support for this method is mandatory in this case.
-   The storage pool in which the [**MSFT\_VirtualDisk**](msft-virtualdisk.md) object will be created needs to be automatically selected by the user.
-   Support for the [**MSFT\_StoragePool**](msft-storagepool.md) and [**MSFT\_ResiliencySetting**](msft-resiliencysetting.md) classes is required. Support for at least one concrete pool and one type of resiliency setting is required.
-   Support for the [**MSFT\_StoragePool.CreateVirtualDisk**](createvirtualdisk-msft-storagepool.md) method is optional.

Subsystems that support storage pools and storage pool selection and also support storage pool creation, modification, or deletion should implement this method as follows:

-   The **SupportsAutomaticStoragePoolSelection** property of the [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) object should be set to **TRUE** only if the [**MSFT\_StoragePool.CreateVirtualDisk**](createvirtualdisk-msft-storagepool.md) method is implemented.
-   The **SupportsStoragePoolCreation**, **SupportsStoragePoolModification**, and **SupportsStoragePoolDeletion** properties of the [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) object should be set to **TRUE**.
-   The [**MSFT\_VirtualDisk**](msft-virtualdisk.md) object should be created in the subsystem by calling [**MSFT\_StorageSubSystem.CreateVirtualDisk**](msft-storagesubsystem-createvirtualdisk.md). Support for this method is mandatory in this case.
-   The storage pool in which the [**MSFT\_VirtualDisk**](msft-virtualdisk.md) object will be created needs to be automatically selected by the user.
-   Support for the [**MSFT\_StoragePool**](msft-storagepool.md) and [**MSFT\_ResiliencySetting**](msft-resiliencysetting.md) classes is required. Support for at least one concrete pool and one type of resiliency setting is required.
-   Support for the [**MSFT\_StoragePool.CreateVirtualDisk**](createvirtualdisk-msft-storagepool.md) method is optional.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





