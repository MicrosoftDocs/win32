---
title: ITransformProperty get\_PointCount method
description: The get\_PointCount method retrieves a count of time points in the current property.
ms.assetid: ff72451e-7356-4dcc-8420-3bd673f0fe2f
keywords:
- get_PointCount method Windows Movie Maker and DVD Maker
- get_PointCount method Windows Movie Maker and DVD Maker , ITransformProperty interface
- ITransformProperty interface Windows Movie Maker and DVD Maker , get_PointCount method
topic_type:
- apiref
api_name:
- ITransformProperty.get_PointCount
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

# ITransformProperty::get\_PointCount method

The **get\_PointCount** method retrieves a count of time points in the current property.

## Syntax


```C++
HRESULT get_PointCount(
  [out] long *plCount
);
```



## Parameters

<dl> <dt>

*plCount* \[out\]
</dt> <dd>

Pointer to the count of points in the current property. This can be used with the [**get\_Point**](itransformproperty-get-point.md) method to iterate through all the points in the current property.

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

 

 





