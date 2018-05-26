---
title: GetSupportedMaximum method of the MSISCSITARGET\_ReplicationServiceCapabilities class
description: Retrieves the maximum number of the specified component type that the service supports for the specified replication type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d4a5c335-58ad-49f4-b36a-478db6f4d8c1
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSupportedMaximum method iSCSI Software Target API
- GetSupportedMaximum method iSCSI Software Target API , MSISCSITARGET_ReplicationServiceCapabilities class
- MSISCSITARGET_ReplicationServiceCapabilities class iSCSI Software Target API , GetSupportedMaximum method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationServiceCapabilities.GetSupportedMaximum
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetSupportedMaximum method of the MSISCSITARGET\_ReplicationServiceCapabilities class

Retrieves the maximum number of the specified component type that the service supports for the specified replication type.

This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.

## Syntax


```mof
uint32 GetSupportedMaximum(
  [in]  uint16 ReplicationType,
  [in]  uint16 Component,
  [out] uint64 MaxValue
);
```



## Parameters

<dl> <dt>

*ReplicationType* \[in\]
</dt> <dd>

Specifies the replication type.

The [**MSISCSITARGET\_ReplicationServiceCapabilities**](msiscsitarget-replicationservicecapabilities.md).**SupportedReplicationTypes** property values are.

<dt>

<span id="Synchronous_Mirror_Local"></span><span id="synchronous_mirror_local"></span><span id="SYNCHRONOUS_MIRROR_LOCAL"></span>

**Synchronous Mirror Local** (2)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Mirror_Local"></span><span id="asynchronous_mirror_local"></span><span id="ASYNCHRONOUS_MIRROR_LOCAL"></span>

**Asynchronous Mirror Local** (3)


</dt> <dd></dd> <dt>

<span id="Synchronous_Mirror_Remote"></span><span id="synchronous_mirror_remote"></span><span id="SYNCHRONOUS_MIRROR_REMOTE"></span>

**Synchronous Mirror Remote** (4)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Mirror_Remote"></span><span id="asynchronous_mirror_remote"></span><span id="ASYNCHRONOUS_MIRROR_REMOTE"></span>

**Asynchronous Mirror Remote** (5)


</dt> <dd></dd> <dt>

<span id="Synchronous_Snapshot_Local"></span><span id="synchronous_snapshot_local"></span><span id="SYNCHRONOUS_SNAPSHOT_LOCAL"></span>

**Synchronous Snapshot Local** (6)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Snapshot_Local"></span><span id="asynchronous_snapshot_local"></span><span id="ASYNCHRONOUS_SNAPSHOT_LOCAL"></span>

**Asynchronous Snapshot Local** (7)


</dt> <dd></dd> <dt>

<span id="Synchronous_Snapshot_Remote"></span><span id="synchronous_snapshot_remote"></span><span id="SYNCHRONOUS_SNAPSHOT_REMOTE"></span>

**Synchronous Snapshot Remote** (8)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Snapshot_Remote"></span><span id="asynchronous_snapshot_remote"></span><span id="ASYNCHRONOUS_SNAPSHOT_REMOTE"></span>

**Asynchronous Snapshot Remote** (9)


</dt> <dd></dd> <dt>

<span id="Synchronous_Clone_Local"></span><span id="synchronous_clone_local"></span><span id="SYNCHRONOUS_CLONE_LOCAL"></span>

**Synchronous Clone Local** (10)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Clone_Local"></span><span id="asynchronous_clone_local"></span><span id="ASYNCHRONOUS_CLONE_LOCAL"></span>

**Asynchronous Clone Local** (11)


</dt> <dd></dd> <dt>

<span id="Synchronous_Clone_Remote"></span><span id="synchronous_clone_remote"></span><span id="SYNCHRONOUS_CLONE_REMOTE"></span>

**Synchronous Clone Remote** (12)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Clone_Remote"></span><span id="asynchronous_clone_remote"></span><span id="ASYNCHRONOUS_CLONE_REMOTE"></span>

**Asynchronous Clone Remote** (13)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>14 0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> <dt>

*Component* \[in\]
</dt> <dd>

Specifies the component to query.

The possible values are.

<dt>

<span id="Number_of_groups"></span><span id="number_of_groups"></span><span id="NUMBER_OF_GROUPS"></span>

**Number of groups** (2)


</dt> <dd></dd> <dt>

<span id="Number_of_elements_per_source_group"></span><span id="number_of_elements_per_source_group"></span><span id="NUMBER_OF_ELEMENTS_PER_SOURCE_GROUP"></span>

**Number of elements per source group** (3)


</dt> <dd></dd> <dt>

<span id="Number_of_elements_per_target_group"></span><span id="number_of_elements_per_target_group"></span><span id="NUMBER_OF_ELEMENTS_PER_TARGET_GROUP"></span>

**Number of elements per target group** (4)


</dt> <dd></dd> <dt>

<span id="Number_of_target_elements_per_source_element"></span><span id="number_of_target_elements_per_source_element"></span><span id="NUMBER_OF_TARGET_ELEMENTS_PER_SOURCE_ELEMENT"></span>

**Number of target elements per source element** (5)


</dt> <dd></dd> <dt>

<span id="Number_of_total_source_elements"></span><span id="number_of_total_source_elements"></span><span id="NUMBER_OF_TOTAL_SOURCE_ELEMENTS"></span>

**Number of total source elements** (6)


</dt> <dd></dd> <dt>

<span id="Number_of_total_target_elements"></span><span id="number_of_total_target_elements"></span><span id="NUMBER_OF_TOTAL_TARGET_ELEMENTS"></span>

**Number of total target elements** (7)


</dt> <dd></dd> <dt>

<span id="Number_of_peer_systems"></span><span id="number_of_peer_systems"></span><span id="NUMBER_OF_PEER_SYSTEMS"></span>

**Number of peer systems** (8)


</dt> <dd></dd> <dt>

<span id="Number_of_hops_in_multihop_copy"></span><span id="number_of_hops_in_multihop_copy"></span><span id="NUMBER_OF_HOPS_IN_MULTIHOP_COPY"></span>

**Number of hops in multihop copy** (9)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>10 0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> <dt>

*MaxValue* \[out\]
</dt> <dd>

On return, indicates the maximum value. A value of zero indicates unlimited components of the given type. In all cases, the maximum value is also bound by the availability of resources on the computer system.

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Success** (0)
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

**In Use** (6)
</dt> <dt>

**Information is not available** (7)
</dt> <dt>

**DMTF Reserved** (8 0x7FFF)
</dt> <dt>

**Vendor Specific** (0x8000 = *value* )
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_ReplicationServiceCapabilities**](msiscsitarget-replicationservicecapabilities.md)
</dt> <dt>

[**MSISCSITARGET\_ReplicationService**](msiscsitarget-replicationservice.md)
</dt> </dl>

 

 





