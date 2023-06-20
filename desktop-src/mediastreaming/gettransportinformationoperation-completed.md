---
title: GetTransportInformationOperation Completed property
description: Gets or sets an event handler that is invoked when the asynchronous operation started by GetTransportInformationAsync is completed.
ms.assetid: 11E60E00-75B5-4412-B115-4438255AEB8A
keywords:
- Completed property Media Streaming API
- Completed property Media Streaming API , GetTransportInformationOperation interface
- GetTransportInformationOperation interface Media Streaming API , Completed property
topic_type:
- apiref
api_name:
- GetTransportInformationOperation.Completed
- GetTransportInformationOperation.get_Completed
- GetTransportInformationOperation.put_Completed
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# GetTransportInformationOperation::Completed property

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Gets or sets an event handler that is invoked when the asynchronous operation started by [**GetTransportInformationAsync**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-gettransportinformationasync) is completed.

This property is read/write.

## Syntax


```C++
HRESULT put_Completed(
  [in]  GetTransportInformationCompletedHandler *value
);

HRESULT get_Completed(
  [out] GetTransportInformationCompletedHandler **value
);
```



## Property value

The event handler.

## See also

<dl> <dt>

[**GetTransportInformationOperation**](gettransportinformationoperation.md)
</dt> </dl>

 

 