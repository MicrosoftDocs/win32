---
title: IDeviceIcon ContentType method
description: Retrieves the content type of the icon.
ms.assetid: 01928A98-B7D0-4523-9259-81FEB33F052E
keywords:
- ContentType method Media Streaming API
- ContentType method Media Streaming API , IDeviceIcon interface
- IDeviceIcon interface Media Streaming API , ContentType method
topic_type:
- apiref
api_name:
- IDeviceIcon.ContentType
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IDeviceIcon::ContentType method

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Retrieves the content type of the icon.

## Syntax


```C++
HRESULT ContentType(
  [out] HSTRING *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives a pointer to the content type of the icon.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## See also

<dl> <dt>

[**IDeviceIcon**](/previous-versions/windows/desktop/api/windows.media.streaming/nn-windows-media-streaming-ideviceicon)
</dt> </dl>

 

