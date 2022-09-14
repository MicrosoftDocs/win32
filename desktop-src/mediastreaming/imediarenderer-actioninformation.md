---
title: IMediaRenderer ActionInformation method
description: Retrieves information about which methods can currently be invoked on the DMR.
ms.assetid: 7681FF92-DD13-4BBC-B860-E2BDFDA74FB9
keywords:
- ActionInformation method Media Streaming API
- ActionInformation method Media Streaming API , IMediaRenderer interface
- IMediaRenderer interface Media Streaming API , ActionInformation method
topic_type:
- apiref
api_name:
- IMediaRenderer.ActionInformation
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IMediaRenderer::ActionInformation method

Retrieves information about which methods can currently be invoked on the DMR.

## Syntax


```C++
HRESULT ActionInformation(
  [out] IMediaRendererActionInformation **value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives a reference to an [**IMediaRendererActionInformation**](/previous-versions/windows/desktop/api/windows.media.streaming/nn-windows-media-streaming-imediarendereractioninformation) interface.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## See also

<dl> <dt>

[**IMediaRenderer**](imediarenderer.md)
</dt> </dl>

 

