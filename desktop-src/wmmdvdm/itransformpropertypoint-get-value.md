---
title: ITransformPropertyPoint get\_Value method
description: The get\_Value method retrieves the value associated with a property point.
ms.assetid: 'a5ef7a93-75ae-4694-b151-865d5b2e0fce'
keywords: ["get_Value method Windows Movie Maker and DVD Maker", "get_Value method Windows Movie Maker and DVD Maker , ITransformPropertyPoint interface", "ITransformPropertyPoint interface Windows Movie Maker and DVD Maker , get_Value method"]
topic_type:
- apiref
api_name:
- ITransformPropertyPoint.get_Value
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- COM
---

# ITransformPropertyPoint::get\_Value method

The **get\_Value** method retrieves the value associated with a property point.

## Syntax


```C++
HRESULT get_Value(
  [in, out] PROPVARIANT *pvarpropValue
);
```



## Parameters

<dl> <dt>

*pvarpropValue* \[in, out\]
</dt> <dd>

Pointer to the value associated with this property point. This value can be either a single value of any acceptable type, or an array of up to 4 **float** elements (type VT\_R4 \| VT\_VECTOR)

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

 

 





