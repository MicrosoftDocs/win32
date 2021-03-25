---
description: The DoGetWindowStyle method retrieves the current normal or extended window styles.
ms.assetid: 1a854896-4bcb-49d0-92e4-40d1923712f9
title: CBaseControlWindow.DoGetWindowStyle method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.DoGetWindowStyle
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlWindow.DoGetWindowStyle method

The `DoGetWindowStyle` method retrieves the current normal or extended window styles.

## Syntax


```C++
HRESULT DoGetWindowStyle(
   long *pStyle,
   long WindowLong
);
```



## Parameters

<dl> <dt>

*pStyle* 
</dt> <dd>

Pointer to a variable that receives the style information.

</dd> <dt>

*WindowLong* 
</dt> <dd>

Value specifying which styles to retrieve. Must be one of the following:



|              |                                      |
|--------------|--------------------------------------|
| GWL\_STYLE   | Retrieve the window styles.          |
| GWL\_EXSTYLE | Retrieve the extended window styles. |



 

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function calls the Win32 **GetWindowLong** function to retrieve the window style. It is called by the [**CBaseControlWindow::get\_WindowStyle**](cbasecontrolwindow-get-windowstyle.md) and [**CBaseControlWindow::get\_WindowStyleEx**](cbasecontrolwindow-get-windowstyleex.md) member functions.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




