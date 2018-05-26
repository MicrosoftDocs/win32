---
title: RemoveFromRemoteReplicationCollection method of the CIM\_ReplicationService class
description: Remove (or start a job to remove) service access points (i.e.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2edc2d46-d47e-4254-9a64-fb816b48cbdf
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveFromRemoteReplicationCollection method iSCSI Software Target API
- RemoveFromRemoteReplicationCollection method iSCSI Software Target API , CIM_ReplicationService class
- CIM_ReplicationService class iSCSI Software Target API , RemoveFromRemoteReplicationCollection method
topic_type:
- apiref
api_name:
- CIM_ReplicationService.RemoveFromRemoteReplicationCollection
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoveFromRemoteReplicationCollection method of the CIM\_ReplicationService class

Remove (or start a job to remove) service access points (i.e. ProtocolEndpoints) and/or remote systems associations from an existing instance of RemoteReplicationCollection.If 0 is returned, the function completed successfully and no ConcreteJob instance created. If 4096/0x1000 is returned, a ConcreteJob is started, a reference to which is returned in the Job output parameter. If parameter AccessPoints is NULL, then only the remote ComputerSystem is removed for the existing AccessPoints associated to the RemoteReplicationCollection. If ComputerSystem is NULL, then only AccessPoints are removed from the existing remote ComputerSystems known to the RemoteReplicationCollection.

## Syntax


```mof
uint32 RemoveFromRemoteReplicationCollection(
  [in]  CIM_ServiceAccessPoint     REF LocalAccessPoints[],
  [in]  CIM_ServiceAccessPoint     REF RemoteAccessPoints[],
  [in]  CIM_ComputerSystem         REF RemoteComputerSystem,
  [out] CIM_ConcreteJob            REF Job,
  [in]  CIM_ConnectivityCollection REF ConnectivityCollection
);
```



## Parameters

<dl> <dt>

*LocalAccessPoints* \[in\]
</dt> <dd>

An array of references to local ServiceAccessPoints (for example, ProtocolEndpoints) that allow communication to the remote system.

</dd> <dt>

*RemoteAccessPoints* \[in\]
</dt> <dd>

An array of references to remote ServiceAccessPoints (for example, ProtocolEndpoints) that allow communication to the remote system.

</dd> <dt>

*RemoteComputerSystem* \[in\]
</dt> <dd>

A reference to the remote system to remove.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the job (may be NULL if job is completed).

</dd> <dt>

*ConnectivityCollection* \[in\]
</dt> <dd>

The reference to the RemoteReplicationCollection to affect.

</dd> </dl>

## Return value

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

 

 





