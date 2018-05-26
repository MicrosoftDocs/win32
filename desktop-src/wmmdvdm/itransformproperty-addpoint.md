---
title: ITransformProperty AddPoint method
description: The AddPoint method adds a data point to the property.
ms.assetid: 9ed832e0-3ae5-45db-92da-40efadfca303
keywords:
- AddPoint method Windows Movie Maker and DVD Maker
- AddPoint method Windows Movie Maker and DVD Maker , ITransformProperty interface
- ITransformProperty interface Windows Movie Maker and DVD Maker , AddPoint method
topic_type:
- apiref
api_name:
- ITransformProperty.AddPoint
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

# ITransformProperty::AddPoint method

The **AddPoint** method adds a data point to the property.

## Syntax


```C++
HRESULT AddPoint(
  [in]  double                  dblTime,
  [in]  PROPVARIANT             varpropValue,
  [out] ITransformPropertyPoint **ppCreatedPoint
);
```



## Parameters

<dl> <dt>

*dblTime* \[in\]
</dt> <dd>

The time that is associated with this point.

</dd> <dt>

*varpropValue* \[in\]
</dt> <dd>

The value that is associated with this point.

</dd> <dt>

*ppCreatedPoint* \[out\]
</dt> <dd>

Address of a pointer to a copy of the created and added point. The caller must release this interface when it is no longer needed.

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

## Remarks

If a point at the time specified already exists, this method will add a duplicate point with the same time and a new value. Therefore, you should always check first to see if the time point exists, and if so, use [**SetValueAtTime**](itransformproperty-setvalueattime.md) instead.

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

 

 





