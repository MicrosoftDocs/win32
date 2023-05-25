---
title: BasicDevice.Description property
description: Gets a description of the device.
ms.assetid: 2C1892D1-D990-404C-B8B0-B115B16BA66C
keywords:
- Description property Media Streaming API
- Description property Media Streaming API , BasicDevice interface
- BasicDevice interface Media Streaming API , Description property
topic_type:
- apiref
api_name:
- BasicDevice.Description
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# BasicDevice.Description property

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Gets a description of the device.

This property is read-only.

## Syntax


```C++
HRESULT get_Description(
  [out] HSTRING *value
);
```



## Property value

A pointer to the description of the device.

## See also

<dl> <dt>

[**BasicDevice**](/previous-versions/windows/desktop/legacy/hh828813(v=vs.85))
</dt> </dl>

 

 