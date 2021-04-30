---
description: The DoSetWindowForeground method brings the window to the foreground.
ms.assetid: 5aace88b-14c0-41ce-95a3-0e255ca56ae6
title: CBaseWindow.DoSetWindowForeground method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseWindow.DoSetWindowForeground
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseWindow.DoSetWindowForeground method

The `DoSetWindowForeground` method brings the window to the foreground.

## Syntax


```C++
void DoSetWindowForeground(
   BOOL bFocus
);
```



## Parameters

<dl> <dt>

*bFocus* 
</dt> <dd>

Boolean value that specifies whether to give the window focus. If the value is **TRUE**, the window gains focus.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




