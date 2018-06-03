---
title: IBuffer get\_Flags method
description: The get\_Flags method retrieves information about the buffer.
ms.assetid: 275c33ed-4b63-43b4-928b-9769dbf6ef0d
keywords:
- get_Flags method Windows Movie Maker and DVD Maker
- get_Flags method Windows Movie Maker and DVD Maker , IBuffer interface
- IBuffer interface Windows Movie Maker and DVD Maker , get_Flags method
topic_type:
- apiref
api_name:
- IBuffer.get_Flags
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

# IBuffer::get\_Flags method

The **get\_Flags** method retrieves information about the buffer.

## Syntax


```C++
HRESULT get_Flags(
  [out] FORMAT_TYPE *pdwFlags
);
```



## Parameters

<dl> <dt>

*pdwFlags* \[out\]
</dt> <dd>

Pointer to one or more [**FORMAT\_TYPE**](format-type.md) values that describe the buffer.

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

 

 





