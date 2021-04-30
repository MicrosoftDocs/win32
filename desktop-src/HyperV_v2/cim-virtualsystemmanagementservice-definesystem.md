---
description: Defines a virtual system.
ms.assetid: c3964e99-9227-4b98-af87-7caa59296306
title: DefineSystem method of the CIM_VirtualSystemManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_VirtualSystemManagementService.DefineSystem
api_type: 
- COM
api_location: 
- vmms.exe
---

# DefineSystem method of the CIM\_VirtualSystemManagementService class

Defines a virtual system.

Input that is not completely specified may be filled out with default values.

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

String containing an embedded instance of class [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) that is used to define attributes of the virtual system to be created.

</dd> <dt>

*ResourceSettings* \[in\]
</dt> <dd>

Array of strings each containing an embedded instance of class [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md) that describes the virtual aspects of a virtual resource to be created in the scope of the new virtual system.

</dd> <dt>

*ReferenceConfiguration* \[in\]
</dt> <dd>

Reference to a [**CIM\_VirtualSystemSettingDat**](cim-virtualsystemsettingdata.md) object instance that is the top level object of a reference virtual system configuration. The reference configuration is used to complement the configuration of the new virtual system if the *SystemSettings* and *ResourceSettings* parameters did not provide respective information.

</dd> <dt>

*ResultingSystem* \[out\]
</dt> <dd>

If a virtual computer system is successfully defined, a reference to an instance of class [**CIM\_ComputerSystem**](cim-computersystem.md) that represents the newly defined virtual computer system is returned.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

If the operation is long running, then optionally a job may be returned. In this case, the instance of class [**CIM\_ComputerSystem**](cim-computersystem.md) representing the new virtual system is presented via association [**CIM\_AffectedJobElement**](cim-affectedjobelement.md) with the property **AffectedElement** referring to the new instance of class **CIM\_ComputerSystem** and property **ElementEffects** set to 5 (Create).

</dd> </dl>

## Return value

Returns a 0 on success; otherwise, returns an error.

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
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_VirtualSystemManagementService**](cim-virtualsystemmanagementservice.md)
</dt> </dl>

 

 




