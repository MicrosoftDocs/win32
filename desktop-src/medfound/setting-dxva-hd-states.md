---
description: Setting DXVA-HD States
ms.assetid: 7f339ee8-01e6-4bbb-8563-020ff0e02499
title: Setting DXVA-HD States
ms.topic: article
ms.date: 05/31/2018
---

# Setting DXVA-HD States

During video processing, the Microsoft DirectX Video Acceleration High Definition (DXVA-HD) device maintains a persistent state from one frame to the next. Each state has a documented default. After you configure the device, set any states that you wish to change from their defaults. Before you process each frame, update any states that should change.

> [!Note]  
> This design differs from DXVA-VP. In DXVA-VP, the application must specify all of the VP parameters with each frame.

 

Device states fall into two categories:

-   *Stream* states apply each input stream separately. You can apply different settings to each stream.
-   *Blit* states apply globally to the entire video processing blit.

The following stream states are defined.



| Stream State                                   | Description                                                                                                     |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| **DXVAHD\_STREAM\_STATE\_D3DFORMAT**           | Input video format.                                                                                             |
| **DXVAHD\_STREAM\_STATE\_FRAME\_FORMAT**       | Interlacing.                                                                                                    |
| **DXVAHD\_STREAM\_STATE\_INPUT\_COLOR\_SPACE** | Input color space. This state specifies the RGB color range and the YCbCr transfer matrix for the input stream. |
| **DXVAHD\_STREAM\_STATE\_OUTPUT\_RATE**        | Output frame rate. This state controls frame-rate conversion.                                                   |
| **DXVAHD\_STREAM\_STATE\_SOURCE\_RECT**        | Source rectangle.                                                                                               |
| **DXVAHD\_STREAM\_STATE\_DESTINATION\_RECT**   | Destination rectangle.                                                                                          |
| **DXVAHD\_STREAM\_STATE\_ALPHA**               | Planar alpha.                                                                                                   |
| **DXVAHD\_STREAM\_STATE\_PALETTE**             | Color palette. This state applies only to palettized input formats.                                             |
| **DXVAHD\_STREAM\_STATE\_LUMA\_KEY**           | Luma key.                                                                                                       |
| **DXVAHD\_STREAM\_STATE\_ASPECT\_RATIO**       | Pixel aspect ratio.                                                                                             |
| **DXVAHD\_STREAM\_STATE\_FILTER\_Xxxx**        | Image filter settings. The driver can support brightness, contrast, and other image filters.                    |



 

The following blit states are defined:



| Blit State                                   | Description                                                                  |
|----------------------------------------------|------------------------------------------------------------------------------|
| **DXVAHD\_BLT\_STATE\_TARGET\_RECT**         | Target rectangle.                                                            |
| **DXVAHD\_BLT\_STATE\_BACKGROUND\_COLOR**    | Background color.                                                            |
| **DXVAHD\_BLT\_STATE\_OUTPUT\_COLOR\_SPACE** | Output color space.                                                          |
| **DXVAHD\_BLT\_STATE\_ALPHA\_FILL**          | Alpha fill mode.                                                             |
| **DXVAHD\_BLT\_STATE\_CONSTRICTION**         | Constriction. This state controls whether the device downsamples the output. |



 

To set a stream state, call the [**IDXVAHD\_VideoProcessor::SetVideoProcessStreamState**](/windows/desktop/api/dxvahd/nf-dxvahd-idxvahd_videoprocessor-setvideoprocessstreamstate) method. To set a blit state, call the [**IDXVAHD\_VideoProcessor::SetVideoProcessBltState**](/windows/desktop/api/dxvahd/nf-dxvahd-idxvahd_videoprocessor-setvideoprocessbltstate) method. In both of these methods, an enumeration value specifies the state to set. The state data is given using a state-specific data structure, which the application casts to a **void\*** type.

The following code example sets the input format and destination rectangle for stream 0, and sets the background color to black.


```C++
HRESULT SetDXVAHDStates(HWND hwnd, D3DFORMAT inputFormat)
{
    // Set the initial stream states.

    // Set the format of the input stream

    DXVAHD_STREAM_STATE_D3DFORMAT_DATA d3dformat = { inputFormat };

    HRESULT hr = g_pDXVAVP->SetVideoProcessStreamState(
        0,  // Stream index
        DXVAHD_STREAM_STATE_D3DFORMAT,
        sizeof(d3dformat),
        &d3dformat
        );

    if (SUCCEEDED(hr))
    { 
        // For this example, the input stream contains progressive frames.

        DXVAHD_STREAM_STATE_FRAME_FORMAT_DATA frame_format = { DXVAHD_FRAME_FORMAT_PROGRESSIVE };
        
        hr = g_pDXVAVP->SetVideoProcessStreamState(
            0, // Stream index
            DXVAHD_STREAM_STATE_FRAME_FORMAT,
            sizeof(frame_format),
            &frame_format
            );
    }

    if (SUCCEEDED(hr))
    { 
        // Compute the letterbox area.

        RECT rcDest;
        GetClientRect(hwnd, &rcDest);

        RECT rcSrc;
        SetRect(&rcSrc, 0, 0, VIDEO_WIDTH, VIDEO_HEIGHT);

        rcDest = LetterBoxRect(rcSrc, rcDest);

        // Set the destination rectangle, so the frame is displayed within the 
        // letterbox area. Otherwise, the frame is stretched to cover the 
        // entire surface.

        DXVAHD_STREAM_STATE_DESTINATION_RECT_DATA DstRect = { TRUE, rcDest };

        hr = g_pDXVAVP->SetVideoProcessStreamState(
            0, // Stream index 
            DXVAHD_STREAM_STATE_DESTINATION_RECT,
            sizeof(DstRect),
            &DstRect
            );
    }

    if (SUCCEEDED(hr))
    { 
        DXVAHD_COLOR_RGBA rgbBackground = { 0.0f, 0.0f, 0.0f, 1.0f };  // RGBA

        DXVAHD_BLT_STATE_BACKGROUND_COLOR_DATA background = { FALSE, rgbBackground };

        hr = g_pDXVAVP->SetVideoProcessBltState(
            DXVAHD_BLT_STATE_BACKGROUND_COLOR,
            sizeof (background),
            &background
            );
    }

    return hr;
}
```



## Related topics

<dl> <dt>

[DXVA-HD](dxva-hd.md)
</dt> </dl>

 

 



