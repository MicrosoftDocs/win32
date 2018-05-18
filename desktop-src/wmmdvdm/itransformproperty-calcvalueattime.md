---
title: ITransformProperty CalcValueAtTime method
description: The CalcValueAtTime method calculates the property value at a particular time, using the evaluation function type that was specified for the property.
ms.assetid: 'aae70f7a-a097-4668-8730-35921aa3d572'
keywords: ["CalcValueAtTime method Windows Movie Maker and DVD Maker", "CalcValueAtTime method Windows Movie Maker and DVD Maker , ITransformProperty interface", "ITransformProperty interface Windows Movie Maker and DVD Maker , CalcValueAtTime method"]
topic_type:
- apiref
api_name:
- ITransformProperty.CalcValueAtTime
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- COM
---

# ITransformProperty::CalcValueAtTime method

The **CalcValueAtTime** method calculates the property value at a particular time, using the evaluation function type that was specified for the property.

## Syntax


```C++
HRESULT CalcValueAtTime(
  [in]  double      dblTime,
  [out] PROPVARIANT *varCalculatedValue
);
```



## Parameters

<dl> <dt>

*dblTime* \[in\]
</dt> <dd>

The time at which to calculate the property value. This should be within the time scale specified in the XML initialization file (typically from 0.0 to 1.0).

</dd> <dt>

*varCalculatedValue* \[out\]
</dt> <dd>

Pointer to the value at the specified time. This value can be either a single value of any acceptable type, or an array of up to 4 **float** elements (type VT\_R4 \| VT\_VECTOR).

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

[**ITransformProperty Interface**](itransformproperty.md)
</dt> </dl>

 

 





