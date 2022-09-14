---
description: The get\_Caption method retrieves the current window caption.
ms.assetid: 51ce9cf8-0b2a-4459-b005-02dc45444fd8
title: CBaseControlWindow.get_Caption method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlWindow.get_Caption
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlWindow.get\_Caption method

The `get_Caption` method retrieves the current window caption.

## Syntax


```C++
HRESULT get_Caption(
   BSTR *pstrCaption
);
```



## Parameters

<dl> <dt>

*pstrCaption* 
</dt> <dd>

Pointer to the current window caption.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

Most top-level windows on a Windows-based desktop have a title (caption) associated with them. This property can be queried and set through the [**IVideoWindow**](/windows/desktop/api/Control/nn-control-ivideowindow) interface. Any caption set will be visible only if the window has the WS\_CAPTION style applied. If it does not, the caption can still be set (and retrieved), although it will not be visible to the user.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlWindow Class**](cbasecontrolwindow.md)
</dt> </dl>

 

 




