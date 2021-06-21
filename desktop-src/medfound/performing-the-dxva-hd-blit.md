---
description: Performing the DXVA-HD Blit
ms.assetid: fc68704e-68d5-4767-b464-e45ab4c86058
title: Performing the DXVA-HD Blit
ms.topic: article
ms.date: 05/31/2018
---

# Performing the DXVA-HD Blit


```C++
BOOL ProcessVideoFrame(HWND hwnd, UINT frameNumber)
{
    if (!g_pD3D || !g_pDXVAVP)
    {
        return FALSE;
    }

    RECT client;
    GetClientRect(hwnd, &client);

    if (IsRectEmpty(&client))
    {
        return TRUE;
    }

    // Check the current status of D3D9 device.  
    HRESULT hr = TestCooperativeLevel();

    switch (hr)
    {
    case D3D_OK :
        break;

    case D3DERR_DEVICELOST :
        return TRUE;

    case D3DERR_DEVICENOTRESET :
        return FALSE;
        break;

    default :
        return FALSE;
    }

    IDirect3DSurface9 *pRT = NULL;  // Render target

    DXVAHD_STREAM_DATA stream_data = { 0 };

    // Get the render-target surface.
    hr = g_pD3DDevice->GetBackBuffer(0, 0, D3DBACKBUFFER_TYPE_MONO, &pRT);
    if (FAILED(hr)) 
    { 
        goto done; 
    }

    // Initialize the stream data structures for the primary video stream 
    // and the substream.

    stream_data.Enable = TRUE;
    stream_data.OutputIndex = 0;
    stream_data.InputFrameOrField = 0;
    stream_data.pInputSurface = g_pSurface;
 
    // Perform the blit.
    hr = g_pDXVAVP->VideoProcessBltHD(
        pRT,
        frameNumber,
        1,
        &stream_data
        );

    if (FAILED(hr)) { 
        goto done; 
    }

    // Present the frame.
    hr = g_pD3DDevice->Present(NULL, NULL, NULL, NULL);

done:
    SafeRelease(&pRT);
    return SUCCEEDED(hr);
}
```



## Related topics

<dl> <dt>

[DXVA-HD](dxva-hd.md)
</dt> </dl>

 

 



