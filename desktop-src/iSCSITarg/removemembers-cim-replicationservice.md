---
title: RemoveMembers method of the CIM\_ReplicationService class
description: Remove members from a replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: eaf39373-1db8-4d51-b7c8-2bee41e94483
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveMembers method iSCSI Software Target API
- RemoveMembers method iSCSI Software Target API , CIM_ReplicationService class
- CIM_ReplicationService class iSCSI Software Target API , RemoveMembers method
topic_type:
- apiref
api_name:
- CIM_ReplicationService.RemoveMembers
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoveMembers method of the CIM\_ReplicationService class

Remove members from a replication group.

## Syntax


```mof
uint32 RemoveMembers(
  [in] CIM_LogicalElement     REF Members[],
  [in] boolean                    DeleteOnEmptyElement,
  [in] CIM_ReplicationGroup   REF ReplicationGroup,
  [in] CIM_ServiceAccessPoint REF ServiceAccessPoint,
  [in] string                     ReplicationSettingData
);
```



## Parameters

<dl> <dt>

*Members* \[in\]
</dt> <dd>

List of elements to remove from a group. A member can not be removed if it is in a replication relationship. Deleting all members of a group is equivalent to deleting the group if empty groups are not supported by the implementation.

</dd> <dt>

*DeleteOnEmptyElement* \[in\]
</dt> <dd>

If true and removal of the members causes the group to become empty, the group will be deleted. Note, if empty groups are not allowed, the group will be deleted automatically when the group becomes empty. If this parameter is not NULL, it overrides the group's property DeleteOnEmptyElement.

</dd> <dt>

*ReplicationGroup* \[in\]
</dt> <dd>

Reference to an existing replication group.

</dd> <dt>

*ServiceAccessPoint* \[in\]
</dt> <dd>

Reference to access point information to allow the service to access the group on a remote system.

</dd> <dt>

*ReplicationSettingData* \[in\]
</dt> <dd>

If supplied, it provides additional replication settings for the method. For example, what should happen OnGroupOrListError.

</dd> </dl>

## Return value

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

**DMTF Reserved** (9 32767)
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

 

 





