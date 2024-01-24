---
title: PlaybackOperation.GetResults method
description: Returns the results of an asynchronous operation started by one of the MediaRenderer playback methods.
ms.assetid: EAA5B342-51EF-449A-A7E2-FFBDBE07757C
keywords:
- GetResults method Media Streaming API
- GetResults method Media Streaming API , PlaybackOperation interface
- PlaybackOperation interface Media Streaming API , GetResults method
topic_type:
- apiref
api_name:
- PlaybackOperation.GetResults
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# PlaybackOperation.GetResults method

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Returns the results of an asynchronous operation started by one of the [**MediaRenderer**](mediarenderer.md) playback methods.

## Syntax


```C++
HRESULT GetResults(
  [out, retval] UINT32 *value
);
```



## Parameters

<dl> <dt>

*value* \[out, retval\]
</dt> <dd>

The result of the operation. A value of 0 indicates that the operation completed. Other values are reserved.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

The **GetResults** method is typically called from the event handler that was registered by setting the [**Completed**](playbackoperation-completed.md) property.

## See also

<dl> <dt>

[**PlaybackOperation**](playbackoperation.md)
</dt> </dl>

 

 





