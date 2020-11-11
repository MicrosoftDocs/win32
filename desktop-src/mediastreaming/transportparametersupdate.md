---
title: TransportParametersUpdate event
description: Occurs whenever any of a set of transport parameters are updated on the DMR.
ms.assetid: 'df9256ca-6c59-462c-b32f-4653546db384'
keywords:
- TransportParametersUpdate event Media Streaming API
topic_type:
- apiref
api_name:
- TransportParametersUpdate
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# TransportParametersUpdate event

Occurs whenever any of a set of transport parameters are updated on the DMR.

## Syntax


```C++
void TransportParametersUpdate();
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Remarks

To handle notifications from this event, register a [**TransportParametersUpdateHandler**](/previous-versions/windows/desktop/legacy/hh829007(v=vs.85)) event handler function using the [**add\_TransportParametersUpdate**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-add_transportparametersupdate) method. To unregister the event handler, use the [**remove\_TransportParametersUpdate**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-remove_transportparametersupdate) method.

 

 