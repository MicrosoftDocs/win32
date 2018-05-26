---
title: ITransformProperty get\_Name method
description: The get\_Name method retrieves the name of a property.
ms.assetid: f2be79e6-6de2-4016-8e86-358de2d1c678
keywords:
- get_Name method Windows Movie Maker and DVD Maker
- get_Name method Windows Movie Maker and DVD Maker , ITransformProperty interface
- ITransformProperty interface Windows Movie Maker and DVD Maker , get_Name method
topic_type:
- apiref
api_name:
- ITransformProperty.get_Name
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

# ITransformProperty::get\_Name method

The **get\_Name** method retrieves the name of a property.

## Syntax


```C++
HRESULT get_Name(
  [out]     LPTSTR szBuffer,
  [in, out] long   *plSizeBufferChars
);
```



## Parameters

<dl> <dt>

*szBuffer* \[out\]
</dt> <dd>

A caller-allocated buffer holding the name of the property. To get the size that is required, call this method with this parameter set to **NULL** and the required size will be returned in *plSizeBufferChars*.

</dd> <dt>

*plSizeBufferChars* \[in, out\]
</dt> <dd>

Pointer to the size of the buffer in characters, including the termination character. On input, the size allocated by the caller. On output, the size required (if *szBuffer* is **NULL**) or the size of the returned buffer.

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

[**ITransformProperty Interface**](itransformproperty.md)
</dt> </dl>

 

 





