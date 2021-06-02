---
title: MediaRenderer.StopAsync method
description: Instructs the DMR asynchronously to stop playing the current content. | MediaRenderer.StopAsync method
ms.assetid: '04cf6d5a-8aa5-4821-8117-f250bfaf7ebd'
keywords:
- StopAsync method Media Streaming API
- StopAsync method Media Streaming API , MediaRenderer interface
- MediaRenderer interface Media Streaming API , StopAsync method
topic_type:
- apiref
api_name:
- MediaRenderer.StopAsync
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# MediaRenderer.StopAsync method

Instructs the DMR asynchronously to stop playing the current content.

## Syntax


```C++
HRESULT StopAsync(
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

[**MediaRenderer**](mediarenderer.md)
</dt> </dl>

 

 





