---
description: CTransformOutputPin.CompleteConnect method - The CompleteConnect method completes a connection to another pin.
ms.assetid: 14bc48bc-ddfb-4491-8d5b-9e5ac601ba04
title: CTransformOutputPin.CompleteConnect method (Transfrm.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformOutputPin.CompleteConnect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CTransformOutputPin.CompleteConnect method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `CompleteConnect` method completes a connection to another pin.

## Syntax


```C++
HRESULT CompleteConnect(
   IPin *pReceivePin
);
```



## Parameters

<dl> <dt>

*pReceivePin* 
</dt> <dd>

Pointer to the other pin's [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface.

</dd> </dl>

## Return value

Returns S\_OK or another **HRESULT** value.

## Remarks

This method overrides the [**CBaseOutputPin::CompleteConnect**](cbaseoutputpin-completeconnect.md) method. It calls the filter's [**CTransformFilter::CompleteConnect**](ctransformfilter-completeconnect.md) method, which returns S\_OK in the base class. The derived class can override the **CTransformFilter::CompleteConnect** method to perform additional checks.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




