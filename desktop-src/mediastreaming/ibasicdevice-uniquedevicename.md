---
title: IBasicDevice UniqueDeviceName method
description: Retrieves the device s unique device name (UDN).
ms.assetid: 393EFF96-69E1-4081-905D-D8CC47B5FC4A
keywords:
- UniqueDeviceName method Media Streaming API
- UniqueDeviceName method Media Streaming API , IBasicDevice interface
- IBasicDevice interface Media Streaming API , UniqueDeviceName method
topic_type:
- apiref
api_name:
- IBasicDevice.UniqueDeviceName
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IBasicDevice::UniqueDeviceName method

Retrieves the device s unique device name (UDN).

## Syntax


```C++
HRESULT UniqueDeviceName(
  [out] HSTRING *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives a pointer to the device s model UDN.

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

 

 





