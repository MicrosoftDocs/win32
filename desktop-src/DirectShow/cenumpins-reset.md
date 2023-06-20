---
description: The Reset method resets the enumeration sequence to the beginning. This method implements the IEnumPins::Reset method.
ms.assetid: b2e86304-bb14-495b-a922-8868b3898d85
title: CEnumPins.Reset method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CEnumPins.Reset
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CEnumPins.Reset method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `Reset` method resets the enumeration sequence to the beginning. This method implements the [**IEnumPins::Reset**](/windows/desktop/api/Strmif/nf-strmif-ienumpins-reset) method.

## Syntax


```C++
HRESULT Reset();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CEnumPins Class**](cenumpins.md)
</dt> </dl>

 

 




