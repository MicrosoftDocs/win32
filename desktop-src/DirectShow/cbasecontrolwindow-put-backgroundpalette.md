---
description: The put\_BackgroundPalette method sets a flag to realize the palette in the background.
ms.assetid: db420e75-e300-41fa-bae4-fb267cc99c7c
title: CBaseControlWindow.put_BackgroundPalette method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.put_BackgroundPalette
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlWindow.put\_BackgroundPalette method

The `put_BackgroundPalette` method sets a flag to realize the palette in the background.

## Syntax


```C++
HRESULT put_BackgroundPalette(
   long BackgroundPalette
);
```



## Parameters

<dl> <dt>

*BackgroundPalette* 
</dt> <dd>

Automation Boolean flag (0 is off,  1 is on).

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

To play a video within another application or document, the application might want to use its own palette. It can ask that the video use the current foreground palette rather than its own as the background palette by setting this flag to  1. If this is set to 0, the window will install and realize its own preferred palette. Asking the window to use a different palette will cause severe performance penalties.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




