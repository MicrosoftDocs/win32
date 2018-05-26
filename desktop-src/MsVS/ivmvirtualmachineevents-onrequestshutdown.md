---
title: IVMVirtualMachineEvents OnRequestShutdown method
description: Called when a shutdown has been requested.
ms.assetid: cdcfc30f-1a58-433a-9981-9a4bff483b32
keywords:
- OnRequestShutdown method Virtual Server
- OnRequestShutdown method Virtual Server , IVMVirtualMachineEvents interface
- IVMVirtualMachineEvents interface Virtual Server , OnRequestShutdown method
topic_type:
- apiref
api_name:
- IVMVirtualMachineEvents.OnRequestShutdown
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

# IVMVirtualMachineEvents::OnRequestShutdown method

The **OnRequestShutdown** method is called when a shutdown has been requested.

## Syntax


```C++
HRESULT OnRequestShutdown();
```



## Parameters

This method has no parameters.

## Return value

A [**32-bit value**](hresult-codes-specific-to-the-virtual-server.md) that describes an error or warning.

## Remarks

This method is called whenever the virtual machine session is about to shut down. The client program must implement this interface method to receive notification of the [**vmVirtualMachineEvent\_RequestShutdown**](vmvirtualmachineevents.md) event originating from [**IVMVirtualMachine**](ivmvirtualmachine.md). Clients should set *isAllowed* to **TRUE** to allow the virtual machine to shut down, or **FALSE** to leave it turned on.

This event notification is sent only when the virtual machines session is about to shut down. Operating system shutdown routines, such as [**IVMGuestOS::Shutdown**](ivmguestos-shutdown.md), do not fire this event directly unless they also attempt to perform a software power off of the virtual hardware.

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

 

 





