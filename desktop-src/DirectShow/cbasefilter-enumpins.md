---
description: The EnumPins method enumerates the pins on this filter. This method implements the IBaseFilter::EnumPins method.
ms.assetid: c1015ed3-658f-4f96-a1fb-e04b81a9ddb5
title: CBaseFilter.EnumPins method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseFilter.EnumPins
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseFilter.EnumPins method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `EnumPins` method enumerates the pins on this filter. This method implements the [**IBaseFilter::EnumPins**](/windows/desktop/api/Strmif/nf-strmif-ibasefilter-enumpins) method.

## Syntax


```C++
HRESULT EnumPins(
   IEnumPins **ppEnum
);
```



## Parameters

<dl> <dt>

*ppEnum* 
</dt> <dd>

Address of a variable that receives a pointer to the [**IEnumPins**](/windows/desktop/api/Strmif/nn-strmif-ienumpins) interface.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values.



| Return code                                                                                   | Description                          |
|-----------------------------------------------------------------------------------------------|--------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Success<br/>                   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory<br/>       |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | **NULL** pointer argument<br/> |



 

## Remarks

This method creates an instance of the [**CEnumPins**](cenumpins.md) base class, and returns a pointer to that object, of type **IEnumPins**. The **CEnumPins** class calls the filter's [**CBaseFilter::GetPin**](cbasefilter-getpin.md) method to enumerate the pins on the filter.

If this method succeeds, the **IEnumPins** interface has an outstanding reference count. The caller must release the interface.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




