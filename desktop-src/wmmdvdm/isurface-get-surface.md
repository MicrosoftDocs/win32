---
title: ISurface get\_Surface method
description: The get\_Surface method retrieves an IDirect3DSurface9 interface that points to the video surface.
ms.assetid: '2a88ba69-5cdd-4200-bab1-ac52778d8bd0'
keywords: ["get_Surface method Windows Movie Maker and DVD Maker", "get_Surface method Windows Movie Maker and DVD Maker , ISurface interface", "ISurface interface Windows Movie Maker and DVD Maker , get_Surface method"]
topic_type:
- apiref
api_name:
- ISurface.get_Surface
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- COM
---

# ISurface::get\_Surface method

The **get\_Surface** method retrieves an **IDirect3DSurface9** interface that points to the video surface.

## Syntax


```C++
HRESULT get_Surface(
  [out] IDirect3DSurface9 **ppSurface
);
```



## Parameters

<dl> <dt>

*ppSurface* \[out\]
</dt> <dd>

Pointer to an **IDirect3DSurface9** interface pointer. The transform must release this interface when finished with it.

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

## Requirements



|                                     |                                                                                                                                                                                                                   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                                                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                                                                              |
| Header<br/>                   | <dl> <dt>GPUPipelineTime.h</dt> </dl>                                                                                                                      |
| Library<br/>                  | <dl> <dt>GPUPipelineVC8.lib (Visual Studio 2005); </dt> <dt>GPUPipelineVC7.lib (Visual Studio .NET)</dt> </dl> |



## See also

<dl> <dt>

[**ISurface Interface**](isurface.md)
</dt> </dl>

 

 





