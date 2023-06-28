---
description: Constructor method. The constructor obtains access to the specified pin.
ms.assetid: 518d41aa-8361-4769-aa9b-14676b676d6f
title: CAutoUsingOutputPin.CAutoUsingOutputPin constructor (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAutoUsingOutputPin.CAutoUsingOutputPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CAutoUsingOutputPin.CAutoUsingOutputPin constructor

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Constructor method. The constructor obtains access to the specified pin.

## Syntax


```C++
CAutoUsingOutputPin(
   CDynamicOutputPin *pOutputPin,
   HRESULT           *phr
);
```



## Parameters

<dl> <dt>

*pOutputPin* 
</dt> <dd>

Pointer to a [**CDynamicOutputPin**](cdynamicoutputpin.md) object.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to a variable that contains an **HRESULT** value. The value must be S\_OK.

</dd> </dl>

## Remarks

When the method returns, the value of *\*phr* indicates the success or failure of the method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAutoUsingOutputPin Class**](cautousingoutputpin-cautousingoutputpin.md)
</dt> </dl>

 

 




