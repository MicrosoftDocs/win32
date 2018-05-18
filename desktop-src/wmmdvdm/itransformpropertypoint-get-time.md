---
title: ITransformPropertyPoint get\_Time method
description: The get\_Time method retrieves the time associated with this property point.
ms.assetid: '32e2da35-8ffd-4c15-9849-76e155cf90d2'
keywords: ["get_Time method Windows Movie Maker and DVD Maker", "get_Time method Windows Movie Maker and DVD Maker , ITransformPropertyPoint interface", "ITransformPropertyPoint interface Windows Movie Maker and DVD Maker , get_Time method"]
topic_type:
- apiref
api_name:
- ITransformPropertyPoint.get_Time
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- COM
---

# ITransformPropertyPoint::get\_Time method

The **get\_Time** method retrieves the time associated with this property point.

## Syntax


```C++
HRESULT get_Time(
  [out] double *pdblTime
);
```



## Parameters

<dl> <dt>

*pdblTime* \[out\]
</dt> <dd>

Pointer to the time associated with this property point.

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

[**ITransformPropertyPoint Interface**](itransformpropertypoint.md)
</dt> </dl>

 

 





