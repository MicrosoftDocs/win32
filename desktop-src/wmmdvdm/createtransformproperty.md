---
title: CreateTransformProperty function
description: The CreateTransformProperty function creates a new property object. This property has no name or other values assigned to it.
ms.assetid: '81d9c60d-fba2-4fd7-ba72-12ab530f268e'
keywords: ["CreateTransformProperty function Windows Movie Maker and DVD Maker"]
topic_type:
- apiref
api_name:
- CreateTransformProperty
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- LibDef
---

# CreateTransformProperty function

The **CreateTransformProperty** function creates a new property object. This property has no name or other values assigned to it.

## Syntax


```C++
HRESULT CreateTransformProperty(
  _Out_ ITransformProperty **ppProperty
);
```



## Parameters

<dl> <dt>

*ppProperty* \[out\]
</dt> <dd>

Address of a pointer to a new property object. The caller must release this interface when done with it.

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

## Requirements



|                                     |                                                                                                                                                                                                                   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                                                                                                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                                                                              |
| Header<br/>                   | <dl> <dt>GPUPipelineTime.h</dt> </dl>                                                                                                                      |
| Library<br/>                  | <dl> <dt>GPUPipelineVC8.lib (Visual Studio 2005); </dt> <dt>GPUPipelineVC7.lib (Visual Studio .NET)</dt> </dl> |



## See also

<dl> <dt>

[**Property Management Helper Functions**](property-management-helper-functions.md)
</dt> </dl>

 

 





