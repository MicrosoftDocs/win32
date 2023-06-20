---
title: BasicDevice.ModelName property
description: Gets the model name of the device.
ms.assetid: 1F19EA04-A70A-465D-B761-1707AB8EB063
keywords:
- ModelName property Media Streaming API
- ModelName property Media Streaming API , BasicDevice interface
- BasicDevice interface Media Streaming API , ModelName property
topic_type:
- apiref
api_name:
- BasicDevice.ModelName
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# BasicDevice.ModelName property

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Gets the model name of the device.

This property is read-only.

## Syntax


```C++
HRESULT get_ModelName(
  [out] HSTRING *value
);
```



## Property value

A pointer to the device’s model name.

## See also

<dl> <dt>

[**BasicDevice**](/previous-versions/windows/desktop/legacy/hh828813(v=vs.85))
</dt> </dl>

 

 