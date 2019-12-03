---
title: IMediaRenderer IsAudioSupported method
description: Retrieves a value that indicates whether the DMR is capable of playing audio content.
ms.assetid: D5F0C4ED-5778-4388-A7BD-E3923145D663
keywords:
- IsAudioSupported method Media Streaming API
- IsAudioSupported method Media Streaming API , IMediaRenderer interface
- IMediaRenderer interface Media Streaming API , IsAudioSupported method
topic_type:
- apiref
api_name:
- IMediaRenderer.IsAudioSupported
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IMediaRenderer::IsAudioSupported method

Retrieves a value that indicates whether the DMR is capable of playing audio content.

## Syntax


```C++
HRESULT IsAudioSupported(
  [out] boolean *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

A boolean value that is **True** if the DMR is capable of playing audio content and **False** if it is not.

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

 

 





