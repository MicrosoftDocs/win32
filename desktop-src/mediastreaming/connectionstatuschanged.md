---
title: ConnectionStatusChanged event
description: Occurs when the device’s network connection status changes.
ms.assetid: FFAA0981-508C-4300-9CA9-24C6AFC1183D
keywords:
- ConnectionStatusChanged event Media Streaming API
topic_type:
- apiref
api_name:
- ConnectionStatusChanged
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ConnectionStatusChanged event

Occurs when the device’s network connection status changes.

## Syntax


```C++
void ConnectionStatusChanged();
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Remarks

To handle notifications from this event, register a [**ConnectionStatusHandler**](/windows/desktop/api/mfidl/) event handler function using the [**add\_ConnectionStatusChanged**](ibasicdevice-add-connectionstatuschanged.md) method. To unregister the event handler, use the [**remove\_ConnectionStatusChanged**](ibasicdevice-remove-connectionstatuschanged.md) method.

 

 




