---
description: The get\_Visible method retrieves the current window visibility.
ms.assetid: 7e643569-1116-4562-be33-babd12a7e899
title: CBaseControlWindow.get_Visible method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.get_Visible
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlWindow.get\_Visible method

The `get_Visible` method retrieves the current window visibility.

## Syntax


```C++
HRESULT get_Visible(
   long *pVisible
);
```



## Parameters

<dl> <dt>

*pVisible* 
</dt> <dd>

Pointer to an Automation Boolean flag (0 is off,  1 is on).

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function returns  1 if the window has the WS\_VISIBLE style; 0 otherwise.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




