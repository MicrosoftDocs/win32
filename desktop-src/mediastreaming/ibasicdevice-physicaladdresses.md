---
title: IBasicDevice PhysicalAddresses method
description: Returns a vector of physical addresses.
ms.assetid: 85F48EE3-14A1-46DA-A3C3-F94A8A43CF92
keywords:
- PhysicalAddresses method Media Streaming API
- PhysicalAddresses method Media Streaming API , IBasicDevice interface
- IBasicDevice interface Media Streaming API , PhysicalAddresses method
topic_type:
- apiref
api_name:
- IBasicDevice.PhysicalAddresses
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IBasicDevice::PhysicalAddresses method

Returns a vector of physical addresses.

## Syntax


```C++
HRESULT PhysicalAddresses(
  [out] IVector< HSTRING > **value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives an enumerable collection of pointers to physical addresses.

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

 

 





