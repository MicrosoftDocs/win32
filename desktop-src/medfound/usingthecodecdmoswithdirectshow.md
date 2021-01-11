---
description: Using the Window Media Codecs in DirectShow
ms.assetid: 5b930447-6bf2-4bb3-8dfb-05f4c1e7cd64
title: Using the Window Media Codecs in DirectShow
ms.topic: article
ms.date: 05/31/2018
---

# Using the Window Media Codecs in DirectShow

The Windows Media Audio and Video encoder and decoder objects were originally designed and optimized to work with the ASF file container format and the Windows Media Format SDK. The codec objects work well in DirectShow for certain scenarios, namely one-pass CBR and quality based VBR encoding of video streams. But if you are considering using the codec objects directly in DirectShow using file containers other than ASF, there are certain behaviors and issues that you should be aware of in advance.

> [!Note]  
> If you are going to use standalone codecs with DirectShow, you will probably want to use them as DMOs only. In other words, you will be using the [**IMediaObject**](/previous-versions/windows/desktop/api/mediaobj/nn-mediaobj-imediaobject) interface instead of [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform).

 

## WM Audio in AVI Files

You can use DirectShow to encode WMA streams into any file container format for which you have a multiplexer filter. However, the Windows Media Audio and Video codec interfaces do not support WMA in AVI files because it is impossible, using the default DirectShow AVI playback filters, to maintain audio-video sync in an AVI file with a WMA stream. For more information, see [Storing Compressed Media in AVI Files](storingcompressedmediainavifiles.md).

The audio encoder DMO outputs samples of varying duration, even when in "constant bit rate" mode. It therefore works best with file container formats that use time stamps. AVI files do not provide a time stamp for each audio sample or group of samples. In DirectShow, the AVI Splitter filter manufactures time stamps for each group of samples (each audio frame) based on the **nAvgBytesPerSec** value in the [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure in the AVI stream header.

The assumption underlying this calculation is that all audio samples in the stream are of equal duration; however, the samples output by the DMO are not of equal duration, and so the time stamps applied by the AVI Splitter are not accurate. Therefore, it is not possible, without modifying either the AVI Splitter or the audio decoder DMO, to use any DirectShow-based application to play back AVI files with audio and video streams in sync. The Windows Media Audio 9 Voice codec will work in some cases, but even this will lose sync after any seek operation, so it really cannot be considered a viable solution.

If you have an MP3 encoder, you can create AVI files with WMV and MP3 for the audio stream. Such files will play back and seek correctly in Windows Media Player and other DirectShow-based applications, because the AVI Splitter contains special handling code for MP3 streams. Another option is to use uncompressed PCM audio, although obviously the resulting file size will be much larger than with a compressed audio stream. Because the DirectShow sample application creates AVI files, it does not demonstrate how to use the audio encoder DMO.

## One-pass Encoding

The video encoder DMO works easily in DirectShow for two encoding modes: CBR and quality based VBR. As long as you follow the correct order of operations when building the filter graph, as demonstrated in the sample application, it is relatively simple to place WMV content into an AVI file using the AVI Multiplexer and the File Writer.

## Two-pass Encoding

The two-pass encoding modes require a more complex approach to graph building and streaming in order to prevent the DMO from flushing its contents from the first pass before beginning the second pass. In two-pass encoding, it is necessary to run the graph once so the DMO can perform its preprocessing analysis of the file data, and then rewind the graph and run it again so that the DMO can do the actual encoding.

When the graph goes into a run state for the second pass, the DMO Wrapper sets the DISCONTINUITY flag on the first sample, because the time stamp is not sequential with the last time stamp on the first pass. When the DMO, which was not designed to work in DirectShow in this way, receives the DISCONTINUITY flag, it performs a flush and loses the data stored from the first pass. To work around this issue, the best solution is probably to write a custom DMO Wrapper filter that does not set the DISCONTINUITY flag when the graph is seeked after the first pass. The Video for Windows (VfW) sample in this SDK demonstrates how to perform two-pass encoding.

## Interlaced Content

The WMV encoder DMO is able to encode interlaced content while preserving the interlacing, which is useful for content that is captured from a TV and might also be played back on a TV. However, it is not possible to preserve interlacing using the default DMO Wrapper, because that filter does not support [**INSSBuffer**](/previous-versions/windows/desktop/api/wmsbuffer/nn-wmsbuffer-inssbuffer) on its input samples.

The DMO uses that interface to obtain the interlaced settings for each sample that it receives. If the interface is not found, as is the case with the DMO Wrapper, the DMO simply treats the input samples as noninterlaced. To perform interlaced encoding in DirectShow, there are several alternatives. The easiest approach is probably to use the Windows Media Format 9 Series SDK either directly or using the WM ASF Writer DirectShow filter, to create an interlaced ASF file. You can then transcode that file into some other format. If you transcode into AVI, you will have an interlaced file, but the standard DirectShow AVI playback filters will not recognize it as such because they do not support [**VIDEOINFOHEADER2**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-videoinfoheader2). Another approach is to write your own DMO Wrapper filter that supports the [**INSSBuffer**](/previous-versions/windows/desktop/api/wmsbuffer/nn-wmsbuffer-inssbuffer) interface.

## Related topics

<dl> <dt>

[Working with Codec DMOs](workingwithcodecdmos.md)
</dt> </dl>

 

 
