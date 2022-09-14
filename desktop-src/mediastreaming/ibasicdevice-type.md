---
title: IBasicDevice Type method
description: Retrieves an enumeration value indicating the device type of the DLNA device.
ms.assetid: D9FB3A02-7796-4ACB-B7D3-D171D1D9B77F
keywords:
- Type method Media Streaming API
- Type method Media Streaming API , IBasicDevice interface
- IBasicDevice interface Media Streaming API , Type method
topic_type:
- apiref
api_name:
- IBasicDevice.Type
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IBasicDevice::Type method

Retrieves an enumeration value indicating the device type of the DLNA device.

## Syntax


```C++
HRESULT Type(
  [out] DeviceTypes *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives a pointer to a [**DeviceTypes**](devicetypes.md) value.

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

 

 





