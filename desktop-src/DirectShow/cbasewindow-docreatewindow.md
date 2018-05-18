---
Description: 'The DoCreateWindow method creates the window.'
ms.assetid: 'bbe38a71-bbf7-4380-96a3-074b992a1d1e'
title: 'CBaseWindow.DoCreateWindow method'
---

# CBaseWindow.DoCreateWindow method

The `DoCreateWindow` method creates the window.

## Syntax


```C++
HRESULT DoCreateWindow();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK if successful, or an **HRESULT** value indicating the cause of the failure.

## Remarks

The [**CBaseWindow::PrepareWindow**](cbasewindow-preparewindow.md) method calls this method.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




