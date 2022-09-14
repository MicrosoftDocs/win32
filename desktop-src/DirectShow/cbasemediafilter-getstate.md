---
description: The GetState method retrieves the object's state (running, stopped, or paused). This method implements the IMediaFilter::GetState method.
ms.assetid: d4cc7e2b-5ea5-4165-842f-becc3a81cbce
title: CBaseMediaFilter.GetState method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseMediaFilter.GetState
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseMediaFilter.GetState method

The `GetState` method retrieves the object's state (running, stopped, or paused). This method implements the [**IMediaFilter::GetState**](/windows/desktop/api/Strmif/nf-strmif-imediafilter-getstate) method.

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

Pointer to a variable that receives a member of the [**FILTER\_STATE**](/windows/win32/api/strmif/ne-strmif-filter_state) enumerated type, indicating the object's state.

</dd> </dl>

## Return value

Returns S\_OK or E\_POINTER.

## Remarks

In the base class, all state transitions are synchronous and the *dwMilliSecsTimeout* parameter is ignored. If a derived class performs asynchronous state transitions, it should override this method to wait during state transitions, with a time-out of *dwMilliSecsTimeout* milliseconds.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseMediaFilter Class**](cbasemediafilter.md)
</dt> </dl>

 

 




