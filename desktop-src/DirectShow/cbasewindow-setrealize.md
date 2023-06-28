---
description: The SetRealize method specifies whether the window realizes palettes.
ms.assetid: ab4a6069-c11f-4126-93bf-6de5277970a1
title: CBaseWindow.SetRealize method (Winutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseWindow.SetRealize
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseWindow.SetRealize method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `SetRealize` method specifies whether the window realizes palettes.

## Syntax


```C++
void SetRealize(
   BOOL bRealize
);
```



## Parameters

<dl> <dt>

*bRealize* 
</dt> <dd>

Boolean value that specifies whether to realize palettes. If **TRUE**, the [**CBaseWindow::SetPalette**](cbasewindow-setpalette.md) method realizes palettes.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

By default, the **SetPalette** method realizes the specified palette. Call this method to change the default behavior, so that palettes are selected but not realized. This method sets the [**CBaseWindow::m\_bNoRealize**](cbasewindow-m-bnorealize.md) member variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




