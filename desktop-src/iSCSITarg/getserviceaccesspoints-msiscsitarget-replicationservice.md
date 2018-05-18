---
title: GetServiceAccessPoints method of the MSISCSITARGET\_ReplicationService class
description: Gets service access points (SAPs) that are associated with a peer system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '716dbd18-d9c0-4450-b8b8-b8edfd474146'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetServiceAccessPoints method iSCSI Software Target API", "GetServiceAccessPoints method iSCSI Software Target API , MSISCSITARGET_ReplicationService class", "MSISCSITARGET_ReplicationService class iSCSI Software Target API , GetServiceAccessPoints method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationService.GetServiceAccessPoints
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# GetServiceAccessPoints method of the MSISCSITARGET\_ReplicationService class

Gets service access points (SAPs) that are associated with a peer system.

This method is inherited from the **CIM\_ReplicationService** class.

## Syntax


```mof
uint32 GetServiceAccessPoints(
  [in]  CIM_ComputerSystem Ref     System,
  [out] CIM_ConcreteJob Ref        Job,
  [out] CIM_ServiceAccessPoint Ref ServiceAccessPoints[]
);
```



## Parameters

<dl> <dt>

*System* \[in\]
</dt> <dd>

Specifies the peer system. Required.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

On return, contains a reference to the job, which can be **NULL**, if the job is completed.

If a job is started and after the job is completed, you can examine the [**CIM\_AffectedJobElement**](https://msdn.microsoft.com/library/cc150663) associations for the [**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447) instances that are associated with the peer system.

</dd> <dt>

*ServiceAccessPoints* \[out\]
</dt> <dd>

On return, contains a list of service access points (SAPs) for the specified system.

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

**DMTF Reserved** (7–4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097–0x7FFF)
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

[**CIM\_AffectedJobElement**](https://msdn.microsoft.com/library/cc150663)
</dt> <dt>

[**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447)
</dt> </dl>

 

 





