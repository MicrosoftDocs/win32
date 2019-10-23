---
title: IBasicDevice ModelNumber method
description: Retrieves the device s model number.
ms.assetid: C4199135-0C6C-4427-8152-224D7D29C270
keywords:
- ModelNumber method Media Streaming API
- ModelNumber method Media Streaming API , IBasicDevice interface
- IBasicDevice interface Media Streaming API , ModelNumber method
topic_type:
- apiref
api_name:
- IBasicDevice.ModelNumber
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IBasicDevice::ModelNumber method

Retrieves the device s model number.

## Syntax


```C++
HRESULT ModelNumber(
  [out] HSTRING *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives a pointer to the device s model number.

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

 

 





