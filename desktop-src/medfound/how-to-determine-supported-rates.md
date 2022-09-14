---
description: How to Determine Supported Rates
ms.assetid: 7f2b64e1-1062-4f77-b8e0-62b6d962ae8b
title: How to Determine Supported Rates
ms.topic: article
ms.date: 05/31/2018
---

# How to Determine Supported Rates

Before changing the playback rate, an application should check whether the playback rate is supported by the objects in the pipeline. The [**IMFRateSupport**](/windows/desktop/api/mfidl/nn-mfidl-imfratesupport) interface provides methods to get the maximum forward and reverse rates, the supported rate nearest to a requested rate, and the slowest rate. Each of these rate queries can specify the playback direction and whether to use thinning. The exact playback rate is queried by using the [**IMFRateControl**](/windows/desktop/api/mfidl/nn-mfidl-imfratecontrol) interface.

For information about changing playback rates, see [How to Set the Playback Rate on the Media Session](how-to-set-the-playback-rate-on-the-media-session.md).

For general information about playback rates, see [About Rate Control](about-rate-control.md).

## To determine the current playback rate

1.  Get the rate control service from the Media Session.

    ```C++
    IMFRateControl *pRateControl = NULL;
    hr = MFGetService(
           pMediaSession, 
           MF_RATE_CONTROL_SERVICE,
           IID_IMFRateControl, 
           (void**) &pRateControl );
    ```

    

    Pass an initialized [**IMFMediaSession**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasession) interface pointer in the *punkObject* parameter of [**MFGetService**](/windows/desktop/api/mfidl/nf-mfidl-mfgetservice).

    The application must query for the rate control service through the Media Session. Internally, the Media Session queries the objects in the topology.

2.  Call the [**IMFRateControl::GetRate**](/windows/desktop/api/mfidl/nf-mfidl-imfratecontrol-getrate) method to get the current playback rate.

    ```C++
    hr = pRateControl->GetRate(&bThin, &rate);
    ```

    

    The *pfThin* parameter of [**GetRate**](/windows/desktop/api/mfidl/nf-mfidl-imfratecontrol-getrate) receives a **BOOL** value that indicates whether the stream is currently being thinned. The application must pass **NULL** if it does not want to query thinning support for the stream. The *pflRate* parameter receives the current playback rate.

## To determine the nearest supported rate

1.  Get the rate support service from the Media Session.

    ```C++
    IMFRateSupport *pRateSupport = NULL;
    hr = MFGetService(
           pMediaSession, 
           MF_RATE_CONTROL_SERVICE,
           IID_IMFRateSupport, 
           (void**) &pRateSupport );
    ```

    

    Pass an initialized [**IMFMediaSession**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasession) interface pointer in the *punkObject* parameter of [**MFGetService**](/windows/desktop/api/mfidl/nf-mfidl-mfgetservice).

2.  Call the [**IMFRateSupport::IsRateSupported**](/windows/desktop/api/mfidl/nf-mfidl-imfratesupport-isratesupported) method to retrieve the supported rate nearest to a requested playback rate.

    ```C++
    float rateRequested = 4.0;
    float actualRate = 0;
    hr = pRateSupport->IsRateSupported(
           TRUE, 
           rateRequested, 
           &actualRate );
    ```

    

    The example queries whether a playback rate of 4.0 is supported with thinning. This is indicated by passing **TRUE** in the *fThin* parameter of [**IsRateSupported**](/windows/desktop/api/mfidl/nf-mfidl-imfratesupport-isratesupported). If this rate is supported, *actualRate* contains the playback rate of 4.0, and the call succeeds with a return value of S\_OK. If the exact playback rate is not supported, the nearest supported rate is received in *actualRate*. If the rate is not supported and there is no available nearest playback rate, the call returns an appropriate error code.

    These values can change depending on which pipeline components are loaded. Therefore, you should query the values again whenever you load a new topololgy.

    If the desired playback rate is not supported, one option is to query each object in the topology individually, to find out if a particular component does not support the rate. You might be able to rebuild the topology without this component and then play at the desired rate. For example, if every component except the audio renderer supports a given rate, you could rebuild the topology without the audio branch and play at the desired rate without audio.

## To determine the slowest supported rate

1.  Get the rate support service from the Media Session.

    ```C++
    IMFRateSupport *pRateSupport = NULL;
    hr = MFGetService(
           pMediaSession, 
           MF_RATE_CONTROL_SERVICE,
           IID_IMFRateSupport, 
           (void**) &pRateSupport );
    ```

    

    Pass an initialized [**IMFMediaSession**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasession) interface pointer in the *punkObject* parameter of [**MFGetService**](/windows/desktop/api/mfidl/nf-mfidl-mfgetservice).

2.  Call the [**IMFRateSupport::GetSlowestRate**](/windows/desktop/api/mfidl/nf-mfidl-imfratesupport-getslowestrate) method to retrieve the slowest supported rate.

    ```C++
    float slowestRate = 0;
    hr = pRateSupport->GetSlowestRate(
           MFRATE_REVERSE, 
           TRUE, 
           &slowestRate);
    ```

    

    The example queries for the slowest reverse playback rate with thinning. The lower bound rate is received in *slowestRate* parameter of [**GetSlowestRate**](/windows/desktop/api/mfidl/nf-mfidl-imfratesupport-getslowestrate).

    If reverse playback or thinning is not supported, the call returns an appropriate error code.

## Related topics

<dl> <dt>

[Media Session](media-session.md)
</dt> <dt>

[Rate Control](rate-control.md)
</dt> <dt>

[Seeking, Fast Forward, and Reverse Play](seeking--fast-forward--and-reverse-play.md)
</dt> </dl>

 

 



