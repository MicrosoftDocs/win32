---
description: The DoRealisePalette method realizes the window's current palette.
ms.assetid: dd023c81-0cd0-48c6-bc63-5891f2a4acf7
title: CBaseWindow.DoRealisePalette method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseWindow.DoRealisePalette
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseWindow.DoRealisePalette method

The `DoRealisePalette` method realizes the window's current palette.

## Syntax


```C++
virtual HRESULT DoRealisePalette(
   BOOL bForceBackground
);
```



## Parameters

<dl> <dt>

*bForceBackground* 
</dt> <dd>

Boolean value that specifies whether the palette is forced to be a background palette. For more information, see **SelectPalette** in the Platform SDK.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                             | Description                                                    |
|-----------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | An internal call to **GdiFlush** returned an error.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                                            |



 

## Remarks

The [**CBaseWindow::OnPaletteChange**](cbasewindow-onpalettechange.md) method calls this method. To set a new palette, call the [**CBaseWindow::SetPalette**](cbasewindow-setpalette.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




