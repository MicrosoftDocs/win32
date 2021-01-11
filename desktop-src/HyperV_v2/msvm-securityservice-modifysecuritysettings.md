---
description: Modifies the current security settings of a virtual machine.
ms.assetid: b3eedab6-fd69-4c54-a8bf-4e3b77207687
title: ModifySecuritySettings method of the Msvm_SecurityService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_SecurityService.ModifySecuritySettings
api_type: 
- COM
api_location: 
- vmms.exe
---

# ModifySecuritySettings method of the Msvm\_SecurityService class

Modifies the current security settings of a virtual machine.

## Syntax


```mof
uint32 ModifySecuritySettings(
  [in]  string              SecuritySettingData,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*SecuritySettingData* \[in\]
</dt> <dd>

The new security setting data.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

An optional parameter for monitoring progress of the operation, which is used if the method could not be executed synchronously. If the operation is executing asynchronously, the return value is 4096.

</dd> </dl>

## Return value

On success, returns a 0; otherwise, returns an error.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Failed** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Invalid Parameter** (4)
</dt> <dt>

**Invalid State** (5)
</dt> <dt>

**Incompatible Parameters** (6)
</dt> <dt>

**DMTF Reserved** (..)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097..32767)
</dt> <dt>

**Vendor Specific** (32768..65535)
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

 

 




