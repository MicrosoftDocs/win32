---
description: The DoSetWindowStyle method changes the typical or extended window styles.
ms.assetid: 4a9a97fb-b527-44ce-af8c-e5ea832ed4c4
title: CBaseControlWindow.DoSetWindowStyle method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.DoSetWindowStyle
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlWindow.DoSetWindowStyle method

The `DoSetWindowStyle` method changes the typical or extended window styles.

## Syntax


```C++
HRESULT DoSetWindowStyle(
   long Style,
   long WindowLong
);
```



## Parameters

<dl> <dt>

*Style* 
</dt> <dd>

Appropriate window styles.

</dd> <dt>

*WindowLong* 
</dt> <dd>

Value specifying which styles to set. Must be one of the following:



| Label | Value |
|--------------|--------------------------------------|
| GWL\_STYLE   | Retrieve the window styles.          |
| GWL\_EXSTYLE | Retrieve the extended window styles. |



 

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function calls the Win32 **SetWindowLong** function to set the window style, and then redisplays the window in the current position. This member function is called by the [**CBaseControlWindow::put\_WindowStyle**](cbasecontrolwindow-put-windowstyle.md) and [**CBaseControlWindow::put\_WindowStyleEx**](cbasecontrolwindow-put-windowstyleex.md) member functions.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




