---
title: DeleteGroup method of the CIM\_ReplicationService class
description: Delete a replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b6f67233-c8ab-4118-ad2c-87bd720afef6
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DeleteGroup method iSCSI Software Target API
- DeleteGroup method iSCSI Software Target API , CIM_ReplicationService class
- CIM_ReplicationService class iSCSI Software Target API , DeleteGroup method
topic_type:
- apiref
api_name:
- CIM_ReplicationService.DeleteGroup
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DeleteGroup method of the CIM\_ReplicationService class

Delete a replication group.

## Syntax


```mof
uint32 DeleteGroup(
  [in] CIM_ReplicationGroup   REF ReplicationGroup,
  [in] CIM_ServiceAccessPoint REF ServiceAccessPoint,
  [in] boolean                    RemoveElements,
  [in] string                     ReplicationSettingData
);
```



## Parameters

<dl> <dt>

*ReplicationGroup* \[in\]
</dt> <dd>

Reference to a replication group.

</dd> <dt>

*ServiceAccessPoint* \[in\]
</dt> <dd>

Reference to access point information to allow the service to delete the group on a remote system.

</dd> <dt>

*RemoveElements* \[in\]
</dt> <dd>

Delete the group even if it is not empty. If one or more elements in the group are in a replication relationship, RemoveElements has no effect.

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

**One or more elements in a replication relationship** (7)
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

 

 





