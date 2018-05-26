---
title: IBufferManager AllocBuffer method
description: The AllocBuffer method allocates a buffer for the transform to use.
ms.assetid: 36146162-4b7a-43bd-803e-c39fcae8ee44
keywords:
- AllocBuffer method Windows Movie Maker and DVD Maker
- AllocBuffer method Windows Movie Maker and DVD Maker , IBufferManager interface
- IBufferManager interface Windows Movie Maker and DVD Maker , AllocBuffer method
topic_type:
- apiref
api_name:
- IBufferManager.AllocBuffer
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

# IBufferManager::AllocBuffer method

The **AllocBuffer** method allocates a buffer for the transform to use.

## Syntax


```C++
HRESULT AllocBuffer(
  [in]  FORMAT_TYPE type,
  [out] IBuffer     **ppBuffer
);
```



## Parameters

<dl> <dt>

*type* \[in\]
</dt> <dd>

One or more [**FORMAT\_TYPE**](format-type.md) values specifying the type of buffer to create.

</dd> <dt>

*ppBuffer* \[out\]
</dt> <dd>

Pointer to a new [**IBuffer**](ibuffer.md) interface pointer to use. The application must release this interface when it is no longer needed.

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

## Remarks

The **AllocBuffer** method should be for temporary use only, because the output buffer is provided to the transform by Windows Movie Maker. Do not cache this buffer between calls to [**IMediaTransform::Process**](imediatransform-process.md), for reasons described in the **Process** method documentation.

## Requirements



|                                     |                                                                                                                                                                                                                   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                                                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                                                                              |
| Header<br/>                   | <dl> <dt>GPUPipelineTime.h</dt> </dl>                                                                                                                      |
| Library<br/>                  | <dl> <dt>GPUPipelineVC8.lib (Visual Studio 2005); </dt> <dt>GPUPipelineVC7.lib (Visual Studio .NET)</dt> </dl> |



## See also

<dl> <dt>

[**IBufferManager Interface**](ibuffermanager.md)
</dt> </dl>

 

 





