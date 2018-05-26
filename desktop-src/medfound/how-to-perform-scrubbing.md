---
Description: How to Perform Scrubbing
ms.assetid: 3cf56caf-5c6d-4318-811a-c8bdc1959148
title: How to Perform Scrubbing
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# How to Perform Scrubbing

Scrubbing is performed to instantaneously seek to specific points within a file by interacting with a visual representation of time, such as a scrollbar. In Media Foundation, scrubbing means seeking on a file and getting one updated frame.

For information about scrubbing, see [About Rate Control](about-rate-control.md).

## To perform scrubbing

1.  Call [**MFGetService**](/windows/win32/mfidl/nf-mfidl-mfgetservice?branch=master) to get the [**IMFRateControl**](/windows/win32/mfidl/nn-mfidl-imfratecontrol?branch=master) interface from the [Media Session](media-session.md).
    > [!Note]  
    > Do not get the [**IMFRateControl**](/windows/win32/mfidl/nn-mfidl-imfratecontrol?branch=master) interface from the media source. Always get the interface from the Media Session.

     

2.  Call [**IMFRateControl::SetRate**](/windows/win32/mfidl/nf-mfidl-imfratecontrol-setrate?branch=master) to set the playback rate to zero. For more information about calling this method, see [How to Set the Playback Rate on the Media Session](how-to-set-the-playback-rate-on-the-media-session.md).
3.  Create a seek position in a **PROPVARIANT** by specifying the presentation time to seek to in a **MFTIME** type.
4.  Call [**IMFMediaSession::Start**](/windows/win32/mfidl/nf-mfidl-imfmediasession-start?branch=master) with the seek position to start playback.
5.  When the scrub operation is complete, the Media Session sends an [MESessionScrubSampleComplete](mesessionscrubsamplecomplete.md) event. Wait for this event before calling [**Start**](/windows/win32/mfidl/nf-mfidl-imfmediasession-start?branch=master) again for another scrubbing operation.

## Example

The following code example shows how to perform scrubbing.


```C++
HRESULT SkipToPosition (MFTIME SeekTime, IMFMediaSession *pMediaSession)
{
    PROPVARIANT var;
    PropVariantInit(&amp;var);

    IMFRateControl *pRateControl = NULL;

    // Get the rate control service.
    HRESULT hr = MFGetService(pMediaSession, MF_RATE_CONTROL_SERVICE, IID_PPV_ARGS(&amp;pRateControl));

    // Set the playback rate to zero without thinning.
    if(SUCCEEDED(hr))
    {
        hr = pRateControl ->SetRate( FALSE, 0.0F); 
    }

    // Create the Media Session start position.
    if( SeekTime == PRESENTATION_CURRENT_POSITION )
    {
        var.vt = VT_EMPTY;
    }
    else
    {
        var.vt = VT_I8;
        var.hVal.QuadPart = SeekTime;
    }

    // Start the Media Session.
    if(SUCCEEDED(hr))
    {
        hr = pMediaSession->Start( NULL, &amp;var);
    }

// Clean up.
    SafeRelease(&amp;pRateControl);
    PropVariantClear(&amp;var)
    return hr;
}
```



A successful scrubbing operation generates the [MESessionScrubSampleComplete](mesessionscrubsamplecomplete.md) event after all the stream sinks are updated with the new frame and the scrubbing operation completes successfully. Scrubbing a video file displays the frame that was seeked to, but does not generate an audio output.

The application can perform frame stepping by setting the playback rate to zero and then passing a **PROPVARIANT** that is set to **VT\_EMPTY** in the call to [**IMFMediaSession::Start**](/windows/win32/mfidl/nf-mfidl-imfmediasession-start?branch=master).

## Related topics

<dl> <dt>

[Media Session](media-session.md)
</dt> <dt>

[Rate Control](rate-control.md)
</dt> </dl>

 

 



