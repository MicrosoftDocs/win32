---
title: IBasicDevice ManufacturerUrl method
description: Retrieves the device s manufacturer URL.
ms.assetid: E8372D15-D8B5-49E4-950A-96B4A88B0450
keywords:
- ManufacturerUrl method Media Streaming API
- ManufacturerUrl method Media Streaming API , IBasicDevice interface
- IBasicDevice interface Media Streaming API , ManufacturerUrl method
topic_type:
- apiref
api_name:
- IBasicDevice.ManufacturerUrl
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IBasicDevice::ManufacturerUrl method

Retrieves the device s manufacturer URL.

## Syntax


```C++
HRESULT ManufacturerUrl(
  [out] HSTRING *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives a pointer to the device s manufacturer URL.

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

 

 





