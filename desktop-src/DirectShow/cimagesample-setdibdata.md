---
description: The SetDIBData method specifies information about the GDI device-independent bitmap (DIB) that this object is managing. Call this method to initialize the CImageSample object.
ms.assetid: 850fa16b-d4b9-4fe6-b202-7b54c49a4589
title: CImageSample.SetDIBData method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImageSample.SetDIBData
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CImageSample.SetDIBData method

The `SetDIBData` method specifies information about the GDI device-independent bitmap (DIB) that this object is managing. Call this method to initialize the **CImageSample** object.

## Syntax


```C++
void SetDIBData(
   DIBDATA *pDibData
);
```



## Parameters

<dl> <dt>

*pDibData* 
</dt> <dd>

Pointer to a [**DIBDATA**](dibdata.md) structure.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImageSample Class**](cimagesample.md)
</dt> </dl>

 

 




