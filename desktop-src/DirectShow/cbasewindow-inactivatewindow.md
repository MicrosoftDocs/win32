---
description: The InactivateWindow method inactivates the window. In the base class, this method hides the window.
ms.assetid: b575d4fd-dee1-4ae5-abb4-e92ae361e82a
title: CBaseWindow.InactivateWindow method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseWindow.InactivateWindow
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseWindow.InactivateWindow method

The `InactivateWindow` method inactivates the window. In the base class, this method hides the window.

## Syntax


```C++
virtual HRESULT InactivateWindow();
```



## Parameters

This method has no parameters.

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                             | Description                            |
|-----------------------------------------------------------------------------------------|----------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                    |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Window is already inactive.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




