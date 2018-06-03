---
title: CreateVirtualDisk method of the MSFT\_StorageSubSystem class
description: Creates a new virtual disk.
ms.assetid: D31EEC10-7DEA-4701-9025-FBD04A50E5F7
keywords:
- CreateVirtualDisk method Windows Storage Management API
- CreateVirtualDisk method Windows Storage Management API , MSFT_StorageSubSystem class
- MSFT_StorageSubSystem class Windows Storage Management API , CreateVirtualDisk method
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystem.CreateVirtualDisk
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

# CreateVirtualDisk method of the MSFT\_StorageSubSystem class

Creates a new virtual disk.

## Syntax


```mof
UInt32 CreateVirtualDisk(
  [in]      String              FriendlyName,
  [in]      UInt16              Usage,
  [in]      String              OtherUsageDescription,
  [in, out] UInt64              Size,
  [in]      Boolean             UseMaximumSize,
  [in]      UInt16              NumberOfDataCopies,
  [in]      UInt16              PhysicalDiskRedundancy,
  [in]      UInt16              NumberOfColumns,
  [in]      UInt64              Interleave,
  [in]      UInt16              ParityLayout,
  [in]      Boolean             RequestNoSinglePointOfFailure,
  [in]      Boolean             IsEnclosureAware,
  [in]      UInt16              ProvisioningType,
  [in]      Boolean             RunAsJob,
  [out]     String              CreatedVirtualDisk,
  [out]     MSFT_StorageJob REF CreatedStorageJob,
  [out]     String              ExtendedStatus
);
```



## Parameters

<dl> <dt>

*FriendlyName* \[in\]
</dt> <dd>

The friendly name for the virtual disk.

Friendly names are expected to be descriptive, but they are not required to be unique. Note that some storage subsystems do not allow setting a friendly name during virtual disk creation. If a subsystem doesn't support this, virtual disk creation should still succeed, however the disk may have a different name assigned to it.

This parameter is required and cannot be **NULL**.

</dd> <dt>

*Usage* \[in\]
</dt> <dd>

Specifies the intended usage for the virtual disk.

You can specify a predefined description or a custom description. To specify a predefined description, use a value other than **Other**.

To specify a custom description, use **Other** and specify a non-**NULL** value for the *OtherUsageDescription* parameter.

<dl> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="Unrestricted"></span><span id="unrestricted"></span><span id="UNRESTRICTED"></span>**Unrestricted** (2)
</dt> <dt>

<span id="Reserved_for_ComputerSystem__the_block_server_"></span><span id="reserved_for_computersystem__the_block_server_"></span><span id="RESERVED_FOR_COMPUTERSYSTEM__THE_BLOCK_SERVER_"></span>**Reserved for ComputerSystem (the block server)** (3)
</dt> <dt>

<span id="Reserved_by_Replication_Services"></span><span id="reserved_by_replication_services"></span><span id="RESERVED_BY_REPLICATION_SERVICES"></span>**Reserved by Replication Services** (4)
</dt> <dt>

<span id="Reserved_by_Migration_Services"></span><span id="reserved_by_migration_services"></span><span id="RESERVED_BY_MIGRATION_SERVICES"></span>**Reserved by Migration Services** (5)
</dt> <dt>

<span id="Local_Replica_Source"></span><span id="local_replica_source"></span><span id="LOCAL_REPLICA_SOURCE"></span>**Local Replica Source** (6)
</dt> <dt>

<span id="Remote_Replica_Source"></span><span id="remote_replica_source"></span><span id="REMOTE_REPLICA_SOURCE"></span>**Remote Replica Source** (7)
</dt> <dt>

<span id="Local_Replica_Target"></span><span id="local_replica_target"></span><span id="LOCAL_REPLICA_TARGET"></span>**Local Replica Target** (8)
</dt> <dt>

<span id="Remote_Replica_Target"></span><span id="remote_replica_target"></span><span id="REMOTE_REPLICA_TARGET"></span>**Remote Replica Target** (9)
</dt> <dt>

<span id="Local_Replica_Source_or_Target"></span><span id="local_replica_source_or_target"></span><span id="LOCAL_REPLICA_SOURCE_OR_TARGET"></span>**Local Replica Source or Target** (10)
</dt> <dt>

<span id="Remote_Replica_Source_or_Target"></span><span id="remote_replica_source_or_target"></span><span id="REMOTE_REPLICA_SOURCE_OR_TARGET"></span>**Remote Replica Source or Target** (11)
</dt> <dt>

<span id="Delta_Replica_Target"></span><span id="delta_replica_target"></span><span id="DELTA_REPLICA_TARGET"></span>**Delta Replica Target** (12)
</dt> <dt>

<span id="Element_Component"></span><span id="element_component"></span><span id="ELEMENT_COMPONENT"></span>**Element Component** (13)
</dt> <dt>

<span id="Reserved_as_Pool_Contributor"></span><span id="reserved_as_pool_contributor"></span><span id="RESERVED_AS_POOL_CONTRIBUTOR"></span>**Reserved as Pool Contributor** (14)
</dt> <dt>

<span id="Composite_Volume_Member"></span><span id="composite_volume_member"></span><span id="COMPOSITE_VOLUME_MEMBER"></span>**Composite Volume Member** (15)
</dt> <dt>

<span id="Composite_VirtualDisk_Member"></span><span id="composite_virtualdisk_member"></span><span id="COMPOSITE_VIRTUALDISK_MEMBER"></span>**Composite VirtualDisk Member** (16)
</dt> <dt>

<span id="Reserved_for_Sparing"></span><span id="reserved_for_sparing"></span><span id="RESERVED_FOR_SPARING"></span>**Reserved for Sparing** (17)
</dt> </dl> </dd> <dt>

*OtherUsageDescription* \[in\]
</dt> <dd>

A vendor specific usage for the new virtual disk. This parameter can only be specified if the *Usage* parameter is set to **Other**.

</dd> <dt>

*Size* \[in, out\]
</dt> <dd>

Desired size, in bytes, of the virtual disk. Note that some storage subsystems will round the size up or down to a multiple of its allocation unit size.

The storage subsystem uses this parameter only if the *UseMaximumSize* parameter is **FALSE** or **NULL**.

If the *UseMaximumSize* parameter is **TRUE**, this parameter is ignored.

This parameter is required and cannot be zero.

</dd> <dt>

*UseMaximumSize* \[in\]
</dt> <dd>

If **TRUE**, use the maximum size available to create the virtual disk.

This parameter cannot be used together with the *Size* parameter.

</dd> <dt>

*NumberOfDataCopies* \[in\]
</dt> <dd>

The number of complete data copies to maintain for this virtual disk.

</dd> <dt>

*PhysicalDiskRedundancy* \[in\]
</dt> <dd>

The number of physical disk failures that the virtual disk should be able to withstand before data loss occurs.

</dd> <dt>

*NumberOfColumns* \[in\]
</dt> <dd>

The number of underlying physical disks across which data should be striped. This parameter is required.

</dd> <dt>

*Interleave* \[in\]
</dt> <dd>

The number of bytes that should for a strip in common striping-based resiliency settings. The strip is defined as the size of the portion of a stripe that lies on one physical disk. Thus *Interleave* \* *NumberOfColumns* will yield the size of one stripe. This parameter is required.

</dd> <dt>

*ParityLayout* \[in\]
</dt> <dd>

If a parity-based resiliency setting is desired, set this parameter to one of the following values.

If the desired resiliency setting is not parity-based, this property must be **NULL**.

<dl> <dt>

<span id="Non-rotated_Parity"></span><span id="non-rotated_parity"></span><span id="NON-ROTATED_PARITY"></span>**Non-rotated Parity** (1)
</dt> <dt>

<span id="Rotated_Parity"></span><span id="rotated_parity"></span><span id="ROTATED_PARITY"></span>**Rotated Parity** (2)
</dt> </dl> </dd> <dt>

*RequestNoSinglePointOfFailure* \[in\]
</dt> <dd>

Set to **TRUE** to request no single point of failure.

</dd> <dt>

*IsEnclosureAware* \[in\]
</dt> <dd>

The allocation behavior for this virtual disk. Enclosure-aware virtual disks will intelligently pick the physical disks to use for their redundancy. If **TRUE**, the virtual disk will attempt to use physical disks from different enclosures to balance the fault tolerance between two or more physical enclosures.

</dd> <dt>

*ProvisioningType* \[in\]
</dt> <dd>

The provisioning type for the virtual disk.

<dl> <dt>

<span id="Thin"></span><span id="thin"></span><span id="THIN"></span>**Thin** (1)
</dt> <dt>

<span id="Fixed"></span><span id="fixed"></span><span id="FIXED"></span>**Fixed** (2)
</dt> </dl> </dd> <dt>

*RunAsJob* \[in\]
</dt> <dd>

If **TRUE**, this method uses the *CreatedStorageJob* parameter when the request is taking a long time to service. If a storage job has been created to track the operation, this method will return **Method Parameters Checked - Job Started**.

> [!Note]  
> Even if *RunAsJob* is **TRUE**, this method can still return a result if it has finished in sufficient time.

 

If **FALSE** or **NULL**, this method will follow default WMI asynchronous behavior as determined by the client's method for invocation. In other words, it is synchronous unless requested otherwise.

</dd> <dt>

*CreatedVirtualDisk* \[out\]
</dt> <dd>

If the virtual disk is successfully created, this parameter receives a string that contains an embedded [**MSFT\_VirtualDisk**](msft-virtualdisk.md) object.

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

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Size Not Supported** (4097)
</dt> <dt>

**Not enough free space** (40000)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cache out of date** (40003)
</dt> <dt>

**You must specify a size by using either the Size or the UseMaximumSize parameter. You can specify only one of these parameters at a time.** (40005)
</dt> <dt>

**Cannot connect to the storage provider.** (46000)
</dt> <dt>

**The storage provider cannot connect to the storage subsystem.** (46001)
</dt> <dt>

**No storage pools were found that can support this virtual disk configuration.** (47000)
</dt> <dt>

**The value for NoSinglePointOfFailure is not supported.** (49001)
</dt> <dt>

**The value for PhysicalDiskRedundancy is outside of the supported range of values.** (49002)
</dt> <dt>

**The value for NumberOfDataCopies is outside of the supported range of values.** (49003)
</dt> <dt>

**The value for ParityLayout is outside of the supported range of values.** (49004)
</dt> <dt>

**The value for Interleave is outside of the supported range of values.** (49005)
</dt> <dt>

**The value for NumberOfColumns is outside of the supported range of values.** (49006)
</dt> </dl>

## Remarks

This method is typically used when one of the following is true:

-   The storage subsystem's storage pools do not allow virtual disk creation directly.
-   The storage subsystem doesn't support storage pools.

Storage management providers can also choose to implement this method to "intelligently" pick a storage pool for the user. If this method is supported, the subsystem's **SupportsAutomaticStoragePoolSelection** property should be set to **TRUE**.

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

 

 





