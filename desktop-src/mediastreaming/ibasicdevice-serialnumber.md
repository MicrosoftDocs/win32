---
title: IBasicDevice SerialNumber method
description: Retrieves the device s serial number.
ms.assetid: 238A5999-0E8B-4462-AFCF-790DB58CFCB4
keywords:
- SerialNumber method Media Streaming API
- SerialNumber method Media Streaming API , IBasicDevice interface
- IBasicDevice interface Media Streaming API , SerialNumber method
topic_type:
- apiref
api_name:
- IBasicDevice.SerialNumber
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IBasicDevice::SerialNumber method

Retrieves the device s serial number.

## Syntax


```C++
HRESULT SerialNumber(
  [out] HSTRING *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives a pointer to the device s serial number.

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

 

 





