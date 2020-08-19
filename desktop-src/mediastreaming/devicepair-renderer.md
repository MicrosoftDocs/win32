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
ms.topic: reference
ms.date: 05/31/2018
api_location: 
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

Receives a [**ActiveBasicDevice**](/previous-versions/windows/desktop/legacy/dn385755(v=vs.85)) object that represents the renderer device.

## See also

<dl> <dt>

[**DevicePair**](/previous-versions/windows/desktop/legacy/dn385771(v=vs.85))
</dt> </dl>

 

 