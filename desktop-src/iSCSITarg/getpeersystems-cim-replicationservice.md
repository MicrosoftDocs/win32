---
title: GetPeerSystems method of the CIM\_ReplicationService class
description: Get (or start a job to get) all of the peer systems.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd59952fd-08bc-4437-8e7d-0eb4f899d66f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetPeerSystems method iSCSI Software Target API", "GetPeerSystems method iSCSI Software Target API , CIM_ReplicationService class", "CIM_ReplicationService class iSCSI Software Target API , GetPeerSystems method"]
topic_type:
- apiref
api_name:
- CIM_ReplicationService.GetPeerSystems
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# GetPeerSystems method of the CIM\_ReplicationService class

Get (or start a job to get) all of the peer systems. A peer system is a system that is known and visible to the Replication Service. Peer systems are discovered through discovery services and/or implementation specific services.If a job is started, once the job completes, examine the AffectedJobElement associations for the peer systems.

## Syntax


```mof
uint32 GetPeerSystems(
  [in]  uint16                 Options,
  [out] CIM_ConcreteJob    REF Job,
  [out] CIM_ComputerSystem REF Systems[]
);
```



## Parameters

<dl> <dt>

*Options* \[in\]
</dt> <dd>

This parameter specifies which peer systems to return. If NULL, all known systems are returned, whether those systems are currently reachable or not.

<dt>

<span id="Only_systems_currently_reachable"></span><span id="only_systems_currently_reachable"></span><span id="ONLY_SYSTEMS_CURRENTLY_REACHABLE"></span>

**Only systems currently reachable** (2)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>3–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl> </dd> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the job (may be NULL if the task completed).

</dd> <dt>

*Systems* \[out\]
</dt> <dd>

List of peer ComputerSystems.

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

**DMTF Reserved** (7–4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097–32767)
</dt> <dt>

**Vendor Specific** (32768–4294967295)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

**CIM\_ReplicationService**
</dt> </dl>

 

 





