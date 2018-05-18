---
title: GetReplicationRelationships method of the MSISCSITARGET\_ReplicationService class
description: Gets all of the specified synchronization relationships that are available to the processing replication service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5cc87809-48b5-43bd-beb9-1dc73355f42c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetReplicationRelationships method iSCSI Software Target API", "GetReplicationRelationships method iSCSI Software Target API , MSISCSITARGET_ReplicationService class", "MSISCSITARGET_ReplicationService class iSCSI Software Target API , GetReplicationRelationships method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationService.GetReplicationRelationships
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# GetReplicationRelationships method of the MSISCSITARGET\_ReplicationService class

Gets all of the specified synchronization relationships that are available to the processing replication service.

This method is inherited from the **CIM\_ReplicationService** class.

## Syntax


```mof
uint32 GetReplicationRelationships(
  [in, optional] uint16               Type,
  [in, optional] uint16               SyncType,
  [in, optional] uint16               Mode,
  [in, optional] uint16               Locality,
  [in, optional] uint16               CopyState,
  [out]          CIM_ConcreteJob Ref  Job,
  [out]          CIM_Synchronized Ref Synchronizations[]
);
```



## Parameters

<dl> <dt>

*Type* \[in, optional\]
</dt> <dd>

Specifies the type of synchronization relationships to retrieve. If **NULL**, all relationship types are retrieved.

The possible values are.

<dt>

<span id="StorageSynchronized"></span><span id="storagesynchronized"></span><span id="STORAGESYNCHRONIZED"></span>

**StorageSynchronized** (2)


</dt> <dd></dd> <dt>

<span id="GroupSynchronized"></span><span id="groupsynchronized"></span><span id="GROUPSYNCHRONIZED"></span>

**GroupSynchronized** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4–0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> <dt>

*SyncType* \[in, optional\]
</dt> <dd>

Specifies the synchronization type to retrieve. If **NULL**, the method returns relationships with all synchronization types.

The possible values are.

<dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd> *value* = 5</dd> <dt>

<span id="Mirror"></span><span id="mirror"></span><span id="MIRROR"></span>

**Mirror** (6)


</dt> <dd></dd> <dt>

<span id="Snapshot"></span><span id="snapshot"></span><span id="SNAPSHOT"></span>

**Snapshot** (7)


</dt> <dd></dd> <dt>

<span id="Clone"></span><span id="clone"></span><span id="CLONE"></span>

**Clone** (8)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>9–0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> <dt>

*Mode* \[in, optional\]
</dt> <dd>

Specifies the mode of relationships to return. If **NULL**, the method returns relationships with either **mode**.

The possible values are.

<dt>

<span id="Synchronous"></span><span id="synchronous"></span><span id="SYNCHRONOUS"></span>

**Synchronous** (2)


</dt> <dd></dd> <dt>

<span id="Asynchronous"></span><span id="asynchronous"></span><span id="ASYNCHRONOUS"></span>

**Asynchronous** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4–0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> <dt>

*Locality* \[in, optional\]
</dt> <dd>

Specifies the locality of elements to return. If **NULL**, replication relationships are retrieved regardless of the locality of elements.

<dt>

<span id="Local_only"></span><span id="local_only"></span><span id="LOCAL_ONLY"></span>

<span id="Local_only"></span><span id="local_only"></span><span id="LOCAL_ONLY"></span>**Local only** (2)


</dt> <dd>

Source and target elements are in the same system.

</dd> <dt>

<span id="Remote_only"></span><span id="remote_only"></span><span id="REMOTE_ONLY"></span>

<span id="Remote_only"></span><span id="remote_only"></span><span id="REMOTE_ONLY"></span>**Remote only** (3)


</dt> <dd>

Source and target elements are contained in two different systems.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

Reserved.

</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific**


</dt> <dd>

Reserved.

</dd> </dl> </dd> <dt>

*CopyState* \[in, optional\]
</dt> <dd>

Specifies the **CIM\_Synchronized.CopyState** property value to retrieve. If **NULL**, relationships are retrieved regardless of their **CopyState** property.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

On return, contains a reference to the job, which can be **NULL**, if the job is completed.

If a job is started and after the job is completed, you can examine the [**CIM\_AffectedJobElement**](https://msdn.microsoft.com/library/cc150663) associations for targets.

</dd> <dt>

*Synchronizations* \[out\]
</dt> <dd>

On return, contains an array of elements that are found.

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

**In Use** (6)
</dt> <dt>

**DMTF Reserved** (7–4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097–0x7FFF)
</dt> <dt>

**Vendor Specific** (0x8000 = *value* )
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

[**MSISCSITARGET\_ReplicationService**](msiscsitarget-replicationservice.md)
</dt> <dt>

[**GetReplicationRelationshipInstances**](getreplicationrelationshipinstances-msiscsitarget-replicationservice.md)
</dt> <dt>

[**MSISCSITARGET\_AffectedJobElement**](msiscsitarget-affectedjobelement.md)
</dt> </dl>

 

 





