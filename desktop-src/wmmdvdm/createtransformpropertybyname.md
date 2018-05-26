---
title: CreateTransformPropertyByName function
description: The CreateTransformPropertyByName function creates a new property object with a name and an initial value.
ms.assetid: 94044361-0ba1-4f5f-a1c6-d382a0c8a1bf
keywords:
- CreateTransformPropertyByName function Windows Movie Maker and DVD Maker
topic_type:
- apiref
api_name:
- CreateTransformPropertyByName
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

# CreateTransformPropertyByName function

The **CreateTransformPropertyByName** function creates a new property object with a name and an initial value.

## Syntax


```C++
HRESULT CreateTransformPropertyByName(
  _In_  LPCTSTR                                             lpszName,
  _In_  LPCTSTR lpszName PROPVARIANT                        var,
  _Out_ LPCTSTR lpszName PROPVARIANT var ITransformProperty **ppProperty
);
```



## Parameters

<dl> <dt>

*lpszName* \[in\]
</dt> <dd>

The name of the new property.

</dd> <dt>

*var* \[in\]
</dt> <dd>

The value of the new property at time zero.

</dd> <dt>

*ppProperty* \[out\]
</dt> <dd>

Address of a pointer to the new property.

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

 

 





