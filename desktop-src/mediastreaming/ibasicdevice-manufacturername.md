---
title: IBasicDevice ManufacturerName method
description: Retrieves the device s manufacturer name.
ms.assetid: F04400C9-02FC-4CB5-B355-A7E84BECD098
keywords:
- ManufacturerName method Media Streaming API
- ManufacturerName method Media Streaming API , IBasicDevice interface
- IBasicDevice interface Media Streaming API , ManufacturerName method
topic_type:
- apiref
api_name:
- IBasicDevice.ManufacturerName
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IBasicDevice::ManufacturerName method

Retrieves the device s manufacturer name.

## Syntax


```C++
HRESULT ManufacturerName(
  [out] HSTRING *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives a pointer to the device s manufacturer name.

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

 

 





