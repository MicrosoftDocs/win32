---
title: IMediaRendererFactory CreateMediaRendererFromBasicDeviceAsync method
description: Asynchronously creates a new instance of an object that implements the IMediaRenderer interface using the specified IBasicDevice interface.
ms.assetid: 14A83789-0F3C-467B-8EFD-3BB421C54217
keywords:
- CreateMediaRendererFromBasicDeviceAsync method Media Streaming API
- CreateMediaRendererFromBasicDeviceAsync method Media Streaming API , IMediaRendererFactory interface
- IMediaRendererFactory interface Media Streaming API , CreateMediaRendererFromBasicDeviceAsync method
topic_type:
- apiref
api_name:
- IMediaRendererFactory.CreateMediaRendererFromBasicDeviceAsync
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IMediaRendererFactory::CreateMediaRendererFromBasicDeviceAsync method

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Asynchronously creates a new instance of an object that implements the [**IMediaRenderer**](imediarenderer.md) interface using the specified [**IBasicDevice**](ibasicdevice.md) interface.

## Syntax


```C++
HRESULT CreateMediaRendererFromBasicDeviceAsync(
  [in]          IBasicDevice                 *basicDevice,
  [out, retval] CreateMediaRendererOperation **value
);
```



## Parameters

<dl> <dt>

*basicDevice* \[in\]
</dt> <dd>

A pointer to an [**IBasicDevice**](ibasicdevice.md) interface representing the device for which an instance of [**IMediaRenderer**](imediarenderer.md) will be created.

</dd> <dt>

*value* \[out, retval\]
</dt> <dd>

Receives a reference to a [**CreateMediaRendererOperation**](createmediarendereroperation.md) object that is used to get results from the asynchronous operation.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## See also

<dl> <dt>

[**IMediaRendererFactory**](/previous-versions/windows/desktop/api/windows.media.streaming/nn-windows-media-streaming-imediarendererfactory)
</dt> </dl>

 

