---
Description: The put\_Visible method makes shows or hides the window.
ms.assetid: 77e8d071-f876-4e35-945c-d1daf96ad02b
title: CBaseControlWindow.put\_Visible method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CBaseControlWindow.put\_Visible method

The `put_Visible` method makes shows or hides the window.

## Syntax


```C++
HRESULT put_Visible(
   long Visible
);
```



## Parameters

<dl> <dt>

*Visible* 
</dt> <dd>

Automation Boolean flag (0 means window is hidden,  1 means window is shown).

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

 

 




