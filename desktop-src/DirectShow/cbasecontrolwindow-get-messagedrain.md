---
Description: The get\_MessageDrain method retrieves the current message drain.
ms.assetid: d679e7f7-4628-479b-b722-843cdd91ffe6
title: CBaseControlWindow.get\_MessageDrain method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseControlWindow.get\_MessageDrain method

The `get_MessageDrain` method retrieves the current message drain.

## Syntax


```C++
HRESULT get_MessageDrain(
   OAHWND *Drain
);
```



## Parameters

<dl> <dt>

*Drain* 
</dt> <dd>

Pointer to the current window receiving window messages.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

Messages sent to the video renderer filter can be posted to another window. The window registered to receive these messages (using the **CBaseControlWindow::get\_MessageDrain** member function) is the current message drain.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




