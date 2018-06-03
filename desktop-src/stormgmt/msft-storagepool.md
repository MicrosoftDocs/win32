---
title: MSFT\_StoragePool class
description: Represents a logical grouping of physical disks that may be used to create virtual disks.
ms.assetid: 5b6c5566-7a3f-4bc4-b69e-53664920c9b2
keywords:
- MSFT_StoragePool class Windows Storage Management API
- MSFT_StoragePool class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StoragePool
- MSFT_StoragePool.FriendlyName
- MSFT_StoragePool.Name
- MSFT_StoragePool.Usage
- MSFT_StoragePool.OtherUsageDescription
- MSFT_StoragePool.IsPrimordial
- MSFT_StoragePool.HealthStatus
- MSFT_StoragePool.OperationalStatus
- MSFT_StoragePool.OtherOperationalStatusDescription
- MSFT_StoragePool.Size
- MSFT_StoragePool.AllocatedSize
- MSFT_StoragePool.LogicalSectorSize
- MSFT_StoragePool.PhysicalSectorSize
- MSFT_StoragePool.ProvisioningTypeDefault
- MSFT_StoragePool.SupportedProvisioningTypes
- MSFT_StoragePool.ResiliencySettingNameDefault
- MSFT_StoragePool.IsReadOnly
- MSFT_StoragePool.ReadOnlyReason
- MSFT_StoragePool.IsClustered
- MSFT_StoragePool.SupportsDeduplication
- MSFT_StoragePool.ThinProvisioningAlertThresholds
- MSFT_StoragePool.ClearOnDeallocate
- MSFT_StoragePool.IsPowerProtected
- MSFT_StoragePool.RepairPolicy
- MSFT_StoragePool.EnclosureAwareDefault
- MSFT_StoragePool.FaultDomainAwarenessDefault
- MSFT_StoragePool.RetireMissingPhysicalDisks
- MSFT_StoragePool.Version
- MSFT_StoragePool.WriteCacheSizeDefault
- MSFT_StoragePool.WriteCacheSizeMin
- MSFT_StoragePool.WriteCacheSizeMax
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StoragePool class

Represents a logical grouping of physical disks that may be used to create virtual disks.

The virtual disks can be created with different characteristics and levels of resiliency based on the number of available physical disks and the capabilities of the storage pool.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_StoragePool : MSFT_StorageObject
{
  String  FriendlyName;
  String  Name;
  UInt16  Usage;
  String  OtherUsageDescription;
  Boolean IsPrimordial;
  UInt16  HealthStatus;
  UInt16  OperationalStatus[];
  String  OtherOperationalStatusDescription;
  UInt64  Size;
  UInt64  AllocatedSize;
  UInt64  LogicalSectorSize;
  UInt64  PhysicalSectorSize;
  UInt16  ProvisioningTypeDefault;
  UInt16  SupportedProvisioningTypes[];
  String  ResiliencySettingNameDefault;
  Boolean IsReadOnly;
  UInt16  ReadOnlyReason;
  Boolean IsClustered;
  Boolean SupportsDeduplication;
  UInt16  ThinProvisioningAlertThresholds[];
  Boolean ClearOnDeallocate;
  Boolean IsPowerProtected;
  UInt16  RepairPolicy;
  Boolean EnclosureAwareDefault;
  UInt16  FaultDomainAwarenessDefault;
  UInt16  RetireMissingPhysicalDisks;
  UInt16  Version;
  UInt64  WriteCacheSizeDefault;
  UInt64  WriteCacheSizeMin;
  UInt64  WriteCacheSizeMax;
};
```

## Members

The **MSFT\_StoragePool** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_StoragePool** class has these methods.



| Method                                                                  | Description                                                                                    |
|:------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------|
| [**AddPhysicalDisk**](addphysicaldisk-msft-storagepool.md)             | Adds physical disks to a storage pool.<br/>                                              |
| [**CreateStorageTier**](msft-storagepool-createstoragetier.md)         | Creates a storage tier template on the storage pool.<br/>                                |
| [**CreateVirtualDisk**](createvirtualdisk-msft-storagepool.md)         | Creates a virtual disk within the storage pool.<br/>                                     |
| [**CreateVolume**](msft-storagepool-createvolume.md)                   | Creates a virtual disk and single volume using the resources of the storage pool. <br/>  |
| [**DeleteObject**](msft-storagepool-deleteobject.md)                   | Deletes an empty storage pool.<br/>                                                      |
| [**GetSecurityDescriptor**](getsecuritydescriptor-msft-storagepool.md) | Retrieves the security descriptor for the storage pool object instance.<br/>             |
| [**GetSupportedSize**](msft-storagepool-getsupportedsize.md)           | Retrieves the supported virtual disk sizes that can be created in the storage pool.<br/> |
| [**Optimize**](msft-storagepool-optimize.md)                           | Optimizes the storage pool.<br/>                                                         |
| [**RemovePhysicalDisk**](removephysicaldisk-msft-storagepool.md)       | Removes physical disks from a storage pool.<br/>                                         |
| [**SetAttributes**](msft-storagepool-setattributes.md)                 | Sets or changes the attribute values for the storage pool object.<br/>                   |
| [**SetDefaults**](msft-storagepool-setdefaults.md)                     | Sets or changes the default values for properties of the storage pool object.<br/>       |
| [**SetFriendlyName**](msft-storagepool-setfriendlyname.md)             | Sets or changes the friendly name for the storage pool object.<br/>                      |
| [**SetSecurityDescriptor**](setsecuritydescriptor-msft-storagepool.md) | Sets or changes the security descriptor for the storage pool object.<br/>                |
| [**SetUsage**](msft-storagepool-setusage.md)                           | Sets or changes the intended usage for the storage pool object.<br/>                     |
| [**Upgrade**](msft-storagepool-upgrade.md)                             | Upgrades the metadata on the storage pool.<br/>                                          |



 

### Properties

The **MSFT\_StoragePool** class has these properties.

<dl> <dt>

**AllocatedSize**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes")
</dt> </dl>

The total capacity used by this storage pool. If the pool is primordial, this will be the sum of all capacity currently allocated to concrete storage pools. If the pool is concrete, this value should be the sum of all capacity currently allocated to virtual disks and other pool metadata.

</dd> <dt>

**ClearOnDeallocate**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if physical disks should be zeroed (cleared of all data) when unmapped or removed from the storage pool.

</dd> <dt>

**EnclosureAwareDefault**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The default allocation behavior for virtual disks created in this pool. Enclosure aware virtual disks will intelligently pick the physical disks to use for their redundancy. If **TRUE**, the virtual disk will use physical disks from different enclosures to balance the fault tolerance between two or more physical enclosures.

</dd> <dt>

**FaultDomainAwarenessDefault**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Determines the default allocation behavior for virtual disks created in this pool. Fault domain-aware virtual disks intelligently pick the physical disks to use for their redundancy to balance the fault tolerance between two (or more) fault domain units of the specified type.

<dl> <dt>

<span id="PhysicalDisk"></span><span id="physicaldisk"></span><span id="PHYSICALDISK"></span>**PhysicalDisk** (1)
</dt> <dt>

<span id="StorageEnclosure"></span><span id="storageenclosure"></span><span id="STORAGEENCLOSURE"></span>**StorageEnclosure** (2)
</dt> <dt>

<span id="StorageScaleUnit"></span><span id="storagescaleunit"></span><span id="STORAGESCALEUNIT"></span>**StorageScaleUnit** (3)
</dt> <dt>

<span id="StorageChassis"></span><span id="storagechassis"></span><span id="STORAGECHASSIS"></span>**StorageChassis** (4)
</dt> <dt>

<span id="StorageRack"></span><span id="storagerack"></span><span id="STORAGERACK"></span>**StorageRack** (5)
</dt> </dl>

</dd> <dt>

**FriendlyName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A user-friendly name for the storage pool. This name can be set by calling the [**SetFriendlyName**](msft-storagepool-setfriendlyname.md) method.

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The health status of the storage pool.

Health of a storage pool is derived from the health of the backing physical disks, and whether or not the storage pool can maintain the required redundancy levels.



| Value                                                                                                                                                                                                                                    | Meaning                                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| <span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span><dl> <dt>**Healthy**</dt> <dt>0</dt> </dl>              | All physical disks are present and in a healthy state. <br/>                                                               |
| <span id="Warning"></span><span id="warning"></span><span id="WARNING"></span><dl> <dt>**Warning**</dt> <dt>1</dt> </dl>              | The majority of physical disks are healthy, but one or more may be failing I/O requests.<br/>                              |
| <span id="Unhealthy_"></span><span id="unhealthy_"></span><span id="UNHEALTHY_"></span><dl> <dt>**Unhealthy** </dt> <dt>2 </dt> </dl> | The majority of physical disks are unhealthy or in a failed state, and the storage pool no longer has data integrity.<br/> |
| <span id="Unknown_"></span><span id="unknown_"></span><span id="UNKNOWN_"></span><dl> <dt>**Unknown** </dt> <dt>5 </dt> </dl>         | The health status of the storage pool is unknown.<br/>                                                                     |



 

</dd> <dt>

**IsClustered**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if the storage pool is used in a clustered environment.

</dd> <dt>

**IsPowerProtected**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if the disks in this pool are able to tolerate power loss without data loss. For example, they automatically flush volatile buffers to non-volatile media after external power is disconnected.

</dd> <dt>

**IsPrimordial**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

If this field is set to **TRUE**, the storage pool is primordial. A primordial pool, also known as the 'available storage' pool is where storage capacity is drawn and returned in the creation and deletion of concrete storage pools. Primordial pools cannot be created or deleted.

If this field is set to **FALSE**, the storage pool is a concrete pool. These pools are subject to all of the management operations defined on the storage pool class, including creation and deletion of virtual disks.

</dd> <dt>

**IsReadOnly**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether or not the storage pool's configuration is read only. If **TRUE**, the storage pool will not allow modification to itself or any of its virtual and physical disks. Note that the data on the virtual disk may still be writable, even if this property is **TRUE**.

</dd> <dt>

**LogicalSectorSize**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes")
</dt> </dl>

Logical sector size, in bytes, of the storage pool. This value should be derived from the backing physical disks, as well as the preference specified at the time this storage pool was created.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A semi-unique (scoped to the owning storage subsystem), human-readable string used to identify the storage pool.

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The operational status of the storage pool. Unlike **HealthStatus**, this property indicates the status of hardware, software, and infrastructure issues related to the storage pool, and can contain multiple values.



| Value                                                                                                                                                                                                                                                                                                    | Meaning                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                                              | The operational status is unknown.<br/>                                                                                                                                                         |
| <span id="Other"></span><span id="other"></span><span id="OTHER"></span><dl> <dt>**Other**</dt> <dt>1</dt> </dl>                                                                                      | A vendor-specific **OperationalStatus** has been specified by setting the **OtherOperationalStatusDescription** property.<br/>                                                                  |
| <span id="OK"></span><span id="ok"></span><dl> <dt>**OK**</dt> <dt>2</dt> </dl>                                                                                                                       | The storage pool is responding to commands and is in a normal operating state.<br/>                                                                                                             |
| <span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span><dl> <dt>**Degraded**</dt> <dt>3</dt> </dl>                                                                          | The storage pool is responding to commands, but is not running in an optimal operating state.<br/>                                                                                              |
| <span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span><dl> <dt>**Stressed**</dt> <dt>4</dt> </dl>                                                                          | The storage pool is functioning, but needs attention. For example, the storage subsystem may be overloaded or overheated.<br/>                                                                  |
| <span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span><dl> <dt>**Predictive Failure**</dt> <dt>5</dt> </dl>                                  | The storage pool is functioning, but predicting a failure in the near future.<br/>                                                                                                              |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span><dl> <dt>**Error**</dt> <dt>6</dt> </dl>                                                                                      | An error has occurred.<br/>                                                                                                                                                                     |
| <span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span><dl> <dt>**Non-Recoverable Error**</dt> <dt>7</dt> </dl>                      | An nonrecoverable error has occurred.<br/>                                                                                                                                                      |
| <span id="Starting"></span><span id="starting"></span><span id="STARTING"></span><dl> <dt>**Starting**</dt> <dt>8</dt> </dl>                                                                          | The storage pool is in the process of starting.<br/>                                                                                                                                            |
| <span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span><dl> <dt>**Stopping**</dt> <dt>9</dt> </dl>                                                                          | The storage pool is in the process of stopping.<br/>                                                                                                                                            |
| <span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span><dl> <dt>**Stopped**</dt> <dt>10</dt> </dl>                                                                             | The storage pool was stopped in a clean and orderly fashion.<br/>                                                                                                                               |
| <span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span><dl> <dt>**In Service**</dt> <dt>11</dt> </dl>                                                                 | The storage pool is being configured, maintained, cleaned, or otherwise administered.<br/>                                                                                                      |
| <span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span><dl> <dt>**No Contact**</dt> <dt>12</dt> </dl>                                                                 | The storage provider has knowledge of the storage pool, but has never been able to establish communication with it.<br/>                                                                        |
| <span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span><dl> <dt>**Lost Communication**</dt> <dt>13</dt> </dl>                                 | The storage provider has knowledge of the storage pool and has contacted it successfully in the past, but is the storage subsystem is currently unreachable.<br/>                               |
| <span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span><dl> <dt>**Aborted**</dt> <dt>14</dt> </dl>                                                                             | Similar to **Stopped**, except that the storage pool stopped abruptly and may require configuration or maintenance.<br/>                                                                        |
| <span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span><dl> <dt>**Dormant**</dt> <dt>15</dt> </dl>                                                                             | The storage pool is reachable, but it is inactive.<br/>                                                                                                                                         |
| <span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span><dl> <dt>**Supporting Entity in Error**</dt> <dt>16</dt> </dl> | This status value does not necessarily indicate trouble with the storage pool, but it does indicate that another device or connection that the storage pool depends on may need attention.<br/> |
| <span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span><dl> <dt>**Completed**</dt> <dt>17</dt> </dl>                                                                     | The storage pool has completed an operation. This status value should be combined with **OK**, **Error**, or **Degraded**, depending on the outcome of the operation<br/>                       |
| <span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span><dl> <dt>**Power Mode**</dt> <dt>18</dt> </dl>                                                                 | This value is reserved for system use.<br/>                                                                                                                                                     |
| <span id="Relocating"></span><span id="relocating"></span><span id="RELOCATING"></span><dl> <dt>**Relocating**</dt> <dt>19</dt> </dl>                                                                 | The storage pool is in the process of relocating.<br/>                                                                                                                                          |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span><dl> <dt>**Microsoft Reserved**</dt> <dt>..</dt> </dl>                                 | This value is reserved for system use.<br/>                                                                                                                                                     |
| <span id="Majority_Disks_Unhealthy"></span><span id="majority_disks_unhealthy"></span><span id="MAJORITY_DISKS_UNHEALTHY"></span><dl> <dt>**Majority Disks Unhealthy**</dt> <dt>0x8000</dt> </dl>     | This value is reserved for system use.<br/>                                                                                                                                                     |
| <span id="Minority_Disks_Unhealthy"></span><span id="minority_disks_unhealthy"></span><span id="MINORITY_DISKS_UNHEALTHY"></span><dl> <dt>**Minority Disks Unhealthy**</dt> <dt>0x8001</dt> </dl>     | This value is reserved for system use.<br/>                                                                                                                                                     |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span><dl> <dt>**Microsoft Reserved**</dt> <dt>0x8002..</dt> </dl>                           | This value is reserved for system use.<br/>                                                                                                                                                     |



 

</dd> <dt>

**OtherOperationalStatusDescription**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string representation of the vendor-defined status. This property should only be set if the value of the **OperationalStatus** property is **Other**.

</dd> <dt>

**OtherUsageDescription**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string representation of the vendor defined usage for the storage pool. This property can only be specified if the **Usage** property is set to **Other**.

</dd> <dt>

**PhysicalSectorSize**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes")
</dt> </dl>

Physical sector size, in bytes. This value is derived from the backing physical disks that belong to the storage pool.

</dd> <dt>

**ProvisioningTypeDefault**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The default provisioning scheme to use when creating new virtual disks in the storage pool.



| Value                                                                                                                                                                                                                       | Meaning                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl> | The allocation policy is unknown. This could mean that this information is unavailable, or the storage pool uses a proprietary method of allocation.<br/> |
| <span id="Thin"></span><span id="thin"></span><span id="THIN"></span><dl> <dt>**Thin**</dt> <dt>1</dt> </dl>             | Storage for the virtual disk is allocated on demand.<br/>                                                                                                 |
| <span id="Fixed"></span><span id="fixed"></span><span id="FIXED"></span><dl> <dt>**Fixed**</dt> <dt>2 </dt> </dl>        | Storage for the virtual disk is allocated at the time of virtual disk creation.<br/>                                                                      |



 

</dd> <dt>

**ReadOnlyReason**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The reason why the storage pool is read-only.



| Value                                                                                                                                                                                                                                                                                           | Meaning                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                                     | The reason is unknown.<br/>                                                                                                                 |
| <span id="None"></span><span id="none"></span><span id="NONE"></span><dl> <dt>**None**</dt> <dt>1</dt> </dl>                                                                                 | The pool is not read-only.<br/>                                                                                                             |
| <span id="By_Policy"></span><span id="by_policy"></span><span id="BY_POLICY"></span><dl> <dt>**By Policy**</dt> <dt>2 </dt> </dl>                                                            | The administrator has requested the pool to be read-only or has enacted a policy on the system that requires the pool to be read-only.<br/> |
| <span id="Majority_Disks_Unhealthy"></span><span id="majority_disks_unhealthy"></span><span id="MAJORITY_DISKS_UNHEALTHY"></span><dl> <dt>**Majority Disks Unhealthy**</dt> <dt>3</dt> </dl> | The majority of the supporting physical disks are in an unhealthy state, which has forced the storage pool into a read-only state.<br/>     |



 

</dd> <dt>

**RepairPolicy**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

How the operating system repairs virtual disks for this storage pool.



| Value                                                                                                | Meaning                                                                                                                                                |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Sequential - processes one allocation slab at a time. Repairs take longer, but with less impact on the I/O load.<br/>                            |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | Parallel - processes as many allocation slabs as it can in parallel. Repair time is minimized, but with significant impact on the I/O load.<br/> |



 

</dd> <dt>

**ResiliencySettingNameDefault**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**ModelCorrespondence {"MSFT\_ResiliencySetting.Name"}**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The desired resiliency setting to be used by default when creating new virtual disks on the storage pool. This default value can be overridden at the time of virtual disk creation. This property's value should correspond to the [**MSFT\_ResiliencySetting**](msft-resiliencysetting.md) object's **Name** property.

</dd> <dt>

**RetireMissingPhysicalDisks**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** ( "Auto", "Always", "Never" ), **ValueMap** ("1", "2", "3")
</dt> </dl>

Specifies whether the storage subsystem will automatically retire physical disks that are missing from this storage pool and replace them with hot spares or other physical disks that are available in the storage pool.

</dd> <dt>

**Size**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes")
</dt> </dl>

The capacity of the storage pool. If the pool is primordial, this is the sum of all the healthy physical disk sizes. If the pool is concrete, this is the sum of all associated physical disks (except hot spares, and including failed drives).

</dd> <dt>

**SupportedProvisioningTypes**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The provisioning schemes that the storage pool supports for creating virtual disks.



| Value                                                                                                                                                                                                                       | Meaning                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl> | The allocation policy is unknown. This could mean that this information is unavailable, or the storage pool uses a proprietary method of allocation.<br/> |
| <span id="Thin"></span><span id="thin"></span><span id="THIN"></span><dl> <dt>**Thin**</dt> <dt>1</dt> </dl>             | Storage for the virtual disk is allocated on demand.<br/>                                                                                                 |
| <span id="Fixed"></span><span id="fixed"></span><span id="FIXED"></span><dl> <dt>**Fixed**</dt> <dt>2 </dt> </dl>        | Storage for the virtual disk is allocated at the time of virtual disk creation.<br/>                                                                      |



 

</dd> <dt>

**SupportsDeduplication**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if the storage pool supports data deduplication.

</dd> <dt>

**ThinProvisioningAlertThresholds**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Percentage"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (0), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (100)
</dt> </dl>

An array of percentage values that represent various sparse (thin provisioning) thresholds. When the virtual disk space usage crosses one of these thresholds, a notification will be broadcasted to all subscribed clients.

</dd> <dt>

**Usage**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The intended use of the storage pool.

You can specify a predefined description or a custom description. To specify a predefined description, use a value other than **Other**.

To specify a custom description, use **Other** and specify a non-NULL value for the **OtherUsageDescription** property.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

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
</dt> </dl>

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The minimum OS version that supports this storage pool.



| Value                                                                                                | Meaning                                   |
|------------------------------------------------------------------------------------------------------|-------------------------------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | Windows Server 2012<br/>            |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Windows Server 2012 R2 Preview<br/> |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | Windows Server 2012 R2<br/>         |



 

</dd> <dt>

**WriteCacheSizeDefault**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Default size of write cache for virtual disk creation.

</dd> <dt>

**WriteCacheSizeMax**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum size of write cache for virtual disk creation.

</dd> <dt>

**WriteCacheSizeMin**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Minimum size of write cache for virtual disk creation.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



 

 





