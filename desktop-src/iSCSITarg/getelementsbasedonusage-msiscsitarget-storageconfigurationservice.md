---
title: GetElementsBasedOnUsage method of the MSISCSITARGET\_StorageConfigurationService class
description: Retrieves storage elements that match specified usage and availability criteria.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a8769fa3-9c53-46a8-89dc-f61d0feccef8'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetElementsBasedOnUsage method iSCSI Software Target API", "GetElementsBasedOnUsage method iSCSI Software Target API , MSISCSITARGET_StorageConfigurationService class", "MSISCSITARGET_StorageConfigurationService class iSCSI Software Target API , GetElementsBasedOnUsage method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageConfigurationService.GetElementsBasedOnUsage
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# GetElementsBasedOnUsage method of the MSISCSITARGET\_StorageConfigurationService class

Retrieves storage elements that match specified usage and availability criteria.

This method is inherited from the **CIM\_StorageConfigurationService** class.

## Syntax


```mof
uint32 GetElementsBasedOnUsage(
  [in]  uint16                       ElementType,
  [in]  uint16                       Usage,
  [in]  uint16                       Criteria,
  [in]  CIM_StoragePool Ref          ThePool,
  [out] CIM_ManagedSystemElement Ref TheElements[]
);
```



## Parameters

<dl> <dt>

*ElementType* \[in\]
</dt> <dd>

Specifies the type of elements to retrieve.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="StorageVolume"></span><span id="storagevolume"></span><span id="STORAGEVOLUME"></span>

**StorageVolume** (2)


</dt> <dd></dd> <dt>

<span id="StorageExtent"></span><span id="storageextent"></span><span id="STORAGEEXTENT"></span>

**StorageExtent** (3)


</dt> <dd></dd> <dt>

<span id="StoragePool"></span><span id="storagepool"></span><span id="STORAGEPOOL"></span>

**StoragePool** (4)


</dt> <dd></dd> <dt>

<span id="Logical_Disk"></span><span id="logical_disk"></span><span id="LOGICAL_DISK"></span>

**Logical Disk** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>6–0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl> </dd> <dt>

*Usage* \[in\]
</dt> <dd>

Specifies the usage value of the elements to retrieve. This parameter corresponds to the **Usage** property of the storage elements specified in the *ElementType* parameter. Different classes have different possible values for the **Usage** property, for example.

The possible values for the [**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md).**Usage** property are.

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


</dt> <dd>9–0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

The possible values for the [**MSISCSITARGET\_StorageVolume**](msiscsitarget-storagevolume.md).**Usage** property are.

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

<span id="Reserved_for_Migration_Services"></span><span id="reserved_for_migration_services"></span><span id="RESERVED_FOR_MIGRATION_SERVICES"></span>

**Reserved for Migration Services** (5)


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


</dt> <dd>18–0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl> </dd> <dt>

*Criteria* \[in\]
</dt> <dd>

Specifies which elements to retrieve based on their availability.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="All"></span><span id="all"></span><span id="ALL"></span>

**All** (2)


</dt> <dd></dd> <dt>

<span id="Available_Only"></span><span id="available_only"></span><span id="AVAILABLE_ONLY"></span>

**Available Only** (3)


</dt> <dd></dd> <dt>

<span id="In_Use_Only"></span><span id="in_use_only"></span><span id="IN_USE_ONLY"></span>

**In Use Only** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5–0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl> </dd> <dt>

*ThePool* \[in\]
</dt> <dd>

Specifies limiting the search to the specified storage pool. If set to **NULL**, all available storage pools will be searched.

</dd> <dt>

*TheElements* \[out\]
</dt> <dd>

On return, contains references to the retrieved storage element instances.

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unknown** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**DMTF Reserved** (6–4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097–32767)
</dt> <dt>

**Vendor Specific** (32768–65535)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_StorageConfigurationService**](msiscsitarget-storageconfigurationservice.md)
</dt> <dt>

[**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md)
</dt> <dt>

[**MSISCSITARGET\_StorageVolume**](msiscsitarget-storagevolume.md)
</dt> </dl>

 

 





