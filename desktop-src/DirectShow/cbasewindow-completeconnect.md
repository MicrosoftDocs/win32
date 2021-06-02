---
description: The CompleteConnect method notifies the window that the renderer's input pin has been connected.
ms.assetid: 82347ded-eb37-4360-9333-7c837d532115
title: CBaseWindow.CompleteConnect method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseWindow.CompleteConnect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseWindow.CompleteConnect method

The `CompleteConnect` method notifies the window that the renderer's input pin has been connected.

## Syntax


```C++
HRESULT CompleteConnect();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

This method resets the window activation flag ([**CBaseWindow::m\_bActivated**](cbasewindow-m-bactivated.md)) to **FALSE**. When a video renderer completes a pin connection, it might call the [**CBaseWindow::ActivateWindow**](cbasewindow-activatewindow.md) method to set the window's size and position. To force **ActivateWindow** to recalculate these attributes, first call the `CompleteConnect` method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




