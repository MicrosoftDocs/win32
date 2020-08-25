---
title: ConnectionStatusChanged event
description: Occurs when the device’s network connection status changes.
ms.assetid: 'd1f04fa5-895e-4e86-9643-e880388dcded'
keywords:
- ConnectionStatusChanged event Media Streaming API
topic_type:
- apiref
api_name:
- ConnectionStatusChanged
api_type:
- COM
ms.topic: reference
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

To handle notifications from this event, register a [**ConnectionStatusHandler**](/previous-versions/windows/desktop/legacy/hh828836(v=vs.85)) event handler function using the [**add\_ConnectionStatusChanged**](ibasicdevice-add-connectionstatuschanged.md) method. To unregister the event handler, use the [**remove\_ConnectionStatusChanged**](ibasicdevice-remove-connectionstatuschanged.md) method.

 

 