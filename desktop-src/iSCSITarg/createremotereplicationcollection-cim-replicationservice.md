---
title: CreateRemoteReplicationCollection method of the CIM\_ReplicationService class
description: Create (or start a job to create) a new instance of RemoteReplicationCollection, and optionally supply the remote system and the paths (i.e.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3df5a71b-b3c7-46d2-8a6e-fa253a3e518d
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateRemoteReplicationCollection method iSCSI Software Target API
- CreateRemoteReplicationCollection method iSCSI Software Target API , CIM_ReplicationService class
- CIM_ReplicationService class iSCSI Software Target API , CreateRemoteReplicationCollection method
topic_type:
- apiref
api_name:
- CIM_ReplicationService.CreateRemoteReplicationCollection
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateRemoteReplicationCollection method of the CIM\_ReplicationService class

Create (or start a job to create) a new instance of RemoteReplicationCollection, and optionally supply the remote system and the paths (i.e. ProtocolEndpoints) that are used to perform replication operations to/from the remote system. If 0 is returned, the function completed successfully and no ConcreteJob instance created. If 4096/0x1000 is returned, a ConcreteJob is started, a reference to which is returned in the Job output parameter. Once the job completes, examine the AffectedJobElement associations for the created instance of RemoteReplicationCollection.

## Syntax


```mof
uint32 CreateRemoteReplicationCollection(
  [in]  string                         ElementName,
  [in]  CIM_ServiceAccessPoint     REF LocalAccessPoints[],
  [in]  CIM_ServiceAccessPoint     REF RemoteAccessPoints[],
  [in]  CIM_ComputerSystem         REF RemoteComputerSystem,
  [in]  boolean                        Active,
  [in]  boolean                        DeleteOnUnassociated,
  [out] CIM_ConcreteJob            REF Job,
  [out] CIM_ConnectivityCollection REF ConnectivityCollection
);
```



## Parameters

<dl> <dt>

*ElementName* \[in\]
</dt> <dd>

A end user relevant name for the element being created. If NULL, then a system supplied default name can be used. The value will be stored in the 'ElementName' property for the created element.

</dd> <dt>

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

A reference to the remote system.

</dd> <dt>

*Active* \[in\]
</dt> <dd>

If true, the instance of RemoteReplicationCollection will be enabled and allows replication operations to to the remote system. Use the intrinsic method ModifyInstance to change this property after the RemoteReplicationCollection is created.

</dd> <dt>

*DeleteOnUnassociated* \[in\]
</dt> <dd>

If true, the instance of RemoteReplicationCollection will be deleted when it is no longer associated to a ServiceAccessPoint. Use the intrinsic method ModifyInstance to change this property after the RemoteReplicationCollection is created.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the job (may be NULL if job is completed).

</dd> <dt>

*ConnectivityCollection* \[out\]
</dt> <dd>

Reference to the created instance ofRemoteReplicationCollection.

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

 

 





