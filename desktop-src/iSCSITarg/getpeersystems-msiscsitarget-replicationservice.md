---
title: GetPeerSystems method of the MSISCSITARGET\_ReplicationService class
description: Gets all of the peer systems. A peer system is a system that is known and visible to the replication service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 53150b7f-31f6-4467-9e31-64b2f7981c3e
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetPeerSystems method iSCSI Software Target API
- GetPeerSystems method iSCSI Software Target API , MSISCSITARGET_ReplicationService class
- MSISCSITARGET_ReplicationService class iSCSI Software Target API , GetPeerSystems method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationService.GetPeerSystems
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetPeerSystems method of the MSISCSITARGET\_ReplicationService class

Gets all of the peer systems. A peer system is a system that is known and visible to the replication service.

This method is inherited from the **CIM\_ReplicationService** class.

## Syntax


```mof
uint32 GetPeerSystems(
  [in, optional] uint16                 Options,
  [out]          CIM_ConcreteJob Ref    Job,
  [out]          CIM_ComputerSystem Ref Systems[]
);
```



## Parameters

<dl> <dt>

*Options* \[in, optional\]
</dt> <dd>

Specifies which peer systems to return. If **NULL**, all known systems are returned, whether those systems are currently available or not.

The possible values are.

<dt>

<span id="Only_systems_currently_reachable"></span><span id="only_systems_currently_reachable"></span><span id="ONLY_SYSTEMS_CURRENTLY_REACHABLE"></span>

**Only systems currently reachable** (2)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>3 0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> <dt>

*Job* \[out\]
</dt> <dd>

On return, contains a reference to the job, which can be **NULL**, if the job is completed.

If a job is started and after the job is completed, you can examine the [**CIM\_AffectedJobElement**](https://msdn.microsoft.com/library/cc150663) associations for available targets.

</dd> <dt>

*Systems* \[out\]
</dt> <dd>

On return, contains a list of peer computer systems.

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

**DMTF Reserved** (7 4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097 0x7FFF)
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

[**MSISCSITARGET\_ReplicationService**](msiscsitarget-replicationservice.md)
</dt> <dt>

[**MSISCSITARGET\_AffectedJobElement**](msiscsitarget-affectedjobelement.md)
</dt> </dl>

 

 





