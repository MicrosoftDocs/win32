---
title: AddServiceAccessPoint method of the MSISCSITARGET\_ReplicationService class
description: Introduces a new instance of a CIM\_ServiceAccessPoint class or one of its subclasses.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3bb8527b-d8e8-4ed9-bb9d-74a1135cd57f
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddServiceAccessPoint method iSCSI Software Target API
- AddServiceAccessPoint method iSCSI Software Target API , MSISCSITARGET_ReplicationService class
- MSISCSITARGET_ReplicationService class iSCSI Software Target API , AddServiceAccessPoint method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationService.AddServiceAccessPoint
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddServiceAccessPoint method of the MSISCSITARGET\_ReplicationService class

Introduces a new instance of a [**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447) class or one of its subclasses.

This method is inherited from the **CIM\_ReplicationService** class.

## Syntax


```mof
uint32 AddServiceAccessPoint(
  [in]           string                     ServiceAccessPoint,
  [in, optional] string                     InstanceNamespace,
  [out]          CIM_ServiceAccessPoint Ref ServiceAccessPointPath
);
```



## Parameters

<dl> <dt>

*ServiceAccessPoint* \[in\]
</dt> <dd>

Specifies an embedded [**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447) instance that specifies the properties of the instance to create. Required.

</dd> <dt>

*InstanceNamespace* \[in, optional\]
</dt> <dd>

Specifies the namespace of the created instance. If **NULL**, the created instance is in the same namespace as the service.

</dd> <dt>

*ServiceAccessPointPath* \[out\]
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
</dt> <dt>

[**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447)
</dt> </dl>

 

 





