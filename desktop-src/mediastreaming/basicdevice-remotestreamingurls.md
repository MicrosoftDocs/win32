---
title: BasicDevice.RemoteStreamingUrls property
description: Gets a vector of remote streaming URLs.
ms.assetid: E0F05E04-FED0-42E7-BC42-AFFA9780C366
keywords:
- RemoteStreamingUrls property Media Streaming API
- RemoteStreamingUrls property Media Streaming API , BasicDevice interface
- BasicDevice interface Media Streaming API , RemoteStreamingUrls property
topic_type:
- apiref
api_name:
- BasicDevice.RemoteStreamingUrls
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BasicDevice.RemoteStreamingUrls property

Gets a vector of remote streaming URLs.

This property is read-only.

## Syntax


```C++
HRESULT get_RemoteStreamingUrls(
  [out] IVector< HSTRING > **value
);
```



## Property value

An enumerable collection of pointers to remote streaming URLs.

## See also

<dl> <dt>

[**BasicDevice**](basicdevice.md)
</dt> </dl>

 

 




