---
description: This method is used to find the actual reserve with the input parameter being the number of virtual machine processors for which the reserve is calculated.
ms.assetid: C0497900-00F3-4975-9D12-C82C13C03D8E
title: CalculatePossibleReserve method of the Msvm_ProcessorPool class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ProcessorPool.CalculatePossibleReserve
api_type: 
- COM
api_location: 
- vmms.exe
---

# CalculatePossibleReserve method of the Msvm\_ProcessorPool class

This method is used to find the actual reserve with the input parameter being the number of virtual machine processors for which the reserve is calculated. This method is necessary because the reservation of processor resources is highly dependent on the number of processors which must be scheduled in parallel.

## Syntax


```mof
uint32 CalculatePossibleReserve(
  [in] uint16 ProcessorCount
);
```



## Parameters

<dl> <dt>

*ProcessorCount* \[in\]
</dt> <dd>

Type: **uint16**

The number of virtual machine processors for which the reserve is calculated. The maximum value for this property is the logical processor count for the host computer.

</dd> </dl>

## Return value

Type: **uint32**

The amount of CPU resources that may be reserved for a virtual machine.

## Remarks

Access to the [**Msvm\_ProcessorPool**](msvm-processorpool.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

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

[**Msvm\_ProcessorPool**](msvm-processorpool.md)
</dt> </dl>

 

