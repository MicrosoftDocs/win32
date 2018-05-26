---
Description: The SetMediaType method is called when the media type is set on one of the filters pins.
ms.assetid: 3e505036-7fa6-42cf-a683-3a39a43d209d
title: CTransformFilter.SetMediaType method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CTransformFilter.SetMediaType method

The `SetMediaType` method is called when the media type is set on one of the filter's pins.

## Syntax


```C++
virtual HRESULT SetMediaType(
         PIN_DIRECTION direction,
   const CMediaType    *pmt
);
```



## Parameters

<dl> <dt>

*direction* 
</dt> <dd>

Member of the [**PIN\_DIRECTION**](/windows/win32/strmif/ne-strmif-_pindirection?branch=master) enumerated type, specifying a pin on the filter (input or output).

</dd> <dt>

*pmt* 
</dt> <dd>

Pointer to a [**CMediaType**](cmediatype.md) object that specifies the media type.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

The [**CTransformInputPin::SetMediaType**](ctransforminputpin-setmediatype.md) and [**CTransformOutputPin::SetMediaType**](ctransformoutputpin-setmediatype.md) methods call this method when a pin's media type is set. This method does nothing in the base class, but the derived class can override it.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




