---
description: Creates a new virtual switch.
ms.assetid: de7495e9-48c5-427a-b9bb-0821b53a9b09
title: DefineSystem method of the Msvm_VirtualEthernetSwitchManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualEthernetSwitchManagementService.DefineSystem
api_type: 
- COM
api_location: 
- vmms.exe
---

# DefineSystem method of the Msvm\_VirtualEthernetSwitchManagementService class

Creates a new virtual switch. Properties that are not specified will be populated with default values.

## Syntax


```mof
uint32 DefineSystem(
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

An embedded instance of the [**Msvm\_VirtualEthernetSwitchSettingData**](msvm-virtualethernetswitchsettingdata.md) class that is used to define the attributes of the virtual switch to be created. This parameter is required.

</dd> <dt>

*ResourceSettings* \[in\]
</dt> <dd>

An array of embedded instances of the [**Msvm\_EthernetPortAllocationSettingData**](msvm-ethernetportallocationsettingdata.md) class that describes the settings of the switch ports to be created in the scope of the new virtual switch. If **Null** is specified, the virtual switch will be created with no resources (i.e. no switch ports).

</dd> <dt>

*ReferenceConfiguration* \[in\]
</dt> <dd>

This parameter is not used.

</dd> <dt>

*ResultingSystem* \[out\]
</dt> <dd>

If a virtual switch is successfully created, a reference to an instance of the [**Msvm\_VirtualEthernetSwitch**](msvm-virtualethernetswitch.md) class that represents the newly defined virtual switch.

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
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_VirtualEthernetSwitchManagementService**](msvm-virtualethernetswitchmanagementservice.md)
</dt> </dl>

 

