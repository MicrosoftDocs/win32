---
description: Adds guest service settings to a virtual system configuration.
ms.assetid: 2c8c2f2b-332a-470e-af7f-80c82e3e2caf
title: AddGuestServiceSettings method of the Msvm_VirtualSystemManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemManagementService.AddGuestServiceSettings
api_type: 
- COM
api_location: 
- vmms.exe
---

# AddGuestServiceSettings method of the Msvm\_VirtualSystemManagementService class

Adds guest service settings to a virtual system configuration.

When applied to parts of a "current" virtual system configuration, as a side effect guest services of the active virtual system may be modified.

## Syntax


```mof
uint32 AddGuestServiceSettings(
  [in]  CIM_VirtualSystemSettingData REF AffectedConfiguration,
  [in]  string                           GuestServiceSettings[],
  [out] CIM_SettingData              REF ResultingGuestServiceSettings[],
  [out] CIM_ConcreteJob              REF Job
);
```



## Parameters

<dl> <dt>

*AffectedConfiguration* \[in\]
</dt> <dd>

Reference to a [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) that describes the affected configuration.

</dd> <dt>

*GuestServiceSettings* \[in\]
</dt> <dd>

An array containing the guest service settings.

</dd> <dt>

*ResultingGuestServiceSettings* \[out\]
</dt> <dd>

On success, contains a reference to a [**CIM\_SettingData**](cim-settingdata.md) that describes the resulting guest service settings.

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

 

