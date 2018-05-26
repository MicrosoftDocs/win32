---
Description: The GetReader method returns a pointer to the output pins IAsyncReader interface.
ms.assetid: bb7ed3f2-a5bc-496c-8a52-f9915a75105e
title: CPullPin.GetReader method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CPullPin.GetReader method

The `GetReader` method returns a pointer to the output pin's [**IAsyncReader**](/windows/win32/Strmif/nn-strmif-iasyncreader?branch=master) interface.

## Syntax


```C++
IAsyncReader* GetReader();
```



## Parameters

This method has no parameters.

## Return value

Returns a pointer to the [**IAsyncReader**](/windows/win32/Strmif/nn-strmif-iasyncreader?branch=master) interface.

## Remarks

The returned interface has an outstanding reference count. The caller must release the interface.

The method does not check the value of the interface pointer before calling **AddRef**, so do not call this until you have successfully called the [**CPullPin::Connect**](cpullpin-connect.md) method. Otherwise, the interface pointer might be **NULL** and calling **AddRef** will throw an exception.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pullpin.h</dt> </dl>                                                                                                       |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPullPin Class**](cpullpin.md)
</dt> </dl>

 

 




