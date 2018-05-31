---
title: IVMVirtualServerEvents OnVMStateChange method
description: Called when the state changes for any virtual machine.
ms.assetid: d0c10b68-b215-4671-a8ea-b27a99726f18
keywords:
- OnVMStateChange method Virtual Server
- OnVMStateChange method Virtual Server , IVMVirtualServerEvents interface
- IVMVirtualServerEvents interface Virtual Server , OnVMStateChange method
topic_type:
- apiref
api_name:
- IVMVirtualServerEvents.OnVMStateChange
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

# IVMVirtualServerEvents::OnVMStateChange method

The **OnVMStateChange** method is called when the state changes for any virtual machine.

## Syntax


```C++
HRESULT OnVMStateChange(
  [in] BSTR      virtualMachineConfig,
  [in] VMVMState virtualMachineState
);
```



## Parameters

<dl> <dt>

*virtualMachineConfig* \[in\]
</dt> <dd>

The name of the virtual machine.

</dd> <dt>

*virtualMachineState* \[in\]
</dt> <dd>

The new state of the virtual machine.

</dd> </dl>

## Return value

A [**32-bit value**](hresult-codes-specific-to-the-virtual-server.md) that describes an error or warning.

## Remarks

The client program must implement this interface method to receive notification of the [**vmVirtualServerEvent\_VMStateChanged**](vmvirtualserverevent.md) event originating from [**IVMVirtualServer**](ivmvirtualserver.md). To monitor a specific virtual machine, use the [**IVMVirtualMachineEvents::OnStateChange**](ivmvirtualmachineevents-onstatechange.md) method.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServerEvents**](ivmvirtualserverevents.md)
</dt> <dt>

[**VMVMState**](vmvmstate.md)
</dt> </dl>

 

 





