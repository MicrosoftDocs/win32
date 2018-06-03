---
title: IBasicDevice Icons method
description: Returns a vector of IDeviceIcon interfaces.
ms.assetid: 0C083AF3-FE22-4A8E-87B7-0FFA7B65ADBD
keywords:
- Icons method Media Streaming API
- Icons method Media Streaming API , IBasicDevice interface
- IBasicDevice interface Media Streaming API , Icons method
topic_type:
- apiref
api_name:
- IBasicDevice.Icons
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IBasicDevice::Icons method

Returns a vector of [**IDeviceIcon**](https://www.bing.com/search?q=**IDeviceIcon**) interfaces.

## Syntax


```C++
HRESULT Icons(
  [out] IVector< IDeviceIcon > **value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives an enumerable collection of [**IDeviceIcon**](https://www.bing.com/search?q=**IDeviceIcon**) interface pointers.

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

 

 





