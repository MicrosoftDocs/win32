---
title: IVMVirtualMachineEvents OnReset method
description: Called when a virtual machine has been reset.
ms.assetid: 6539762a-c996-4ec0-b4a4-06f20c33c712
keywords:
- OnReset method Virtual Server
- OnReset method Virtual Server , IVMVirtualMachineEvents interface
- IVMVirtualMachineEvents interface Virtual Server , OnReset method
topic_type:
- apiref
api_name:
- IVMVirtualMachineEvents.OnReset
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMVirtualMachineEvents::OnReset method

The **OnReset** method is called when a virtual machine has been reset.

## Syntax


```C++
HRESULT OnReset();
```



## Parameters

This method has no parameters.

## Return value

A [**32-bit value**](hresult-codes-specific-to-the-virtual-server.md) that describes an error or warning.

## Remarks

This method is called when the virtual machine has been reset. The client program must implement this interface method to receive notification of the [**vmVirtualMachineEvent\_Reset**](vmvirtualmachineevents.md) event originating from [**IVMVirtualMachine**](ivmvirtualmachine.md).

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

 

 





