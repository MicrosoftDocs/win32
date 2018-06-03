---
title: ITransformProperties get\_PropertyByIndex method
description: The get\_PropertyByIndex method retrieves a property in the collection by index.
ms.assetid: 3ef870de-c530-4000-bca9-bbfa7bd913a1
keywords:
- get_PropertyByIndex method Windows Movie Maker and DVD Maker
- get_PropertyByIndex method Windows Movie Maker and DVD Maker , ITransformProperties interface
- ITransformProperties interface Windows Movie Maker and DVD Maker , get_PropertyByIndex method
topic_type:
- apiref
api_name:
- ITransformProperties.get_PropertyByIndex
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

# ITransformProperties::get\_PropertyByIndex method

The **get\_PropertyByIndex** method retrieves a property in the collection by index.

## Syntax


```C++
HRESULT get_PropertyByIndex(
  [in]  long               lIndex,
  [out] ITransformProperty **ppProperty
);
```



## Parameters

<dl> <dt>

*lIndex* \[in\]
</dt> <dd>

A zero-based index to a property in the collection.

</dd> <dt>

*ppProperty* \[out\]
</dt> <dd>

Address of a pointer to the property that was requested. The caller must release this interface when it is no longer needed.

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

## Remarks

You can query the returned property for [**ITransformProperties**](itransformproperties.md) to examine any child properties that it may have.

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

 

 





