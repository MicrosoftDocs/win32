---
description: The GetDefaultRect method retrieves the default size of the client area.
ms.assetid: 9eb9e3a4-0d45-4aa3-a496-1b0bd92d4989
title: CBaseWindow.GetDefaultRect method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseWindow.GetDefaultRect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseWindow.GetDefaultRect method

The `GetDefaultRect` method retrieves the default size of the client area.

## Syntax


```C++
virtual RECT GetDefaultRect();
```



## Parameters

This method has no parameters.

## Return value

Returns the default rectangle.

## Remarks

When the window is activated, the object calls this method to determine how large it should make the window's client area. In the base class, this method returns a rectangle whose height and width are the defined constants DEFHEIGHT and DEFWIDTH. A derived class should override this method. For a video renderer, the derived class will typically return the size of the native video image.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




