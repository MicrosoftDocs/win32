---
description: Restores back to the last known good key protector.
ms.assetid: 0d1ea5d8-d25e-400c-be65-afe1bd65b1f0
title: RestoreLastKnownGoodKeyProtector method of the Msvm_SecurityService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_SecurityService.RestoreLastKnownGoodKeyProtector
api_type: 
- COM
api_location: 
- vmms.exe
---

# RestoreLastKnownGoodKeyProtector method of the Msvm\_SecurityService class

Restores back to the last known good key protector.

## Syntax


```mof
uint32 RestoreLastKnownGoodKeyProtector(
  [in]  string              SecuritySettingData,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*SecuritySettingData* \[in\]
</dt> <dd>

String contains an embedded instance of the [**Msvm\_SecuritySettingData**](msvm-securitysettingdata.md) class representing the security settings of a virtual system.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

An optional parameter for monitoring progress of the operation, which is used if the method could not be executed synchronously. If the operation is executing asynchronously, the return value is 4096.

</dd> </dl>

## Return value

On success, returns a 0 or 4096; otherwise, returns an error.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Failed** (32768)
</dt> <dt>

**Access Denied** (32769)
</dt> <dt>

**Not Supported** (32770)
</dt> <dt>

**Status is unknown** (32771)
</dt> <dt>

**Timeout** (32772)
</dt> <dt>

**Invalid parameter** (32773)
</dt> <dt>

**System is in use** (32774)
</dt> <dt>

**Invalid state for this operation** (32775)
</dt> <dt>

**Incorrect data type** (32776)
</dt> <dt>

**System is not available** (32777)
</dt> <dt>

**Out of memory** (32778)
</dt> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_SecurityService**](msvm-securityservice.md)
</dt> </dl>

 

 




