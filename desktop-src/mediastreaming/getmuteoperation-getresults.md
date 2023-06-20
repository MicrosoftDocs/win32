---
title: GetMuteOperation.GetResults method
description: Returns the results of the asynchronous operation started by GetMuteAsync.
ms.assetid: 5B6DB1B3-54D4-486D-AA03-5FEEC92304B0
keywords:
- GetResults method Media Streaming API
- GetResults method Media Streaming API , GetMuteOperation interface
- GetMuteOperation interface Media Streaming API , GetResults method
topic_type:
- apiref
api_name:
- GetMuteOperation.GetResults
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# GetMuteOperation.GetResults method

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Returns the results of the asynchronous operation started by [**GetMuteAsync**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-getmuteasync).

## Syntax


```C++
HRESULT GetResults(
  [out, retval] boolean *value
);
```



## Parameters

<dl> <dt>

*value* \[out, retval\]
</dt> <dd>

The mute value. A value of true indicates that audio is currently muted. A value of false indicates that audio is not muted.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

The **GetResults** method is typically called from the event handler that was registered by setting the [**Completed**](getmuteoperation-completed.md) property.

## See also

<dl> <dt>

[**GetMuteOperation**](getmuteoperation.md)
</dt> </dl>

 

