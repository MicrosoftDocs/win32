---
title: IBasicDevice RemoteStreamingUrls method
description: Returns a vector of remote streaming URLs.
ms.assetid: 19B4475F-A7E4-4DC4-9C88-68D91D023AF4
keywords:
- RemoteStreamingUrls method Media Streaming API
- RemoteStreamingUrls method Media Streaming API , IBasicDevice interface
- IBasicDevice interface Media Streaming API , RemoteStreamingUrls method
topic_type:
- apiref
api_name:
- IBasicDevice.RemoteStreamingUrls
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IBasicDevice::RemoteStreamingUrls method

Returns a vector of remote streaming URLs.

## Syntax


```C++
HRESULT RemoteStreamingUrls(
  [out] IVector< HSTRING > **value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives an enumerable collection of pointers to remote streaming URLs.

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

 

 





