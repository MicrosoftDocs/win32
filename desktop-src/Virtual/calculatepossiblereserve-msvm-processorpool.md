---
title: CalculatePossibleReserve method of the Msvm\_ProcessorPool class
description: This method is used to find the actual reserve with the input parameter being the number of virtual machine processors for which the reserve is calculated.
ms.assetid: eda54edc-2ecc-4ec9-93c1-25d7a6acf09a
keywords:
- CalculatePossibleReserve method Hyper-V
- CalculatePossibleReserve method Hyper-V , Msvm_ProcessorPool class
- Msvm_ProcessorPool class Hyper-V , CalculatePossibleReserve method
topic_type:
- apiref
api_name:
- Msvm_ProcessorPool.CalculatePossibleReserve
api_location:
- Root\Virtualization
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CalculatePossibleReserve method of the Msvm\_ProcessorPool class

This method is used to find the actual reserve with the input parameter being the number of virtual machine processors for which the reserve is calculated. This method is necessary because the reservation of processor resources is highly dependent on the number of processors which must be scheduled in parallel.

**Windows Server 2008:** Before Windows Server 2008 R2, this method does nothing and always returns 0.

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

The amount of CPU resources that may be reserved for a virtual system.

## Remarks

Access to the [**Msvm\_ProcessorPool**](msvm-processorpool.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**Msvm\_ProcessorPool**](msvm-processorpool.md)
</dt> </dl>

 

 





