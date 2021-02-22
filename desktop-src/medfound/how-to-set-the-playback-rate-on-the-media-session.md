---
description: How to Set the Playback Rate on the Media Session
ms.assetid: 3663b63f-127c-49fc-923a-d05521fe3d35
title: How to Set the Playback Rate on the Media Session
ms.topic: article
ms.date: 05/31/2018
---

# How to Set the Playback Rate on the Media Session

To implement playback functionality such as fast forward and rewind, applications may need to change the playback rate for a media stream. Media Foundation provides the rate control service that the applications must use to set the playback rate dynamically.

Before setting the playback rate, an application should check whether the rate is supported by the media source. For information about querying for supported rates, see [How to Determine Supported Rates](how-to-determine-supported-rates.md).

For information about playback rates, see [About Rate Control](about-rate-control.md).

## To set the playback rate

1.  Call [**MFGetService**](/windows/desktop/api/mfidl/nf-mfidl-mfgetservice) to get the rate control object from the Media Session.

    Applications calling [**MFGetService**](/windows/desktop/api/mfidl/nf-mfidl-mfgetservice) must ensure the following:

    -   The *punkObject* parameter contains an initialized [**IMFMediaSession**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasession) interface pointer.
    -   The rate control object received in the *ppvObject* parameter is released to avoid memory leaks.

2.  Call the [**IMFRateControl::SetRate**](/windows/desktop/api/mfidl/nf-mfidl-imfratecontrol-setrate) method to set the playback rate. After **SetRate** completes asynchronously, the application receives the [MESessionRateChanged](mesessionratechanged.md) event.

## Example

The following code shows how to set the playback rate by calling the [**SetRate**](/windows/desktop/api/mfidl/nf-mfidl-imfclockstatesink-onclocksetrate) method.


```C++
///////////////////////////////////////////////////////////////////////
//  Name: SetPlaybackRate
//  Description: 
//      Gets the rate control service from Media Session.
//      Sets the playback rate to the specified rate.
//  Parameter:
//      pMediaSession: [in] Media session object to query.
//      rateRequested: [in] Playback rate to set.
//      bThin: [in] Indicates whether to use thinning.
///////////////////////////////////////////////////////////////////////

HRESULT SetPlaybackRate(
          IMFMediaSession *pMediaSession, 
          float rateRequested, 
          BOOL bThin)
{
    HRESULT hr = S_OK;
    IMFRateControl *pRateControl = NULL;

    // Get the rate control object from the Media Session.
    hr = MFGetService( 
           pMediaSession, 
           MF_RATE_CONTROL_SERVICE, 
           IID_IMFRateControl, 
           (void**) &pRateControl ); 

    // Set the playback rate.
    if(SUCCEEDED(hr))
    {
        hr = pRateControl ->SetRate( bThin, rateRequested); 
    }

    // Clean up.
    SAFE_RELEASE(pRateControl );

    return hr;
}
```



The application must be stopped or paused before it can make a transition from a negative or zero rate to a positive rate. For information about these states, see [How to Control Presentation States](how-to-control-presentation-states.md).

## Related topics

<dl> <dt>

[Media Session](media-session.md)
</dt> <dt>

[Rate Control](rate-control.md)
</dt> <dt>

[Seeking, Fast Forward, and Reverse Play](seeking--fast-forward--and-reverse-play.md)
</dt> </dl>

 

 



