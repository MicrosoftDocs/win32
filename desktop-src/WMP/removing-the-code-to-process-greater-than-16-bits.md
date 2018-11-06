---
title: Removing the Code to Process Greater than 16 Bits
description: Removing the Code to Process Greater than 16 Bits
ms.assetid: 90c165e1-bc77-42a5-878d-056762c62991
keywords:
- Windows Media Player plug-ins,Echo sample DoProcessOutput method
- plug-ins,Echo sample DoProcessOutput method
- digital signal processing plug-ins,Echo sample DoProcessOutput method
- DSP plug-ins,Echo sample DoProcessOutput method
- Echo DSP plug-in sample,DoProcessOutput method
- Echo DSP plug-in sample,processing greater than 16 bits
ms.topic: article
ms.date: 05/31/2018
---

# Removing the Code to Process Greater than 16 Bits

Because this sample only processes 8-bit or 16-bit audio, you need to modify the code in **CEcho::ValidateMediaType** to return DMO\_E\_TYPE\_NOT\_ACCEPTED for media types greater than 16 bits. To accomplish this, you must change the code in the switch block that tests formats of type WAVE\_FORMAT\_EXTENSIBLE. Replace the wizard code with the following example code:


```C++
case WAVE_FORMAT_EXTENSIBLE:
    {
         // Sample size is greater than 16-bit or is multichannel.
        WAVEFORMATEXTENSIBLE *pWaveXT = (WAVEFORMATEXTENSIBLE *) pWave;

        if (KSDATAFORMAT_SUBTYPE_PCM != pWaveXT->SubFormat)
        {
            return DMO_E_TYPE_NOT_ACCEPTED;
        }
    }
    break;

```



Next, delete or comment out the sections of code in **DoProcessOutput** that handle high bit resolution audio. These are the sections that begin with case 24 and case 32.

## Related topics

<dl> <dt>

[**Implementing CEcho::DoProcessOutput**](implementing-cecho--doprocessoutput.md)
</dt> </dl>

 

 




