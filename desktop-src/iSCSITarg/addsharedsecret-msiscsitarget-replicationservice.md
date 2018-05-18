---
title: AddSharedSecret method of the MSISCSITARGET\_ReplicationService class
description: Introduces a new instance of the CIM\_SharedSecret class in the specified namespace and optionally associates it to an instance of a CIM\_ServiceAccessPoint.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '13a8e85e-5099-4376-93c7-8715555b86c3'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddSharedSecret method iSCSI Software Target API", "AddSharedSecret method iSCSI Software Target API , MSISCSITARGET_ReplicationService class", "MSISCSITARGET_ReplicationService class iSCSI Software Target API , AddSharedSecret method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationService.AddSharedSecret
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# AddSharedSecret method of the MSISCSITARGET\_ReplicationService class

Introduces a new instance of the **CIM\_SharedSecret** class in the specified namespace and optionally associates it to an instance of a [**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447).

This method is inherited from the **CIM\_ReplicationService** class.

## Syntax


```mof
uint32 AddSharedSecret(
  [in]           string                     SharedSecret,
  [in, optional] CIM_ServiceAccessPoint Ref ServiceAccessPoint,
  [in, optional] string                     InstanceNamespace,
  [out]          CIM_SharedSecret Ref       SharedSecretPath
);
```



## Parameters

<dl> <dt>

*SharedSecret* \[in\]
</dt> <dd>

Specifies an embedded **CIM\_SharedSecret** instance that specifies properties for the created instance. Required.

</dd> <dt>

*ServiceAccessPoint* \[in, optional\]
</dt> <dd>

Specifies a [**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447) instance to associate with the created shared secret. If **NULL**, no association is established.

</dd> <dt>

*InstanceNamespace* \[in, optional\]
</dt> <dd>

Specifies the namespace of the created instance. If **NULL**, the created instance is in the same namespace as the service.

</dd> <dt>

*SharedSecretPath* \[out\]
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

**DMTF Reserved** (7–)x7FFF)
</dt> <dt>

**Vendor Specific** (0x8000 = *value* )
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_ReplicationService**](msiscsitarget-replicationservice.md)
</dt> <dt>

[**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447)
</dt> </dl>

 

 





