---
title: ITransformProperty SetValueAtTime method
description: The SetValueAtTime method specifies a property value at a particular time.
ms.assetid: 'ae142ce1-bfe5-48cd-8cab-c04968cfda4c'
keywords: ["SetValueAtTime method Windows Movie Maker and DVD Maker", "SetValueAtTime method Windows Movie Maker and DVD Maker , ITransformProperty interface", "ITransformProperty interface Windows Movie Maker and DVD Maker , SetValueAtTime method"]
topic_type:
- apiref
api_name:
- ITransformProperty.SetValueAtTime
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- COM
---

# ITransformProperty::SetValueAtTime method

The **SetValueAtTime** method specifies a property value at a particular time.

## Syntax


```C++
HRESULT SetValueAtTime(
  [in] double      dblTime,
  [in] PROPVARIANT varValue
);
```



## Parameters

<dl> <dt>

*dblTime* \[in\]
</dt> <dd>

The time to associate with the submitted value. This is typically a value from 0.0 to 1.0.

</dd> <dt>

*varValue* \[in\]
</dt> <dd>

The value at the specified time. This value can be either a single value of any acceptable type, or an array of up to 4 **float** elements (type VT\_R4 \| VT\_VECTOR).

</dd> </dl>

## Return value

The method returns an **HRESULT** of S\_OK for success, or a standard COM error code for failure.

## Remarks

If no point exists at the specified time, this method will create a new point at the specified time. If a point already exists, this method overwrites the existing value at that time.

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

 

 





