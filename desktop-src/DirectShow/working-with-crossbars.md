---
description: Working with Crossbars
ms.assetid: 6e8ee9c3-6776-498b-ad38-36f8172a27ae
title: Working with Crossbars
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Working with Crossbars

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

If a video capture card has more than one physical input, or supports more than one hardware path for data, then the filter graph may contain the [Analog Video Crossbar Filter](analog-video-crossbar-filter.md). The Capture Graph Builder automatically adds this filter when needed; it will be upstream from the capture filter. Depending on the hardware, the filter graph might contain more than one instance of the crossbar filter.

The crossbar filter exposes the [**IAMCrossbar**](/windows/desktop/api/Strmif/nn-strmif-iamcrossbar) interface, which you can use to route a particular input to a particular output. For example, a video card might have a coaxial connector and an S-Video input. These would be represented as input pins on the crossbar filter. To select an input, route the corresponding input pin to the crossbar's output pin, using the [**IAMCrossbar::Route**](/windows/desktop/api/Strmif/nf-strmif-iamcrossbar-route) method.

To locate crossbar filters in the graph, you can use the [**ICaptureGraphBuilder2::FindInterface**](/windows/desktop/api/Strmif/nf-strmif-icapturegraphbuilder2-findinterface) method to search for filters that support **IAMCrossbar**. For example, the following code searches for two crossbars:


```C++
// Search upstream for a crossbar.
IAMCrossbar *pXBar1 = NULL;
hr = pBuild->FindInterface(&LOOK_UPSTREAM_ONLY, NULL, pSrc,
        IID_IAMCrossbar, (void**)&pXBar1);
if (SUCCEEDED(hr)) 
{
    // Found one crossbar. Get its IBaseFilter interface.
    IBaseFilter *pFilter = NULL;
    hr = pXBar1->QueryInterface(IID_IBaseFilter, (void**)&pFilter);
    if (SUCCEEDED(hr)) 
    {
        // Search upstream for another crossbar.
        IAMCrossbar *pXBar2 = NULL;
        hr = pBuild->FindInterface(&LOOK_UPSTREAM_ONLY, NULL, pFilter,
                 IID_IAMCrossbar, (void**)&pXBar2);
        pFilter->Release();

        if (SUCCEEDED(hr))
        {
            /* ... */
            pXBar2->Release();
        }
    }
    pXBar1->Release();
}
```



For a more generalized approach, see the CCrossbar class in the [AmCap Sample](amcap-sample.md).

Once you have a pointer to the **IAMCrossbar** interface, you can get information about the crossbar filter, including the physical type of each pin, and the matrix of which input pins can be routed to which output pins.

-   To determine the type of physical connector to which a pin corresponds, call the [**IAMCrossbar::get\_CrossbarPinInfo**](/windows/desktop/api/Strmif/nf-strmif-iamcrossbar-get_crossbarpininfo) method. The method returns a member of the [**PhysicalConnectorType**](/windows/win32/api/strmif/ne-strmif-physicalconnectortype) enumeration. For example, an S-Video pin returns the value PhysConn\_Video\_SVideo.

    The **get\_CrossbarInfo** method also indicates whether two pins are related to each other. For example, a video tuner pin might be related to an audio tuner pin. Related pins have the same pin direction, and are typically part of the same physical jack or connector on the card.

-   To determine whether you can route an input pin to a particular output pin, call the [**IAMCrossbar::CanRoute**](/windows/desktop/api/Strmif/nf-strmif-iamcrossbar-canroute) method.
-   To determine the current routing between pins, call the [**IAMCrossbar::get\_IsRoutedTo**](/windows/desktop/api/Strmif/nf-strmif-iamcrossbar-get_isroutedto) method.

The previous methods all specify pins by index number, with output pins and input pins both indexed from zero. Call the **IAMCrossbar::get\_PinCounts** method to find the number of pins on the filter.

For example, the following code displays information about a crossbar filter to the console window:


```C++
// Helper function to associate a name with the type.
const char * GetPhysicalPinName(long lType)
{
    switch (lType) 
    {
    case PhysConn_Video_Tuner:            return "Video Tuner";
    case PhysConn_Video_Composite:        return "Video Composite";
    case PhysConn_Video_SVideo:           return "S-Video";
    case PhysConn_Video_RGB:              return "Video RGB";
    case PhysConn_Video_YRYBY:            return "Video YRYBY";
    case PhysConn_Video_SerialDigital:    return "Video Serial Digital";
    case PhysConn_Video_ParallelDigital:  return "Video Parallel Digital"; 
    case PhysConn_Video_SCSI:             return "Video SCSI";
    case PhysConn_Video_AUX:              return "Video AUX";
    case PhysConn_Video_1394:             return "Video 1394";
    case PhysConn_Video_USB:              return "Video USB";
    case PhysConn_Video_VideoDecoder:     return "Video Decoder";
    case PhysConn_Video_VideoEncoder:     return "Video Encoder";
        
    case PhysConn_Audio_Tuner:            return "Audio Tuner";
    case PhysConn_Audio_Line:             return "Audio Line";
    case PhysConn_Audio_Mic:              return "Audio Microphone";
    case PhysConn_Audio_AESDigital:       return "Audio AES/EBU Digital";
    case PhysConn_Audio_SPDIFDigital:     return "Audio S/PDIF";
    case PhysConn_Audio_SCSI:             return "Audio SCSI";
    case PhysConn_Audio_AUX:              return "Audio AUX";
    case PhysConn_Audio_1394:             return "Audio 1394";
    case PhysConn_Audio_USB:              return "Audio USB";
    case PhysConn_Audio_AudioDecoder:     return "Audio Decoder";
        
    default:                              return "Unknown Type";
    }    
}

void DisplayCrossbarInfo(IAMCrossbar *pXBar)
{
    HRESULT hr;
    long cOutput = -1, cInput = -1;
    hr = pXBar->get_PinCounts(&cOutput, &cInput);

    for (long i = 0; i < cOutput; i++)
    {
        long lRelated = -1, lType = -1, lRouted = -1;

        hr = pXBar->get_CrossbarPinInfo(FALSE, i, &lRelated, &lType);
        hr = pXBar->get_IsRouted(i, &lRouted);

        printf("Output pin %d: %s\n", i, GetPhysicalPinName(lType));
        printf("\tRelated out: %d, Routed in: %d\n", lRelated, lRouted);
        printf("\tSwitching Matrix: ");

        for (long j = 0; j < cInput; j++)
        {
            hr = pXBar->CanRoute(i, j);
            printf("%d-%s", j, (S_OK == hr ? "Yes" : "No"));
        }
        printf("\n\n");
    }

    for (i = 0; i < cInput; i++)
    {
        long lRelated = -1, lType = -1;

        hr = pXBar->get_CrossbarPinInfo(TRUE, i, &lRelated, &lType);

        printf("Input pin %d - %s\n", i, GetPhysicalPinName(lType));
        printf("\tRelated in: %d\n", lRelated);
    }
}
```



For a hypothetical card, this function might produce the following output:


```C++
Output pin 0: S-Video
    Related out: 2, Routed in: 0
    Switching Matrix: 0-Yes 1-No 2-No 3-No
Output pin 1 - Video Tuner
    Related out: 2, Routed in: 1
    Switching Matrix: 0-No 1-Yes 2-No 3-No
Output pin 2 - Audio decoder
    Related out: 1, Routed in: -1
    Switching Matrix: 0-No 1-No 2-Yes 3-Yes

Input pin 0 - S-Video
    Related in: 2
Input pin 1 - Video Tuner
    Related in: 3
Input pin 2 - Audio line
    Related in: 0
Input pin 3 - Audio tuner
    Related in: 1
```



On the output side, the S-Video and the video tuner are both related to the audio decoder. On the input side, the video tuner is related to the audio tuner, and the S-Video is related to the audio line in. The S-Video input is routed to the S-Video output; and the video tuner input is routed to the video tuner output. Currently nothing is routed to the audio decoder, but either the audio line in or the audio tuner could be routed to it.

You can change the existing routing by calling the [**IAMCrossbar::Route**](/windows/desktop/api/Strmif/nf-strmif-iamcrossbar-route) method.

 

 



