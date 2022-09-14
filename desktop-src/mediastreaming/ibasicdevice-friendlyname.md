---
title: IBasicDevice FriendlyName method
description: Retrieves the device s friendly name.
ms.assetid: 693806E1-CA66-457D-A25B-D79064776965
keywords:
- FriendlyName method Media Streaming API
- FriendlyName method Media Streaming API , IBasicDevice interface
- IBasicDevice interface Media Streaming API , FriendlyName method
topic_type:
- apiref
api_name:
- IBasicDevice.FriendlyName
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IBasicDevice::FriendlyName method

Retrieves the device s friendly name.

## Syntax


```C++
HRESULT FriendlyName(
  [out] HSTRING *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives a pointer to the device s friendly name.

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

 

 





