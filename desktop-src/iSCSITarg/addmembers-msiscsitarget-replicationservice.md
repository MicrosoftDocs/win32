---
title: AddMembers method of the MSISCSITARGET\_ReplicationService class
description: Adds members to an existing replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 22690ac3-7d2a-48a6-9e3f-d665d79f87c1
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddMembers method iSCSI Software Target API
- AddMembers method iSCSI Software Target API , MSISCSITARGET_ReplicationService class
- MSISCSITARGET_ReplicationService class iSCSI Software Target API , AddMembers method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationService.AddMembers
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddMembers method of the MSISCSITARGET\_ReplicationService class

Adds members to an existing replication group.

This method is inherited from the **CIM\_ReplicationService** class.

## Syntax


```mof
uint32 AddMembers(
  [in]           CIM_LogicalElement Ref     Members[],
  [in]           CIM_ReplicationGroup Ref   ReplicationGroup,
  [in, optional] CIM_ServiceAccessPoint Ref ServiceAccessPoint,
  [in, optional] string                     ReplicationSettingData
);
```



## Parameters

<dl> <dt>

*Members* \[in\]
</dt> <dd>

Specifies the elements to add to the group. New members are added to the end of the existing members of the group in the order that they are supplied. It is not an error, if a newly added member is already in the group.

</dd> <dt>

*ReplicationGroup* \[in\]
</dt> <dd>

Specifies the existing replication group to be modified. Required.

</dd> <dt>

*ServiceAccessPoint* \[in, optional\]
</dt> <dd>

Specifies access point information to allow the service to access the group on a remote system.

</dd> <dt>

*ReplicationSettingData* \[in, optional\]
</dt> <dd>

If provided, specifies the replication setting data for the given *SyncType* parameter in the form of an embedded **CIM\_ReplicationSettingData** instance. If not provided, the management server uses the default replication setting data. Optional.

</dd> </dl>

## Return value

This method returns one of the following values:

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

**Group does not exist** (7)
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

[**MSISCSITARGET\_ReplicationService**](msiscsitarget-replicationservice.md)
</dt> </dl>

 

 





