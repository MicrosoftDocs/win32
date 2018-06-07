---
title: IDeviceIcon Stream method
description: Retrieves the icon as a stream.
ms.assetid: 0B9E852F-4F72-4721-8F88-24A850A088C4
keywords:
- Stream method Media Streaming API
- Stream method Media Streaming API , IDeviceIcon interface
- IDeviceIcon interface Media Streaming API , Stream method
topic_type:
- apiref
api_name:
- IDeviceIcon.Stream
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IDeviceIcon::Stream method

Retrieves the icon as a stream.

## Syntax


```C++
HRESULT Stream(
  [out] IRandomAccessStreamWithContentType **value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives a reference to a [**IRandomAccessStreamWithContentType**](https://msdn.microsoft.com/library/windows/apps/br241736) that can be used to retrieve the image data.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## See also

<dl> <dt>

[**IDeviceIcon**](https://www.bing.com/search?q=**IDeviceIcon**)
</dt> </dl>

 

 





