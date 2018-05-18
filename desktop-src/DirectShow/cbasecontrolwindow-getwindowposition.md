---
Description: 'The GetWindowPosition method retrieves the current coordinates for the window.'
ms.assetid: 'a2f46a87-b2cd-450f-8d2b-0f8695432fda'
title: 'CBaseControlWindow.GetWindowPosition method'
---

# CBaseControlWindow.GetWindowPosition method

The `GetWindowPosition` method retrieves the current coordinates for the window.

## Syntax


```C++
HRESULT GetWindowPosition(
   long *pLeft,
   long *pTop,
   long *pWidth,
   long *pHeight
);
```



## Parameters

<dl> <dt>

*pLeft* 
</dt> <dd>

Pointer to the left coordinate, in screen coordinates.

</dd> <dt>

*pTop* 
</dt> <dd>

Pointer to the top coordinate, in screen coordinates.

</dd> <dt>

*pWidth* 
</dt> <dd>

Pointer to the window width, in screen coordinates.

</dd> <dt>

*pHeight* 
</dt> <dd>

Pointer to the window height, in screen coordinates.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




