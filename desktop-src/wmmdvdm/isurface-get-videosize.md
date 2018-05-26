---
title: ISurface get\_VideoSize method
description: The get\_VideoSize method retrieves the size of the video surface.
ms.assetid: d52ca294-80f4-4842-8d0b-0b12cd8f0198
keywords:
- get_VideoSize method Windows Movie Maker and DVD Maker
- get_VideoSize method Windows Movie Maker and DVD Maker , ISurface interface
- ISurface interface Windows Movie Maker and DVD Maker , get_VideoSize method
topic_type:
- apiref
api_name:
- ISurface.get_VideoSize
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

# ISurface::get\_VideoSize method

The **get\_VideoSize** method retrieves the size of the video surface.

## Syntax


```C++
HRESULT get_VideoSize(
  [out] VIDEO_SIZE *pSize
);
```



## Parameters

<dl> <dt>

*pSize* \[out\]
</dt> <dd>

Pointer to a [VIDEO\_SIZE](video-size.md) structure describing the surface.

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

[**ISurface Interface**](isurface.md)
</dt> </dl>

 

 





