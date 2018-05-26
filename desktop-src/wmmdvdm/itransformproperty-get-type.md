---
title: ITransformProperty get\_Type method
description: The get\_Type method retrieves the data type of the property value, as a VARTYPE.
ms.assetid: f772b645-a77a-4cfe-b2d2-1778b77463c4
keywords:
- get_Type method Windows Movie Maker and DVD Maker
- get_Type method Windows Movie Maker and DVD Maker , ITransformProperty interface
- ITransformProperty interface Windows Movie Maker and DVD Maker , get_Type method
topic_type:
- apiref
api_name:
- ITransformProperty.get_Type
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

# ITransformProperty::get\_Type method

The **get\_Type** method retrieves the data type of the property value, as a **VARTYPE**.

## Syntax


```C++
HRESULT get_Type(
  [out] VARTYPE *pVarType
);
```



## Parameters

<dl> <dt>

*pVarType* \[out\]
</dt> <dd>

Pointer to the data type of the property value.

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

 

 





