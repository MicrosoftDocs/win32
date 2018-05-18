---
title: GetSurface method
description: The GetSurface method retrieves an IDirect3DSurface9 interface from an IBuffer interface.
ms.assetid: 'a8f58ec3-17ef-452c-a918-2979023a3e1e'
keywords: ["GetSurface method Windows Movie Maker and DVD Maker"]
topic_type:
- apiref
api_name:
- GetSurface
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- COM
---

# GetSurface method

The **GetSurface** method retrieves an **IDirect3DSurface9** interface from an [**IBuffer**](ibuffer.md) interface.

## Syntax


```C++
HRESULT GetSurface(
  [in]  IBuffer           *pBuffer,
  [out] IDirect3DSurface9 **ppSurface
);
```



## Parameters

<dl> <dt>

*pBuffer* \[in\]
</dt> <dd>

Pointer to a buffer object.

</dd> <dt>

*ppSurface* \[out\]
</dt> <dd>

Pointer to a new Direct3D **IDirect3DSurface9** interface pointer to read from or write to. The caller must release this interface when done with it.

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

## Remarks

Your application will call this function on the input and output buffers passed to [**IMediaTransform::Process**](imediatransform-process.md).

## Requirements



|                                     |                                                                                                                                                                                                                   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                                                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                                                                              |
| Header<br/>                   | <dl> <dt>GPUPipelineTime.h</dt> </dl>                                                                                                                      |
| Library<br/>                  | <dl> <dt>GPUPipelineVC8.lib (Visual Studio 2005); </dt> <dt>GPUPipelineVC7.lib (Visual Studio .NET)</dt> </dl> |



## See also

<dl> <dt>

[**Transform Helper Functions**](transform-helper-functions.md)
</dt> </dl>

 

 





