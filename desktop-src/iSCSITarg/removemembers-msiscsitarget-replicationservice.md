---
title: RemoveMembers method of the MSISCSITARGET\_ReplicationService class
description: Removes members from a replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e8f0a7eb-9551-4c7f-9e38-f914bfc008e5
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveMembers method iSCSI Software Target API
- RemoveMembers method iSCSI Software Target API , MSISCSITARGET_ReplicationService class
- MSISCSITARGET_ReplicationService class iSCSI Software Target API , RemoveMembers method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationService.RemoveMembers
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoveMembers method of the MSISCSITARGET\_ReplicationService class

Removes members from a replication group.

This method is inherited from the **CIM\_ReplicationService** class.

## Syntax


```mof
uint32 RemoveMembers(
  [in, optional] CIM_LogicalElement Ref     Members[],
  [in, optional] boolean                    DeleteOnEmptyElement,
  [in]           CIM_ReplicationGroup Ref   ReplicationGroup,
  [in, optional] CIM_ServiceAccessPoint Ref ServiceAccessPoint,
  [in, optional] string                     ReplicationSettingData
);
```



## Parameters

<dl> <dt>

*Members* \[in, optional\]
</dt> <dd>

Specifies a list of elements to remove from a group. A member cannot be removed if it is in a replication relationship. Deleting all members of a group is equivalent to deleting the group if empty groups are not supported by the implementation.

</dd> <dt>

*DeleteOnEmptyElement* \[in, optional\]
</dt> <dd>

Specifies whether to delete the group when the last element is removed. If **True**, the group is deleted after the last element is removed from the group. Otherwise, the empty group is retained.

> [!Note]  
> If empty groups are not allowed, the group is deleted automatically when the group becomes empty even if the value is **false**.

 

If this parameter is not **NULL**, its value overrides the **DeleteOnEmptyElement** property of the group.

</dd> <dt>

*ReplicationGroup* \[in\]
</dt> <dd>

Specifies an existing replication group to modify. Required.

</dd> <dt>

*ServiceAccessPoint* \[in, optional\]
</dt> <dd>

Specifies a reference to access point information for the service to create a group on a remote system. If **NULL**, the group is created on the local system.

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

**Group does not exist** (7)
</dt> <dt>

**Member not in group** (8)
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

 

 





