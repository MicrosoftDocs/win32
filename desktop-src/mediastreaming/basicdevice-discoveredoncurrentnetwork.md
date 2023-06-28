---
title: BasicDevice.DiscoveredOnCurrentNetwork property
description: Gets a value that indicates if the device is on the current network.
ms.assetid: 239A9863-BD18-44AE-96C6-3C85289EF709
keywords:
- DiscoveredOnCurrentNetwork property Media Streaming API
- DiscoveredOnCurrentNetwork property Media Streaming API , BasicDevice interface
- BasicDevice interface Media Streaming API , DiscoveredOnCurrentNetwork property
topic_type:
- apiref
api_name:
- BasicDevice.DiscoveredOnCurrentNetwork
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# BasicDevice.DiscoveredOnCurrentNetwork property

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Gets a value that indicates if the device is on the current network.

This property is read-only.

## Syntax


```C++
HRESULT get_DiscoveredOnCurrentNetwork(
  [out] boolean *value
);
```



## Property value

A pointer to a boolean value that is **True** if the device is on the current network.

## See also

<dl> <dt>

[**BasicDevice**](/previous-versions/windows/desktop/legacy/hh828813(v=vs.85))
</dt> </dl>

 

 