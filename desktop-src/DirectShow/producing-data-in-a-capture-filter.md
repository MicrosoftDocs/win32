---
description: This topic describes how a custom DirectShow capture filter should generate output data.
ms.assetid: e407e9ed-f1f7-43c4-a048-c27476c910ea
title: Producing Data in a Capture Filter
ms.topic: article
ms.date: 05/31/2018
---

# Producing Data in a Capture Filter

This topic describes how a custom DirectShow capture filter should generate output data.

## Filter State Changes

A capture filter should produce data only when the filter is running. Do not send data from your pins when the filter is paused. Also, return **VFW\_S\_CANT\_CUE** from the [**CBaseFilter::GetState**](cbasefilter-getstate.md) method when the filter is paused. This return value informs the Filter Graph Manager that it should not wait for any data from your filter while the filter is paused. For more information, see [Filter States](filter-states.md).

The following code shows how to implement the [**IMediaFilter::GetState**](/windows/desktop/api/Strmif/nf-strmif-imediafilter-getstate) method:


```C++
CMyVidcapFilter::GetState(DWORD dw, FILTER_STATE *pState)
{
    CheckPointer(pState, E_POINTER);
    *pState = m_State;
    if (m_State == State_Paused)
    {
        return VFW_S_CANT_CUE;
    }
    else
    {
        return S_OK;
    }
}
```



## Controlling Individual Streams

A capture filter's output pins should support the [**IAMStreamControl**](/windows/desktop/api/Strmif/nn-strmif-iamstreamcontrol) interface, so that an application can turn each pin on or off individually. For example, an application can preview without capturing, and then switch to capture mode without rebuilding the filter graph. You can use the [**CBaseStreamControl**](cbasestreamcontrol.md) class to implement this interface.

## Time Stamps

When the filter captures a sample, time stamp the sample with the current stream time. The end time is the start time plus the duration. For example, if the filter is capturing at ten samples per second, and the stream time is 200,000,000 units when the filter captures the sample, the time stamps should be 200000000 and 201000000. (There are 10,000,000 units per second.)

To calculate the stream time, call the [**IReferenceClock::GetTime**](/windows/desktop/api/Strmif/nf-strmif-ireferenceclock-gettime) method to get the current reference time, and then substract the original start time. Alternatively, call the [**CBaseFilter::StreamTime**](cbasefilter-streamtime.md) method, which performs the same calculation. To set the time stamp on a sample, call the [**IMediaSample::SetTime**](/windows/desktop/api/Strmif/nf-strmif-imediasample-settime) method.

If the filter has a preview pin, however, samples from the preview pin should not have time stamps. The reason is that samples will always reach the renderer slightly after the time of capture. If the samples are time stamped, the renderer will treat them as late, and it may try to catch up by dropping samples. (For more information, see [DirectShow Video Capture Filters](directshow-video-capture-filters.md).) Note that the [**IAMStreamControl**](/windows/desktop/api/Strmif/nn-strmif-iamstreamcontrol) interface requires the pin to keep track of sample times. For a preview pin, you might need to modify the implementation so that it does not rely on time stamps.

Time stamps must always increase from one sample to the next. This is true even when the filter pauses. If the filter runs, pauses, and then runs again, the first sample after the pause must have a larger time stamp than the last sample before the pause.

Depending on the data you are capturing, it might be appropriate to set the media time on the samples.

For more information, see [Time and Clocks in DirectShow](time-and-clocks-in-directshow.md).

## Related topics

<dl> <dt>

[DirectShow Video Capture Filters](directshow-video-capture-filters.md)
</dt> <dt>

[Time and Clocks in DirectShow](time-and-clocks-in-directshow.md)
</dt> <dt>

[Writing Capture Filters](writing-capture-filters.md)
</dt> </dl>

 

 



