---
Description: The SetSyncSource method sets a reference clock for the filter. This method implements the IMediaFilterSetSyncSource method.
ms.assetid: 298039fc-dd38-4063-8752-2669b134b8ef
title: CBaseFilter.SetSyncSource method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseFilter.SetSyncSource method

The **SetSyncSource** method sets a reference clock for the filter. This method implements the [**IMediaFilter::SetSyncSource**](/windows/win32/Strmif/nf-strmif-imediafilter-setsyncsource?branch=master) method.

## Syntax


```C++
HRESULT SetSyncSource(
   IReferenceClock *pClock
);
```



## Parameters

<dl> <dt>

*pClock* 
</dt> <dd>

Pointer to the clock's [**IReferenceClock**](/windows/win32/Strmif/nn-strmif-ireferenceclock?branch=master) interface, or **NULL**.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




