---
title: IBasicDevice IpAddresses method
description: Returns a vector of IP addresses.
ms.assetid: F48B91DC-3AE2-462F-835B-292BF86904B3
keywords:
- IpAddresses method Media Streaming API
- IpAddresses method Media Streaming API , IBasicDevice interface
- IBasicDevice interface Media Streaming API , IpAddresses method
topic_type:
- apiref
api_name:
- IBasicDevice.IpAddresses
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IBasicDevice::IpAddresses method

Returns a vector of IP addresses.

## Syntax


```C++
HRESULT IpAddresses(
  [out] IVector< HSTRING > **value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives an enumerable collection of pointers to IP addresses.

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

 

 





