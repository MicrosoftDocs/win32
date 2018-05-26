---
title: IVMVirtualServerEvents OnEventLogged method
description: Called when Virtual Server logs an event.
ms.assetid: ef8e6d01-8f6c-4feb-84f3-7c89c13c76fd
keywords:
- OnEventLogged method Virtual Server
- OnEventLogged method Virtual Server , IVMVirtualServerEvents interface
- IVMVirtualServerEvents interface Virtual Server , OnEventLogged method
topic_type:
- apiref
api_name:
- IVMVirtualServerEvents.OnEventLogged
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

# IVMVirtualServerEvents::OnEventLogged method

The **OnEventLogged** method is called when Virtual Server logs an event.

## Syntax


```C++
HRESULT OnEventLogged(
  [in] long logMessageID
);
```



## Parameters

<dl> <dt>

*logMessageID* \[in\]
</dt> <dd>

The message identifier of the event log message that was logged.

</dd> </dl>

## Return value

A [**32-bit value**](hresult-codes-specific-to-the-virtual-server.md) that describes an error or warning.

## Remarks

This method is called when Virtual Server logs a message to the Windows event log. The client program must implement this interface method to receive notification of the [**vmVirtualServerEvent\_EventLogged**](vmvirtualserverevent.md) event originating from [**IVMVirtualServer**](ivmvirtualserver.md). To be notified only of major service events, use the [**OnServiceEvent**](ivmvirtualserverevents-onserviceevent.md) method.

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

 

 





