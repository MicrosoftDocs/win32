---
title: IMediaTransform get\_MediaType method
description: The get\_MediaType method enables your transform to report the media type that it can handle.
ms.assetid: 3ef6d273-8460-42d8-8bbb-d6b0fa68276c
keywords:
- get_MediaType method Windows Movie Maker and DVD Maker
- get_MediaType method Windows Movie Maker and DVD Maker , IMediaTransform interface
- IMediaTransform interface Windows Movie Maker and DVD Maker , get_MediaType method
topic_type:
- apiref
api_name:
- IMediaTransform.get_MediaType
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMediaTransform::get\_MediaType method

The **get\_MediaType** method enables your transform to report the media type that it can handle.

## Syntax


```C++
HRESULT get_MediaType(
  [out] MEDIA_FORMAT_TYPE *pfType
);
```



## Parameters

<dl> <dt>

*pfType* \[out\]
</dt> <dd>

Pointer to a **MEDIA\_FORMAT\_TYPE** enumerated value that describes the type of media that the node can handle. Currently, the only valid type is MEDIA\_TYPE\_VIDEO.

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

## Requirements



|                                     |                                                                                                                                                                                                                   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                                                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                                                                              |
| Header<br/>                   | <dl> <dt>GPUPipelineTime.h</dt> </dl>                                                                                                                      |
| Library<br/>                  | <dl> <dt>GPUPipelineVC8.lib (Visual Studio 2005); </dt> <dt>GPUPipelineVC7.lib (Visual Studio .NET)</dt> </dl> |



## See also

<dl> <dt>

[**IMediaTransform Interface**](imediatransform.md)
</dt> </dl>

 

 





