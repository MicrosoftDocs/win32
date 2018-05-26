---
title: IVMVirtualMachineEvents OnTripleFault method
description: Called when a virtual machine has triple-faulted.
ms.assetid: 97e871da-d1f2-4e7d-b4b6-c8842e324c2d
keywords:
- OnTripleFault method Virtual Server
- OnTripleFault method Virtual Server , IVMVirtualMachineEvents interface
- IVMVirtualMachineEvents interface Virtual Server , OnTripleFault method
topic_type:
- apiref
api_name:
- IVMVirtualMachineEvents.OnTripleFault
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMVirtualMachineEvents::OnTripleFault method

The **OnTripleFault** method is called when a virtual machine has triple-faulted.

## Syntax


```C++
HRESULT OnTripleFault();
```



## Parameters

This method has no parameters.

## Return value

A [**32-bit value**](hresult-codes-specific-to-the-virtual-server.md) that describes an error or warning.

## Remarks

This method is called when a virtual machine has triple-faulted. The client program must implement this interface method to receive notification of the [**vmVirtualMachineEvent\_TripleFault**](vmvirtualmachineevents.md) event originating from [**IVMVirtualMachine**](ivmvirtualmachine.md).

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualMachineEvents**](ivmvirtualmachineevents.md)
</dt> </dl>

 

 





