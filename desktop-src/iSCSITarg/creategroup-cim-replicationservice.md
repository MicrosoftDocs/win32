---
title: CreateGroup method of the CIM\_ReplicationService class
description: Create a new replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7338f63d-22dd-46cb-b313-49081ca20b2a
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateGroup method iSCSI Software Target API
- CreateGroup method iSCSI Software Target API , CIM_ReplicationService class
- CIM_ReplicationService class iSCSI Software Target API , CreateGroup method
topic_type:
- apiref
api_name:
- CIM_ReplicationService.CreateGroup
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateGroup method of the CIM\_ReplicationService class

Create a new replication group.

## Syntax


```mof
uint32 CreateGroup(
  [in]  string                     GroupName,
  [in]  CIM_LogicalElement     REF Members[],
  [in]  boolean                    Persistent,
  [in]  boolean                    DeleteOnEmptyElement,
  [in]  boolean                    DeleteOnUnassociated,
  [in]  CIM_ServiceAccessPoint REF ServiceAccessPoint,
  [out] CIM_ReplicationGroup   REF ReplicationGroup,
  [in]  string                     ReplicationSettingData
);
```



## Parameters

<dl> <dt>

*GroupName* \[in\]
</dt> <dd>

If nameable, an end user relevant name for the group being created. If NULL or not nameable, then system assigns a name.

</dd> <dt>

*Members* \[in\]
</dt> <dd>

List of elements to add to the group -- order is maintained. If NULL, the group will be empty -- if empty groups are supported.

</dd> <dt>

*Persistent* \[in\]
</dt> <dd>

If false, the group, not the elements associated with the group, may be deleted at the completion of a copy operation. Use the intrinsic method ModifyInstance to change Persistencyof a group.

</dd> <dt>

*DeleteOnEmptyElement* \[in\]
</dt> <dd>

If true and empty groups are allowed, the group will be deleted when the last element is removed from the group. If empty groups are not allowed, the group will be deleted automatically when the group becomes empty. If this parameter is not NULL, its value will be used to set the group's DeleteOnEmptyElement property. Use the intrinsic method ModifyInstance to change this property after the group is created.

</dd> <dt>

*DeleteOnUnassociated* \[in\]
</dt> <dd>

If true, the group will be deleted when the group is no longer associated with another group. This can happen if all synchronization associations to the individual elements of the group are dissolved. If this parameter is not NULL, its value will be used to set the group's DeleteOnUnassociated property. Use the intrinsic method ModifyInstance to change this property after the group is created.

</dd> <dt>

*ServiceAccessPoint* \[in\]
</dt> <dd>

Reference to access point information to allow the service to create a group on a remote system. If NULL, the group is created on the local system.

</dd> <dt>

*ReplicationGroup* \[out\]
</dt> <dd>

Reference to the created group.

</dd> <dt>

*ReplicationSettingData* \[in\]
</dt> <dd>

If supplied, it provides additional replication settings for the method. For example, to supply the "Description" for the created group.

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

**Groups are not nameable** (7)
</dt> <dt>

**DMTF Reserved** (8 32767)
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

 

 





