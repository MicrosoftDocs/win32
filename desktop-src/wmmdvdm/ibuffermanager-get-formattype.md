---
title: IBufferManager get\_FormatType method
description: The get\_FormatType method retrieves information about the type of buffer that this object can create.
ms.assetid: 7fce2357-6dc4-4c9f-8019-1a420f3563da
keywords:
- get_FormatType method Windows Movie Maker and DVD Maker
- get_FormatType method Windows Movie Maker and DVD Maker , IBufferManager interface
- IBufferManager interface Windows Movie Maker and DVD Maker , get_FormatType method
topic_type:
- apiref
api_name:
- IBufferManager.get_FormatType
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

# IBufferManager::get\_FormatType method

The **get\_FormatType** method retrieves information about the type of buffer that this object can create.

## Syntax


```C++
HRESULT get_FormatType(
  [out] FORMAT_TYPE *pType
);
```



## Parameters

<dl> <dt>

*pType* \[out\]
</dt> <dd>

One or more [**FORMAT\_TYPE**](format-type.md) values that describe what type of buffer this object manages.

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

[**IBufferManager Interface**](ibuffermanager.md)
</dt> </dl>

 

 





