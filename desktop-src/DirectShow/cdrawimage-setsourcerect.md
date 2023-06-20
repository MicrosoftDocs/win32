---
description: The SetSourceRect method sets the source rectangle.
ms.assetid: 982636fe-73ea-4f13-9f2b-7ae8df839ab1
title: CDrawImage.SetSourceRect method (Winutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDrawImage.SetSourceRect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CDrawImage.SetSourceRect method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `SetSourceRect` method sets the source rectangle.

## Syntax


```C++
void SetSourceRect(
   RECT *pSourceRect
);
```



## Parameters

<dl> <dt>

*pSourceRect* 
</dt> <dd>

Pointer to a **RECT** structure that defines the new source rectangle.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The owning filter should call this method if the source rectangle changes; for example, in response to an [**IBasicVideo::SetSourcePosition**](/windows/desktop/api/Control/nf-control-ibasicvideo-setsourceposition) call.

Validate the rectangle given in *pSourceRect* before calling this method, to make sure it does not extend beyond the native video size.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDrawImage Class**](cdrawimage.md)
</dt> </dl>

 

 




