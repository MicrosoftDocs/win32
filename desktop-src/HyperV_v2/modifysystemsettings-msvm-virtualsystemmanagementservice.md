---
description: Modifies virtual machine settings.
ms.assetid: 3266bd0d-398b-4d3b-9248-e29c069aab11
title: ModifySystemSettings method of the Msvm_VirtualSystemManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemManagementService.ModifySystemSettings
api_type: 
- COM
api_location: 
- vmms.exe
---

# ModifySystemSettings method of the Msvm\_VirtualSystemManagementService class

Modifies virtual machine settings. When applied to the system settings of a "current" virtual machine configuration, as a side effect the virtual machine instance may be modified.

## Syntax


```mof
uint32 ModifySystemSettings(
  [in]  string              SystemSettings,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*SystemSettings* \[in\]
</dt> <dd>

An embedded instance of the [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md) class that contains the modified aspects of the virtual machine. The **InstanceID** property identifies the virtual machine setting to be modified.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

If the operation is performed asynchronously, this method will return 4096, and this parameter will contain a reference to an object derived from [**CIM\_ConcreteJob**](/previous-versions//cc136808(v=vs.85)).

</dd> </dl>

## Return value

This method returns one of the following values.

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
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**ModifyVirtualSystem (V1)**](/previous-versions/windows/desktop/virtual/modifyvirtualsystem-msvm-virtualsystemmanagementservice)
</dt> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

