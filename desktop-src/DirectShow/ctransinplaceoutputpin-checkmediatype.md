---
description: CTransInPlaceOutputPin.CheckMediaType method - The CheckMediaType method determines if the pin accepts a specific media type.
ms.assetid: be720021-ef7b-4281-a9f4-93abbdafc75d
title: CTransInPlaceOutputPin.CheckMediaType method (Transip.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransInPlaceOutputPin.CheckMediaType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CTransInPlaceOutputPin.CheckMediaType method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `CheckMediaType` method determines if the pin accepts a specific media type.

## Syntax


```C++
HRESULT CheckMediaType(
   const CMediaType *pmt
);
```



## Parameters

<dl> <dt>

*pmt* 
</dt> <dd>

Pointer to a [**CMediaType**](cmediatype.md) object that contains the proposed media type.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                                                | Description                         |
|------------------------------------------------------------------------------------------------------------|-------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | Success.<br/>                 |
| <dl> <dt>**VFW\_E\_TYPE\_NOT\_ACCEPTED**</dt> </dl> | Media type not accepted.<br/> |



 

## Remarks

This method overrides the [**CTransformOutputPin::CheckMediaType**](ctransformoutputpin-checkmediatype.md) method.

If the filter is already streaming and is using two allocators, this method rejects any format changes. Otherwise, this method calls the filter's [**CTransformFilter::CheckInputType**](ctransformfilter-checkinputtype.md) method to check the media type. If the input pin is connected, it also calls the [**IPin::QueryAccept**](/windows/desktop/api/Strmif/nf-strmif-ipin-queryaccept) method on the upstream output pin.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceOutputPin Class**](ctransinplaceoutputpin.md)
</dt> </dl>

 

 




