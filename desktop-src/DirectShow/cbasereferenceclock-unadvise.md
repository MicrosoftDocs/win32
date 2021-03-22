---
description: The Unadvise method removes a pending advise request. This method implements the IReferenceClock::Unadvise method.
ms.assetid: b137234a-e260-42f9-b583-9e6a5fd7bca4
title: CBaseReferenceClock.Unadvise method (Refclock.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseReferenceClock.Unadvise
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseReferenceClock.Unadvise method

The `Unadvise` method removes a pending advise request. This method implements the [**IReferenceClock::Unadvise**](/windows/desktop/api/Strmif/nf-strmif-ireferenceclock-unadvise) method.

## Syntax


```C++
HRESULT Unadvise(
   DWORD_PTR dwAdviseToken
);
```



## Parameters

<dl> <dt>

*dwAdviseToken* 
</dt> <dd>

Identifier of the request to remove. Use the value returned by the [**CBaseReferenceClock::AdviseTime**](cbasereferenceclock-advisetime.md) or [**CBaseReferenceClock::AdvisePeriodic**](cbasereferenceclock-adviseperiodic.md) methods in the *pdwAdviseToken* parameter.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                             | Description           |
|-----------------------------------------------------------------------------------------|-----------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | Not found.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>   |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Refclock.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseReferenceClock Class**](cbasereferenceclock.md)
</dt> </dl>

 

 




