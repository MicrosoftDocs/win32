---
title: DevicePair Renderer property
description: Gets the renderer for the active basic device pair.
ms.assetid: DB2ED5D3-CCDF-4704-A29A-F1A13F7B953A
keywords:
- Renderer property Media Streaming API
- Renderer property Media Streaming API , DevicePair interface
- DevicePair interface Media Streaming API , Renderer property
topic_type:
- apiref
api_name:
- DevicePair.Renderer
- DevicePair.get_Renderer
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DevicePair::Renderer property

Gets the renderer for the active basic device pair.

This property is read-only.

## Syntax


```C++
HRESULT get_Renderer(
  [out] ActiveBasicDevice **value
);
```



## Property value

Receives a [**ActiveBasicDevice**](activebasicdevice.md) object that represents the renderer device.

## See also

<dl> <dt>

[**DevicePair**](devicepair.md)
</dt> </dl>

 

 




