---
description: The SetPalette method installs a palette for the window. This method has no parameters.
ms.assetid: 86eb34c6-85ff-4a40-8085-ea55dbc2727e
title: CBaseWindow.SetPalette method (Winutil.h) - No parameters
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseWindow.SetPalette
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseWindow.SetPalette method (Winutil.h) - No parameters

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `SetPalette` method installs a palette for the window.

## Syntax


```C++
HRESULT SetPalette();
```



## Parameters

This method has no parameters.

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                             | Description                                                    |
|-----------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | An internal call to **GdiFlush** returned an error.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                                            |



 

## Remarks

The palette given by the [**CBaseWindow::m\_hPalette**](cbasewindow-m-hpalette.md) member variable is selected. The caller must ensure the validity of **m\_hPalette**.

If the value of the [**CBaseWindow::m\_bNoRealize**](cbasewindow-m-bnorealize.md) member variable is **FALSE** (the default), this method selects the palette and realizes it. Otherwise, it selects the palette but does not realize it. The object does not delete any previous palette that it was using. The caller is responsible for deleting palettes.

Any thread can safely call this method, not just the thread that owns the window. The window sends a private message to itself, which triggers a call to the [**CBaseWindow::OnPaletteChange**](cbasewindow-onpalettechange.md) method.

## Requirements

| Requirement | Value |
|-|-|
| Header | Winutil.h (include Streams.h) |
| Library| Strmbase.lib (retail builds); Strmbasd.lib (debug builds) |

## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




