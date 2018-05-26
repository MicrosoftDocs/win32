---
title: CreateVirtualDisk method of the MSFT\_StoragePool class
description: Creates a virtual disk using the resources of the storage pool.
ms.assetid: 1a5bf78d-356c-44a7-8f76-2cad85d3c171
keywords:
- CreateVirtualDisk method Windows Storage Management API
- CreateVirtualDisk method Windows Storage Management API , MSFT_StoragePool class
- MSFT_StoragePool class Windows Storage Management API , CreateVirtualDisk method
topic_type:
- apiref
api_name:
- MSFT_StoragePool.CreateVirtualDisk
api_location:
- vdssys.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CreateVirtualDisk method of the MSFT\_StoragePool class

Creates a virtual disk using the resources of the storage pool.

## Syntax


```mof
UInt32 CreateVirtualDisk(
  [in]  String              FriendlyName,
  [in]  UInt64              Size,
  [in]  Boolean             UseMaximumSize,
  [in]  UInt16              ProvisioningType,
  [in]  String              ResiliencySettingName,
  [in]  UInt16              Usage,
  [in]  String              OtherUsageDescription,
  [in]  UInt16              NumberOfDataCopies,
  [in]  UInt16              PhysicalDiskRedundancy,
  [in]  UInt16              NumberOfColumns,
  [in]  Boolean             AutoNumberOfColumns,
  [in]  UInt64              Interleave,
  [in]  Boolean             IsEnclosureAware,
  [in]  String              PhysicalDisksToUse[],
  [in]  String              StorageTiers[],
  [in]  UInt64              StorageTierSizes[],
  [in]  UInt64              WriteCacheSize,
  [in]  Boolean             AutoWriteCacheSize,
  [in]  Boolean             RunAsJob,
  [out] String              CreatedVirtualDisk,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

<dl> <dt>

*FriendlyName* \[in\]
</dt> <dd>

The friendly name for the virtual disk.

Friendly names are expected to be descriptive, but they are not required to be unique. Note that some storage pools do not allow setting a friendly name during virtual disk creation. If a storage pool doesn't support this, virtual disk creation should still succeed, however the virtual disk may have a different name assigned to it.

This parameter is required and cannot be **NULL**.

</dd> <dt>

*Size* \[in\]
</dt> <dd>

Indicates the desired size, in bytes, of the virtual disk. Note that some storage subsystems will round the size up or down to a multiple of its allocation unit size. On output, this parameter indicates the actual size of the virtual disk that was created. This parameter cannot be used if *UseMaximumSize* is set to **TRUE**.

</dd> <dt>

*UseMaximumSize* \[in\]
</dt> <dd>

If **TRUE**, this parameter instructs the storage array to create the largest possible virtual disk given the available resources of this storage pool. This parameter cannot be used if the *Size* parameter is set.

</dd> <dt>

*ProvisioningType* \[in\]
</dt> <dd>

Specifies the provisioning type for the virtual disk.



| Value                                                                                                                                                                                                                       | Meaning                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl> | The provisioning type is unknown. This could mean that this information is unavailable, or that the storage subsystem uses a proprietary method of allocation.<br/> |
| <span id="Thin"></span><span id="thin"></span><span id="THIN"></span><dl> <dt>**Thin**</dt> <dt>1</dt> </dl>             | The storage for the virtual disk is allocated on demand.<br/>                                                                                                       |
| <span id="Fixed"></span><span id="fixed"></span><span id="FIXED"></span><dl> <dt>**Fixed**</dt> <dt>2</dt> </dl>         | The storage for the virtual disk is allocated when the disk is created.<br/>                                                                                        |



 

</dd> <dt>

*ResiliencySettingName* \[in\]
</dt> <dd>

The desired resiliency setting to use as a template for this virtual disk. This parameter's value should correspond to the particular [**MSFT\_ResiliencySetting**](msft-resiliencysetting.md) object's **Name** property. Only resiliency settings associated with this storage pool may be used.

</dd> <dt>

*Usage* \[in\]
</dt> <dd>

Specifies the intended usage for the virtual disk.

You can specify a predefined description or a custom description. To specify a predefined description, use a value other than **Other**.

To specify a custom description, use **Other** and specify a non-NULL value for the **OtherUsageDescription** property.

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

A vendor specific usage for the new virtual disk. This parameter can only be specified if the **Usage** property is set to **Other**.

</dd> <dt>

*NumberOfDataCopies* \[in\]
</dt> <dd>

Specifies the number of complete data copies to maintain for the virtual disk.

If specified, this value will override the **NumberOfDataCopiesDefault** which would have been inherited from the resiliency setting specified by *ResiliencySettingName*.

</dd> <dt>

*PhysicalDiskRedundancy* \[in\]
</dt> <dd>

Specifies how many physical disk failures the virtual disk should be able to withstand before data loss occurs. If specified, this value will override the **PhysicalDiskRedundancyDefault** which would have been inherited from the resiliency setting specified by *ResiliencySettingName*.

</dd> <dt>

*NumberOfColumns* \[in\]
</dt> <dd>

Specifies the number of underlying physical disks across which data should be striped. If specified, this value will override the **NumberOfColumnsDefault** which would have been inherited from the resiliency setting specified by *ResiliencySettingName*.

</dd> <dt>

*AutoNumberOfColumns* \[in\]
</dt> <dd>

If **TRUE**, this field instructs the storage provider (or subsystem) to automatically choose what it determines to be the best number of columns for the virtual disk. If this field is **TRUE**, the *NumberOfColumns* parameter must be **NULL**.

</dd> <dt>

*Interleave* \[in\]
</dt> <dd>

Specifies the number of bytes that should for a strip in the common striping-based resiliency settings. The strip is defined as the size of the portion of a stripe that lies on one physical disk. Thus *Interleave* \* *NumberOfColumns* will yield the size of one stripe of user data.

If this parameter is specified, this value will override the **InterleaveDefault** which would have been inherited from the resiliency setting specified by *ResiliencySettingName*.

</dd> <dt>

*IsEnclosureAware* \[in\]
</dt> <dd>

Determines the allocation behavior for this virtual disk. Enclosure aware virtual disks will intelligently pick the physical disks to use for their redundancy. If **TRUE**, the virtual disk will attempt to use physical disks from different enclosures to balance the fault tolerance between two or more physical enclosures.

</dd> <dt>

*PhysicalDisksToUse* \[in\]
</dt> <dd>

If this parameter contains a list of physical disks, allocation of this virtual disk's storage is limited to the physical disks in the list. These physical disks must already be added to this storage pool.

</dd> <dt>

*StorageTiers* \[in\]
</dt> <dd>

Storage tiers on this virtual disk. Each element of the array is an [**MSFT\_StorageTier**](msft-storagetier.md) object.

</dd> <dt>

*StorageTierSizes* \[in\]
</dt> <dd>

Sizes of the storage tiers.

</dd> <dt>

*WriteCacheSize* \[in\]
</dt> <dd>

Size of write cache on the virtual disk.

</dd> <dt>

*AutoWriteCacheSize* \[in\]
</dt> <dd>

**TRUE** if the provider should pick up the auto write cache size; otherwise, **FALSE**.

</dd> <dt>

*RunAsJob* \[in\]
</dt> <dd>

If **TRUE**, this method uses the *CreatedStorageJob* parameter when the request is taking a long time to service. If a storage job has been created to track the operation, this method will return **Method Parameters Checked - Job Started**.

> [!Note]  
> Even if *RunAsJob* is **TRUE**, this method can still return a result if it has finished in sufficient time.

 

If **FALSE** or **NULL**, this method will follow default WMI asynchronous behavior as determined by the client's method for invocation. In other words, it is synchronous unless requested otherwise.

</dd> <dt>

*CreatedVirtualDisk* \[out\]
</dt> <dd>

Receives a [**MSFT\_VirtualDisk**](msft-virtualdisk.md) object if this method is run normally (with *RunAsJob* set to **FALSE**) and the virtual disk is successfully created.

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

**You must specify a size by using either the Size or the UseMaximumSize parameter. You can specify only one of these parameters at a time.** (40005)
</dt> <dt>

**Cannot connect to the storage provider.** (46000)
</dt> <dt>

**The storage provider cannot connect to the storage subsystem.** (46001)
</dt> <dt>

**Failover clustering could not be enabled for this storage object.** (46008)
</dt> <dt>

**This subsystem does not support creation of virtual disks with the specified provisioning type.** (47001)
</dt> <dt>

**This operation is not supported on primordial storage pools.** (48000)
</dt> <dt>

**The storage pool is reserved for special usage only.** (48001)
</dt> <dt>

**The specified resiliency setting is not supported by this storage pool.** (48002)
</dt> <dt>

**There are not enough physical disks in the storage pool to create the specified virtual disk configuration.** (48004)
</dt> <dt>

**The storage pool could not complete the operation because its health or operational status does not permit it.** (48006)
</dt> <dt>

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
</dt> <dt>

**You must specify the size info (either the Size or UseMaximumSize parameter) or the tier info (the StorageTiers and StorageTierSizes parameters), but not both size info and tier info.** (48010)
</dt> <dt>

**No auto-allocation drives found in storage pool.** (48011)
</dt> <dt>

**No resiliency setting with that name exists.** (49000)
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
</dt> <dt>

**The value for WriteCacheSize is outside of the supported range of values.** (50005)
</dt> <dt>

**One of the physical disks specified is not supported by this operation.** (51000)
</dt> <dt>

**Not enough physical disks were specified to successfully complete the operation.** (51001)
</dt> </dl>

## Remarks

This method is only available when the **SupportsVirtualDiskCreation** property on the storage subsystem is set to **TRUE**. If it is set to **FALSE**, this method will fail with **MI\_RESULT\_NOT\_SUPPORTED**.

This method is not supported for primordial pools.

This method only requires a *FriendlyName* and *Size* to be specified. Sizes can be specified explicitly through the *Size* parameter, or told to use the maximum available space from the storage pool by using the *UseMaximumSize* parameter. Both *FriendlyName* and *Size* are treated as goals rather than hard requirements. For example, not all SMI-S based arrays may support custom friendly names, however the virtual disk creation will still succeed. If the size specified is not achieved, then the actual size used for the virtual disk will be returned in the out parameter structure.

The usage of this virtual disk can be set using the *Usage* and *OtherUsageDescription* parameters. If a value for *OtherUsageDescription* is given, *Usage* must be set to 1 - 'Other', otherwise an error will be returned.

By default, the resiliency setting applied to this virtual disk will be whatever is specified in the storage pool's **ResiliencySettingNameDefault** property. This can be overridden using the *ResiliencySettingName* parameter. Note that the name given here must correspond to a resiliency setting associated with this storage pool. Any other value will result in an error.

Individual settings of the resiliency setting can be overridden using the *NumberOfDataCopies*, *PhysicalDiskRedundancy*, *NumberOfColumns*, and *Interleave* parameters. If these parameters are not used, the defaults from the resiliency setting will be used. These overrides will not persist back to the particular resiliency setting instance; however some storage providers may choose to create a new resiliency setting instance to capture this new configuration. If any of the goals specified in the override parameters are out of range, or are not supported by the storage pool, an error will be returned.

The provisioning policy for the virtual disk is determined in a similar way to the resiliency setting. If no preference is specified in the *ProvisioningType* parameter, the policy is determined by the storage pool's **ProvisioningTypeDefault** property. If the *ProvisioningType* parameter is specified, the default is ignored and the value specified will be used instead.

Allocation can be further controlled by the *PhysicalDisksToUse* parameter. There may be certain scenarios where a storage administrator wants to manually choose which physical disks should back the virtual disk. When this parameter is specified, data for the virtual disk will only be stored on the physical disks in this array and not on any others.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| Header<br/>                   | <dl> <dt>Vdssys.h</dt> </dl>       |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StoragePool**](msft-storagepool.md)
</dt> </dl>

 

 





