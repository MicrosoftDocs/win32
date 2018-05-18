---
title: AddServiceAccessPoint method of the CIM\_ReplicationService class
description: Introduces a new instance of a ServiceAccessPoint, or one of its subclasses, for example, a RemoteServiceAccessPoint in the specified namespace.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd35cc029-772b-416a-a5a3-f4eef29dd640'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddServiceAccessPoint method iSCSI Software Target API", "AddServiceAccessPoint method iSCSI Software Target API , CIM_ReplicationService class", "CIM_ReplicationService class iSCSI Software Target API , AddServiceAccessPoint method"]
topic_type:
- apiref
api_name:
- CIM_ReplicationService.AddServiceAccessPoint
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# AddServiceAccessPoint method of the CIM\_ReplicationService class

Introduces a new instance of a ServiceAccessPoint, or one of its subclasses, for example, a RemoteServiceAccessPoint in the specified namespace.

## Syntax


```mof
uint32 AddServiceAccessPoint(
  [in]  string                     ServiceAccessPoint,
  [in]  string                     InstanceNamespace,
  [out] CIM_ServiceAccessPoint REF ServiceAccessPointPath
);
```



## Parameters

<dl> <dt>

*ServiceAccessPoint* \[in\]
</dt> <dd>

Specifies an embedded [**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447) instance that specifies the properties of the instance to create. Required.

</dd> <dt>

*InstanceNamespace* \[in\]
</dt> <dd>

Namespace of created instance. If null, created instance will be in the same namespace as the service.

</dd> <dt>

*ServiceAccessPointPath* \[out\]
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

 

 





