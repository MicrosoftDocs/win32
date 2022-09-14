---
description: Defines a planned virtual system.
ms.assetid: f129554b-e43e-4c3a-8418-d5d810f4c4b5
title: DefinePlannedSystem method of the Msvm_VirtualSystemManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemManagementService.DefinePlannedSystem
api_type: 
- COM
api_location: 
- vmms.exe
---

# DefinePlannedSystem method of the Msvm\_VirtualSystemManagementService class

Defines a planned virtual system.

Input that is not completely specified may be filled out with default values.

## Syntax


```mof
uint32 DefinePlannedSystem(
  [in]  string                           SystemSettings,
  [in]  string                           ResourceSettings[],
  [in]  CIM_VirtualSystemSettingData REF ReferenceConfiguration,
  [out] CIM_ComputerSystem           REF ResultingSystem,
  [out] CIM_ConcreteJob              REF Job
);
```



## Parameters

<dl> <dt>

*SystemSettings* \[in\]
</dt> <dd>

The system settings for the virtual system.

</dd> <dt>

*ResourceSettings* \[in\]
</dt> <dd>

The resource settings for the virtual system.

</dd> <dt>

*ReferenceConfiguration* \[in\]
</dt> <dd>

A [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) containing the reference configuration.

</dd> <dt>

*ResultingSystem* \[out\]
</dt> <dd>

A [**CIM\_ComputerSystem**](cim-computersystem.md) containing the resulting system.

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
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

