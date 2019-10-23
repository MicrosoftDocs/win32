---
title: IBasicDevice Description method
description: Retrieves a description of the device.
ms.assetid: 9973AC46-E6BA-4931-BDEB-E64B147AB291
keywords:
- Description method Media Streaming API
- Description method Media Streaming API , IBasicDevice interface
- IBasicDevice interface Media Streaming API , Description method
topic_type:
- apiref
api_name:
- IBasicDevice.Description
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IBasicDevice::Description method

Retrieves a description of the device.

## Syntax


```C++
HRESULT Description(
  [out] HSTRING *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives a pointer to the description of the device.

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

 

 





