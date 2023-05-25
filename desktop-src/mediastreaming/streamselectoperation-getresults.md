---
title: StreamSelectOperation.GetResults method
description: Returns the results of the asynchronous operation started by SelectBestStreamAsync.
ms.assetid: 2D9887E7-17C8-4161-984F-FA44591D2052
keywords:
- GetResults method Media Streaming API
- GetResults method Media Streaming API , StreamSelectOperation interface
- StreamSelectOperation interface Media Streaming API , GetResults method
topic_type:
- apiref
api_name:
- StreamSelectOperation.GetResults
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# StreamSelectOperation.GetResults method

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Returns the results of the asynchronous operation started by [**SelectBestStreamAsync**](/previous-versions/windows/desktop/legacy/hh829001(v=vs.85)).

## Syntax


```C++
HRESULT GetResults(
  [out, retval] UINT32 *value
);
```



## Parameters

<dl> <dt>

*value* \[out, retval\]
</dt> <dd></dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## See also

<dl> <dt>

[**StreamSelectOperation**](streamselectoperation.md)
</dt> </dl>

 

