---
title: IDeviceController CachedDevices method
description: Retrieves a collection of IBasicDevice interface pointers that represents the cached view of all discoverable DLNA devices. | IDeviceController CachedDevices method
ms.assetid: 94C2A7FF-5AF8-4F13-BBA5-54ED78C3BBF6
keywords:
- CachedDevices method Media Streaming API
- CachedDevices method Media Streaming API , IDeviceController interface
- IDeviceController interface Media Streaming API , CachedDevices method
topic_type:
- apiref
api_name:
- IDeviceController.CachedDevices
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IDeviceController::CachedDevices method

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

[**IDeviceController**](/previous-versions/windows/desktop/api/windows.media.streaming/nn-windows-media-streaming-idevicecontroller)
</dt> </dl>

 

