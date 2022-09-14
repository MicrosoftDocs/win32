---
description: The PrepareWindow method creates the window.
ms.assetid: c4c0d177-6351-4ecc-b1eb-399b4a94c463
title: CBaseWindow.PrepareWindow method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseWindow.PrepareWindow
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseWindow.PrepareWindow method

The `PrepareWindow` method creates the window.

## Syntax


```C++
virtual HRESULT PrepareWindow();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                            | Description         |
|----------------------------------------------------------------------------------------|---------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl> | Failure.<br/> |



 

## Remarks

Call this method after creating the object. This method performs some initial bookkeeping and then calls the [**CBaseWindow::DoCreateWindow**](cbasewindow-docreatewindow.md) method to create the window.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




