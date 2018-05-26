---
title: IVMVirtualServerEvents OnHeartbeatStopped method
description: Called when the heartbeat stops for any virtual machine, indicating that a virtual machine has stopped running.
ms.assetid: ce5b92da-8def-4b3c-8305-cf8b9de735dd
keywords:
- OnHeartbeatStopped method Virtual Server
- OnHeartbeatStopped method Virtual Server , IVMVirtualServerEvents interface
- IVMVirtualServerEvents interface Virtual Server , OnHeartbeatStopped method
topic_type:
- apiref
api_name:
- IVMVirtualServerEvents.OnHeartbeatStopped
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

# IVMVirtualServerEvents::OnHeartbeatStopped method

The **OnHeartbeatStopped** method is called when the heartbeat stops for any virtual machine, indicating that a virtual machine has stopped running.

## Syntax


```C++
HRESULT OnHeartbeatStopped(
  [in] BSTR virtualMachineConfig
);
```



## Parameters

<dl> <dt>

*virtualMachineConfig* \[in\]
</dt> <dd>

The name of the virtual machine.

</dd> </dl>

## Return value

A [**32-bit value**](hresult-codes-specific-to-the-virtual-server.md) that describes an error or warning.

## Remarks

The client program must implement this interface method to receive notification of the [**vmVirtualServerEvent\_VMHeartbeatStopped**](vmvirtualserverevent.md) event originating from [**IVMVirtualServer**](ivmvirtualserver.md). To monitor a specific virtual machine, use the [**IVMVirtualMachineEvents::OnHeartbeatStopped**](ivmvirtualmachineevents-onheartbeatstopped.md) method.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServerEvents**](ivmvirtualserverevents.md)
</dt> </dl>

 

 





