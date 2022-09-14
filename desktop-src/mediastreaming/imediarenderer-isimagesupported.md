---
title: IMediaRenderer IsImageSupported method
description: Retrieves a value that indicates whether the DMR is capable of displaying images.
ms.assetid: 3941789B-0FFF-4F00-B63C-2586B39B6546
keywords:
- IsImageSupported method Media Streaming API
- IsImageSupported method Media Streaming API , IMediaRenderer interface
- IMediaRenderer interface Media Streaming API , IsImageSupported method
topic_type:
- apiref
api_name:
- IMediaRenderer.IsImageSupported
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IMediaRenderer::IsImageSupported method

Retrieves a value that indicates whether the DMR is capable of displaying images.

## Syntax


```C++
HRESULT IsImageSupported(
  [out] boolean *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

A boolean value that is **True** if the DMR is capable of displaying images and **False** if it is not.

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

 

 





