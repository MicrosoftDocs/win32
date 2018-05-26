---
title: GetReplicationRelationshipInstances method of the CIM\_ReplicationService class
description: Get (or start a job to get) all of the synchronization relationships known to the processing replication service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 04e319c7-9b35-4ac6-a606-f3ad51ea2c98
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetReplicationRelationshipInstances method iSCSI Software Target API
- GetReplicationRelationshipInstances method iSCSI Software Target API , CIM_ReplicationService class
- CIM_ReplicationService class iSCSI Software Target API , GetReplicationRelationshipInstances method
topic_type:
- apiref
api_name:
- CIM_ReplicationService.GetReplicationRelationshipInstances
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetReplicationRelationshipInstances method of the CIM\_ReplicationService class

Get (or start a job to get) all of the synchronization relationships known to the processing replication service. If a job is started, once the job completes, examine the AffectedJobElement associations for the synchronization relationships. This method is similar to GetReplicationRelationships, except that this method returns the instances as opposed to object paths.

## Syntax


```mof
uint32 GetReplicationRelationshipInstances(
  [in]  uint16              Type,
  [in]  uint16              SyncType,
  [in]  uint16              Mode,
  [in]  uint16              Locality,
  [in]  uint16              CopyState,
  [out] CIM_ConcreteJob REF Job,
  [out] string              Synchronizations[]
);
```



## Parameters

<dl> <dt>

*Type* \[in\]
</dt> <dd>

The type of synchronization relationships, for example, StorageSynchronized or GroupSynchronized. If this parameter is not supplied, all such relationships are retrieved.

<dt>

<span id="StorageSynchronized"></span><span id="storagesynchronized"></span><span id="STORAGESYNCHRONIZED"></span>

**StorageSynchronized** (2)


</dt> <dd></dd> <dt>

<span id="GroupSynchronized"></span><span id="groupsynchronized"></span><span id="GROUPSYNCHRONIZED"></span>

**GroupSynchronized** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*SyncType* \[in\]
</dt> <dd>

Describes the desired synchronization type. If this parameter is not specified, all SyncType are retrieved.

<dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>0 5</dd> <dt>

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


</dt> <dd>9 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*Mode* \[in\]
</dt> <dd>

Describes the desired mode. If this parameter is not supplied, both synchronous and asynchronous modes are retrieved.

<dt>

<span id="Synchronous"></span><span id="synchronous"></span><span id="SYNCHRONOUS"></span>

**Synchronous** (2)


</dt> <dd></dd> <dt>

<span id="Asynchronous"></span><span id="asynchronous"></span><span id="ASYNCHRONOUS"></span>

**Asynchronous** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*Locality* \[in\]
</dt> <dd>

Describes the desired locality. If this parameter is not supplied, all replication relationships are retrieved, regardless of the locality of elements. Local only: Source and target elements are contained in the same system. Remote only: Source and target elements are contained in two different systems.

<dt>

<span id="Local_only"></span><span id="local_only"></span><span id="LOCAL_ONLY"></span>

**Local only** (2)


</dt> <dd></dd> <dt>

<span id="Remote_only"></span><span id="remote_only"></span><span id="REMOTE_ONLY"></span>

**Remote only** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*CopyState* \[in\]
</dt> <dd>

Only retrieve synchronization relationships that are currently in this CopyState. If this parameter is not supplied, relationships are retrieved regardless of their current CopyState.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the job (may be NULL if the task completed).

</dd> <dt>

*Synchronizations* \[out\]
</dt> <dd>

An array of instances found.

</dd> </dl>

## Return value

<dl> <dt>

**Completed with No Error** (0)
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

**In Use** (6)
</dt> <dt>

**DMTF Reserved** (7 4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097 32767)
</dt> <dt>

**Vendor Specific** (32768 4294967295)
</dt> </dl>

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

**CIM\_ReplicationService**
</dt> </dl>

 

 





