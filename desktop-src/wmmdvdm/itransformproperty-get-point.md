---
title: ITransformProperty get\_Point method
description: The get\_Point method retrieves a point by index.
ms.assetid: 93db9d8a-bf94-44df-87fd-85e0f92f3415
keywords:
- get_Point method Windows Movie Maker and DVD Maker
- get_Point method Windows Movie Maker and DVD Maker , ITransformProperty interface
- ITransformProperty interface Windows Movie Maker and DVD Maker , get_Point method
topic_type:
- apiref
api_name:
- ITransformProperty.get_Point
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

# ITransformProperty::get\_Point method

The **get\_Point** method retrieves a point by index.

## Syntax


```C++
HRESULT get_Point(
  [in]  long                    lIndex,
  [out] ITransformPropertyPoint **ppPoint
);
```



## Parameters

<dl> <dt>

*lIndex* \[in\]
</dt> <dd>

The zero-based index of the point to retrieve.

</dd> <dt>

*ppPoint* \[out\]
</dt> <dd>

Address of a pointer to the retrieved point. The caller must release this interface when it is no longer needed.

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

 

 





