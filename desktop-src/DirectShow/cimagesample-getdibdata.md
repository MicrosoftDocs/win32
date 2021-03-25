---
description: The GetDIBData method retrieves information about the GDI device-independent bitmap (DIB) that this object is managing.
ms.assetid: ec337336-69ec-47ff-a522-42c0388f9bc0
title: CImageSample.GetDIBData method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImageSample.GetDIBData
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CImageSample.GetDIBData method

The `GetDIBData` method retrieves information about the GDI device-independent bitmap (DIB) that this object is managing.

## Syntax


```C++
DIBDATA* GetDIBData();
```



## Parameters

This method has no parameters.

## Return value

Returns a pointer to a [**DIBDATA**](dibdata.md) structure.

## Remarks

The caller must initialize the **DIBDATA** structure before calling this method; check the value of **CImageSample::m\_bInit**. To initialize the structure, call the [**CImageSample::SetDIBData**](cimagesample-setdibdata.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImageSample Class**](cimagesample.md)
</dt> </dl>

 

 




