---
description: The OnDisplayChange method posts an EC\_DISPLAY\_CHANGED event to the filter graph manager.
ms.assetid: e4cdcdf2-7fc2-4893-9897-97bcf2c12610
title: CBaseRenderer.OnDisplayChange method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.OnDisplayChange
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.OnDisplayChange method

The `OnDisplayChange` method posts an [**EC\_DISPLAY\_CHANGED**](ec-display-changed.md) event to the filter graph manager.

## Syntax


```C++
BOOL OnDisplayChange();
```



## Parameters

This method has no parameters.

## Return value

Returns **TRUE** if the event was posted, or **FALSE** otherwise.

## Remarks

Video renderers should call this method in response to WM\_DISPLAYCHANGE messages. If the input pin is connected, the method sends an EC\_DISPLAY\_CHANGED event to the filter graph manager.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




