---
title: AddMembers method of the CIM\_ReplicationService class
description: Add members to an existing replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a5f3c3d3-f124-4700-b6f2-39ca3be93061
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddMembers method iSCSI Software Target API
- AddMembers method iSCSI Software Target API , CIM_ReplicationService class
- CIM_ReplicationService class iSCSI Software Target API , AddMembers method
topic_type:
- apiref
api_name:
- CIM_ReplicationService.AddMembers
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddMembers method of the CIM\_ReplicationService class

Add members to an existing replication group.

## Syntax


```mof
uint32 AddMembers(
  [in] CIM_LogicalElement     REF Members[],
  [in] CIM_ReplicationGroup   REF ReplicationGroup,
  [in] CIM_ServiceAccessPoint REF ServiceAccessPoint,
  [in] string                     ReplicationSettingData
);
```



## Parameters

<dl> <dt>

*Members* \[in\]
</dt> <dd>

Specifies a list of elements to add to the group. New members are added, in the order supplied, to the end of the existing members of the group. It is not an error, if a new member is already in the group.

</dd> <dt>

*ReplicationGroup* \[in\]
</dt> <dd>

Specifies an existing replication group.

</dd> <dt>

*ServiceAccessPoint* \[in\]
</dt> <dd>

Specifies access point information to allow the service to access the group on a remote system.

</dd> <dt>

*ReplicationSettingData* \[in\]
</dt> <dd>

Specifies additional replication settings for the method.

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

 

 





