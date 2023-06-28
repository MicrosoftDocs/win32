---
title: IBasicDevice IpAddresses method
description: Returns a vector of IP addresses.
ms.assetid: F48B91DC-3AE2-462F-835B-292BF86904B3
keywords:
- IpAddresses method Media Streaming API
- IpAddresses method Media Streaming API , IBasicDevice interface
- IBasicDevice interface Media Streaming API , IpAddresses method
topic_type:
- apiref
api_name:
- IBasicDevice.IpAddresses
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IBasicDevice::IpAddresses method

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Returns a vector of IP addresses.

## Syntax


```C++
HRESULT IpAddresses(
  [out] IVector< HSTRING > **value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives an enumerable collection of pointers to IP addresses.

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

 

 





