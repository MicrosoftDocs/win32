---
Description: Modifies virtual resource settings.
ms.assetid: 3fb2a65f-9f40-4eb9-99e8-8fe1451427d9
title: ModifyResourceSettings method of the Msvm\_VirtualSystemManagementService class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ModifyResourceSettings method of the Msvm\_VirtualSystemManagementService class

Modifies virtual resource settings. When applied to parts of a current virtual machine configuration, as a side effect, the resources of the active virtual machine may be modified.

## Syntax


```mof
uint32 ModifyResourceSettings(
  [in]  string                                ResourceSettings[],
  [out] CIM_ResourceAllocationSettingData REF ResultingResourceSettings[],
  [out] CIM_ConcreteJob                   REF Job
);
```



## Parameters

<dl> <dt>

*ResourceSettings* \[in\]
</dt> <dd>

An array of strings that contain an embedded instance of a class derived from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214), that contain the modified aspects of existing virtual resources. The **InstanceID** property of each instance identifies the virtual resource setting to be modified.

</dd> <dt>

*ResultingResourceSettings* \[out\]
</dt> <dd>

An array of references to instances of objects derived from [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) representing virtual aspects of the modified virtual resources.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

If the operation is performed asynchronously, this method will return 4096, and this parameter will contain a reference to an object derived from [**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808).

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



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**ModifyVirtualSystemResources (V1)**](https://msdn.microsoft.com/library/cc136807)
</dt> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 




