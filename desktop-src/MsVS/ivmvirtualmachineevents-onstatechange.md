---
title: IVMVirtualMachineEvents OnStateChange method
description: The OnStateChange method is called when the state of a virtual machine has changed.
ms.assetid: 13bb89e6-60d9-4361-a1e6-3107637525b1
keywords:
- OnStateChange method Virtual Server
- OnStateChange method Virtual Server , IVMVirtualMachineEvents interface
- IVMVirtualMachineEvents interface Virtual Server , OnStateChange method
topic_type:
- apiref
api_name:
- IVMVirtualMachineEvents.OnStateChange
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachineEvents::OnStateChange method

The **OnStateChange** method is called when the state of a virtual machine has changed.

## Syntax


```C++
HRESULT OnStateChange(
  [in] VMVMState virtualMachineState
);
```



## Parameters

<dl> <dt>

*virtualMachineState* \[in\]
</dt> <dd>

The new state of the virtual machine.

</dd> </dl>

## Return value

A [**32-bit value**](hresult-codes-specific-to-the-virtual-server.md) that describes an error or warning.

## Remarks

This method is called when the state for this virtual machine changes. The client program must implement this interface method to receive notification of the [**vmVirtualMachineEvent\_StateChanged**](vmvirtualmachineevents.md) event originating from [**IVMVirtualMachine**](ivmvirtualmachine.md). To monitor state changes for all virtual machines, use the [**IVMVirtualServerEvents::OnVMStateChange**](ivmvirtualserverevents-onvmstatechange.md) method.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualMachineEvents**](ivmvirtualmachineevents.md)
</dt> <dt>

[**VMVMState**](vmvmstate.md)
</dt> </dl>

 

 





