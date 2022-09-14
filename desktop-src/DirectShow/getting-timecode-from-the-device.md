---
description: Getting Timecode from the Device
ms.assetid: e3d06e0c-a595-4bc3-be62-168bd5122397
title: Getting Timecode from the Device
ms.topic: article
ms.date: 05/31/2018
---

# Getting Timecode from the Device

While a DV tape is playing or is in record-pause mode, you can retrieve the SMPTE timecode or the absolute track number. To do this, call the [**IAMTimecodeReader::GetTimecode**](/windows/desktop/api/Strmif/nf-strmif-iamtimecodereader-gettimecode) method. This method takes a pointer to a [**TIMECODE\_SAMPLE**](/windows/win32/api/strmif/ns-strmif-timecode_sample) structure, which describes the timecode. Before calling the method, initialize the **dwFlags** member of the structure. Use the value ED\_DEVCAP\_TIMECODE\_READ to retrieve the timecode or the value ED\_DEVCAP\_ATN\_READ to retrieve the absolute track number.

The **timecode** member of the **TIMECODE\_SAMPLE** structure is a TIMECODE structure. When the method returns, the **dwFrames** member of the TIMECODE structure contains the timecode or track number. For timecode, the hours, minutes, seconds, and frames are packed into a DWORD as binary coded decimal (BCD) values, with the format *hhmmssff*. Use bitmasks to extract the individual values.

The following example retrieves the timecode and track number.


```C++
if (MyDevCap.bHasTimecode)
{
    TIMECODE_SAMPLE TimecodeSample;
    TimecodeSample.timecode.dwFrames = 0;
    char szBuf[32];

    TimecodeSample.dwFlags = ED_DEVCAP_TIMECODE_READ;
    if (hr = MyDevCap.pTimecode->GetTimecode(&TimecodeSample),  SUCCEEDED(hr)) 
    {
        DWORD dwTime = TimecodeSample.timecode.dwFrames; // Packed BCD value.
        int hour  = ((dwTime & 0x0F000000) >> 24) + 
                    (10 * ((dwTime & 0xF0000000) >> 28));
        int min   = ((dwTime & 0x0F0000) >> 16) + 
                    (10 * ((dwTime & 0xF00000) >> 20));
        int sec   = ((dwTime & 0x0F00) >> 8) + 
                    (10 * ((dwTime & 0xF000) >> 12));
        int frame = (dwTime & 0x0F) + 
                    (10 * ((dwTime & 0xF0) >> 4));
    }

    TimecodeSample.dwFlags = ED_DEVCAP_ATN_READ;
    if (hr = MyDevCap.pTimecode->GetTimecode(&TimecodeSample), SUCCEEDED(hr)) 
    {
        DWORD dwTrackNumber = TimecodeSample.timecode.dwFrames;
    }
}
```



## Related topics

<dl> <dt>

[Controlling a DV Camcorder](controlling-a-dv-camcorder.md)
</dt> </dl>

 

 
