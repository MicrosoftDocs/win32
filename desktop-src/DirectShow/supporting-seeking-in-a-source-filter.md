---
description: This topic describes how to implement seeking in a Microsoft DirectShow source filter. It uses the Ball Filter sample as the starting point and describes the additional code needed to support seeking in this filter.
ms.assetid: a2b4be09-2fd6-4aac-8ad6-c3d62377c1f2
title: Supporting Seeking in a Source Filter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Supporting Seeking in a Source Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This topic describes how to implement seeking in a Microsoft DirectShow source filter. It uses the [Ball Filter](ball-filter-sample.md) sample as the starting point and describes the additional code needed to support seeking in this filter.

The [Ball Filter](ball-filter-sample.md) sample is a source filter that creates an animated bouncing ball. This article describes how to add seeking functionality to this filter. Once you have added this functionality, you can render the filter in GraphEdit and control the ball by dragging the GraphEdit slider.

This topic contains the following sections:

-   [Overview of Seeking in DirectShow](#overview-of-seeking-in-directshow)
-   [Quick Overview of the Ball Filter](#quick-overview-of-the-ball-filter)
-   [Modifying the Ball Filter for Seeking](#modifying-the-ball-filter-for-seeking)
-   [Limitations of the CSourceSeeking Class](#limitations-of-the-csourceseeking-class)

## Overview of Seeking in DirectShow

An application seeks the filter graph by calling an [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking) method on the Filter Graph Manager. The Filter Graph Manager then distributes the call to every renderer in the graph. Each renderer sends the call upstream, through the output pin of the next upstream filter. The call travels upstream until it reaches a filter that can execute the seek command, typically a source filter or a parser filter. In general, the filter that originates the time stamps also handles seeking.

A filter responds to a seek command as follows:

1.  The filter flushes the graph. This clears any stale data from graph, which improves responsiveness. Otherwise, samples that were buffered prior to the seek command might get delivered.
2.  The filter calls [**IPin::NewSegment**](/windows/desktop/api/Strmif/nf-strmif-ipin-newsegment) to inform downstream filters of the new stop time, start time, and playback rate.
3.  The filter then sets the discontinuity flag on the first sample after the seek command.

Time stamps start from zero after any seek command (including rate changes).

## Quick Overview of the Ball Filter

The Ball filter is a push source, which means that it uses a worker thread to deliver samples downstream, as opposed to a pull source, which passively waits for a downstream filter to request samples. The Ball filter is built from the [**CSource**](csource.md) class, and its output pin is built from the [**CSourceStream**](csourcestream.md) class. The **CSourceStream** class creates the worker thread that drives the flow of data. This thread enters a loop that gets samples from the allocator, fills them with data, and delivers them downstream.

Most of the action in [**CSourceStream**](csourcestream.md) happens in the [**CSourceStream::FillBuffer**](csourcestream-fillbuffer.md) method, which the derived class implements. The argument to this method is a pointer to the sample to be delivered. The Ball filter's implementation of **FillBuffer** retrieves the address of the sample buffer and draws directly to the buffer by setting individual pixel values. (The drawing is done by a helper class, CBall, so you can ignore the details regarding bit depths, palettes, and so forth.)

## Modifying the Ball Filter for Seeking

To make the Ball filter seekable, use the [**CSourceSeeking**](csourceseeking.md) class, which is designed for implementing seeking in filters with one output pin. Add the **CSourceSeeking** class to the inheritance list for the CBallStream class:


```C++
class CBallStream :  // Defines the output pin.
    public CSourceStream, public CSourceSeeking
```



Also, you will need to add an initializer for [**CSourceSeeking**](csourceseeking.md) to the CBallStream constructor:


```C++
    CSourceSeeking(NAME("SeekBall"), (IPin*)this, phr, &m_cSharedState),
```



This statement calls the base constructor for [**CSourceSeeking**](csourceseeking.md). The parameters are a name, a pointer to the owning pin, an **HRESULT** value, and the address of a critical section object. The name is used only for debugging, and the [**NAME**](name.md) macro compiles to an empty string in retail builds. The pin directly inherits **CSourceSeeking**, so the second parameter is a pointer to itself, cast to an [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) pointer. The **HRESULT** value is ignored in the current version of the base classes; it remains for compatibility with previous versions. The critical section protects shared data, such as the current start time, stop time, and playback rate.

Add the following statement inside the [**CSourceSeeking**](csourceseeking.md) constructor:


```C++
m_rtStop = 60 * UNITS;
```



The *m\_rtStop* variable specifies the stop time. By default, the value is \_I64\_MAX / 2, which is approximately 14,600 years. The previous statement sets it to a more conservative 60 seconds.

Two additional member variables must be added to CBallStream:


```C++
BOOL            m_bDiscontinuity; // If true, set the discontinuity flag.
REFERENCE_TIME  m_rtBallPosition; // Position of the ball. 
```



After every seek command, the filter must set the discontinuity flag on the next sample by calling [**IMediaSample::SetDiscontinuity**](/windows/desktop/api/Strmif/nf-strmif-imediasample-setdiscontinuity). The *m\_bDiscontinuity* variable will keep track of this. The *m\_rtBallPosition* variable will specify the position of the ball within the video frame. The original Ball filter calculates the position from the stream time, but the stream time resets to zero after each seek command. In a seekable stream, the absolute position is independent of the stream time.

### QueryInterface

The [**CSourceSeeking**](csourceseeking.md) class implements the [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking) interface. To expose this interface to clients, override the [**NonDelegatingQueryInterface**](cunknown-nondelegatingqueryinterface.md) method:


```C++
STDMETHODIMP CBallStream::NonDelegatingQueryInterface
    (REFIID riid, void **ppv)
{
    if( riid == IID_IMediaSeeking ) 
    {
        return CSourceSeeking::NonDelegatingQueryInterface( riid, ppv );
    }
    return CSourceStream::NonDelegatingQueryInterface(riid, ppv);
}
```



The method is called "NonDelegating" because of the way the DirectShow base classes support Component Object Model (COM) aggregation. For more information, see the "How to Implement IUnknown" topic in the DirectShow SDK.

### Seeking Methods

The [**CSourceSeeking**](csourceseeking.md) class maintains several member variables relating to seeking.



| Variable          | Description   | Default Value  |
|-------------------|---------------|----------------|
| *m\_rtStart*      | Start time    | Zero           |
| *m\_rtStop*       | Stop time     | \_I64\_MAX / 2 |
| *m\_dRateSeeking* | Playback rate | 1.0            |



 

The [**CSourceSeeking**](csourceseeking.md) implementation of [**IMediaSeeking::SetPositions**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-setpositions) updates the start and stop times, and then calls two pure virtual methods on the derived class, [**CSourceSeeking::ChangeStart**](csourceseeking-changestart.md) and [**CSourceSeeking::ChangeStop**](csourceseeking-changestop.md). The implementation of [**IMediaSeeking::SetRate**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-setrate) is similar: It updates the playback rate and then calls the pure virtual method [**CSourceSeeking::ChangeRate**](csourceseeking-changerate.md). In each of these virtual methods, the pin must do the following:

1.  Call [**IPin::BeginFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-beginflush) to start flushing data.
2.  Halt the streaming thread.
3.  Call [**IPin::EndFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-endflush).
4.  Restart the streaming thread.
5.  Call [**IPin::NewSegment**](/windows/desktop/api/Strmif/nf-strmif-ipin-newsegment).
6.  Set the discontinuity flag on the next sample.

The order of these steps is crucial, because the streaming thread can block while it waits to deliver a sample or get a new sample. The [**BeginFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-beginflush) method ensures that the streaming thread is not blocked and therefore will not deadlock in step 2. The [**EndFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-endflush) call informs the downstream filters to expect new samples, so they do not reject them when the thread starts again in step 4.

The following private method performs steps 1 through 4:


```C++
void CBallStream::UpdateFromSeek()
{
    if (ThreadExists()) 
    {
        DeliverBeginFlush();
        // Shut down the thread and stop pushing data.
        Stop();
        DeliverEndFlush();
        // Restart the thread and start pushing data again.
        Pause();
    }
}
```



When the streaming thread starts again, it calls the [**CSourceStream::OnThreadStartPlay**](csourcestream-onthreadstartplay.md) method. Override this method to perform steps 5 and 6:


```C++
HRESULT CBallStream::OnThreadStartPlay()
{
    m_bDiscontinuity = TRUE;
    return DeliverNewSegment(m_rtStart, m_rtStop, m_dRateSeeking);
}
```



In the [**ChangeStart**](csourceseeking-changestart.md) method, set the stream time to zero and the position of the ball to the new start time. Then call CBallStream::UpdateFromSeek:


```C++
HRESULT CBallStream::ChangeStart( )
{
    {
        CAutoLock lock(CSourceSeeking::m_pLock);
        m_rtSampleTime = 0;
        m_rtBallPosition = m_rtStart;
    }
    UpdateFromSeek();
    return S_OK;
}
```



In the [**ChangeStop**](csourceseeking-changestop.md) method, call CBallStream::UpdateFromSeek if the new stop time is less than the current position. Otherwise, the stop time is still in the future, so there's no need to flush the graph.


```C++
HRESULT CBallStream::ChangeStop( )
{
    {
        CAutoLock lock(CSourceSeeking::m_pLock);
        if (m_rtBallPosition < m_rtStop)
        {
            return S_OK;
        }
    }

    // We're already past the new stop time. Flush the graph.
    UpdateFromSeek();
    return S_OK;
}
```



For rate changes, the [**CSourceSeeking::SetRate**](csourceseeking-setrate.md) method sets *m\_dRateSeeking* to the new rate (discarding the old value) before it calls [**ChangeRate**](csourceseeking-changerate.md). Unfortunately, if the caller gave an invalid rate—for example, less than zero—it's too late by the time **ChangeRate** is called. One solution is to override **SetRate** and check for valid rates:


```C++
HRESULT CBallStream::SetRate(double dRate)
{
    if (dRate <= 1.0)
    {
        return E_INVALIDARG;
    }
    {
        CAutoLock lock(CSourceSeeking::m_pLock);
        m_dRateSeeking = dRate;
    }
    UpdateFromSeek();
    return S_OK;
}
// Now ChangeRate won't ever be called, but it's pure virtual, so it needs
// a dummy implementation.
HRESULT CBallStream::ChangeRate() { return S_OK; }
```



### Drawing in the Buffer

Here is the modified version of [**CSourceStream::FillBuffer**](csourcestream-fillbuffer.md), the routine that draws the ball on each frame:


```C++
HRESULT CBallStream::FillBuffer(IMediaSample *pMediaSample)
{
    BYTE *pData;
    long lDataLen;
    pMediaSample->GetPointer(&pData);
    lDataLen = pMediaSample->GetSize();
    {
        CAutoLock cAutoLockShared(&m_cSharedState);
        if (m_rtBallPosition >= m_rtStop) 
        {
            // End of the stream.
            return S_FALSE;
        }
        // Draw the ball in its current position.
        ZeroMemory( pData, lDataLen );
        m_Ball->MoveBall(m_rtBallPosition);
        m_Ball->PlotBall(pData, m_BallPixel, m_iPixelSize);
        
        // The sample times are modified by the current rate.
        REFERENCE_TIME rtStart, rtStop;
        rtStart = static_cast<REFERENCE_TIME>(
                      m_rtSampleTime / m_dRateSeeking);
        rtStop  = rtStart + static_cast<int>(
                      m_iRepeatTime / m_dRateSeeking);
        pMediaSample->SetTime(&rtStart, &rtStop);

        // Increment for the next loop.
        m_rtSampleTime += m_iRepeatTime;
        m_rtBallPosition += m_iRepeatTime;
    }
    pMediaSample->SetSyncPoint(TRUE);
    if (m_bDiscontinuity) 
    {
        pMediaSample->SetDiscontinuity(TRUE);
        m_bDiscontinuity = FALSE;
    }
    return NOERROR;
}
```



The major differences between this version and the original are the following:

-   As mentioned earlier, the *m\_rtBallPosition* variable is used to set the position of the ball, rather than the stream time.
-   After holding the critical section, the method checks whether the current position exceeds the stop time. If so, it returns **S\_FALSE**, which signals the base class to stop sending data and deliver an end-of-stream notification.
-   The time stamps are divided by the current rate.
-   If *m\_bDiscontinuity* is **TRUE**, the method sets the discontinuity flag on the sample.

There is another minor difference. Because the original version relies on having exactly one buffer, it fills the entire buffer with zeroes once, when streaming begins. After that, it just erases the ball from its previous position. However, this optimization reveals a slight bug in the Ball filter. When the [**CBaseOutputPin::DecideAllocator**](cbaseoutputpin-decideallocator.md) method calls [**IMemInputPin::NotifyAllocator**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-notifyallocator), it sets the read-only flag to **FALSE**. As a result, the downstream filter is free to write on the buffer. One solution is to override **DecideAllocator** so that it sets the read-only flag to **TRUE**. For simplicity, however, the new version simply removes the optimization altogether. Instead, this version fills the buffer with zeroes each time.

### Miscellaneous Changes

In the new version, these two lines are removed from the CBall constructor:


```C++
    m_iRandX = rand();
    m_iRandY = rand();
```



The original Ball filter uses these values to add some randomness to the initial ball position. For our purposes, we want the ball to be deterministic. Also, some variables have been changed from [**CRefTime**](creftime.md) objects to [**REFERENCE\_TIME**](reference-time.md) variables. (The **CRefTime** class is a thin wrapper for a **REFERENCE\_TIME** value.) Lastly, the implementation of [**IQualityControl::Notify**](/windows/desktop/api/Strmif/nf-strmif-iqualitycontrol-notify) has been modified slightly; you can refer to the source code for details.

## Limitations of the CSourceSeeking Class

The [**CSourceSeeking**](csourceseeking.md) class is not meant for filters with multiple output pins, because of issues with cross-pin communication. For example, imagine a parser filter that receives an interleaved audio-video stream, splits the stream into its audio and video components, and delivers video from one output pin and audio from another. Both output pins will receive every seek command, but the filter should seek only once per seek command. The solution is to designate one of the pins to control seeking and to ignore seek commands received by the other pin.

After the seek command, however, both pins should flush data. To complicate matters further, the seek command happens on the application thread, not the streaming thread. Therefore, you must make certain that neither pin is blocked and waiting for a [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) call to return, or it might cause a deadlock. For more information about thread-safe flushing in pins, see [Threads and Critical Sections](threads-and-critical-sections.md).

## Related topics

<dl> <dt>

[Writing Source Filters](writing-source-filters.md)
</dt> </dl>

 

 



