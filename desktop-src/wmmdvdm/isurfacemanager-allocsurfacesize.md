---
title: ISurfaceManager AllocSurfaceSize method
description: The AllocSurfaceSize method allocates a new ISurface of a specific size. ISurface wraps an IDirect3DSurface9 interface. However, the recommended way to allocate a surface is described in the IMediaTransform Process documentation.
ms.assetid: '73f50239-e4b8-437e-9c39-a355c43bd468'
keywords: ["AllocSurfaceSize method Windows Movie Maker and DVD Maker", "AllocSurfaceSize method Windows Movie Maker and DVD Maker , ISurfaceManager interface", "ISurfaceManager interface Windows Movie Maker and DVD Maker , AllocSurfaceSize method"]
topic_type:
- apiref
api_name:
- ISurfaceManager.AllocSurfaceSize
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- COM
---

# ISurfaceManager::AllocSurfaceSize method

The **AllocSurfaceSize** method allocates a new [**ISurface**](isurface.md) of a specific size. **ISurface** wraps an **IDirect3DSurface9** interface. However, the recommended way to allocate a surface is described in the [**IMediaTransform::Process**](imediatransform-process.md) documentation.

## Syntax


```C++
HRESULT AllocSurfaceSize(
  [in]  FORMAT_TYPE type,
        VIDEO_SIZE  *pSize,
  [out] ISurface    **ppBuffer
);
```



## Parameters

<dl> <dt>

*type* \[in\]
</dt> <dd>

A [**FORMAT\_TYPE**](format-type.md) value that specifies the type of surface to create.

</dd> <dt>

*pSize* 
</dt> <dd>

A [VIDEO\_SIZE](video-size.md) structure that specifies the size of the surface to allocate.

</dd> <dt>

*ppBuffer* \[out\]
</dt> <dd>

Pointer to an **ISurface** interface pointer that wraps a Direct3D video surface. The caller must release this interface when done with it.

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

## Remarks

If you do not know the exact size of the surface to allocate, use [**AllocSurface**](isurfacemanager-allocsurface.md).

## Requirements



|                                     |                                                                                                                                                                                                                   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                                                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                                                                              |
| Header<br/>                   | <dl> <dt>GPUPipelineTime.h</dt> </dl>                                                                                                                      |
| Library<br/>                  | <dl> <dt>GPUPipelineVC8.lib (Visual Studio 2005); </dt> <dt>GPUPipelineVC7.lib (Visual Studio .NET)</dt> </dl> |



## See also

<dl> <dt>

[**ISurfaceManager::AllocSurface**](isurfacemanager-allocsurface.md)
</dt> <dt>

[**ISurfaceManager Interface**](isurfacemanager.md)
</dt> </dl>

 

 





