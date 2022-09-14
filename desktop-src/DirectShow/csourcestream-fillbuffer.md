---
description: The FillBuffer method fills a media sample with data.
ms.assetid: dddad8c7-44f1-4ba3-8fb1-7e7e88e40941
title: CSourceStream.FillBuffer method (Source.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceStream.FillBuffer
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSourceStream.FillBuffer method

The `FillBuffer` method fills a media sample with data.

## Syntax


```C++
virtual HRESULT FillBuffer(
   IMediaSample *pSample
) = 0;
```



## Parameters

<dl> <dt>

*pSample* 
</dt> <dd>

Pointer to the sample's [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                             | Description              |
|-----------------------------------------------------------------------------------------|--------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | End of stream<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success<br/>       |



 

## Remarks

The derived class must implement this method.

The media sample given to this method has no time stamps. The derived class should call the [**IMediaSample::SetTime**](/windows/desktop/api/Strmif/nf-strmif-imediasample-settime) method to set the time stamps. If appropriate for the media type, the derived class should also set the media times, by calling the [**IMediaSample::SetMediaTime**](/windows/desktop/api/Strmif/nf-strmif-imediasample-setmediatime) method. For more information, see [Time and Clocks in DirectShow](time-and-clocks-in-directshow.md).

Return S\_FALSE at the end of the stream. This causes the **CSourceStream** class to send the end-of-stream notification and halt the buffer processing loop. See [**CSourceStream::DoBufferProcessingLoop**](csourcestream-dobufferprocessingloop.md) for more information.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceStream Class**](csourcestream.md)
</dt> </dl>

 

 




