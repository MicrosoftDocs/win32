---
title: IMediaRenderer PauseAsync method
description: Instructs the DMR asynchronously to pause playing the current content. | IMediaRenderer PauseAsync method
ms.assetid: 2EADD9BE-2306-4CDA-AD5C-8342C06EAF1B
keywords:
- PauseAsync method Media Streaming API
- PauseAsync method Media Streaming API , IMediaRenderer interface
- IMediaRenderer interface Media Streaming API , PauseAsync method
topic_type:
- apiref
api_name:
- IMediaRenderer.PauseAsync
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IMediaRenderer::PauseAsync method

Instructs the DMR asynchronously to pause playing the current content.

## Syntax


```C++
HRESULT PauseAsync(
  [out] PlaybackOperation **value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives a reference to a [**PlaybackOperation**](playbackoperation.md) object that is used to get results from the asynchronous operation.

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

 

 





