---
Description: Pauses the object. Implements the IMediaFilterPause method.
ms.assetid: 4f4cbe7e-3004-4731-864f-737c2f51afff
title: CBaseMediaFilter.Pause method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseMediaFilter.Pause method

Pauses the object. Implements the [**IMediaFilter::Pause**](/windows/win32/Strmif/nf-strmif-imediafilter-pause?branch=master) method.

## Syntax


```C++
HRESULT Pause();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

In the base class, this method sets the [**CBaseMediaFilter::m\_State**](cbasemediafilter-m-state.md) member variable to State\_Paused but does nothing else.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseMediaFilter Class**](cbasemediafilter.md)
</dt> </dl>

 

 




