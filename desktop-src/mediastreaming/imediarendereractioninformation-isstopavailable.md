---
title: IMediaRendererActionInformation IsStopAvailable method
description: Retrieves a value that indicates whether the DMR is currently accepting the StopAsync method.
ms.assetid: 6EE8F56D-2A5A-49B0-A9B2-0A7EE57D03FD
keywords:
- IsStopAvailable method Media Streaming API
- IsStopAvailable method Media Streaming API , IMediaRendererActionInformation interface
- IMediaRendererActionInformation interface Media Streaming API , IsStopAvailable method
topic_type:
- apiref
api_name:
- IMediaRendererActionInformation.IsStopAvailable
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IMediaRendererActionInformation::IsStopAvailable method

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Retrieves a value that indicates whether the DMR is currently accepting the [**StopAsync**](imediarenderer-stopasync.md) method.

## Syntax


```C++
HRESULT IsStopAvailable(
  [out] boolean *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

A boolean value that is **True** if the DMR is currently accepting the [**StopAsync**](imediarenderer-stopasync.md) method and **False** if it is not.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## See also

<dl> <dt>

[**IMediaRendererActionInformation**](/previous-versions/windows/desktop/api/windows.media.streaming/nn-windows-media-streaming-imediarendereractioninformation)
</dt> </dl>

 

