---
title: MediaRenderer.PauseAsync method
description: Instructs the DMR asynchronously to pause playing the current content. | MediaRenderer.PauseAsync method
ms.assetid: '1bd36349-0551-44e8-9550-3fd80900de9a'
keywords:
- PauseAsync method Media Streaming API
- PauseAsync method Media Streaming API , MediaRenderer interface
- MediaRenderer interface Media Streaming API , PauseAsync method
topic_type:
- apiref
api_name:
- MediaRenderer.PauseAsync
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# MediaRenderer.PauseAsync method

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

[**MediaRenderer**](mediarenderer.md)
</dt> </dl>

 

 





