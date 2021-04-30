---
description: The SetPalette method installs a palette for the window.
ms.assetid: 64fa0d3a-c2eb-4e58-8b8d-c8e5ec3bb479
title: CBaseWindow.SetPalette method (Winutil.h)
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
virtual HRESULT SetPalette(
   HPALETTE hPalette
);
```



## Parameters

<dl> <dt>

*hPalette* 
</dt> <dd>

Handle to the new palette. Cannot be **NULL**.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                             | Description                                                    |
|-----------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | An internal call to **GdiFlush** returned an error.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                                            |



 

## Remarks

If the value of the [**CBaseWindow::m\_bNoRealize**](cbasewindow-m-bnorealize.md) member variable is **FALSE** (the default), this method selects the palette and realizes it. Otherwise, it selects the palette but does not realize it. The object does not delete any previous palette that it was using. The caller is responsible for deleting palettes.

Any thread can safely call this method, not just the thread that owns the window. The window sends a private message to itself, which triggers a call to the [**CBaseWindow::OnPaletteChange**](cbasewindow-onpalettechange.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




