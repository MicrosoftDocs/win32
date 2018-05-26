---
Description: The HideCursor method hides or displays the cursor.
ms.assetid: 80175d1b-9874-4295-9ebc-b0d78961a263
title: CBaseControlWindow.HideCursor method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseControlWindow.HideCursor method

The `HideCursor` method hides or displays the cursor.

## Syntax


```C++
HRESULT HideCursor(
   long HideCursor
);
```



## Parameters

<dl> <dt>

*HideCursor* 
</dt> <dd>

Value specifying whether to show the cursor. Set to OATRUE to hide the cursor, or OAFALSE to display the cursor.

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

 

 




