---
title: IVMVirtualServerEvents interface
description: Defines the outgoing event interface for IVMVirtualServer.
ms.assetid: 2077ab1b-b16e-44e2-b1c7-cd10223bdb4a
keywords:
- IVMVirtualServerEvents interface Virtual Server
- IVMVirtualServerEvents interface Virtual Server , described
topic_type:
- apiref
api_name:
- IVMVirtualServerEvents
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMVirtualServerEvents interface

The **IVMVirtualServerEvents** interface defines the outgoing event interface for [**IVMVirtualServer**](ivmvirtualserver.md).

## When to implement

The client implements these methods to receive events sent from [**IVMVirtualServer**](ivmvirtualserver.md).

## Members

The **IVMVirtualServerEvents** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IVMVirtualServerEvents** also has these types of members:

-   [Methods](#methods)

### Methods

The **IVMVirtualServerEvents** interface has these methods.



| Method                                                                  | Description                                                              |
|:------------------------------------------------------------------------|:-------------------------------------------------------------------------|
| [**OnEventLogged**](ivmvirtualserverevents-oneventlogged.md)           | Called when Virtual Server logs an event.<br/>                     |
| [**OnHeartbeatStopped**](ivmvirtualserverevents-onheartbeatstopped.md) | Called when the heartbeat of a virtual machine stops.<br/>         |
| [**OnServiceEvent**](ivmvirtualserverevents-onserviceevent.md)         | Called when a Virtual Server service event occurs.<br/>            |
| [**OnVMStateChange**](ivmvirtualserverevents-onvmstatechange.md)       | Called when the state of a virtual machine state has changed.<br/> |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





