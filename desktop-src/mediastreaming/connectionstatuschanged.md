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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

To handle notifications from this event, register a [**ConnectionStatusHandler**](/windows/win32/mfidl/?branch=master) event handler function using the [**add\_ConnectionStatusChanged**](ibasicdevice-add-connectionstatuschanged.md) method. To unregister the event handler, use the [**remove\_ConnectionStatusChanged**](ibasicdevice-remove-connectionstatuschanged.md) method.

 

 




