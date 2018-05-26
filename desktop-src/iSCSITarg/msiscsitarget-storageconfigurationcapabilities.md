---
title: MSISCSITARGET\_StorageConfigurationCapabilities class
description: Defines the capabilities of a MSISCSITARGET\_StorageConfigurationService instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 289b005a-50b0-4b56-bdf8-760e3e15daf8
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSISCSITARGET_StorageConfigurationCapabilities class iSCSI Software Target API
- MSISCSITARGET_StorageConfigurationCapabilities class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageConfigurationCapabilities
- MSISCSITARGET_StorageConfigurationCapabilities.Caption
- MSISCSITARGET_StorageConfigurationCapabilities.Description
- MSISCSITARGET_StorageConfigurationCapabilities.InstanceID
- MSISCSITARGET_StorageConfigurationCapabilities.ElementName
- MSISCSITARGET_StorageConfigurationCapabilities.SupportedAsynchronousActions
- MSISCSITARGET_StorageConfigurationCapabilities.SupportedSynchronousActions
- MSISCSITARGET_StorageConfigurationCapabilities.SupportedStorageElementTypes
- MSISCSITARGET_StorageConfigurationCapabilities.SupportedStoragePoolFeatures
- MSISCSITARGET_StorageConfigurationCapabilities.SupportedStorageElementFeatures
- MSISCSITARGET_StorageConfigurationCapabilities.SupportedCopyTypes
- MSISCSITARGET_StorageConfigurationCapabilities.InitialReplicationState
- MSISCSITARGET_StorageConfigurationCapabilities.SupportedStorageElementUsage
- MSISCSITARGET_StorageConfigurationCapabilities.ClientSettableElementUsage
- MSISCSITARGET_StorageConfigurationCapabilities.SupportedStoragePoolUsage
- MSISCSITARGET_StorageConfigurationCapabilities.ClientSettablePoolUsage
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSISCSITARGET\_StorageConfigurationCapabilities class

Defines the capabilities of a [**MSISCSITARGET\_StorageConfigurationService**](msiscsitarget-storageconfigurationservice.md) instance. An instance of **MSISCSITARGET\_StorageConfigurationCapabilities** is associated with a [**MSISCSITARGET\_StorageConfigurationService**](msiscsitarget-storageconfigurationservice.md) by using [**MSISCSITARGET\_ElementCapabilities**](msiscsitarget-elementcapabilities.md).

The **MSISCSITARGET\_StorageConfigurationCapabilities** class specifies the range of capabilities for storage configuration in an associated storage pool or service. It contains properties that correspond to the properties of the same base names in the [**MSISCSITARGET\_StorageSetting**](msiscsitarget-storagesetting.md) and **CIM\_StorageSettingWithHints** classes, which can be used as the *Goal* parameter in several [**MSISCSITARGET\_StorageConfigurationService**](msiscsitarget-storageconfigurationservice.md) methods.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Static, Version("1.0.0")]
class MSISCSITARGET_StorageConfigurationCapabilities : CIM_StorageConfigurationCapabilities
{
  string Caption;
  string Description;
  string InstanceID;
  string ElementName;
  uint16 SupportedAsynchronousActions[];
  uint16 SupportedSynchronousActions[];
  uint16 SupportedStorageElementTypes[];
  uint16 SupportedStoragePoolFeatures[];
  uint16 SupportedStorageElementFeatures[];
  uint16 SupportedCopyTypes[];
  uint16 InitialReplicationState;
  uint16 SupportedStorageElementUsage[];
  uint16 ClientSettableElementUsage[];
  uint16 SupportedStoragePoolUsage[];
  uint16 ClientSettablePoolUsage[];
};
```

## Members

The **MSISCSITARGET\_StorageConfigurationCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSISCSITARGET\_StorageConfigurationCapabilities** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The Caption property is a short textual description (one- line string) of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ClientSettableElementUsage**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageExtent.Usage")
</dt> </dl>

Indicates the intended usage or any restrictions that may have been imposed on the usage of Client Settable Elements. For example, an element may be reserved for use by the block server. In that case the Usage of the element is marked as "Reserved for the ComputerSystem". In the case of "Other", see OtherUsageDescription for more information.

This property is inherited from [**CIM\_StorageConfigurationCapabilities**](cim-storageconfigurationcapabilities.md).

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

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**ClientSettablePoolUsage**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StoragePool.OtherUsageDescription")
</dt> </dl>

Indicates the intended usage or any restrictions that may have been imposed on the usage a client settable storage pool. For example, a storage pool may be reserved for use by the block server. In that case the Usage of the storage pool is marked as "Reserved for the ComputerSystem". In the case of "Other", see OtherUsageDescription for more information.

This property is inherited from [**CIM\_StorageConfigurationCapabilities**](cim-storageconfigurationcapabilities.md).

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


</dt> <dd>9 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Contains a textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The user friendly name for this instance of Capabilities. In addition, the user friendly name can be used as a index property for a search of query. (Note: Name does not have to be unique within a namespace.)

This property is inherited from [**CIM\_Capabilities**](cim-capabilities.md).

</dd> <dt>

**InitialReplicationState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageConfigurationService.AttachReplica", "CIM\_StorageConfigurationService.CreateReplica")
</dt> </dl>

InitialReplicationState specifies which initial ReplicationState is supported by a particular provider. Values are:

Initialized: The replication relationship is known and unsynchronized, but time required to synchronize may be long.

Prepared: The replication relationship is known and unsynchronized and the time required to synchronize will be short.

Synchronized: The replicas are synchronized.

This property is inherited from [**CIM\_StorageConfigurationCapabilities**](cim-storageconfigurationcapabilities.md).

<dt>

<span id="Initialized"></span><span id="initialized"></span><span id="INITIALIZED"></span>

**Initialized** (2)


</dt> <dd></dd> <dt>

<span id="Prepared"></span><span id="prepared"></span><span id="PREPARED"></span>

**Prepared** (3)


</dt> <dd></dd> <dt>

<span id="Synchronized"></span><span id="synchronized"></span><span id="SYNCHRONIZED"></span>

**Synchronized** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following 'preferred' algorithm: &lt;OrgID&gt;:&lt;LocalID&gt; Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon ':', and where &lt;OrgID&gt; MUST include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating/defining the InstanceID, or is a registered ID that is assigned to the business entity by a recognized global authority (This is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness &lt;OrgID&gt; MUST NOT contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID MUST appear between &lt;OrgID&gt; and &lt;LocalID&gt;. &lt;LocalID&gt; is chosen by the business entity and SHOULD not be re-used to identify different underlying (real-world) elements. If the above 'preferred' algorithm is not used, the defining entity MUST assure that the resultant InstanceID is not re-used across any InstanceIDs produced by this or other providers for this instance's NameSpace. For DMTF defined instances, the 'preferred' algorithm MUST be used with the &lt;OrgID&gt; set to 'CIM'.

This property is inherited from [**CIM\_Capabilities**](cim-capabilities.md).

</dd> <dt>

**SupportedAsynchronousActions**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageConfigurationCapabilities.SupportedSynchronousActions")
</dt> </dl>

Enumeration indicating what operations will be executed as asynchronous jobs. If an operation is included in both this and SupportedSynchronousActions then the underlying implementation is indicating that it may or may not create a job.

The following values have been deprecated and replaced by values in StorageReplicationCapabilities. SupportedAsynchronousActions:

Replica Creation(8) to Local Replica Creation(2) and Remote Replica Creation(3)

Replica Modification(9) to Local Replica Modification(4), Remote Replica Modification(5) and

Replica Attachment(10) to Local Replica Attachment(6) and Remote Replica Attachment(7).

This property is inherited from [**CIM\_StorageConfigurationCapabilities**](cim-storageconfigurationcapabilities.md).

<dt>

<span id="Storage_Pool_Creation"></span><span id="storage_pool_creation"></span><span id="STORAGE_POOL_CREATION"></span>

**Storage Pool Creation** (2)


</dt> <dd></dd> <dt>

<span id="Storage_Pool_Deletion"></span><span id="storage_pool_deletion"></span><span id="STORAGE_POOL_DELETION"></span>

**Storage Pool Deletion** (3)


</dt> <dd></dd> <dt>

<span id="Storage_Pool_Modification"></span><span id="storage_pool_modification"></span><span id="STORAGE_POOL_MODIFICATION"></span>

**Storage Pool Modification** (4)


</dt> <dd></dd> <dt>

<span id="Storage_Element_Creation"></span><span id="storage_element_creation"></span><span id="STORAGE_ELEMENT_CREATION"></span>

**Storage Element Creation** (5)


</dt> <dd></dd> <dt>

<span id="Storage_Element_Return"></span><span id="storage_element_return"></span><span id="STORAGE_ELEMENT_RETURN"></span>

**Storage Element Return** (6)


</dt> <dd></dd> <dt>

<span id="Storage_Element_Modification"></span><span id="storage_element_modification"></span><span id="STORAGE_ELEMENT_MODIFICATION"></span>

**Storage Element Modification** (7)


</dt> <dd></dd> <dt>

<span id="Replica_Creation"></span><span id="replica_creation"></span><span id="REPLICA_CREATION"></span>

**Replica Creation** (8)


</dt> <dd></dd> <dt>

<span id="Replica_Modification"></span><span id="replica_modification"></span><span id="REPLICA_MODIFICATION"></span>

**Replica Modification** (9)


</dt> <dd></dd> <dt>

<span id="Replica_Attachment"></span><span id="replica_attachment"></span><span id="REPLICA_ATTACHMENT"></span>

**Replica Attachment** (10)


</dt> <dd></dd> <dt>

<span id="SCSI_Scan"></span><span id="scsi_scan"></span><span id="SCSI_SCAN"></span>

**SCSI Scan** (11)


</dt> <dd></dd> <dt>

<span id="Storage_Element_from_Element_Creation"></span><span id="storage_element_from_element_creation"></span><span id="STORAGE_ELEMENT_FROM_ELEMENT_CREATION"></span>

**Storage Element from Element Creation** (12)


</dt> <dd></dd> <dt>

<span id="Storage_Element_from_Element_Modification"></span><span id="storage_element_from_element_modification"></span><span id="STORAGE_ELEMENT_FROM_ELEMENT_MODIFICATION"></span>

**Storage Element from Element Modification** (13)


</dt> <dd></dd> <dt>

<span id="Element_Usage_Modification"></span><span id="element_usage_modification"></span><span id="ELEMENT_USAGE_MODIFICATION"></span>

**Element Usage Modification** (14)


</dt> <dd></dd> <dt>

<span id="StoragePool_Usage_Modification"></span><span id="storagepool_usage_modification"></span><span id="STORAGEPOOL_USAGE_MODIFICATION"></span>

**StoragePool Usage Modification** (15)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>16 65535</dd> </dl>

</dd> <dt>

**SupportedCopyTypes**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageConfigurationService.CreateReplica.CopyType")
</dt> </dl>

SupportedCopyTypes describes the replication capabilities supported by the associated StorageConfigurationServices. Values are:

Async: asynchronous copies may be created and maintained.

Sync: synchronous copies may be created and maintained.

UnSyncAssoc: unsynchronized copies may be created and maintained.

UnSyncUnAssoc: a 'straight copy' may be created.

This property is inherited from [**CIM\_StorageConfigurationCapabilities**](cim-storageconfigurationcapabilities.md).

<dt>

<span id="Async"></span><span id="async"></span><span id="ASYNC"></span>

**Async** (2)


</dt> <dd></dd> <dt>

<span id="Sync"></span><span id="sync"></span><span id="SYNC"></span>

**Sync** (3)


</dt> <dd></dd> <dt>

<span id="UnSyncAssoc"></span><span id="unsyncassoc"></span><span id="UNSYNCASSOC"></span>

**UnSyncAssoc** (4)


</dt> <dd></dd> <dt>

<span id="UnSyncUnAssoc"></span><span id="unsyncunassoc"></span><span id="UNSYNCUNASSOC"></span>

**UnSyncUnAssoc** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>6 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**SupportedStorageElementFeatures**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageConfigurationService.CreateOrModifyElementFromStoragePool.ElementType", "CIM\_StorageConfigurationService.CreateOrModifyElementFromStoragePool.InPool", "CIM\_StorageConfigurationService", "CreateOrModifyElementFromElements.InElements")
</dt> </dl>

Enumeration indicating features supported by the Storage Element methods.

This property is inherited from [**CIM\_StorageConfigurationCapabilities**](cim-storageconfigurationcapabilities.md).

<dt>

<span id="StorageExtent_Creation"></span><span id="storageextent_creation"></span><span id="STORAGEEXTENT_CREATION"></span>

**StorageExtent Creation** (2)


</dt> <dd></dd> <dt>

<span id="StorageVolume_Creation"></span><span id="storagevolume_creation"></span><span id="STORAGEVOLUME_CREATION"></span>

**StorageVolume Creation** (3)


</dt> <dd></dd> <dt>

<span id="StorageExtent_Modification"></span><span id="storageextent_modification"></span><span id="STORAGEEXTENT_MODIFICATION"></span>

**StorageExtent Modification** (4)


</dt> <dd></dd> <dt>

<span id="StorageVolume_Modification"></span><span id="storagevolume_modification"></span><span id="STORAGEVOLUME_MODIFICATION"></span>

**StorageVolume Modification** (5)


</dt> <dd></dd> <dt>

<span id="Single_InPool"></span><span id="single_inpool"></span><span id="SINGLE_INPOOL"></span>

**Single InPool** (6)


</dt> <dd></dd> <dt>

<span id="Multiple_InPools"></span><span id="multiple_inpools"></span><span id="MULTIPLE_INPOOLS"></span>

**Multiple InPools** (7)


</dt> <dd></dd> <dt>

<span id="LogicalDisk_Creation"></span><span id="logicaldisk_creation"></span><span id="LOGICALDISK_CREATION"></span>

**LogicalDisk Creation** (8)


</dt> <dd></dd> <dt>

<span id="LogicalDisk_Modification"></span><span id="logicaldisk_modification"></span><span id="LOGICALDISK_MODIFICATION"></span>

**LogicalDisk Modification** (9)


</dt> <dd></dd> <dt>

<span id="InElements"></span><span id="inelements"></span><span id="INELEMENTS"></span>

**InElements** (10)


</dt> <dd></dd> <dt>

<span id="Storage_Element_QoS_Change"></span><span id="storage_element_qos_change"></span><span id="STORAGE_ELEMENT_QOS_CHANGE"></span>

**Storage Element QoS Change** (11)


</dt> <dd></dd> <dt>

<span id="Storage_Element_Capacity_Expansion"></span><span id="storage_element_capacity_expansion"></span><span id="STORAGE_ELEMENT_CAPACITY_EXPANSION"></span>

**Storage Element Capacity Expansion** (12)


</dt> <dd></dd> <dt>

<span id="Storage_Element_Capacity_Reduction"></span><span id="storage_element_capacity_reduction"></span><span id="STORAGE_ELEMENT_CAPACITY_REDUCTION"></span>

**Storage Element Capacity Reduction** (13)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>14 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**SupportedStorageElementTypes**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageConfigurationService.CreateOrModifyElementFromStoragePool.ElementType", "CIM\_StorageConfigurationService", "CreateOrModifyElementFromElements.ElementType")
</dt> </dl>

Enumeration indicating the type of storage elements that are supported by the associated StorageConfigurationService.

This property is inherited from [**CIM\_StorageConfigurationCapabilities**](cim-storageconfigurationcapabilities.md).

<dt>

<span id="StorageVolume"></span><span id="storagevolume"></span><span id="STORAGEVOLUME"></span>

**StorageVolume** (2)


</dt> <dd></dd> <dt>

<span id="StorageExtent"></span><span id="storageextent"></span><span id="STORAGEEXTENT"></span>

**StorageExtent** (3)


</dt> <dd></dd> <dt>

<span id="LogicalDisk"></span><span id="logicaldisk"></span><span id="LOGICALDISK"></span>

**LogicalDisk** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**SupportedStorageElementUsage**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageExtent.Usage")
</dt> </dl>

Indicates the intended usage or any restrictions that may have been imposed on the usage of Supported Storage Elements. For example, an element may be reserved for use by the block server. In that case the Usage of the element is marked as "Reserved for the ComputerSystem". In the case of "Other", see OtherUsageDescription for more information.

This property is inherited from [**CIM\_StorageConfigurationCapabilities**](cim-storageconfigurationcapabilities.md).

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

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**SupportedStoragePoolFeatures**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageConfigurationService.CreateOrModifyStoragePool.InPools", "CIM\_StorageConfigurationService", "CreateOrModifyStoragePool.InExtents")
</dt> </dl>

Enumeration indicating features supported by the StoragePool methods.

This property is inherited from [**CIM\_StorageConfigurationCapabilities**](cim-storageconfigurationcapabilities.md).

<dt>

<span id="InExtents"></span><span id="inextents"></span><span id="INEXTENTS"></span>

**InExtents** (2)


</dt> <dd></dd> <dt>

<span id="Single_InPool"></span><span id="single_inpool"></span><span id="SINGLE_INPOOL"></span>

**Single InPool** (3)


</dt> <dd></dd> <dt>

<span id="Multiple_InPools"></span><span id="multiple_inpools"></span><span id="MULTIPLE_INPOOLS"></span>

**Multiple InPools** (4)


</dt> <dd></dd> <dt>

<span id="Storage_Pool_QoS_Change"></span><span id="storage_pool_qos_change"></span><span id="STORAGE_POOL_QOS_CHANGE"></span>

**Storage Pool QoS Change** (5)


</dt> <dd></dd> <dt>

<span id="Storage_Pool_Capacity_Expansion"></span><span id="storage_pool_capacity_expansion"></span><span id="STORAGE_POOL_CAPACITY_EXPANSION"></span>

**Storage Pool Capacity Expansion** (6)


</dt> <dd></dd> <dt>

<span id="Storage_Pool_Capacity_Reduction"></span><span id="storage_pool_capacity_reduction"></span><span id="STORAGE_POOL_CAPACITY_REDUCTION"></span>

**Storage Pool Capacity Reduction** (7)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>8 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**SupportedStoragePoolUsage**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StoragePool.OtherUsageDescription")
</dt> </dl>

Indicates the intended usage or any restrictions that may have been imposed on the usage a supported storage pool. For example, a storage pool may be reserved for use by the block server. In that case the Usage of the storage pool is marked as "Reserved for the ComputerSystem". In the case of "Other", see OtherUsageDescription for more information.

This property is inherited from [**CIM\_StorageConfigurationCapabilities**](cim-storageconfigurationcapabilities.md).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unrestricted"></span><span id="unrestricted"></span><span id="UNRESTRICTED"></span>

**Unrestricted** (2)


</dt> <dd></dd> <dt>

<span id="Reserved_for_ComputerSystem__the_block_server__"></span><span id="reserved_for_computersystem__the_block_server__"></span><span id="RESERVED_FOR_COMPUTERSYSTEM__THE_BLOCK_SERVER__"></span>

**Reserved for ComputerSystem (the block server),** (3)


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


</dt> <dd>9 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**SupportedSynchronousActions**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageConfigurationCapabilities.SupportedAsynchronousActions")
</dt> </dl>

Enumeration indicating what operations will be executed without the creation of a job. If an operation is included in both this and SupportedAsynchronousActions then the underlying instrumentation is indicating that it may or may not create a job.

The following values have been deprecated and replaced by values in StorageReplicationCapabilities.SupportedSynchronousActions:

Replica Creation(8) to Local Replica Creation(2) and Remote Replica Creation(3)

Replica Modification(9) to Local Replica Modification(4), Remote Replica Modification(5) and

Replica Attachment(10) to Local Replica Attachment(6) and Remote Replica Attachment(7).

This property is inherited from [**CIM\_StorageConfigurationCapabilities**](cim-storageconfigurationcapabilities.md).

<dt>

<span id="Storage_Pool_Creation"></span><span id="storage_pool_creation"></span><span id="STORAGE_POOL_CREATION"></span>

**Storage Pool Creation** (2)


</dt> <dd></dd> <dt>

<span id="Storage_Pool_Deletion"></span><span id="storage_pool_deletion"></span><span id="STORAGE_POOL_DELETION"></span>

**Storage Pool Deletion** (3)


</dt> <dd></dd> <dt>

<span id="Storage_Pool_Modification"></span><span id="storage_pool_modification"></span><span id="STORAGE_POOL_MODIFICATION"></span>

**Storage Pool Modification** (4)


</dt> <dd></dd> <dt>

<span id="Storage_Element_Creation"></span><span id="storage_element_creation"></span><span id="STORAGE_ELEMENT_CREATION"></span>

**Storage Element Creation** (5)


</dt> <dd></dd> <dt>

<span id="Storage_Element_Return"></span><span id="storage_element_return"></span><span id="STORAGE_ELEMENT_RETURN"></span>

**Storage Element Return** (6)


</dt> <dd></dd> <dt>

<span id="Storage_Element_Modification"></span><span id="storage_element_modification"></span><span id="STORAGE_ELEMENT_MODIFICATION"></span>

**Storage Element Modification** (7)


</dt> <dd></dd> <dt>

<span id="Replica_Creation"></span><span id="replica_creation"></span><span id="REPLICA_CREATION"></span>

**Replica Creation** (8)


</dt> <dd></dd> <dt>

<span id="Replica_Modification"></span><span id="replica_modification"></span><span id="REPLICA_MODIFICATION"></span>

**Replica Modification** (9)


</dt> <dd></dd> <dt>

<span id="Replica_Attachment"></span><span id="replica_attachment"></span><span id="REPLICA_ATTACHMENT"></span>

**Replica Attachment** (10)


</dt> <dd></dd> <dt>

<span id="SCSI_Scan"></span><span id="scsi_scan"></span><span id="SCSI_SCAN"></span>

**SCSI Scan** (11)


</dt> <dd></dd> <dt>

<span id="Storage_Element_from_Element_Creation"></span><span id="storage_element_from_element_creation"></span><span id="STORAGE_ELEMENT_FROM_ELEMENT_CREATION"></span>

**Storage Element from Element Creation** (12)


</dt> <dd></dd> <dt>

<span id="Storage_Element_from_Element_Modification"></span><span id="storage_element_from_element_modification"></span><span id="STORAGE_ELEMENT_FROM_ELEMENT_MODIFICATION"></span>

**Storage Element from Element Modification** (13)


</dt> <dd></dd> <dt>

<span id="Element_Usage_Modification"></span><span id="element_usage_modification"></span><span id="ELEMENT_USAGE_MODIFICATION"></span>

**Element Usage Modification** (14)


</dt> <dd></dd> <dt>

<span id="StoragePool_Usage_Modification"></span><span id="storagepool_usage_modification"></span><span id="STORAGEPOOL_USAGE_MODIFICATION"></span>

**StoragePool Usage Modification** (15)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>16 65535</dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_StorageConfigurationCapabilities**](cim-storageconfigurationcapabilities.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> <dt>

[**MSISCSITARGET\_StorageConfigurationService**](msiscsitarget-storageconfigurationservice.md)
</dt> <dt>

[**MSISCSITARGET\_ElementCapabilities**](msiscsitarget-elementcapabilities.md)
</dt> <dt>

[**MSISCSITARGET\_StorageSetting**](msiscsitarget-storagesetting.md)
</dt> </dl>

 

 





