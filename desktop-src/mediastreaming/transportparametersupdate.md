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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# TransportParametersUpdate event

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 