---
title: IBasicDevice CanWakeDevices method
description: Retrieves a value that indicates if the device can wake.
ms.assetid: AAD0597C-AD33-40EE-A5DA-27AC66375D38
keywords:
- CanWakeDevices method Media Streaming API
- CanWakeDevices method Media Streaming API , IBasicDevice interface
- IBasicDevice interface Media Streaming API , CanWakeDevices method
topic_type:
- apiref
api_name:
- IBasicDevice.CanWakeDevices
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IBasicDevice::CanWakeDevices method

Retrieves a value that indicates if the device can wake.

## Syntax


```C++
HRESULT CanWakeDevices(
  [out] boolean *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives a pointer to a boolean value that is **True** if the device can wake.

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

 

 





