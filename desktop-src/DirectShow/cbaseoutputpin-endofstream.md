---
Description: The EndOfStream method notifies the pin that no additional data is expected. This method implements the IPinEndOfStream method.
ms.assetid: 5c3b5f90-4194-4d65-9f1a-55edf327e3b3
title: CBaseOutputPin.EndOfStream method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseOutputPin.EndOfStream method

The `EndOfStream` method notifies the pin that no additional data is expected. This method implements the [**IPin::EndOfStream**](/windows/win32/Strmif/nf-strmif-ipin-endofstream?branch=master) method.

## Syntax


```C++
HRESULT EndOfStream();
```



## Parameters

This method has no parameters.

## Return value

Returns E\_UNEXPECTED.

## Remarks

This method should only be called on input pins, so the **CBaseOutputPin** implementation returns E\_UNEXPECTED.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseOutputPin Class**](cbaseoutputpin.md)
</dt> </dl>

 

 




