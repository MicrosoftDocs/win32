---
title: BasicDevice.PhysicalAddresses property
description: Gets a vector of physical addresses.
ms.assetid: E9D86D13-8DD4-40BA-8608-54F8B3832E05
keywords:
- PhysicalAddresses property Media Streaming API
- PhysicalAddresses property Media Streaming API , BasicDevice interface
- BasicDevice interface Media Streaming API , PhysicalAddresses property
topic_type:
- apiref
api_name:
- BasicDevice.PhysicalAddresses
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# BasicDevice.PhysicalAddresses property

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Gets a vector of physical addresses.

This property is read-only.

## Syntax


```C++
HRESULT get_PhysicalAddresses(
  [out] IVector< HSTRING > **value
);
```



## Property value

An enumerable collection of pointers to physical addresses.

## See also

<dl> <dt>

[**BasicDevice**](/previous-versions/windows/desktop/legacy/hh828813(v=vs.85))
</dt> </dl>

 

 