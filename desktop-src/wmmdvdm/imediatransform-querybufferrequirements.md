---
title: IMediaTransform QueryBufferRequirements method
description: Windows Movie Maker calls the QueryBufferRequirements method on startup to learn any special buffer requirements of the transform.
ms.assetid: c3915dfb-2d7a-4ed9-ad2e-b56aeabbf993
keywords:
- QueryBufferRequirements method Windows Movie Maker and DVD Maker
- QueryBufferRequirements method Windows Movie Maker and DVD Maker , IMediaTransform interface
- IMediaTransform interface Windows Movie Maker and DVD Maker , QueryBufferRequirements method
topic_type:
- apiref
api_name:
- IMediaTransform.QueryBufferRequirements
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMediaTransform::QueryBufferRequirements method

Windows Movie Maker calls the **QueryBufferRequirements** method on startup to learn any special buffer requirements of the transform.

## Syntax


```C++
HRESULT QueryBufferRequirements(
  [in]  DWORD        dwStream,
  [out] BufferFormat *pFormat
);
```



## Parameters

<dl> <dt>

*dwStream* \[in\]
</dt> <dd>

One of the following **DWORD** values specifying an input or output stream:

0 indicates the output stream.

1 indicates the first input stream.

2 indicates the second input stream.

The transform should indicate the total number of input streams in its implementation of [**get\_InputCount**](imediatransform-get-inputcount.md).

</dd> <dt>

*pFormat* \[out\]
</dt> <dd>

Pointer to a [**BufferFormat**](bufferformat.md) structure that specifies the format for that stream. The caller allocates this structure; the transform should fill it with the buffer requirements. For more information, see Remarks.

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

## Remarks

Most transforms will not have any special buffer requirements; unless your transform has special requirements, this method should return S\_OK and not process the *pFormat* parameter that is passed in.

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

 

 





