---
title: MediaRenderer.ActionInformation property
description: Gets information about which methods can currently be invoked on the DMR.
ms.assetid: 'c36d45cb-c01a-4418-8f21-906c95950d6f'
keywords:
- ActionInformation property Media Streaming API
- ActionInformation property Media Streaming API , MediaRenderer interface
- MediaRenderer interface Media Streaming API , ActionInformation property
topic_type:
- apiref
api_name:
- MediaRenderer.ActionInformation
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# MediaRenderer.ActionInformation property

Gets information about which methods can currently be invoked on the DMR.

This property is read-only.

## Syntax


```C++
HRESULT get_ActionInformation(
  [out] IMediaRendererActionInformation **value
);
```



## Property value

A reference to an [**IMediaRendererActionInformation**](/previous-versions/windows/desktop/api/windows.media.streaming/nn-windows-media-streaming-imediarendereractioninformation) interface.

## See also

<dl> <dt>

[**MediaRenderer**](mediarenderer.md)
</dt> </dl>

 

 