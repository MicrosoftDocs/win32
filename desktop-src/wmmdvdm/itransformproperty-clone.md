---
title: ITransformProperty Clone method
description: The Clone method creates a duplicate ITransformProperty interface.
ms.assetid: 3d15da46-49da-4dc8-8d72-62a5f867b31d
keywords:
- Clone method Windows Movie Maker and DVD Maker
- Clone method Windows Movie Maker and DVD Maker , ITransformProperty interface
- ITransformProperty interface Windows Movie Maker and DVD Maker , Clone method
topic_type:
- apiref
api_name:
- ITransformProperty.Clone
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

# ITransformProperty::Clone method

The **Clone** method creates a duplicate **ITransformProperty** interface.

## Syntax


```C++
HRESULT Clone(
  [out] ITransformProperty **ppClonedProperty
);
```



## Parameters

<dl> <dt>

*ppClonedProperty* \[out\]
</dt> <dd>

Address of a pointer to a duplicate of the current property. The caller must release this interface when done with it.

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

 

 





