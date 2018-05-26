---
Description: The GetState method retrieves the objects state (running, stopped, or paused). This method implements the IMediaFilterGetState method.
ms.assetid: d4cc7e2b-5ea5-4165-842f-becc3a81cbce
title: CBaseMediaFilter.GetState method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseMediaFilter.GetState method

The `GetState` method retrieves the object's state (running, stopped, or paused). This method implements the [**IMediaFilter::GetState**](/windows/win32/Strmif/nf-strmif-imediafilter-getstate?branch=master) method.

## Syntax


```C++
HRESULT GetState(
   DWORD        dwMilliSecsTimeout,
   FILTER_STATE *State
);
```



## Parameters

<dl> <dt>

*dwMilliSecsTimeout* 
</dt> <dd>

Time-out interval, in milliseconds.

</dd> <dt>

*State* 
</dt> <dd>

Pointer to a variable that receives a member of the [**FILTER\_STATE**](/windows/win32/strmif/ne-strmif-_filterstate?branch=master) enumerated type, indicating the object's state.

</dd> </dl>

## Return value

Returns S\_OK or E\_POINTER.

## Remarks

In the base class, all state transitions are synchronous and the *dwMilliSecsTimeout* parameter is ignored. If a derived class performs asynchronous state transitions, it should override this method to wait during state transitions, with a time-out of *dwMilliSecsTimeout* milliseconds.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseMediaFilter Class**](cbasemediafilter.md)
</dt> </dl>

 

 




