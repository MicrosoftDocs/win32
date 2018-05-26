---
title: MSFT\_SMStorageVolume class
description: Represents a storage volume.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b2573546-fc9f-428b-9fb9-53d7b5443472
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMStorageVolume class
- MSFT_SMStorageVolume class, described
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SMStorageVolume class

Represents a storage volume.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

**Windows Server 2012 R2 and Windows Server 2012:** This class does not inherit from [**MSFT\_SMStorageObject**](msft-smstorageobject.md) which is new for Windows Server 2016.

## Syntax

``` syntax
[dynamic, provider("WMIStorage"), AMENDMENT]
class MSFT_SMStorageVolume : MSFT_SMStorageObject
{
  String  ObjectId;
  String  Identifier;
  String  DisplayName;
  String  Name;
  Uint16  NameFormat;
  Uint16  NameNamespace;
  String  OtherNameFormat;
  String  OtherNameNamespace;
  String  SMLunId;
  Uint16  SMLunIdFormat;
  String  SMLunIdFormatDescription;
  Uint16  SMLunIdNamespace;
  String  SMLunIdNamespaceDescription;
  uint16  HealthStatus;
  string  HealthStatusDescription;
  uint16  OperationalStatus[];
  string  StatusDescription;
  Uint64  BlockSize;
  Uint64  NumberOfBlocks;
  Uint64  ConsumableBlocks;
  Boolean Primordial;
  String  OtherIdentifyingInfo[];
  String  IdentifyingDescriptions[];
  boolean NoSinglePointOfFailure;
  uint16  ExtentStripeLength;
  uint64  UserDataStripeDepth;
  uint16  DataRedundancy;
  uint16  PackageRedundancy;
  uint16  ParityLayout;
  uint16  Access;
  String  AccessDescription;
  Boolean ThinlyProvisioned = FALSE;
  uint16  Usage;
  Boolean IsSnapshot;
};
```

## Members

The **MSFT\_SMStorageVolume** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_SMStorageVolume** class has these methods.



| Method                                                                                | Description                                                                                                                                                                                  |
|:--------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateClone**](createclone-msft-smstoragevolume.md)                               | Starts a job to create an associated un-synced Clone of the **MSFT\_SMStorageVolume**.<br/>                                                                                            |
| [**CreateReplica**](createreplica-msft-smstoragevolume.md)                           | Creates a replication relationship between virtual disks.<br/> **Windows Server 2012 R2 and Windows Server 2012:** This method is not available before Windows Server 2016.<br/> |
| [**CreateSnapshot**](createsnapshot-msft-smstoragevolume.md)                         | Starts a job to create an associated un-synced snapshot of the **MSFT\_SMStorageVolume**.<br/>                                                                                         |
| [**Delete**](delete-msft-smstoragevolume.md)                                         | Starts a job to delete a storage volume previously created from a storage pool.<br/>                                                                                                   |
| [**ModifySize**](modifysize-msft-smstoragevolume.md)                                 | Starts a job to modify the size of a storage volume.<br/>                                                                                                                              |
| [**SetReadonly**](setreadonly-msft-smstoragevolume.md)                               | Changes the device access of the storage volume to Readable.<br/>                                                                                                                      |
| [**SetReadWrite**](setreadwrite-msft-smstoragevolume.md)                             | Changes the device access of the storage volume to Read/Write.<br/>                                                                                                                    |
| [**SetReplicationRelationship**](setreplicationrelationship-msft-smstoragevolume.md) | Updates a replication relationship between virtual disks.<br/> **Windows Server 2012 R2 and Windows Server 2012:** This method is not available before Windows Server 2016.<br/> |



 

### Properties

The **MSFT\_SMStorageVolume** class has these properties.

<dl> <dt>

**Access**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates read and write access on the volume.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Readable"></span><span id="readable"></span><span id="READABLE"></span>

**Readable** (1)


</dt> <dd></dd> <dt>

<span id="Writeable"></span><span id="writeable"></span><span id="WRITEABLE"></span>

**Writeable** (2)


</dt> <dd></dd> <dt>

<span id="Read_Write_Supported"></span><span id="read_write_supported"></span><span id="READ_WRITE_SUPPORTED"></span>

**Read/Write Supported** (3)


</dt> <dd></dd> <dt>

<span id="Write_Once"></span><span id="write_once"></span><span id="WRITE_ONCE"></span>

**Write Once** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**AccessDescription**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the **Access** value.

</dd> <dt>

**BlockSize**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The size, in bytes, of the blocks in this storage extent. If there is a variable block size, then the maximum block size in bytes is specified. If the block size is "unknown" or if a block concept is not valid (for example, for Aggregate Extents, Memory, or LogicalDisks), the value is "1" (one).

</dd> <dt>

**ConsumableBlocks**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**DataRedundancy**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageExtent.DataRedundancy")
</dt> </dl>

Number of complete copies of data currently maintained.

</dd> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user-friendly name of the storage volume.

</dd> <dt>

**ExtentStripeLength**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

The current status of the LUN (StorageVolume).

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

The current status of the LUN (StorageVolume) in a string format.

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

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md) .

</dd> <dt>

**IdentifyingDescriptions**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains descriptions of the format used in the custom identifiers in **OtherIdentifyingInfo**. There must be a 1:1 mapping between this array and **OtherIdentifyingInfo**.

</dd> <dt>

**IsSnapshot**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if the volume is a snapshot volume.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The system defined name of the storage volume.

</dd> <dt>

**NameFormat**
</dt> <dd> <dl> <dt>

Data type: **Uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the format of the **Name** property.

</dd> <dt>

**NameNamespace**
</dt> <dd> <dl> <dt>

Data type: **Uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The namespace of **Name** value.

</dd> <dt>

**NoSinglePointOfFailure**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageExtent.NoSinglePointOfFailure")
</dt> </dl>

Whether or not there exists no single point of failure.

</dd> <dt>

**NumberOfBlocks**
</dt> <dd> <dl> <dt>

Data type: **Uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of consecutive blocks that form this storage extent. Total size of the storage extent can be calculated by multiplying the value of the **BlockSize** property by the value of this property. If the value of **BlockSize** is "1", this property is the total size of the storage extent.

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

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md) .

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageVolume.OperationalStatus")
</dt> </dl>

The current SMIS status of the LUN (StorageVolume).

The possible values are.

<dt>

<span id="OK"></span><span id="ok"></span>

**OK** (2)


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** (3)


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** (6)


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** (8)


</dt> <dd></dd> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>

**Dormant** (15)


</dt> <dd></dd> </dl>

</dd> <dt>

**OtherIdentifyingInfo**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains custom identifiers for the switch. If this property is set, **IdentifyingDescriptions** must also be set.

</dd> <dt>

**OtherNameFormat**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**OtherNameNamespace**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**PackageRedundancy**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageExtent.PackageRedundancy")
</dt> </dl>

Indicates how many physical packages can fail without data loss.

</dd> <dt>

**ParityLayout**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageSetting.ParityLayout")
</dt> </dl>

Indicates whether a parity-based storage organization is using rotated or non-rotated parity.

The possible values are.

<dt>

<span id="Non-rotated_Parity"></span><span id="non-rotated_parity"></span><span id="NON-ROTATED_PARITY"></span>

**Non-rotated Parity** (1)


</dt> <dd></dd> <dt>

<span id="Rotated_Parity"></span><span id="rotated_parity"></span><span id="ROTATED_PARITY"></span>

**Rotated Parity** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**Primordial**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if the storage volume is a member of a primordial pool; otherwise, **False**.

</dd> <dt>

**SMLunId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**SMLunIdFormat**
</dt> <dd> <dl> <dt>

Data type: **Uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**SMLunIdFormatDescription**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**SMLunIdNamespace**
</dt> <dd> <dl> <dt>

Data type: **Uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**SMLunIdNamespaceDescription**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**StatusDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current SMIS status of the LUN (StorageVolume) in a string format.

</dd> <dt>

**ThinlyProvisioned**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("SNIA\_StorageVolume.ThinlyProvisioned")
</dt> </dl>

**True** if the volume is thinly provisioned; otherwise **False**.

</dd> <dt>

**Usage**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageExtent.Usage")
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

<span id="Reserved_by_Replication_Services"></span><span id="reserved_by_replication_services"></span><span id="RESERVED_BY_REPLICATION_SERVICES"></span>

**Reserved by Replication Services** (4)


</dt> <dd></dd> <dt>

<span id="Reserved_by_Migration_Services"></span><span id="reserved_by_migration_services"></span><span id="RESERVED_BY_MIGRATION_SERVICES"></span>

**Reserved by Migration Services** (5)


</dt> <dd></dd> <dt>

<span id="Local_Replica_Source"></span><span id="local_replica_source"></span><span id="LOCAL_REPLICA_SOURCE"></span>

**Local Replica Source** (6)


</dt> <dd></dd> <dt>

<span id="Remote_Replica_Source"></span><span id="remote_replica_source"></span><span id="REMOTE_REPLICA_SOURCE"></span>

**Remote Replica Source** (7)


</dt> <dd></dd> <dt>

<span id="Local_Replica_Target"></span><span id="local_replica_target"></span><span id="LOCAL_REPLICA_TARGET"></span>

**Local Replica Target** (8)


</dt> <dd></dd> <dt>

<span id="Remote_Replica_Target"></span><span id="remote_replica_target"></span><span id="REMOTE_REPLICA_TARGET"></span>

**Remote Replica Target** (9)


</dt> <dd></dd> <dt>

<span id="Local_Replica_Source_or_Target"></span><span id="local_replica_source_or_target"></span><span id="LOCAL_REPLICA_SOURCE_OR_TARGET"></span>

**Local Replica Source or Target** (10)


</dt> <dd></dd> <dt>

<span id="Remote_Replica_Source_or_Target"></span><span id="remote_replica_source_or_target"></span><span id="REMOTE_REPLICA_SOURCE_OR_TARGET"></span>

**Remote Replica Source or Target** (11)


</dt> <dd></dd> <dt>

<span id="Delta_Replica_Target"></span><span id="delta_replica_target"></span><span id="DELTA_REPLICA_TARGET"></span>

**Delta Replica Target** (12)


</dt> <dd></dd> <dt>

<span id="Element_Component"></span><span id="element_component"></span><span id="ELEMENT_COMPONENT"></span>

**Element Component** (13)


</dt> <dd></dd> <dt>

<span id="Reserved_as_Pool_Contributor"></span><span id="reserved_as_pool_contributor"></span><span id="RESERVED_AS_POOL_CONTRIBUTOR"></span>

**Reserved as Pool Contributor** (14)


</dt> <dd></dd> <dt>

<span id="Composite_Volume_Member"></span><span id="composite_volume_member"></span><span id="COMPOSITE_VOLUME_MEMBER"></span>

**Composite Volume Member** (15)


</dt> <dd></dd> <dt>

<span id="Composite_LogicalDisk_Member"></span><span id="composite_logicaldisk_member"></span><span id="COMPOSITE_LOGICALDISK_MEMBER"></span>

**Composite LogicalDisk Member** (16)


</dt> <dd></dd> <dt>

<span id="Reserved_for_Sparing"></span><span id="reserved_for_sparing"></span><span id="RESERVED_FOR_SPARING"></span>

**Reserved for Sparing** (17)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>18 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**UserDataStripeDepth**
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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMStorageObject**](msft-smstorageobject.md)
</dt> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





