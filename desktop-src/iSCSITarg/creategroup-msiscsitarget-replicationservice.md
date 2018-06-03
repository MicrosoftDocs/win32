---
title: CreateGroup method of the MSISCSITARGET\_ReplicationService class
description: Creates a new replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9cac9fa2-6d66-4cd7-949b-d2a02cb0cb53
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateGroup method iSCSI Software Target API
- CreateGroup method iSCSI Software Target API , MSISCSITARGET_ReplicationService class
- MSISCSITARGET_ReplicationService class iSCSI Software Target API , CreateGroup method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationService.CreateGroup
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateGroup method of the MSISCSITARGET\_ReplicationService class

Creates a new replication group.

This method is inherited from the **CIM\_ReplicationService** class.

## Syntax


```mof
uint32 CreateGroup(
  [in, optional] string                     GroupName,
  [in, optional] CIM_LogicalElement Ref     Members[],
  [in, optional] boolean                    Persistent,
  [in, optional] boolean                    DeleteOnEmptyElement,
  [in, optional] boolean                    DeleteOnUnassociated,
  [in, optional] CIM_ServiceAccessPoint Ref ServiceAccessPoint,
  [out]          CIM_ReplicationGroup Ref   ReplicationGroup,
  [in, optional] string                     ReplicationSettingData
);
```



## Parameters

<dl> <dt>

*GroupName* \[in, optional\]
</dt> <dd>

Specifies an end user name that is meaningful for the group that is to be created. If **NULL**, or the group is not nameable, then the system assigns a name.

</dd> <dt>

*Members* \[in, optional\]
</dt> <dd>

Specifies a list of elements to add to the group. The order of the specified elements is maintained. If **NULL**, the group is empty.

> [!Note]  
> Empty groups might not be allowed, in which case this parameter is required.

 

</dd> <dt>

*Persistent* \[in, optional\]
</dt> <dd>

Specifies whether the group persists after a copy operation. If **false**, the group, but not the elements that are associated with the group, can be deleted at the completion of a copy operation. Otherwise, the group persists.

</dd> <dt>

*DeleteOnEmptyElement* \[in, optional\]
</dt> <dd>

Specifies whether to delete the group when the last element is removed. If **True**, the group is deleted after the last element is removed from the group. Otherwise, the empty group is retained.

> [!Note]  
> If empty groups are not allowed, the group is deleted automatically after the group becomes empty even if this parameter is **false**.

 

If this parameter is not **NULL**, its value is used to set the **DeleteOnEmptyElement** property of the group.

</dd> <dt>

*DeleteOnUnassociated* \[in, optional\]
</dt> <dd>

Specifies whether to delete the group when the group is no longer associated with another group. If **True**, the group is deleted after the last association is dissolved.

This can happen if all synchronization associations to the individual elements of the group are dissolved.

If this parameter is not **NULL**, its value is used to set the **DeleteOnUnassociated** property of the group.

</dd> <dt>

*ServiceAccessPoint* \[in, optional\]
</dt> <dd>

Specifies a reference to access point information to enable the service to create a group on a remote system. If **NULL**, the group is created on the local system.

</dd> <dt>

*ReplicationGroup* \[out\]
</dt> <dd>

On return, contains a reference to the created group.

</dd> <dt>

*ReplicationSettingData* \[in, optional\]
</dt> <dd>

If provided, specifies the replication setting data in the form of an embedded **CIM\_ReplicationSettingData** instance. If not provided, the management server uses the default replication setting data.

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

**Groups are not nameable** (7)
</dt> <dt>

**Method Reserved** (8 0x7FFF)
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

[**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447)
</dt> </dl>

 

 





