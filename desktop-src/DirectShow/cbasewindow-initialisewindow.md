---
description: The InitialiseWindow method initializes the window.
ms.assetid: 0cf07714-6846-4271-8095-bc4ab865171f
title: CBaseWindow.InitialiseWindow method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseWindow.InitialiseWindow
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseWindow.InitialiseWindow method

The `InitialiseWindow` method initializes the window.

## Syntax


```C++
virtual HRESULT InitialiseWindow(
   HWND hwnd
);
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

Handle to the window.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

By default, this method retrieves a handle to the window's device context (DC) and creates a compatible memory DC. If the value of the [**CBaseWindow::m\_bDoGetDC**](cbasewindow-m-bdogetdc.md) flag is **FALSE**, however, this method does not retrieve the device contexts. The memory DC is useful for selecting bitmaps before blitting them to the window.

The [**CBaseWindow::DoCreateWindow**](cbasewindow-docreatewindow.md) method calls this method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




