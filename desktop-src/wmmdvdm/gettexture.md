---
title: GetTexture method
description: The GetTexture method retrieves an IDirect3DTexture9 interface from an IBuffer interface.
ms.assetid: f56a6e7a-9a65-4020-9ec4-dd363799b856
keywords:
- GetTexture method Windows Movie Maker and DVD Maker
topic_type:
- apiref
api_name:
- GetTexture
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

# GetTexture method

The **GetTexture** method retrieves an **IDirect3DTexture9** interface from an [**IBuffer**](ibuffer.md) interface.

## Syntax


```C++
HRESULT GetTexture(
  [in]  IBuffer           *pBuffer,
  [out] IDirect3DTexture9 **ppTexture
);
```



## Parameters

<dl> <dt>

*pBuffer* \[in\]
</dt> <dd>

Pointer to an **IBuffer** interface.

</dd> <dt>

*ppTexture* \[out\]
</dt> <dd>

Pointer to a new Direct3D **IDirect3DTexture9** interface pointer to read from or write to. The caller must release this interface when done with it.

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

## Remarks

Your application will call this function on the input and output buffers passed to [**IMediaTransform::Process**](imediatransform-process.md).

## Requirements



|                                     |                                                                                                                                                                                                                   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                                                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                                                                              |
| Header<br/>                   | <dl> <dt>GPUPipelineTime.h</dt> </dl>                                                                                                                      |
| Library<br/>                  | <dl> <dt>GPUPipelineVC8.lib (Visual Studio 2005); </dt> <dt>GPUPipelineVC7.lib (Visual Studio .NET)</dt> </dl> |



## See also

<dl> <dt>

[**Transform Helper Functions**](transform-helper-functions.md)
</dt> </dl>

 

 





