---
description: The ResetPaletteVersion method resets the palette version. Call this method if the owning filter's pin reconnects.
ms.assetid: c9e5588c-5501-4356-bdec-a339d33f9eb5
title: CDrawImage.ResetPaletteVersion method (Winutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDrawImage.ResetPaletteVersion
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CDrawImage.ResetPaletteVersion method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `ResetPaletteVersion` method resets the palette version. Call this method if the owning filter's pin reconnects.

## Syntax


```C++
void ResetPaletteVersion();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method sets the value of **m\_PaletteVersion** to a predefined constant, **PALETTE\_VERSION**.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDrawImage Class**](cdrawimage.md)
</dt> <dt>

[**CDrawImage::GetPaletteVersion**](cdrawimage-getpaletteversion.md)
</dt> <dt>

[**CDrawImage::IncrementPaletteVersion**](cdrawimage-incrementpaletteversion.md)
</dt> </dl>

 

 




