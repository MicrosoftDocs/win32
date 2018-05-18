---
title: AddReplicationEntity method of the CIM\_ReplicationService class
description: Introduces a new instance of ReplicationEntity in the specified Namespace.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4e40f476-ea3f-47f6-9c3d-8bac2b9585ef'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddReplicationEntity method iSCSI Software Target API", "AddReplicationEntity method iSCSI Software Target API , CIM_ReplicationService class", "CIM_ReplicationService class iSCSI Software Target API , AddReplicationEntity method"]
topic_type:
- apiref
api_name:
- CIM_ReplicationService.AddReplicationEntity
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# AddReplicationEntity method of the CIM\_ReplicationService class

Introduces a new instance of ReplicationEntity in the specified Namespace.

## Syntax


```mof
uint32 AddReplicationEntity(
  [in]  string                    ReplicationEntity,
  [in]  boolean                   Persistent,
  [in]  string                    InstanceNamespace,
  [out] CIM_ReplicationEntity REF ReplicationEntityPath
);
```



## Parameters

<dl> <dt>

*ReplicationEntity* \[in\]
</dt> <dd>

Specifies an embedded **CIM\_ReplicationEntity** instance that specifies properties for the created instance.

</dd> <dt>

*Persistent* \[in\]
</dt> <dd>

If true, the instance must persist across Management Server reboot. If NULL, the value will be based on the default value of the class in the MOF. Use the intrinsic method ModifyInstance to change the Persistency value.

</dd> <dt>

*InstanceNamespace* \[in\]
</dt> <dd>

Namespace of created instance. If null, created instance will be in the same namespace as the service.

</dd> <dt>

*ReplicationEntityPath* \[out\]
</dt> <dd>

Reference to the created instance.

</dd> </dl>

## Return value

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**In Use** (6)
</dt> <dt>

**DMTF Reserved** (7–32767)
</dt> <dt>

**Vendor Specific** (32768–4294967295)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

**CIM\_ReplicationService**
</dt> </dl>

 

 





