---
title: MSFT\_SMPool class
description: Represents a storage pool. A storage pool is a logical grouping of physical disks that may be used to create virtual disks.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5e32a339-a229-493f-88c5-4d1d210bf94a'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMPool class", "MSFT_SMPool class, described"]
---

# MSFT\_SMPool class

Represents a storage pool. A storage pool is a logical grouping of physical disks that may be used to create virtual disks.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

**Windows Server 2012 R2 and Windows Server 2012:** This class does not inherit from [**MSFT\_SMStorageObject**](msft-smstorageobject.md) which is new for Windows Server 2016.

## Syntax

``` syntax
[dynamic, provider("WMIStorage"), AMENDMENT]
class MSFT_SMPool : MSFT_SMStorageObject
{
  String  ObjectId;
  String  Identifier;
  String  DisplayName;
  String  Name;
  String  PoolID;
  Boolean Primordial;
  Uint64  RemainingManagedSpace;
  Uint64  TotalManagedSpace;
  String  DefaultSettingName;
  boolean NoSinglePointOfFailure;
  boolean NoSinglePointOfFailureDefault;
  uint16  DataRedundancyMax;
  uint16  DataRedundancyMin;
  uint16  DataRedundancyDefault;
  uint16  PackageRedundancyMax;
  uint16  PackageRedundancyMin;
  uint16  PackageRedundancyDefault;
  uint16  ExtentStripeLengthDefault;
  uint16  ParityLayoutDefault;
  uint64  UserDataStripeDepthDefault;
  uint16  Usage;
  string  UsageDescription;
  boolean SupportsStorageVolumeCreation;
  boolean SupportsThinlyProvisionedStorageVolume;
  uint64  SpaceLimit;
  uint16  SpaceLimitDetermination;
  uint16  LowSpaceWarningThreshold;
  uint64  ThinProvisionMetaDataSpace;
  uint16  OperationalStatus[];
  string  StatusDescriptions[];
  uInt16  HealthStatus;
  string  HealthStatusDescription;
};
```

## Members

The **MSFT\_SMPool** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_SMPool** class has these methods.



| Method                                                         | Description                                                                                                                              |
|:---------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|
| [**AddDiskDrives**](adddiskdrives-msft-smpool.md)             | Adds disk drives to a concrete pool.<br/>                                                                                          |
| [**CreateFileSystem**](createfilesystem-msft-smpool.md)       | This method creates a file system<br/>                                                                                             |
| [**CreateStorageVolume**](createstoragevolume-msft-smpool.md) | Starts a job to create a storage volume.<br/>                                                                                      |
| [**Delete**](delete-msft-smpool.md)                           | Starts a job to delete a Pool.<br/>                                                                                                |
| [**GetSizesInfo**](getsizesinfo-msft-smpool.md)               | Returns the possible sizes of child storage volumes that can be created or modified by using capacity from this storage pool.<br/> |



 

### Properties

The **MSFT\_SMPool** class has these properties.

<dl> <dt>

**DataRedundancyDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**DataRedundancyMax**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**DataRedundancyMin**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**DefaultSettingName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user-friendly name of the storage pool.

</dd> <dt>

**ExtentStripeLengthDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **uInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current status of the pool.

The possible values are.

<dt>

<span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span>

**Healthy** (0)


</dt> <dd></dd> <dt>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>

**Warning** (1)


</dt> <dd></dd> <dt>

<span id="Unhealthy"></span><span id="unhealthy"></span><span id="UNHEALTHY"></span>

**Unhealthy** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**HealthStatusDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current status of the pool in a string format.

</dd> <dt>

**Identifier**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The ID of the logical instance of the object. This ID must be unique within the scope of the storage system.

This property is inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md) .

</dd> <dt>

**LowSpaceWarningThreshold**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (0), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (100), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StoragePool.RemainingManagedSpace"), **PUnit** ("percent"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Percentage")
</dt> </dl>

A low space warning is generated when the remaining space is reduced to this percentage of the total storage capacity.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A human-readable string used to identify the storage pool. This property is unique within the storage subsystem.

</dd> <dt>

**NoSinglePointOfFailure**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**NoSinglePointOfFailureDefault**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**ObjectId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The ID of this class instance. This ID must be unique within the scope of the Windows Storage Management server that hosts the provider object.

This property is inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md) .

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ManagedSystemElement.StatusDescriptions")
</dt> </dl>

The current status of the pool.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="OK"></span><span id="ok"></span>

**OK** (2)


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** (3)


</dt> <dd></dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

**Stressed** (4)


</dt> <dd></dd> <dt>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>

**Predictive Failure** (5)


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** (6)


</dt> <dd></dd> <dt>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>

**Non-Recoverable Error** (7)


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** (8)


</dt> <dd></dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

**Stopping** (9)


</dt> <dd></dd> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>

**Stopped** (10)


</dt> <dd></dd> <dt>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>

**In Service** (11)


</dt> <dd></dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

**No Contact** (12)


</dt> <dd></dd> <dt>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>

**Lost Communication** (13)


</dt> <dd></dd> <dt>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>

**Aborted** (14)


</dt> <dd></dd> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>

**Dormant** (15)


</dt> <dd></dd> <dt>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>

**Supporting Entity in Error** (16)


</dt> <dd></dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>

**Completed** (17)


</dt> <dd></dd> <dt>

<span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span>

**Power Mode** (18)


</dt> <dd></dd> <dt>

<span id="Relocating"></span><span id="relocating"></span><span id="RELOCATING"></span>

**Relocating** (19)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>20–32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**PackageRedundancyDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**PackageRedundancyMax**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**PackageRedundancyMin**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**ParityLayoutDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**PoolID**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The storage pool ID.

</dd> <dt>

**Primordial**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if the storage pool is primordial; otherwise, **False**. A primordial pool, also known as the 'available storage' pool is where storage capacity is drawn and returned in the creation and deletion of concrete storage pools. Primordial pools cannot be created or deleted.

</dd> <dt>

**RemainingManagedSpace**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The amount of unused space in the storage pool, in bytes.

</dd> <dt>

**SpaceLimit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **PUnit** ("byte"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes")
</dt> </dl>

The capacity of the storage allocated to the pool.

When the value of the **SpaceLimitDetermination** property is Allocated, **SpaceLimit** is set to the value of **TotalManagedSpace**.

</dd> <dt>

**SpaceLimitDetermination**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

How the value of the **SpaceLimit** property is determined.

The possible values.

<dt>

<span id="Allocated"></span><span id="allocated"></span><span id="ALLOCATED"></span>

**Allocated** (2)


</dt> <dd></dd> <dt>

<span id="Quote"></span><span id="quote"></span><span id="QUOTE"></span>

**Quote** (3)


</dt> <dd></dd> <dt>

<span id="Limitless"></span><span id="limitless"></span><span id="LIMITLESS"></span>

**Limitless** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ManagedSystemElement.OperationalStatus")
</dt> </dl>

Describes the corresponding entry in the **OperationalStatus** array.

</dd> <dt>

**SupportsStorageVolumeCreation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the pool is capable of providing storage volumes.

</dd> <dt>

**SupportsThinlyProvisionedStorageVolume**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the pool is capable of providing thinly provisioned storage volumes

</dd> <dt>

**ThinProvisionMetaDataSpace**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **PUnit** ("byte"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes")
</dt> </dl>

The size, in bytes, of metadata consumed by this storage pool. This property is only defined if the pool is thinly provisioned."

</dd> <dt>

**TotalManagedSpace**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The size of the storage pool, in bytes.

</dd> <dt>

**Usage**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StoragePool.OtherUsageDescription")
</dt> </dl>

The intended usage or any restrictions that may have been imposed on the usage of this component.

The possible values are.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unrestricted"></span><span id="unrestricted"></span><span id="UNRESTRICTED"></span>

**Unrestricted** (2)


</dt> <dd></dd> <dt>

<span id="Reserved_for_ComputerSystem__the_block_server_"></span><span id="reserved_for_computersystem__the_block_server_"></span><span id="RESERVED_FOR_COMPUTERSYSTEM__THE_BLOCK_SERVER_"></span>

**Reserved for ComputerSystem (the block server)** (3)


</dt> <dd></dd> <dt>

<span id="Reserved_as_a_Delta_Replica_Container"></span><span id="reserved_as_a_delta_replica_container"></span><span id="RESERVED_AS_A_DELTA_REPLICA_CONTAINER"></span>

**Reserved as a Delta Replica Container** (4)


</dt> <dd></dd> <dt>

<span id="Reserved_for_Migration_Services"></span><span id="reserved_for_migration_services"></span><span id="RESERVED_FOR_MIGRATION_SERVICES"></span>

**Reserved for Migration Services** (5)


</dt> <dd></dd> <dt>

<span id="Reserved_for_Local_Replication_Services"></span><span id="reserved_for_local_replication_services"></span><span id="RESERVED_FOR_LOCAL_REPLICATION_SERVICES"></span>

**Reserved for Local Replication Services** (6)


</dt> <dd></dd> <dt>

<span id="Reserved_for_Remote_Replication_Services"></span><span id="reserved_for_remote_replication_services"></span><span id="RESERVED_FOR_REMOTE_REPLICATION_SERVICES"></span>

**Reserved for Remote Replication Services** (7)


</dt> <dd></dd> <dt>

<span id="Reserved_for_Sparing"></span><span id="reserved_for_sparing"></span><span id="RESERVED_FOR_SPARING"></span>

**Reserved for Sparing** (8)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>9–32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**UsageDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the usage when the **Usage** property is **Other**.

</dd> <dt>

**UserDataStripeDepthDefault**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMStorageObject**](msft-smstorageobject.md)
</dt> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





