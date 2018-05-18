---
Description: 'The SetSyncSource method sets the clock used for timing.'
ms.assetid: '646d4d24-f9b7-438a-b842-58e90eb6a945'
title: 'CCmdQueue.SetSyncSource method'
---

# CCmdQueue.SetSyncSource method

The `SetSyncSource` method sets the clock used for timing.

## Syntax


```C++
virtual HRESULT SetSyncSource(
   IReferenceClock *pIrc
);
```



## Parameters

<dl> <dt>

*pIrc* 
</dt> <dd>

Pointer to the [**IReferenceClock**](ireferenceclock.md) interface.

</dd> </dl>

## Return value

Returns S\_OK.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CCmdQueue Class**](ccmdqueue.md)
</dt> </dl>

 

 




