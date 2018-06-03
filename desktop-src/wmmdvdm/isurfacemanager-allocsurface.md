---
title: ISurfaceManager AllocSurface method
description: The AllocSurface method allocates a new ISurface interface for the application to use. ISurface wraps an IDirect3DSurface9 interface. However, the recommended way to allocate a surface is described in the IMediaTransform Process method documentation.
ms.assetid: 9811909e-e6be-4c5c-ac3e-772a9967099c
keywords:
- AllocSurface method Windows Movie Maker and DVD Maker
- AllocSurface method Windows Movie Maker and DVD Maker , ISurfaceManager interface
- ISurfaceManager interface Windows Movie Maker and DVD Maker , AllocSurface method
topic_type:
- apiref
api_name:
- ISurfaceManager.AllocSurface
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

# ISurfaceManager::AllocSurface method

The **AllocSurface** method allocates a new [**ISurface**](isurface.md) interface for the application to use. **ISurface** wraps an **IDirect3DSurface9** interface. However, the recommended way to allocate a surface is described in the [**IMediaTransform::Process**](imediatransform-process.md) method documentation.

## Syntax


```C++
HRESULT AllocSurface(
  [in]  FORMAT_TYPE type,
  [out] ISurface    **ppBuffer
);
```



## Parameters

<dl> <dt>

*type* \[in\]
</dt> <dd>

A [**FORMAT\_TYPE**](format-type.md) value specifying the type of surface to create.

</dd> <dt>

*ppBuffer* \[out\]
</dt> <dd>

Pointer to an **ISurface** interface pointer wrapping a Direct3D video surface. The caller must release this interface when done with it.

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

## Remarks

To allocate a surface of a specific size, call [**AllocSurfaceSize**](isurfacemanager-allocsurfacesize.md).

## Requirements



|                                     |                                                                                                                                                                                                                   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                                                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                                                                              |
| Header<br/>                   | <dl> <dt>GPUPipelineTime.h</dt> </dl>                                                                                                                      |
| Library<br/>                  | <dl> <dt>GPUPipelineVC8.lib (Visual Studio 2005); </dt> <dt>GPUPipelineVC7.lib (Visual Studio .NET)</dt> </dl> |



## See also

<dl> <dt>

[**ISurfaceManager Interface**](isurfacemanager.md)
</dt> <dt>

[**ISurfaceManager::AllocSurfaceSize**](isurfacemanager-allocsurfacesize.md)
</dt> </dl>

 

 





