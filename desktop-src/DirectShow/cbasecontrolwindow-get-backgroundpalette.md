---
description: The get\_BackgroundPalette method retrieves the realized palette in the background flag.
ms.assetid: cc649dbd-d049-4993-b187-4e297bef5152
title: CBaseControlWindow.get_BackgroundPalette method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.get_BackgroundPalette
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlWindow.get\_BackgroundPalette method

The `get_BackgroundPalette` method retrieves the realized palette in the background flag.

## Syntax


```C++
HRESULT get_BackgroundPalette(
   long *pBackgroundPalette
);
```



## Parameters

<dl> <dt>

*pBackgroundPalette* 
</dt> <dd>

Pointer to an Automation Boolean flag (0 is off,  1 is on).

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function implements the [**IVideoWindow::get\_BackgroundPalette**](/windows/desktop/api/Control/nf-control-ivideowindow-get_backgroundpalette) method. If a video will be played within another application or document, the application might want to use its own palette. It can ask that the video use the current foreground palette rather than its own by setting this flag to  1. If this is set to 0, the window will install and realize its own preferred palette. Note that asking the window to use a different palette will cause severe performance penalties.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




