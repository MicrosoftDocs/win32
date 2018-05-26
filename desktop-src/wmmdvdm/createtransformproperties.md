---
title: CreateTransformProperties function
description: The CreateTransformProperties function creates a new ITransformProperties property collection object. The resulting collection can have properties added to it by Windows Movie Maker or the transform.
ms.assetid: fc3fe152-29e4-4561-b3c4-2efb8165dfbc
keywords:
- CreateTransformProperties function Windows Movie Maker and DVD Maker
topic_type:
- apiref
api_name:
- CreateTransformProperties
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CreateTransformProperties function

The **CreateTransformProperties** function creates a new [**ITransformProperties**](itransformproperties.md) property collection object. The resulting collection can have properties added to it by Windows Movie Maker or the transform.

## Syntax


```C++
HRESULT CreateTransformProperties(
  _Out_ ITransformProperties **ppPropertyCollection
);
```



## Parameters

<dl> <dt>

*ppPropertyCollection* \[out\]
</dt> <dd>

Address of a pointer to a new property collection object.

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

[**Property Management Helper Functions**](property-management-helper-functions.md)
</dt> </dl>

 

 





