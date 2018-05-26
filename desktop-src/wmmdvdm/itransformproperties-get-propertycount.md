---
title: ITransformProperties get\_PropertyCount method
description: The get\_PropertyCount method retrieves a count of properties in the collection.
ms.assetid: 9f63296b-1e3d-4d9a-8f2c-c15bc879831e
keywords:
- get_PropertyCount method Windows Movie Maker and DVD Maker
- get_PropertyCount method Windows Movie Maker and DVD Maker , ITransformProperties interface
- ITransformProperties interface Windows Movie Maker and DVD Maker , get_PropertyCount method
topic_type:
- apiref
api_name:
- ITransformProperties.get_PropertyCount
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

# ITransformProperties::get\_PropertyCount method

The **get\_PropertyCount** method retrieves a count of properties in the collection.

## Syntax


```C++
HRESULT get_PropertyCount(
  [in] long *plCount
);
```



## Parameters

<dl> <dt>

*plCount* \[in\]
</dt> <dd>

Pointer to the number of properties in the collection.

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

[**ITransformProperties Interface**](itransformproperties.md)
</dt> </dl>

 

 





