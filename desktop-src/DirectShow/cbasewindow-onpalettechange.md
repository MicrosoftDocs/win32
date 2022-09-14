---
description: The OnPaletteChange method handles palette-change messages.
ms.assetid: 2abae4f1-fbd0-4a32-8772-012fa96b6d6c
title: CBaseWindow.OnPaletteChange method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseWindow.OnPaletteChange
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseWindow.OnPaletteChange method

The `OnPaletteChange` method handles palette-change messages.

## Syntax


```C++
virtual LRESULT OnPaletteChange(
   HWND hwnd,
   UINT Message
);
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

Handle to the window.

</dd> <dt>

*Message* 
</dt> <dd>

Message identifier.

</dd> </dl>

## Return value

Returns 0 if the message was processed, or 1 if the message was not processed.

## Remarks

This method handles WM\_PALETTECHANGED and WM\_QUERYNEWPALETTE messages. It calls the [**CBaseWindow::DoRealisePalette**](cbasewindow-dorealisepalette.md) method to realize the new palette.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




