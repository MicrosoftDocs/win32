---
Description: The SetWindowPosition method sets the window position on the desktop.
ms.assetid: 1c2706dd-d67c-41c7-b672-3c040f37bc41
title: CBaseControlWindow.SetWindowPosition method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CBaseControlWindow.SetWindowPosition method

The `SetWindowPosition` method sets the window position on the desktop.

## Syntax


```C++
HRESULT SetWindowPosition(
   long Left,
   long Top,
   long Width,
   long Height
);
```



## Parameters

<dl> <dt>

*Left* 
</dt> <dd>

New left coordinate.

</dd> <dt>

*Top* 
</dt> <dd>

New top coordinate.

</dd> <dt>

*Width* 
</dt> <dd>

Width of the window.

</dd> <dt>

*Height* 
</dt> <dd>

Height of the window.

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

 

 




