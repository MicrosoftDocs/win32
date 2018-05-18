---
title: MediaRenderer.StopAsync method
description: Instructs the DMR asynchronously to stop playing the current content.
ms.assetid: 'B6B0F3F2-E95E-4A58-9CBD-CF4CB24FDAD0'
keywords: ["StopAsync method Media Streaming API", "StopAsync method Media Streaming API , MediaRenderer interface", "MediaRenderer interface Media Streaming API , StopAsync method"]
topic_type:
- apiref
api_name:
- MediaRenderer.StopAsync
api_type:
- COM
---

# MediaRenderer.StopAsync method

Instructs the DMR asynchronously to stop playing the current content.

## Syntax


```C++
HRESULT StopAsync(
  [out] PlaybackOperation **value
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

 

 





