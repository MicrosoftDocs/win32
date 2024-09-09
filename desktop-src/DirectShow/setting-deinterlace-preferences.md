---
description: Setting Deinterlace Preferences
ms.assetid: 31d59f17-552b-46d1-89e4-751216f54280
title: Setting Deinterlace Preferences
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Setting Deinterlace Preferences

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Video Mixing Renderer (VMR) supports hardware-accelerated deinterlacing, which improves rendering quality for interlaced video. The exact features that are available depend on the underlying hardware. The application can query for the hardware deinterlacing capabilities and set deinterlacing preferences through the [**IVMRDeinterlaceControl**](/windows/desktop/api/Strmif/nn-strmif-ivmrdeinterlacecontrol) interface (VMR-7) or [**IVMRDeinterlaceControl9**](/previous-versions/windows/desktop/api/Vmr9/nn-vmr9-ivmrdeinterlacecontrol9) interface (VMR-9). Deinterlacing is performed on a per-stream basis.

There is one important difference in interlacing behavior between the VMR-7 and the VMR-9. On systems where the graphics hardware doesn't support advanced deinterlacing, the VMR-7 can fall back to the hardware overlay and instruct it to use a BOB style deinterlace. In this case, although the VMR is reporting 30fps the video is actually being rendered at 60 flips per second.

Except in the case of the VMR-7 using hardware overlay, deinterlacing is performed by the VMR's mixer. The mixer uses the DirectX Video Acceleration (DXVA) deinterlacing device driver interface (DDI) to perform the deinterlacing. This DDI is not callable by applications, and applications cannot replace the VMR's deinterlacing functionality. However, an application can select the desired deinterlacing mode, as described in this section.

> [!Note]  
> This section describes the **IVMRDeinterlaceControl9** methods, but the VMR-7 versions are almost identical.

 

To get the deinterlacing capabilities for a video stream, do the following:

1.  Fill in a [**VMR9VideoDesc**](/previous-versions/windows/desktop/api/Vmr9/ns-vmr9-vmr9videodesc) structure with a description of the video stream. Details of how to fill in this structure are given later.
2.  Pass the structure to the [**IVMRDeinterlaceControl9::GetNumberOfDeinterlaceModes**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrdeinterlacecontrol9-getnumberofdeinterlacemodes) method. Call the method twice. The first call returns the number of deinterlace modes the hardware supports for the specified format. Allocate an array of GUIDs of this size, and call the method again, passing in the address of the array. The second call fills the array with GUIDs. Each GUID identifies one deinterlacing mode.
3.  To get the capabiltiies of a particular mode, call the [**IVMRDeinterlaceControl9::GetDeinterlaceModeCaps**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrdeinterlacecontrol9-getdeinterlacemodecaps) method. Pass in the same **VMR9VideoDesc** structure, along with one of the GUIDs from the array. The method fills a [**VMR9DeinterlaceCaps**](/previous-versions/windows/desktop/api/Vmr9/ns-vmr9-vmr9deinterlacecaps) structure with the mode capabilities.

The following code shows these steps:


```C++
VMR9VideoDesc VideoDesc; 
DWORD dwNumModes = 0;
// Fill in the VideoDesc structure (not shown).
hr = pDeinterlace->GetNumberOfDeinterlaceModes(&VideoDesc, 
    &dwNumModes, NULL);
if (SUCCEEDED(hr) && (dwNumModes != 0))
{
    // Allocate an array for the GUIDs that identify the modes.
    GUID *pModes = new GUID[dwNumModes];
    if (pModes)
    {
        // Fill the array.
        hr = pDeinterlace->GetNumberOfDeinterlaceModes(&VideoDesc, 
            &dwNumModes, pModes);
        if (SUCCEEDED(hr))
        {
            // Loop through each item and get the capabilities.
            for (int i = 0; i < dwNumModes; i++)
            {
                VMR9DeinterlaceCaps Caps;
                hr = pDeinterlace->GetDeinterlaceModeCaps(pModes + i, 
                    &VideoDesc, &Caps);
                if (SUCCEEDED(hr))
                {
                    // Examine the Caps structure.
                }
            }
        }
        delete [] pModes;
    }
}
```



Now the application can set the deinterlacing mode for the stream, using the following methods:

-   The [**SetDeinterlaceMode**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrdeinterlacecontrol9-setdeinterlacemode) method sets the preferred mode. Use GUID\_NULL to turn off deinterlacing.
-   The [**SetDeinterlacePrefs**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrdeinterlacecontrol9-setdeinterlaceprefs) method specifies the behavior if the requested mode is not available.
-   The [**GetDeinterlaceMode**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrdeinterlacecontrol9-getdeinterlacemode) method returns the preferred mode that you set.
-   The [**GetActualDeinterlaceMode**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrdeinterlacecontrol9-getactualdeinterlacemode) method returns the actual mode in use, which might be a fallback mode, if the preferred mode is not available.

The method reference pages give more information.

**Using the VMR9VideoDesc Structure**

In the procedure given previously, the first step is to fill in a **VMR9VideoDesc** structure with a description of the video stream. Start by getting the media type of the video stream. You can do this by calling [**IPin::ConnectionMediaType**](/windows/desktop/api/Strmif/nf-strmif-ipin-connectionmediatype) on the VMR filter's input pin. Then confirm whether the video stream is interlaced. Only [**VIDEOINFOHEADER2**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-videoinfoheader2) formats can be interlaced. If the format type is FORMAT\_VideoInfo, it must be a progressive frame. If the format type is FORMAT\_VideoInfo2, check the **dwInterlaceFlags** field for the AMINTERLACE\_IsInterlaced flag. The presence of this flag indicates the video is interlaced.

Assume that the variable **pBMI** is a pointer to the [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) structure in the format block. Set the following values in the **VMR9VideoDesc** structure:

-   **dwSize**: Set this field to `sizeof(VMR9VideoDesc)`.
-   **dwSampleWidth**: Set this field to `pBMI->biWidth`.
-   **dwSampleHeight**: Set this field to `abs(pBMI->biHeight)`.
-   **SampleFormat**: This field describes the interlace characteristics of the media type. Check the **dwInterlaceFlags** field in the **VIDEOINFOHEADER2** structure, and set **SampleFormat** equal to the equivalent [**VMR9\_SampleFormat**](/previous-versions/windows/desktop/api/Vmr9/ne-vmr9-vmr9_sampleformat) flag. A helper function to do this is given below.
-   **InputSampleFreq**: This field gives the input frequency, which can be calculated from the **AvgTimePerFrame** field in the **VIDEOINFOHEADER2** structure. In the general case, set **dwNumerator** to 10000000, and set **dwDenominator** to **AvgTimePerFrame**. However, you can also check for some well-known frame rates:

    | Average time per frame | Frame rate (fps) | Numerator | Denominator |
    |------------------------|------------------|-----------|-------------|
    | 166833                 | 59.94 (NTSC)     | 60000     | 1001        |
    | 333667                 | 29.97 (NTSC)     | 30000     | 1001        |
    | 417188                 | 23.97 (NTSC)     | 24000     | 1001        |
    | 200000                 | 50.00 (PAL)      | 50        | 1           |
    | 400000                 | 25.00 (PAL)      | 25        | 1           |
    | 416667                 | 24.00 (Film)     | 24        | 1           |

    

     

-   **OutputFrameFreq**: This field gives the output frequency, which can be calculated from the **InputSampleFreq** value and the interleaving characteristics of the input stream:
    -   Set **OutputFrameFreq.dwDenominator** equal to **InputSampleFreq.dwDenominator**.
    -   If the input video is interleaved, set **OutputFrameFreq.dwNumerator** to 2 x **InputSampleFreq.dwNumerator**. (After deinterlacing, the frame rate is doubled.) Otherwise, set the value to **InputSampleFreq.dwNumerator**.
-   **dwFourCC**: Set this field to `pBMI->biCompression`.

The following helper function converts AMINTERLACE\_*X* flags to [**VMR9\_SampleFormat**](/previous-versions/windows/desktop/api/Vmr9/ne-vmr9-vmr9_sampleformat) values:


```C++
#define IsInterlaced(x) ((x) & AMINTERLACE_IsInterlaced)
#define IsSingleField(x) ((x) & AMINTERLACE_1FieldPerSample)
#define IsField1First(x) ((x) & AMINTERLACE_Field1First)

VMR9_SampleFormat ConvertInterlaceFlags(DWORD dwInterlaceFlags)
{
    if (IsInterlaced(dwInterlaceFlags)) {
        if (IsSingleField(dwInterlaceFlags)) {
            if (IsField1First(dwInterlaceFlags)) {
                return VMR9_SampleFieldSingleEven;
            }
            else {
                return VMR9_SampleFieldSingleOdd;
            }
        }
        else {
            if (IsField1First(dwInterlaceFlags)) {
                return VMR9_SampleFieldInterleavedEvenFirst;
             }
            else {
                return VMR9_SampleFieldInterleavedOddFirst;
            }
        }
    }
    else {
        return VMR9_SampleProgressiveFrame;  // Not interlaced.
    }
}
```



 

 



