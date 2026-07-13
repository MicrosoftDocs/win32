---
description: CBasePin.BreakConnect method - The BreakConnect method releases the pin from a connection.
ms.assetid: a1f299e1-30bf-4d55-84cf-73acccf38151
title: CBasePin.BreakConnect method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.BreakConnect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBasePin.BreakConnect method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `BreakConnect` method releases the pin from a connection.

## Syntax


```C++
virtual HRESULT BreakConnect();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

This method is called during pin disconnection by the [**CBasePin::Disconnect**](cbasepin-disconnect.md) method. It is also called during a connection attempt if the [**CBasePin::CheckConnect**](cbasepin-checkconnect.md) method fails.

This method must free any resources that were obtained by the **CheckConnect** method. For example, if **CheckConnect** allocates memory, `BreakConnect` should free the memory. If **CheckConnect** queries the connecting pin for an interface, `BreakConnect` should free the interface.

Note that `BreakConnect` can be called without a corresponding call to **CompleteConnect**. Therefore, you cannot assume that **CompleteConnect** has been called previously.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




