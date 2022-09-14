---
title: IBasicDevice DiscoveredOnCurrentNetwork method
description: Retrieves a value that indicates if the device is on the current network.
ms.assetid: E64D4E49-9790-4647-9A01-2C28C407F238
keywords:
- DiscoveredOnCurrentNetwork method Media Streaming API
- DiscoveredOnCurrentNetwork method Media Streaming API , IBasicDevice interface
- IBasicDevice interface Media Streaming API , DiscoveredOnCurrentNetwork method
topic_type:
- apiref
api_name:
- IBasicDevice.DiscoveredOnCurrentNetwork
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IBasicDevice::DiscoveredOnCurrentNetwork method

Retrieves a value that indicates if the device is on the current network.

## Syntax


```C++
HRESULT DiscoveredOnCurrentNetwork(
  [out] boolean *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives a pointer to a boolean value that is **True** if the device is on the current network.

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

 

 





