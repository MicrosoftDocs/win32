---
description: The Unadvise method removes an advise request.
ms.assetid: b3dfda82-577e-4499-a114-1c8721e4af9e
title: CAMSchedule.Unadvise method (Dsschedule.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMSchedule.Unadvise
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAMSchedule.Unadvise method

The `Unadvise` method removes an advise request.

## Syntax


```C++
HRESULT Unadvise(
   DWORD_PTR dwAdviseCookie
);
```



## Parameters

<dl> <dt>

*dwAdviseCookie* 
</dt> <dd>

Identifier of the advise request, returned by the [**CAMSchedule::AddAdvisePacket**](camschedule-addadvisepacket.md) method.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                             | Description          |
|-----------------------------------------------------------------------------------------|----------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | Not found<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success<br/>   |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Dsschedule.h (include Streams.h)</dt> </dl>                                                                                |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMSchedule Class**](camschedule.md)
</dt> </dl>

 

 




