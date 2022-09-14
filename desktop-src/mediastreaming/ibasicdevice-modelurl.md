---
title: IBasicDevice ModelUrl method
description: Retrieves the device s model URL.
ms.assetid: 093D306B-5DFC-4A68-803D-3DDE195A8B85
keywords:
- ModelUrl method Media Streaming API
- ModelUrl method Media Streaming API , IBasicDevice interface
- IBasicDevice interface Media Streaming API , ModelUrl method
topic_type:
- apiref
api_name:
- IBasicDevice.ModelUrl
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IBasicDevice::ModelUrl method

Retrieves the device s model URL.

## Syntax


```C++
HRESULT ModelUrl(
  [out] HSTRING *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives a pointer to the device s model URL.

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

 

 





