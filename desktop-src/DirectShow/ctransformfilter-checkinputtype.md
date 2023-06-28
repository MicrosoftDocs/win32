---
description: The CheckInputType method checks whether a specified media type is acceptable for input.
ms.assetid: 11f156f7-add2-45be-a0d3-05d21f596b89
title: CTransformFilter.CheckInputType method (Transfrm.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformFilter.CheckInputType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CTransformFilter.CheckInputType method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `CheckInputType` method checks whether a specified media type is acceptable for input.

## Syntax


```C++
virtual HRESULT CheckInputType(
   const CMediaType *mtIn
) = 0;
```



## Parameters

<dl> <dt>

*mtIn* 
</dt> <dd>

Pointer to a [**CMediaType**](cmediatype.md) object that specifies the media type.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                                                | Description                              |
|------------------------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | Media type is acceptable.<br/>     |
| <dl> <dt>**VFW\_E\_TYPE\_NOT\_ACCEPTED**</dt> </dl> | Media type is not acceptable.<br/> |



 

## Remarks

The derived class must implement this method. Return S\_OK if the proposed input format is acceptable, or an error code otherwise.

This method does not need to verify that the input format is compatible with the output format (if any). The input pin verifies that by calling the [**CheckTransform**](ctransformfilter-checktransform.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




