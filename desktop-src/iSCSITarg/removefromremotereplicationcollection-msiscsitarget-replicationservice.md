---
title: RemoveFromRemoteReplicationCollection method of the MSISCSITARGET\_ReplicationService class
description: Removes or starts a job to remove service access points (SAPs) and/or remote systems associations from an existing remote replication collection instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5d6464c6-9d19-4bea-9b8f-a760313a8e3b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoveFromRemoteReplicationCollection method iSCSI Software Target API", "RemoveFromRemoteReplicationCollection method iSCSI Software Target API , MSISCSITARGET_ReplicationService class", "MSISCSITARGET_ReplicationService class iSCSI Software Target API , RemoveFromRemoteReplicationCollection method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationService.RemoveFromRemoteReplicationCollection
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# RemoveFromRemoteReplicationCollection method of the MSISCSITARGET\_ReplicationService class

Removes or starts a job to remove service access points (SAPs) and/or remote systems associations from an existing remote replication collection instance.

This method is inherited from the **CIM\_ReplicationService** class.

## Syntax


```mof
uint32 RemoveFromRemoteReplicationCollection(
  [in, optional] CIM_ServiceAccessPoint Ref     LocalAccessPoints[],
  [in, optional] CIM_ServiceAccessPoint Ref     RemoteAccessPoints[],
  [in, optional] CIM_ComputerSystem Ref         RemoteComputerSystem,
  [out]          CIM_ConcreteJob Ref            Job,
  [in]           CIM_ConnectivityCollection Ref ConnectivityCollection
);
```



## Parameters

<dl> <dt>

*LocalAccessPoints* \[in, optional\]
</dt> <dd>

Specifies local SAPs that provide communication to the remote system.

</dd> <dt>

*RemoteAccessPoints* \[in, optional\]
</dt> <dd>

Specifies remote SAPs that provide communication to the remote system.

</dd> <dt>

*RemoteComputerSystem* \[in, optional\]
</dt> <dd>

Specifies the remote system to remove.

If the *LocalAccessPoints* and *RemoteAccessPoints* parameters are **NULL**, then only the remote [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219) instance is removed for the existing service access points that are associated to the specified collection. If the *RemoteComputerSystem* is **NULL**, then only the specified access points are removed from the existing remote computer systems that are available to the specified collection.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

On return, contains a reference to the job, which can be **NULL**, if the job is completed.

</dd> <dt>

*ConnectivityCollection* \[in\]
</dt> <dd>

Specifies the remote replication collection to modify.

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

**Method Reserved** (4097–32767)
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

[**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219)
</dt> <dt>

[**MSISCSITARGET\_ConcreteJob**](msiscsitarget-concretejob.md)
</dt> </dl>

 

 





