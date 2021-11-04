---
description: The ActivateWindow method sizes the window according to the requirements of the derived class.
ms.assetid: 39e23080-e4ae-46d5-bb3f-306c92bbfe14
title: CBaseWindow.ActivateWindow method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseWindow.ActivateWindow
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseWindow.ActivateWindow method

The `ActivateWindow` method sizes the window according to the requirements of the derived class.

## Syntax


```C++
virtual HRESULT ActivateWindow();
```



## Parameters

This method has no parameters.

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                             | Description                              |
|-----------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | Window was already activated.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                      |



 

## Remarks

This methods calls the [**CBaseWindow::GetDefaultRect**](cbasewindow-getdefaultrect.md) method to determine the window size. The derived class should override **GetDefaultRect** to return the size of the images that will be displayed.

If the window is already active, calling `ActivateWindow` moves the window to the top of the Z order, but does not resize the window. The same is true if the window has a parent.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




