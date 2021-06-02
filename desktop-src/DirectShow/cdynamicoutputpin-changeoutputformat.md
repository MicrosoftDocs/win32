---
description: The ChangeOutputFormat method dynamically changes the media type for the connection, and delivers new segment information.
ms.assetid: d1204ca0-a489-48a0-8fe5-3ade04f51c93
title: CDynamicOutputPin.ChangeOutputFormat method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDynamicOutputPin.ChangeOutputFormat
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDynamicOutputPin.ChangeOutputFormat method

The `ChangeOutputFormat` method dynamically changes the media type for the connection, and delivers new segment information. The change can occur while the filter graph is running. Once this method is called, samples with the old media type cannot be delivered. The caller must ensure that no old samples are pending.

## Syntax


```C++
HRESULT ChangeOutputFormat(
   const AM_MEDIA_TYPE  *pmt,
         REFERENCE_TIME tSegmentStart,
         REFERENCE_TIME tSegmentStop,
         double         dSegmentRate
);
```



## Parameters

<dl> <dt>

*pmt* 
</dt> <dd>

Pointer to an [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure that specifies the media type.

</dd> <dt>

*tSegmentStart* 
</dt> <dd>

Start time of the segment.

</dd> <dt>

*tSegmentStop* 
</dt> <dd>

Stop time of the segment.

</dd> <dt>

*dSegmentRate* 
</dt> <dd>

Segment rate.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                                           | Description                                                                                                                              |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                  | Success.<br/>                                                                                                                      |
| <dl> <dt>**E\_FAIL**</dt> </dl>                | Failure. Possibly the owning filter did not call [**CDynamicOutputPin::SetConfigInfo**](cdynamicoutputpin-setconfiginfo.md).<br/> |
| <dl> <dt>**VFW\_E\_NOT\_CONNECTED**</dt> </dl> | The pin is not connected.<br/>                                                                                                     |



 

## Remarks

This method changes the format type while the filter is running. If the downstream pin accepts the new format, no reconnection is necessary. Otherwise, the method attempts to reconnect the pin. If the method successfully changes the format, it delivers the new segment information. This method calls the [**CDynamicOutputPin::ChangeMediaType**](cdynamicoutputpin-changemediatype.md) method to perform the format change.

You must call the [**CDynamicOutputPin::StartUsingOutputPin**](cdynamicoutputpin-startusingoutputpin.md) method before calling this method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> </dl>

 

 




