---
title: DeleteGroup method of the MSISCSITARGET\_ReplicationService class
description: Deletes a replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 91c64a32-a43d-4ac6-b88a-25630d641dce
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DeleteGroup method iSCSI Software Target API
- DeleteGroup method iSCSI Software Target API , MSISCSITARGET_ReplicationService class
- MSISCSITARGET_ReplicationService class iSCSI Software Target API , DeleteGroup method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationService.DeleteGroup
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DeleteGroup method of the MSISCSITARGET\_ReplicationService class

Deletes a replication group.

This method is inherited from the **CIM\_ReplicationService** class.

## Syntax


```mof
uint32 DeleteGroup(
  [in]           CIM_ReplicationGroup Ref   ReplicationGroup,
  [in, optional] CIM_ServiceAccessPoint Ref ServiceAccessPoint,
  [in, optional] boolean                    RemoveElements,
  [in, optional] string                     ReplicationSettingData
);
```



## Parameters

<dl> <dt>

*ReplicationGroup* \[in\]
</dt> <dd>

Specifies the replication group to delete. Required.

</dd> <dt>

*ServiceAccessPoint* \[in, optional\]
</dt> <dd>

Specifies access point information to allow the service to delete the group on a remote system.

</dd> <dt>

*RemoveElements* \[in, optional\]
</dt> <dd>

Specifies whether to remove elements of the group before deleting the group. If **True**, the group can be deleted even if it is not empty. If **false**, the group must be empty before it can be deleted.

> [!Note]  
> If one or more elements in the group are in a replication relationship, the *RemoveElements* parameter has no effect.

 

</dd> <dt>

*ReplicationSettingData* \[in, optional\]
</dt> <dd>

If provided, specifies the replication setting data for the given *SyncType* input parameter in the form of an embedded **CIM\_ReplicationSettingData** instance. If not provided, the management server uses the default replication setting data. Optional.

</dd> </dl>

## Return value

This method returns one of the following values.

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

**One or more elements in a replication relationship** (7)
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

 

 





