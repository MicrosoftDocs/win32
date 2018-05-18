---
title: AddToRemoteReplicationCollection method of the MSISCSITARGET\_ReplicationService class
description: Adds or starts a job to add additional service access points, and optionally, remote systems associations to an existing instance of a remote replication collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '03ff4707-5f8d-40d8-887c-47e65c82e2cb'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddToRemoteReplicationCollection method iSCSI Software Target API", "AddToRemoteReplicationCollection method iSCSI Software Target API , MSISCSITARGET_ReplicationService class", "MSISCSITARGET_ReplicationService class iSCSI Software Target API , AddToRemoteReplicationCollection method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationService.AddToRemoteReplicationCollection
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# AddToRemoteReplicationCollection method of the MSISCSITARGET\_ReplicationService class

Adds or starts a job to add additional service access points, and optionally, remote systems associations to an existing instance of a remote replication collection.

This method is inherited from the **CIM\_ReplicationService** class.

## Syntax


```mof
uint32 AddToRemoteReplicationCollection(
  [in]  CIM_ServiceAccessPoint Ref     LocalAccessPoints[],
  [in]  CIM_ServiceAccessPoint Ref     RemoteAccessPoints[],
  [in]  CIM_ComputerSystem Ref         RemoteComputerSystem,
  [out] CIM_ConcreteJob Ref            Job,
  [in]  CIM_ConnectivityCollection Ref ConnectivityCollection
);
```



## Parameters

<dl> <dt>

*LocalAccessPoints* \[in\]
</dt> <dd>

Specifies the local service access points that enable communication to the remote system.

</dd> <dt>

*RemoteAccessPoints* \[in\]
</dt> <dd>

Specifies the remote service access points that enable communication to the remote system.

If **NULL**, then only the system that is specified in the *RemoteComputerSystem* parameter is added for the existing access points that are associated to the remote replication collection.

</dd> <dt>

*RemoteComputerSystem* \[in\]
</dt> <dd>

Specifies the remote system.

If this parameter is **NULL**, then only access points are added for the remote systems that are already available to the **CIM\_RemoteReplicationCollection** instance.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

On return, contains a reference to the job, which can be **NULL** if the job is completed.

</dd> <dt>

*ConnectivityCollection* \[in\]
</dt> <dd>

Specifies the remote replication collection to be expanded. Required.

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
</dt> </dl>

 

 





