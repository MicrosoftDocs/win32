---
title: DefineVirtualSystem method of the CIM\_VirtualSystemManagementService class
description: Creates a new virtual computer system instance.
ms.assetid: '99f36530-0e92-4cdc-afd2-3f42e651c43e'
keywords: ["DefineVirtualSystem method Hyper-V", "DefineVirtualSystem method Hyper-V , CIM_VirtualSystemManagementService class", "CIM_VirtualSystemManagementService class Hyper-V , DefineVirtualSystem method"]
topic_type:
- apiref
api_name:
- CIM_VirtualSystemManagementService.DefineVirtualSystem
api_location:
- Root\virtualization
api_type:
- COM
---

# DefineVirtualSystem method of the CIM\_VirtualSystemManagementService class

Creates a new virtual computer system instance.

## Syntax


```mof
uint32 DefineVirtualSystem(
  [in]  string                           SystemSettingData,
  [in]  string                           ResourceSettingData[],
  [in]  CIM_VirtualSystemSettingData REF SourceSetting,
  [out] CIM_ComputerSystem           REF DefinedSystem,
  [out] CIM_ConcreteJob              REF Job
);
```



## Parameters

<dl> <dt>

*SystemSettingData* \[in\]
</dt> <dd>

An Embedded instance of the [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) class.

</dd> <dt>

*ResourceSettingData* \[in\]
</dt> <dd>

An optional parameter that contains a number of embedded instances of the [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md) class (or derived classes thereof). Together these instances describe the virtual resources of the virtual computer system. A default set of devices will be created for the virtual system regardless of whether this parameter is set. For example, processor and memory are automatically created and configured with default values

</dd> <dt>

*SourceSetting* \[in\]
</dt> <dd>

reference to an existing instance of [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) to use as a template for the new virtual computer system.

</dd> <dt>

*DefinedSystem* \[out\]
</dt> <dd>

A reference to the newly created virtual computer system.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

An optional reference that is returned if the operation is executed asynchronously.

</dd> </dl>

## Requirements



|                      |                                                                                                      |
|----------------------|------------------------------------------------------------------------------------------------------|
| Namespace<br/> | Root\\virtualization<br/>                                                                      |
| MOF<br/>       | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_VirtualSystemManagementService**](cim-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





