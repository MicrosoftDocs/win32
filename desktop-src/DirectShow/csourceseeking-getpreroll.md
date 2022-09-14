---
description: The GetPreroll method retrieves the preroll time. This method implements the IMediaSeeking::GetPreroll method.
ms.assetid: 2395d5b2-8c1f-40cd-8d4a-48620debe7a7
title: CSourceSeeking.GetPreroll method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceSeeking.GetPreroll
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSourceSeeking.GetPreroll method

The `GetPreroll` method retrieves the preroll time. This method implements the [**IMediaSeeking::GetPreroll**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-getpreroll) method.

## Syntax


```C++
HRESULT GetPreroll(
   LONGLONG *pPreroll
);
```



## Parameters

<dl> <dt>

*pPreroll* 
</dt> <dd>

Pointer to a variable that receives the preroll time. The value is set to zero.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values listed in the following table.



| Return code                                                                               | Description                       |
|-------------------------------------------------------------------------------------------|-----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | Success<br/>                |
| <dl> <dt>**E\_POINTER**</dt> </dl> | **NULL** pointer value<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceSeeking Class**](csourceseeking.md)
</dt> </dl>

 

 




