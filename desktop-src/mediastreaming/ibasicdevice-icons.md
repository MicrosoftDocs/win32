---
title: IBasicDevice Icons method
description: Returns a vector of IDeviceIcon interfaces.
ms.assetid: 0C083AF3-FE22-4A8E-87B7-0FFA7B65ADBD
keywords:
- Icons method Media Streaming API
- Icons method Media Streaming API , IBasicDevice interface
- IBasicDevice interface Media Streaming API , Icons method
topic_type:
- apiref
api_name:
- IBasicDevice.Icons
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IBasicDevice::Icons method

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Returns a vector of [**IDeviceIcon**](/previous-versions/windows/desktop/api/windows.media.streaming/nn-windows-media-streaming-ideviceicon) interfaces.

## Syntax


```C++
HRESULT Icons(
  [out] IVector< IDeviceIcon > **value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives an enumerable collection of [**IDeviceIcon**](/previous-versions/windows/desktop/api/windows.media.streaming/nn-windows-media-streaming-ideviceicon) interface pointers.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## See also

<dl> <dt>

[**IBasicDevice**](ibasicdevice.md)
</dt> </dl>

 

