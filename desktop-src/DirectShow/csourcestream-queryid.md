---
description: The QueryId method retrieves an identifier for the pin.
ms.assetid: 6050292e-6203-4a79-87bf-47394624cb32
title: CSourceStream.QueryId method (Source.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceStream.QueryId
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CSourceStream.QueryId method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `QueryId` method retrieves an identifier for the pin.

## Syntax


```C++
HRESULT QueryId(
   LPWSTR *Id
);
```



## Parameters

<dl> <dt>

*Id* 
</dt> <dd>

Pointer to a variable that receives a string containing the pin identifier.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                                       | Description                                 |
|---------------------------------------------------------------------------------------------------|---------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | Success.<br/>                         |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>     | Insufficient memory.<br/>             |
| <dl> <dt>**E\_POINTER**</dt> </dl>         | **NULL** pointer argument.<br/>       |
| <dl> <dt>**VFW\_E\_NOT\_FOUND**</dt> </dl> | Pin was not found on the filter.<br/> |



 

## Remarks

This method implements the [**IPin::QueryId**](/windows/desktop/api/Strmif/nf-strmif-ipin-queryid) method. To construct an identifier string, the pin calls the [**CSource::FindPinNumber**](csource-findpinnumber.md) method with itself as the parameter. The **FindPinNumber** method returns the pin number, indexed from zero. `QueryId` increments the return value by one and converts the result to a string. For example, the first pin becomes "1"; the second pin becomes "2"; and so forth.

If this method returns VFW\_E\_NOT\_FOUND, it indicates that the filter's array of pins is invalid, presumably caused by a bug in the filter.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceStream Class**](csourcestream.md)
</dt> </dl>

 

 




