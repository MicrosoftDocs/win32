---
title: IBuffer CopyTo method
description: The CopyTo method copies a buffer to another buffer.
ms.assetid: 0ad10cb7-f09e-4e8a-95ff-f16b4c2e5447
keywords:
- CopyTo method Windows Movie Maker and DVD Maker
- CopyTo method Windows Movie Maker and DVD Maker , IBuffer interface
- IBuffer interface Windows Movie Maker and DVD Maker , CopyTo method
topic_type:
- apiref
api_name:
- IBuffer.CopyTo
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

# IBuffer::CopyTo method

The **CopyTo** method copies a buffer to another buffer.

## Syntax


```C++
HRESULT CopyTo(
  [in] IBuffer *pBuffer
);
```



## Parameters

<dl> <dt>

*pBuffer* \[in\]
</dt> <dd>

Pointer to the destination buffer.

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

[**IBuffer Interface**](ibuffer.md)
</dt> </dl>

 

 





