---
description: Adds generic settings to a virtual system configuration.
ms.assetid: ae04be39-0401-43e9-b19b-3539ca1786ec
title: AddSystemComponentSettings method of the Msvm_VirtualSystemManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemManagementService.AddSystemComponentSettings
api_type: 
- COM
api_location: 
- vmms.exe
---

# AddSystemComponentSettings method of the Msvm\_VirtualSystemManagementService class

Adds generic settings to a virtual system configuration.

## Syntax


```mof
uint32 AddSystemComponentSettings(
  [in]  Msvm_VirtualSystemSettingData   REF AffectedConfiguration,
  [in]  string                              ComponentSettings[],
  [out] Msvm_SystemComponentSettingData REF ResultingComponentSettings[],
  [out] CIM_ConcreteJob                 REF Job
);
```



## Parameters

<dl> <dt>

*AffectedConfiguration* \[in\]
</dt> <dd></dd> <dt>

*ComponentSettings* \[in\]
</dt> <dd>

The component settings to add.

</dd> <dt>

*ResultingComponentSettings* \[out\]
</dt> <dd>

On success, references a [**Msvm\_SystemComponentSettingData**](msvm-systemcomponentsettingdata.md) that contains the resulting component settings.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

If the operation is performed asynchronously, this method will return 4096, and this parameter will contain a reference to an object derived from [**CIM\_ConcreteJob**](/previous-versions//cc136808(v=vs.85)).

</dd> </dl>

## Return value

On success, returns 0 or 4096; otherwise, returns an error.

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

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

