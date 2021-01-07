---
description: Video Streaming Sample Code
ms.assetid: 735af042-9800-4f75-a5c9-e1cf17b4a472
title: Video Streaming Sample Code
ms.topic: article
ms.date: 05/31/2018
---

# Video Streaming Sample Code

> [!Note]  
> These APIs are deprecated. Applications should use the [**Sample Grabber**](sample-grabber-filter.md) filter or implement a custom filter to get data from a DirectShow filter graph.

 

This sample code reads a file and renders it to a primary DirectDraw surface. For brevity, this example performs minimal error checking.


```C++
#include <stdio.h>
#include "ddraw.h"       // DirectDraw interfaces
#include "mmstream.h"    // multimedia stream interfaces
#include "amstream.h"    // DirectShow multimedia stream interfaces
#include "ddstream.h"    // DirectDraw multimedia stream interfaces

HRESULT RenderStreamToSurface(IDirectDrawSurface *pSurface, 
    IMultiMediaStream *pMMStream)
{    
    IMediaStream *pPrimaryVidStream;    
    IDirectDrawMediaStream *pDDStream;
    IDirectDrawStreamSample *pSample;
    RECT rect;
    DDSURFACEDESC ddsd;

    HRESULT hr;
    hr = pMMStream->GetMediaStream(MSPID_PrimaryVideo, &pPrimaryVidStream);
    if (FAILED(hr))
    {
        return hr;
    }
    pPrimaryVidStream->QueryInterface(IID_IDirectDrawMediaStream, (void **)&pDDStream);

    ddsd.dwSize = sizeof(ddsd);
    hr = pDDStream->GetFormat(&ddsd, NULL, NULL, NULL);
    if (SUCCEEDED(hr))
    {
        rect.top = rect.left = 0;
        rect.bottom = ddsd.dwHeight;
        rect.right = ddsd.dwWidth;
        hr = pDDStream->CreateSample(pSurface, &rect, 0, &pSample);
        if (SUCCEEDED(hr))
        {
            pMMStream->SetState(STREAMSTATE_RUN);
            while (pSample->Update(0, NULL, NULL, NULL) == S_OK)
            {
                // Empty loop.
            }
            pMMStream->SetState(STREAMSTATE_STOP);
            pSample->Release();    
        }
    }
    pDDStream->Release();
    pPrimaryVidStream->Release();
    return hr;
}

HRESULT RenderFileToMMStream(
    const char * szFileName, 
    IMultiMediaStream **ppMMStream,
    IDirectDraw *pDD)
{
    if (strlen(szFileName) > MAX_PATH)
    {
        return E_INVALIDARG;
    }

    IAMMultiMediaStream *pAMStream;
    HRESULT hr = CoCreateInstance(CLSID_AMMultiMediaStream, NULL, 
        CLSCTX_INPROC_SERVER, IID_IAMMultiMediaStream, 
        (void **)&pAMStream);
    if (FAILED(hr))
    {
        return hr;
    }

    WCHAR wPath[MAX_PATH + 1];
    MultiByteToWideChar(CP_ACP, 0, szFileName, -1, wPath, MAX_PATH + 1);

    pAMStream->Initialize(STREAMTYPE_READ, AMMSF_NOGRAPHTHREAD, NULL);
    pAMStream->AddMediaStream(pDD, &MSPID_PrimaryVideo, 0, NULL);
    pAMStream->AddMediaStream(NULL, &MSPID_PrimaryAudio, AMMSF_ADDDEFAULTRENDERER, NULL);
    hr = pAMStream->OpenFile(wPath, 0);
    if (SUCCEEDED(hr))
    {
        hr = pAMStream->QueryInterface(IID_IMultiMediaStream, 
            (void**)ppMMStream);
    }
    pAMStream->Release();
    return hr;
}

int __cdecl main(int argc, char *argv[])    
{    
    if (argc < 2) 
    {
        printf("Usage : showstrm movie.ext\n");
        exit(0);
    }    

    DDSURFACEDESC ddsd;
    IDirectDraw *pDD;    
    IDirectDrawSurface *pPrimarySurface;
    IMultiMediaStream *pMMStream;

    CoInitialize(NULL);

    DirectDrawCreate(NULL, &pDD, NULL);
    pDD->SetCooperativeLevel(GetDesktopWindow(), DDSCL_NORMAL);

    ddsd.dwSize = sizeof(ddsd);
    ddsd.dwFlags = DDSD_CAPS;
    ddsd.ddsCaps.dwCaps = DDSCAPS_PRIMARYSURFACE;
    pDD->CreateSurface(&ddsd, &pPrimarySurface, NULL);

    HRESULT hr = RenderFileToMMStream(argv[1], &pMMStream, pDD);
    if (SUCCEEDED(hr))
    {
        RenderStreamToSurface(pPrimarySurface, pMMStream);    
        pMMStream->Release();
    }
    pPrimarySurface->Release();    
    pDD->Release(); 
    
    CoUninitialize();
    return 0;
}
```



 

 



