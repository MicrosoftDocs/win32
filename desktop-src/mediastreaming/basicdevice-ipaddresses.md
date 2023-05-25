---
title: BasicDevice.IpAddresses property
description: Gets a vector of IP addresses.
ms.assetid: 00096782-E1A8-41A2-86CE-EA2296A1C047
keywords:
- IpAddresses property Media Streaming API
- IpAddresses property Media Streaming API , BasicDevice interface
- BasicDevice interface Media Streaming API , IpAddresses property
topic_type:
- apiref
api_name:
- BasicDevice.IpAddresses
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# BasicDevice.IpAddresses property

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Gets a vector of IP addresses.

This property is read-only.

## Syntax


```C++
HRESULT get_IpAddresses(
  [out] IVector< HSTRING > **value
);
```



## Property value

An enumerable collection of pointers to IP addresses.

## See also

<dl> <dt>

[**BasicDevice**](/previous-versions/windows/desktop/legacy/hh828813(v=vs.85))
</dt> </dl>

 

 