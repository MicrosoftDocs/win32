---
title: IMediaRenderer IsVideoSupported method
description: Retrieves a value that indicates whether the DMR is capable of playing video content.
ms.assetid: AE9A14D0-A7A2-4A71-9454-06A05C7D85F9
keywords:
- IsVideoSupported method Media Streaming API
- IsVideoSupported method Media Streaming API , IMediaRenderer interface
- IMediaRenderer interface Media Streaming API , IsVideoSupported method
topic_type:
- apiref
api_name:
- IMediaRenderer.IsVideoSupported
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IMediaRenderer::IsVideoSupported method

Retrieves a value that indicates whether the DMR is capable of playing video content.

## Syntax


```C++
HRESULT IsVideoSupported(
  [out] boolean *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

A boolean value that is **True** if the DMR is capable of playing video content and **False** if it is not.

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

 

 





