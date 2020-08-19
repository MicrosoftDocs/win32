---
title: BasicDevice.Icons property
description: Gets a vector of IDeviceIcon interfaces.
ms.assetid: 54933FD0-27A6-48D8-A49A-200AD9214B9A
keywords:
- Icons property Media Streaming API
- Icons property Media Streaming API , BasicDevice interface
- BasicDevice interface Media Streaming API , Icons property
topic_type:
- apiref
api_name:
- BasicDevice.Icons
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# BasicDevice.Icons property

Gets a vector of [**IDeviceIcon**](/previous-versions/windows/desktop/api/windows.media.streaming/nn-windows-media-streaming-ideviceicon) interfaces.

This property is read-only.

## Syntax


```C++
HRESULT get_Icons(
  [out] IVector< IDeviceIcon > **value
);
```



## Property value

An enumerable collection of [**IDeviceIcon**](/previous-versions/windows/desktop/api/windows.media.streaming/nn-windows-media-streaming-ideviceicon) interface pointers.

## See also

<dl> <dt>

[**BasicDevice**](/previous-versions/windows/desktop/legacy/hh828813(v=vs.85))
</dt> </dl>

 

 