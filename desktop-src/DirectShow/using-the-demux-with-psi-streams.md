---
Description: Using the Demux with PSI Streams
ms.assetid: 355e905e-ff21-4bde-a018-ed9631ef5ed5
title: Using the Demux with PSI Streams
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using the Demux with PSI Streams

To get PSI information from an MPEG-2 transport stream using the MPEG-2 demux filter, create an output pin on the demux with the following media type:

-   Major type: KSDATAFORMAT\_TYPE\_MPEG2\_SECTIONS
-   Subtype: MEDIASUBTYPE\_None
-   Format type: GUID\_NULL

Then call the output pin's [**IMPEG2PIDMap::MapPID**](/windows/win32/Bdaiface/nf-bdaiface-impeg2pidmap-mappid?branch=master) method with the desired PID and the flag MEDIA\_MPEG2\_PSI.


```C++
// Query the demux filter for IMpeg2Demultiplexer.
IMpeg2Demultiplexer *pDemux = NULL;
hr = pFilter->QueryInterface(IID_IMpeg2Demultiplexer, (void**)&amp;pDemux);
if (SUCCEEDED(hr))
{
    // Define the media type.
    AM_MEDIA_TYPE mt;
    ZeroMemory(&amp;mt, sizeof(AM_MEDIA_TYPE));
    mt.majortype = KSDATAFORMAT_TYPE_MPEG2_SECTIONS;
    mt.subtype = MEDIASUBTYPE_None;

    // Create a new output pin.
    IPin *pPin;
    hr = pDemux->CreateOutputPin(&amp;mt, L"PSI Pin", &amp;pPin);
    if (SUCCEEDED(hr))
    {
        // Map the PID.
        IMPEG2PIDMap *pPidMap = NULL;
        hr = pPin->QueryInterface(IID_IMPEG2PIDMap, (void**)&amp;pPidMap);
        if (SUCCEEDED(hr))
        {
            ULONG Pid[] = { 0x00 }; // Map any desired PIDs. 
            ULONG cPid = 1;
            hr = pPidMap->MapPID(cPid, Pid, MEDIA_MPEG2_PSI);
            pPidMap->Release();
        }
        pPin->Release();
    }
    pDemux->Release();
}
```



Each complete PSI section is delivered in one media sample. To retrieve the PID number associated with a table section, call [**IMediaSample2::GetProperties**](/windows/win32/Strmif/nf-strmif-imediasample2-getproperties?branch=master) on the media sample. The PID is given in the low 13 bits of the **dwTypeSpecificFlags** flag in the **AM\_SAMPLE2\_PROPERTIES** structure. This is useful if you map multiple PSI PIDs to the same output pin.

## Related topics

<dl> <dt>

[Using the MPEG-2 Demultiplexer](using-the-mpeg-2-demultiplexer.md)
</dt> </dl>

 

 



