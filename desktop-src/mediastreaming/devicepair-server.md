---
title: DevicePair Server property
description: Gets the server for the active basic device pair.
ms.assetid: 25FD523F-36C7-4165-BBB2-6A3410D896EF
keywords:
- Server property Media Streaming API
- Server property Media Streaming API , DevicePair interface
- DevicePair interface Media Streaming API , Server property
topic_type:
- apiref
api_name:
- DevicePair.Server
- DevicePair.get_Server
api_location:
- asptlb.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DevicePair::Server property

Gets the server for the active basic device pair.

This property is read-only.

## Syntax


```C++
HRESULT get_Server(
  [out] ActiveBasicDevice **value
);
```



## Property value

Receives a [**ActiveBasicDevice**](activebasicdevice.md) object that represents the server device.

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Asptlb.h</dt> </dl> |



## See also

<dl> <dt>

[**DevicePair**](devicepair.md)
</dt> </dl>

 

 





