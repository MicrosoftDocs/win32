---
Description: The BeginFlush method begins a flush operation.
ms.assetid: dc652394-c24e-4cea-ac28-30a1e6de205f
title: CBaseRenderer.BeginFlush method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseRenderer.BeginFlush method

The `BeginFlush` method begins a flush operation.

## Syntax


```C++
virtual HRESULT BeginFlush();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

The filter's input pin calls this method when it receives a call to the [**IPin::BeginFlush**](/windows/win32/Strmif/nf-strmif-ipin-beginflush?branch=master) method. The filter releases the streaming thread, and releases any sample that it was holding for rendering.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




