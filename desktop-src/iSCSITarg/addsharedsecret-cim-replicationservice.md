---
title: AddSharedSecret method of the CIM\_ReplicationService class
description: Introduces a new instance of SharedSecret in the specified namespace and optionally associates it to an instance of a ServiceAccessPoint.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a4e04895-9148-441f-b57c-986ef22c1548'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddSharedSecret method iSCSI Software Target API", "AddSharedSecret method iSCSI Software Target API , CIM_ReplicationService class", "CIM_ReplicationService class iSCSI Software Target API , AddSharedSecret method"]
topic_type:
- apiref
api_name:
- CIM_ReplicationService.AddSharedSecret
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# AddSharedSecret method of the CIM\_ReplicationService class

Introduces a new instance of SharedSecret in the specified namespace and optionally associates it to an instance of a ServiceAccessPoint.

## Syntax


```mof
uint32 AddSharedSecret(
  [in]  string                     SharedSecret,
  [in]  CIM_ServiceAccessPoint REF ServiceAccessPoint,
  [in]  string                     InstanceNamespace,
  [out] CIM_SharedSecret       REF SharedSecretPath
);
```



## Parameters

<dl> <dt>

*SharedSecret* \[in\]
</dt> <dd>

Specifies an embedded **CIM\_SharedSecret** instance that specifies properties for the created instance. Required.

</dd> <dt>

*ServiceAccessPoint* \[in\]
</dt> <dd>

Associate created instance to this ServiceAccessPoint. If null, no such association is established.

</dd> <dt>

*InstanceNamespace* \[in\]
</dt> <dd>

Namespace of created instance. If null, created instance will be in the same namespace as the the service.

</dd> <dt>

*SharedSecretPath* \[out\]
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

 

 





