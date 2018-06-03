---
title: CreateRemoteReplicationCollection method of the MSISCSITARGET\_ReplicationService class
description: Creates a new instance of a remote replication collection, and optionally, supplies the remote system and the protocol endpoints that are used to perform replication operations to and from the remote system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7c3d7571-1550-4688-8e3e-c784a3ac1b06
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateRemoteReplicationCollection method iSCSI Software Target API
- CreateRemoteReplicationCollection method iSCSI Software Target API , MSISCSITARGET_ReplicationService class
- MSISCSITARGET_ReplicationService class iSCSI Software Target API , CreateRemoteReplicationCollection method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationService.CreateRemoteReplicationCollection
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateRemoteReplicationCollection method of the MSISCSITARGET\_ReplicationService class

Creates a new instance of a remote replication collection, and optionally, supplies the remote system and the protocol endpoints that are used to perform replication operations to and from the remote system.

This method is inherited from the **CIM\_ReplicationService** class.

## Syntax


```mof
uint32 CreateRemoteReplicationCollection(
  [in, optional] string                         ElementName,
  [in, optional] CIM_ServiceAccessPoint Ref     LocalAccessPoints[],
  [in, optional] CIM_ServiceAccessPoint Ref     RemoteAccessPoints[],
  [in, optional] CIM_ComputerSystem Ref         RemoteComputerSystem,
  [in, optional] boolean                        Active,
  [in, optional] boolean                        DeleteOnUnassociated,
  [out]          CIM_ConcreteJob Ref            Job,
  [out]          CIM_ConnectivityCollection Ref ConnectivityCollection
);
```



## Parameters

<dl> <dt>

*ElementName* \[in, optional\]
</dt> <dd>

Specifies an end user relevant name for the element to be created. If **NULL**, then a system-supplied default name can be used. The value is stored in the **ElementName** property of the created element.

</dd> <dt>

*LocalAccessPoints* \[in, optional\]
</dt> <dd>

Specifies the local Service Access Points (SAPs), for example protocol endpoints, that allow communication to the remote system.

</dd> <dt>

*RemoteAccessPoints* \[in, optional\]
</dt> <dd>

Specifies the remote Service Access Points (SAPs), for example protocol endpoints, that allow communication to the remote system.

</dd> <dt>

*RemoteComputerSystem* \[in, optional\]
</dt> <dd>

Specifies the remote computer system.

</dd> <dt>

*Active* \[in, optional\]
</dt> <dd>

Specifies whether to enable the created remote replication collection. If **True**, the instance is enabled and provides replication operations to the remote system.

Use the intrinsic [CimSession](https://msdn.microsoft.com/library/microsoft.management.infrastructure.cimsession.aspx).[**ModifyInstance**](https://www.bing.com/search?q=**ModifyInstance**) method to change this property after the collection is created.

</dd> <dt>

*DeleteOnUnassociated* \[in, optional\]
</dt> <dd>

Specifies whether to delete the remote replication collection when the collection is no longer associated with an Service Access Point (SAP). If **True**, the collection is deleted after the last association is dissolved.

Use the intrinsic [CimSession](https://msdn.microsoft.com/library/microsoft.management.infrastructure.cimsession.aspx).[**ModifyInstance**](https://www.bing.com/search?q=**ModifyInstance**) method to change this property after the collection is created.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

On return, contains a reference to the job, which can be **NULL**, if the job is completed.

</dd> <dt>

*ConnectivityCollection* \[out\]
</dt> <dd>

On return, contains a reference to the created remote replication collection.

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

**Method Reserved** (4097 32767)
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

[**MSISCSITARGET\_iSCSIProtocolEndpoint**](msiscsitarget-iscsiprotocolendpoint.md)
</dt> <dt>

[**MSISCSITARGET\_TCPProtocolEndpoint**](msiscsitarget-tcpprotocolendpoint.md)
</dt> </dl>

 

 





