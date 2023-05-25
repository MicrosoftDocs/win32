---
title: DeviceController.CachedDevices method
description: Retrieves a collection of IBasicDevice interface pointers that represents the cached view of all discoverable DLNA devices. | DeviceController.CachedDevices method
ms.assetid: 89CFA4BB-EDA8-461A-A3A0-A84CBDA99EA4
keywords:
- CachedDevices method Media Streaming API
- CachedDevices method Media Streaming API , DeviceController interface
- DeviceController interface Media Streaming API , CachedDevices method
topic_type:
- apiref
api_name:
- DeviceController.CachedDevices
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# DeviceController.CachedDevices method

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Retrieves a collection of [**IBasicDevice**](ibasicdevice.md) interface pointers that represents the cached view of all discoverable DLNA devices.

## Syntax


```C++
HRESULT CachedDevices(
  [out] IVector< IBasicDevice > **value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives an enumerable collection of [**IBasicDevice**](ibasicdevice.md) interface pointers.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## See also

<dl> <dt>

[**DeviceController**](/previous-versions/windows/desktop/legacy/hh828842(v=vs.85))
</dt> </dl>

 

