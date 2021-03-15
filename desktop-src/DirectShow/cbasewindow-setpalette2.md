---
description: The SetPalette method installs a palette for the window.
ms.assetid: 86eb34c6-85ff-4a40-8085-ea55dbc2727e
title: CBaseWindow.SetPalette method (Winutil.h) (2)
ms.topic: reference
ms.date: 05/31/2018
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
---

# CBaseWindow.SetPalette method (Winutil.h)

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



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




