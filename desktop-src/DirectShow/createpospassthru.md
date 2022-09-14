---
description: The CreatePosPassThru function creates a CPosPassThru object or CRendererPosPassThru object.
ms.assetid: d6fccfb4-b256-40aa-b927-84c7a886f631
title: CreatePosPassThru function (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CreatePosPassThru
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CreatePosPassThru function

The `CreatePosPassThru` function creates a [**CPosPassThru**](cpospassthru.md) object or [**CRendererPosPassThru**](crendererpospassthru.md) object.

## Syntax


```C++
STDAPI CreatePosPassThru(
   LPUNKNOWN pAgg,
   BOOL      bRenderer,
   IPin      *pPin,
   IUnknown  **ppPassThru
);
```



## Parameters

<dl> <dt>

*pAgg* 
</dt> <dd>

Pointer to the owner of this object. If the object is aggregated, pass a pointer to the aggregating object's **IUnknown** interface. Otherwise, set this parameter to **NULL**.

</dd> <dt>

*bRenderer* 
</dt> <dd>

Boolean value that specifies whether the filter is a renderer. Use the value **TRUE** if the filter is a renderer, or **FALSE** otherwise. If the value is **TRUE**, this method creates an instance of the [**CRendererPosPassThru**](crendererpospassthru.md) class. If the value is **FALSE**, the method creates an instance of the **CPosPassThru** class.

</dd> <dt>

*pPin* 
</dt> <dd>

Pointer to the [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface on the filter's input pin.

</dd> <dt>

*ppPassThru* 
</dt> <dd>

Address of a variable that receives a pointer to the object's **IUnknown** interface.

</dd> </dl>

## Return value

Returns S\_OK if successful. Otherwise, returns an **HRESULT** value indicating the cause of the error.

## Remarks

This method uses the [**ISeekingPassThru**](/windows/desktop/api/Strmif/nn-strmif-iseekingpassthru) interface to create the object. The object is loaded dynamically from Quartz.dll.

If the function succeeds, the returned **IUnknown** interface has an outstanding reference count. The caller must release the interface.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPosPassThru Class**](cpospassthru.md)
</dt> </dl>

 

 




