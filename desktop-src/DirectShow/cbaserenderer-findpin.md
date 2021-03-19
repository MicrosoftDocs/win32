---
description: The FindPin method retrieves the pin with the specified identifier.
ms.assetid: d07a298f-ddb0-44eb-85ca-81735875cdf3
title: CBaseRenderer.FindPin method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.FindPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.FindPin method

The `FindPin` method retrieves the pin with the specified identifier.

## Syntax


```C++
HRESULT FindPin(
   LPCWSTR Id,
   IPin    **ppPin
);
```



## Parameters

<dl> <dt>

*Id* 
</dt> <dd>

Pointer to a constant, null-terminated wide-character string that identifies the pin. Must be L"In".

</dd> <dt>

*ppPin* 
</dt> <dd>

Address of a variable that receives a pointer to the pin's [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface. If the method fails, *\*ppPin* is set to **NULL**.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                                       | Description                           |
|---------------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | Success.<br/>                   |
| <dl> <dt>**E\_POINTER**</dt> </dl>         | **NULL** pointer argument.<br/> |
| <dl> <dt>**VFW\_E\_NOT\_FOUND**</dt> </dl> | Not found.<br/>                 |



 

## Remarks

This method overrides the [**CBaseFilter::FindPin**](cbasefilter-findpin.md) method. The filter's only pin (the input pin) is named "In".

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




