---
title: ITransformPropertyPoint put\_Time method
description: The put\_Time method assigns a time to a property point.
ms.assetid: 'a42f8207-c5c6-4320-a14c-52958579d32c'
keywords: ["put_Time method Windows Movie Maker and DVD Maker", "put_Time method Windows Movie Maker and DVD Maker , ITransformPropertyPoint interface", "ITransformPropertyPoint interface Windows Movie Maker and DVD Maker , put_Time method"]
topic_type:
- apiref
api_name:
- ITransformPropertyPoint.put_Time
api_location:
- GPUPipelineVC8.lib
- GPUPipelineVC8.dll
- GPUPipelineVC7.lib
- GPUPipelineVC7.dll
api_type:
- COM
---

# ITransformPropertyPoint::put\_Time method

The **put\_Time** method assigns a time to a property point.

## Syntax


```C++
HRESULT put_Time(
  [in] double dblTime
);
```



## Parameters

<dl> <dt>

*dblTime* \[in\]
</dt> <dd>

The new time of this property point.

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

 

 





