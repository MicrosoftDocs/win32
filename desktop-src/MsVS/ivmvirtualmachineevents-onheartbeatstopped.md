---
title: IVMVirtualMachineEvents OnHeartbeatStopped method
description: Called when the heartbeat of a virtual machine has stopped.
ms.assetid: ad1d6d37-75c1-4f3b-bdf8-1101b24d8683
keywords:
- OnHeartbeatStopped method Virtual Server
- OnHeartbeatStopped method Virtual Server , IVMVirtualMachineEvents interface
- IVMVirtualMachineEvents interface Virtual Server , OnHeartbeatStopped method
topic_type:
- apiref
api_name:
- IVMVirtualMachineEvents.OnHeartbeatStopped
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

# IVMVirtualMachineEvents::OnHeartbeatStopped method

The **OnHeartbeatStopped** method is called when the heartbeat of a virtual machine has stopped.

## Syntax


```C++
HRESULT OnHeartbeatStopped();
```



## Parameters

This method has no parameters.

## Return value

A [**32-bit value**](hresult-codes-specific-to-the-virtual-server.md) that describes an error or warning.

## Remarks

This method is called when the guest operating system for this virtual machine has stopped abruptly. The client program must implement this interface method to receive notification of the [**vmVirtualMachineEvent\_HeartbeatStopped**](vmvirtualmachineevents.md) event originating from [**IVMVirtualMachine**](ivmvirtualmachine.md). To monitor all virtual machines, use the [**IVMVirtualServerEvents::OnHeartbeatStopped**](ivmvirtualserverevents-onheartbeatstopped.md) method.

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

 

 





