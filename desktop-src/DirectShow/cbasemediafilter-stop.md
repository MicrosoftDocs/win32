---
Description: The Stop method stops the object. This method implements the IMediaFilterStop method.
ms.assetid: 9282d90a-932c-4ba0-84f1-1de2c125bfbd
title: CBaseMediaFilter.Stop method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseMediaFilter.Stop method

The `Stop` method stops the object. This method implements the [**IMediaFilter::Stop**](/windows/win32/Strmif/nf-strmif-imediafilter-stop?branch=master) method.

## Syntax


```C++
HRESULT Stop();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

In the base class, this method sets the [**CBaseMediaFilter::m\_State**](cbasemediafilter-m-state.md) member variable to State\_Stopped but does nothing else.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseMediaFilter Class**](cbasemediafilter.md)
</dt> </dl>

 

 




