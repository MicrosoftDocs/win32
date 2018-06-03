---
title: ITransformPropertyPoint put\_Value method
description: The put\_Value method assigns a value to a property point.
ms.assetid: 04c57726-78f2-4d0e-82da-317a428a1e24
keywords:
- put_Value method Windows Movie Maker and DVD Maker
- put_Value method Windows Movie Maker and DVD Maker , ITransformPropertyPoint interface
- ITransformPropertyPoint interface Windows Movie Maker and DVD Maker , put_Value method
topic_type:
- apiref
api_name:
- ITransformPropertyPoint.put_Value
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

# ITransformPropertyPoint::put\_Value method

The **put\_Value** method assigns a value to a property point.

## Syntax


```C++
HRESULT put_Value(
  [in] PROPVARIANT varpropValue
);
```



## Parameters

<dl> <dt>

*varpropValue* \[in\]
</dt> <dd>

The new value of this property point. This value can be either a single value of any acceptable type, or an array of up to 4 **float** elements (type VT\_R4 \| VT\_VECTOR)

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

[**ITransformPropertyPoint Interface**](itransformpropertypoint.md)
</dt> </dl>

 

 





