---
title: Processing the Audio Data
description: Processing the Audio Data
ms.assetid: ba41e3f4-d991-4da6-9091-7a7e42622e76
keywords:
- Windows Media Player plug-ins,Echo sample DoProcessOutput method
- plug-ins,Echo sample DoProcessOutput method
- digital signal processing plug-ins,Echo sample DoProcessOutput method
- DSP plug-ins,Echo sample DoProcessOutput method
- Echo DSP plug-in sample,DoProcessOutput method
- Echo DSP plug-in sample,audio data
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Processing the Audio Data

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The default implementation of **DoProcessOutput** begins by retrieving a pointer to a valid **WAVEFORMATEX** structure, exactly like was done in **AllocateStreamingResources**. It then uses the information in that structure to calculate the number of samples in the input buffer waiting to be processed. The following code is from the default implementation:


```C++
// Get a pointer to the valid WAVEFORMATEX structure
// for the current media type.
WAVEFORMATEX *pWave = ( WAVEFORMATEX * ) m_mtInput.pbFormat;

// Calculate the number of samples to process.
DWORD dwSamplesToProcess = (*cbBytesProcessed / pWave->nBlockAlign) * pWave->nChannels;

```



Then, the code inspects the **wBitsPerSample** member to determine the bit depth of the audio. This value is used in a switch statement to provide separate processing for 8-bit and 16-bit audio.

## Differences Between 8-bit and 16-bit Audio

There are important differences between 8-bit and 16-bit audio. Therefore, the processing routines to create the echo effect are different. The two formats differ in the following ways:

-   Each format has a different sample size: 8-bit samples each occupy one byte of memory, while 16-bit samples each occupy two bytes.
-   Each format represents the audio amplitude differently. 8-bit audio is represented by an unsigned integer with a range from 0 to 255; a value of 128 represents silence. 16-bit audio is represented by a signed integer with a range from -32768 to 32767; a value of zero represents silence.

While the process of creating the echo effect is fundamentally identical for each format, the details must differ slightly.

## Related topics

<dl> <dt>

[**Implementing CEcho::DoProcessOutput**](implementing-cecho--doprocessoutput.md)
</dt> </dl>

 

 




