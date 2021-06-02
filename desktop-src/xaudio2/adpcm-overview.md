---
description: Adaptive Differential Pulse Code Modulation (ADPCM) is a lossy compression format that is implemented for XAudio2 to provide additional features for specifying the size of the compression sample block.
ms.assetid: ae8a0a3e-293c-8193-d252-046d79771cfb
title: ADPCM Overview
ms.topic: article
ms.date: 05/31/2018
---

# ADPCM Overview

Adaptive Differential Pulse Code Modulation (ADPCM) is a lossy compression format that is implemented for XAudio2 to provide additional features for specifying the size of the compression sample block. With a lossy compression format some data is altered and lost during compression. ADPCM can achieve compression ratios of up to 4:1.

The implementation of ADPCM for XAudio2 provides additional features to specify the size of the compression sample block. ADPCM enables the audio designer to choose a setting that is an appropriate compromise among size, quality, and resolution (for placing loop points).

XAudio2 uses a modified version of the Microsoft ADPCM codec that supports the extended data formatting required to provide custom sample block sizes. For this reason, XAudio2 audio data cannot be played by audio engines that do not support this version of the ADPCM codec.

> [!Note]  
> Currently, ADPCM compression is only available for Windows, including XNA Game Studio Express for Windows deployments.

 

## ADPCM Encoding

Audio data is encoded to ADPCM using the AdpcmEncode command-line tool.

-   AdpcmEncode

    In order to encode audio files as ADPCM for use with XAudio2, use the **AdpcmEncode** command-line tool.

## ADPCM Decoding

Software decoding of ADPCM is supported in XAudio2.

-   XAudio2

    In order to use ADPCM encoded data in XAudio2, you need to initialize a **ADPCMWAVEFORMAT** structure with ADPCM specific values, and pass it as an argument to [**IXAudio2::CreateSourceVoice**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-createsourcevoice) when you create a source voice. For an example of loading and playing a sound in XAudio2, see [How to: Play a Sound with XAudio2](how-to--play-a-sound-with-xaudio2.md).

## SamplesPerBlock

ADPCM compression works by separating the waveform into blocks, and predicting the variation of the waveform samples within each block. The size of the blocks is measured in samples. The smallest block size is 32 samples, and the highest is 512 samples.

Larger blocks allow better compression, which results in smaller file sizes, but at the expense of sound quality and resolution for aligning loop points.

In general, modifying the SamplesPerBlock value results in these tradeoffs:



| If SamplesPerBlock...      | File Compression | Sound Quality | Loop Point Resolution |
|----------------------------|------------------|---------------|-----------------------|
| Increases (up to max 512)  | Increases        | Decreases     | Decreases             |
| Decreases (down to min 32) | Decreases        | Increases     | Increases             |



 

## Restrictions

Because ADPCM uses sample blocks that are aligned one after the other, a wave compressed with ADPCM may have an unfinished, partial block at its end. The ADPCM decoder generates silence for the remainder of this partial block, which keeps the wave from looping seamlessly.

The value of the *SamplesPerBlock* parameter affects the resolution with which you can align wave data and loop points.

If you try to apply compression to a non-aligned wave, you will get an error or a warning depending on whether the wave is used in any looping play events. You cannot compress a wave used in any looping play events. Remove it from the looping play events, and re-apply compression.

If you use the wave exclusively in non-looping mode, the sample block alignment restriction does not apply.

## ADPCM File Structure

An ADPCM file is a standard RIFF file with the following chunk types.



| Chunk FCC     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RIFF          | Standard RIFF chunk containing a file type with the value WAVE in the first four bytes of its data section and the other chunks in the file in the remainder of its data section.                                                                                                                                                                                                                                                                 |
| fmt           | Contains the format header for the ADPCM file. The data in this chunk corresponds to a **ADPCMWAVEFORMAT** structure.                                                                                                                                                                                                                                                                                                                             |
| data          | Contains the encoded ADPCM audio data. When you use ADPCM in XAudio2, you need to read the contents of the data chunk into a buffer, and pass it to a source voice as the **pAudioData** member of an [**XAUDIO2\_BUFFER**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_buffer) structure. You don't need to byte swap the contents of the data chunk.                                                                                                                            |
| smpl and wsmp | Optional chunk types containing the looping information for the ADPCM file. When you use ADPCM in XAudio2, the values contained in the smpl or wsmp chunks are used to populate the **LoopBeginLoopLength** and **LoopCount** members of the [**XAUDIO2\_BUFFER**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_buffer) structure. On the Xbox 360, you need to byte swap the data loaded from a smpl chunk to account for the endianness difference between Windows and Xbox 360. |



 

## Related topics

<dl> <dt>

[Programming Guide](programming-guide.md)
</dt> </dl>

 

 
