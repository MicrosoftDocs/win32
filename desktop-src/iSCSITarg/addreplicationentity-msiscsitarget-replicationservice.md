---
title: AddReplicationEntity method of the MSISCSITARGET\_ReplicationService class
description: Adds a new instance of CIM\_ReplicationEntity in the specified namespace.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 33f970d1-bd57-4ce1-be72-46d6cf591d59
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddReplicationEntity method iSCSI Software Target API
- AddReplicationEntity method iSCSI Software Target API , MSISCSITARGET_ReplicationService class
- MSISCSITARGET_ReplicationService class iSCSI Software Target API , AddReplicationEntity method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationService.AddReplicationEntity
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddReplicationEntity method of the MSISCSITARGET\_ReplicationService class

Adds a new instance of **CIM\_ReplicationEntity** in the specified namespace.

This method is inherited from the **CIM\_ReplicationService** class.

## Syntax


```mof
uint32 AddReplicationEntity(
  [in]  string                    ReplicationEntity,
  [in]  boolean                   Persistent,
  [in]  string                    InstanceNamespace,
  [out] CIM_ReplicationEntity Ref ReplicationEntityPath
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

Specifies how long the instance persists. If **True**, the instance must persist across the management server reboot. If **NULL**, the value is based on the default value of the class in the Managed Object Format (MOF). Use the [CimSession](https://msdn.microsoft.com/library/microsoft.management.infrastructure.cimsession.aspx).[**ModifyInstance**](https://www.bing.com/search?q=**ModifyInstance**) method to change the value after the instance is created.

</dd> <dt>

*InstanceNamespace* \[in\]
</dt> <dd>

Specifies the namespace of the created instance. If **NULL**, the created instance will be in the same namespace as the replication service.

</dd> <dt>

*ReplicationEntityPath* \[out\]
</dt> <dd>

On return, contains a reference to the created instance.

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

**DMTF Reserved** (7 )x7FFF)
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

 

 





