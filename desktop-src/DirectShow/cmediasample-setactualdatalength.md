---
description: The SetActualDataLength method sets the length of the valid data in the buffer. This method implements the IMediaSample::SetActualDataLength method.
ms.assetid: a80a67ef-e490-4874-a123-f2d193cec4d7
title: CMediaSample.SetActualDataLength method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaSample.SetActualDataLength
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaSample.SetActualDataLength method

The `SetActualDataLength` method sets the length of the valid data in the buffer. This method implements the [**IMediaSample::SetActualDataLength**](/windows/desktop/api/Strmif/nf-strmif-imediasample-setactualdatalength) method.

## Syntax


```C++
HRESULT SetActualDataLength(
   long lLen
);
```



## Parameters

<dl> <dt>

*lLen* 
</dt> <dd>

Length of the valid data, in bytes.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                                             | Description                                                 |
|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Success.<br/>                                         |
| <dl> <dt>**VFW\_E\_BUFFER\_OVERFLOW**</dt> </dl> | *lLen* is larger than the allocated buffer size.<br/> |



 

## Remarks

This method sets the [**CMediaSample::m\_lActual**](cmediasample-m-lactual.md) member variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




