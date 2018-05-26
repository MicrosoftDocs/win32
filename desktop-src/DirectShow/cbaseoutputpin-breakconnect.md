---
Description: The BreakConnect method releases the pin from a connection.
ms.assetid: 0dec3c9d-1adf-4fa3-ab5a-c351053f8054
title: CBaseOutputPin.BreakConnect method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseOutputPin.BreakConnect method

The `BreakConnect` method releases the pin from a connection.

## Syntax


```C++
HRESULT BreakConnect();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK if successful, or an **HRESULT** value indicating the cause of the error.

## Remarks

This method overrides the [**CBasePin::BreakConnect**](cbasepin-breakconnect.md) method. It decommits the allocator and releases the [**IMemAllocator**](/windows/win32/Strmif/nn-strmif-imemallocator?branch=master) and [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master) interfaces.

If you override this method, call the base-class method from your overriding method. Otherwise, you might cause memory leaks.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseOutputPin Class**](cbaseoutputpin.md)
</dt> </dl>

 

 




