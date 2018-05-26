---
Description: Codec API Enumerations
ms.assetid: 5d6e48cb-d181-448e-a96e-e5ab500427d7
title: Codec API Enumerations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Codec API Enumerations



| Enumeration                                                                              | Description                                                                                               |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [**eAVAudioChannelConfig**](/windows/win32/codecapi/ne-codecapi-eavaudiochannelconfig?branch=master)                                   | Specifies the speaker configuration for the audio channels in the audio bit stream.                       |
| [**eAVDDSurroundMode**](/windows/win32/codecapi/ne-codecapi-eavddsurroundmode?branch=master)                                           | Specifies whether the audio is encoded in Dolby Surround.                                                 |
| [**eAVDecAACDownmixMode**](/windows/win32/codecapi/?branch=master)                                     | Specifies whether an AAC decoder uses standard MPEG-2/MPEG-4 stereo downmix equations.                    |
| [**eAVDecAudioDualMono**](/windows/win32/codecapi/ne-codecapi-eavdecaudiodualmono?branch=master)                                       | Specifies whether the input audio stream is stereo or dual mono.                                          |
| [**eAVDecAudioDualMonoReproMode**](/windows/win32/codecapi/ne-codecapi-eavdecaudiodualmonorepromode?branch=master)                     | Specifies how the decoder reproduces dual mono audio.                                                     |
| [**eAVDecDDOperationalMode**](/windows/win32/codecapi/ne-codecapi-eavdecddoperationalmode?branch=master)                               | Specifies the compression control mode for a Dolby AC-3 audio stream.                                     |
| [**eAVDecHEAACDynamicRangeControl**](/windows/win32/codecapi/ne-codecapi-eavdecheaacdynamicrangecontrol?branch=master)                 | Specifies whether an AAC decoder performs dynamic range control.                                          |
| [**eAVDecVideoInputScanType**](/windows/win32/codecapi/?branch=master)                             | Specifies how the decoded video stream is interlaced.                                                     |
| [**eAVDecVideoSoftwareDeinterlaceMode**](/windows/win32/codecapi/ne-codecapi-eavdecvideosoftwaredeinterlacemode?branch=master)         | Specifies a video decoder's software deinterlace mode.                                                    |
| [**eAVDecVideoSWPowerLevel**](/windows/win32/codecapi/ne-codecapi-eavdecvideoswpowerlevel?branch=master)                               | Specifies the power-saving level of a video decoder.                                                      |
| [**eAVDSPLoudnessEqualization**](/windows/win32/codecapi/ne-codecapi-eavdsploudnessequalization?branch=master)                         | Specifies whether loudness equalization is enabled in an audio decoder or digital signal processor (DSP). |
| [**eAVDSPSpeakerFill**](/windows/win32/codecapi/ne-codecapi-eavdspspeakerfill?branch=master)                                           | Specifies whether speaker fill is enabled in an audio decoder or DSP.                                     |
| [**eAVEncAudioDualMono**](/windows/win32/codecapi/?branch=master)                                       | Specifies whether 2-channel audio is encoded as stereo or dual mono.                                      |
| [**eAVEncAudioInputContent Enumeration**](/windows/win32/codecapi/?branch=master)                   | Specifies whether the audio content contains music or voice.                                              |
| [**eAVEncCommonRateControlMode**](/windows/win32/codecapi/?branch=master)                       | Specifies the rate control mode.                                                                          |
| [**eAVEncCommonStreamEndHandling**](/windows/win32/codecapi/?branch=master)                   | Specifies whether the encoder discards partial groups of pictures (GOPs) at the end of the stream.        |
| [**eAVEncDDAtoDConverterType**](/windows/win32/codecapi/?branch=master)                           | Specifies the type of analog-to-digital (A/D) conversion for a Dolby Digital audio stream.                |
| [**eAVEncDDDynamicRangeCompressionControl**](/windows/win32/codecapi/?branch=master) | Specifies the dynamic range control profile in a Dolby Digital audio stream.                              |
| [**eAVEncDDHeadphoneMode**](/windows/win32/codecapi/ne-codecapi-eavencddheadphonemode?branch=master)                                   | Specifies headphone mode for a Dolby Digital audio stream.                                                |
| [**eAVEncDDPreferredStereoDownMixMode**](/windows/win32/codecapi/ne-codecapi-eavencddpreferredstereodownmixmode?branch=master)         | Specifies the preferred stereo downmix mode for a Dolby Digital audio stream.                             |
| [**eAVEncDDProductionRoomType**](/windows/win32/codecapi/?branch=master)                         | Specifies the room type for a Dolby Digital audio stream.                                                 |
| [**eAVEncDDService**](/windows/win32/codecapi/ne-codecapi-eavencddservice?branch=master)                                               | Specifies the audio service contained in a Dolby Digital audio stream.                                    |
| [**eAVEncDDSurroundExMode**](/windows/win32/codecapi/ne-codecapi-eavencddsurroundexmode?branch=master)                                 | Specifies whether a Dolby Digital audio stream is encoded in Dolby Digital Surround EX.                   |
| [**eAVEncInputVideoSystem**](/windows/win32/codecapi/ne-codecapi-eavencinputvideosystem?branch=master)                                 | Specifies the nominal range for a video source.                                                           |
| [**eAVEncMPACodingMode**](/windows/win32/codecapi/ne-codecapi-eavencmpacodingmode?branch=master)                                       | Specifies the MPEG audio encoding mode.                                                                   |
| [**eAVEncMPAEmphasisType**](/windows/win32/codecapi/?branch=master)                                   | Specifies the type of de-emphasis filter that should be used when decoding.                               |
| [**eAVEncMPALayer**](/windows/win32/codecapi/?branch=master)                                                 | Specifies the MPEG audio layer.                                                                           |
| [**eAVEncMPVFrameFieldMode**](/windows/win32/codecapi/ne-codecapi-eavencmpvframefieldmode?branch=master)                               | Specifies whether the encoder produces encoded fields or encoded frames.                                  |
| [**eAVEncMPVIntraVLCTable**](/windows/win32/codecapi/ne-codecapi-eavencmpvintravlctable?branch=master)                                 | Specifies which variable-length coding (VLC) table to use for entropy coding.                             |
| [**eAVEncMPVLevel**](/windows/win32/codecapi/ne-codecapi-eavencmpvlevel?branch=master)                                                 | Specifies the MPEG-2 profile.                                                                             |
| [**eAVEncMPVProfile**](/windows/win32/codecapi/?branch=master)                                             | Specifies the MPEG-2 profile.                                                                             |
| [**eAVEncMPVQScaleType**](/windows/win32/codecapi/ne-codecapi-eavencmpvqscaletype?branch=master)                                       | Specifies whether the quantizer scale is linear or non-linear.                                            |
| [**eAVEncMPVScanPattern**](/windows/win32/codecapi/?branch=master)                                     | Specifies the macroblock scan pattern.                                                                    |
| [**eAVEncMPVSceneDetection**](/windows/win32/codecapi/?branch=master)                               | Specifies how the encoder behaves when it detects a new scene.                                            |
| [**eAVEncMuxOutput**](/windows/win32/codecapi/?branch=master)                                               | Specifies the type of output stream produced by a multiplexer.                                            |
| [**eAVEncVideoChromaResolution**](/windows/win32/codecapi/?branch=master)                       | Specifies chroma resolution.                                                                              |
| [**eAVEncVideoChromaSubsampling**](/windows/win32/codecapi/ne-codecapi-eavencvideochromasubsampling?branch=master)                     | Specifies chroma siting.                                                                                  |
| [**eAVEncVideoColorLighting**](/windows/win32/codecapi/ne-codecapi-eavencvideocolorlighting?branch=master)                             | Specifies the intended lighting conditions for viewing a video source.                                    |
| [**eAVEncVideoColorNominalRange**](/windows/win32/codecapi/ne-codecapi-eavencvideocolornominalrange?branch=master)                     | Specifies the nominal range for a video source.                                                           |
| [**eAVEncVideoColorPrimaries**](/windows/win32/codecapi/ne-codecapi-eavencvideocolorprimaries?branch=master)                           | Specifies the color primaries of the video.                                                               |
| [**eAVEncVideoColorTransferFunction**](/windows/win32/codecapi/ne-codecapi-eavencvideocolortransferfunction?branch=master)             | Specifies the conversion function from R'G'B' to RGB.                                                     |
| [**eAVEncVideoColorTransferMatrix**](/windows/win32/codecapi/ne-codecapi-eavencvideocolortransfermatrix?branch=master)                 | Specifies the conversion matrix from the Y'Cb'Cr' color space to the R'G'B' color space.                  |
| [**eAVEncVideoFilmContent**](/windows/win32/codecapi/?branch=master)                                 | Specifies whether the original source of the input video was film or video.                               |
| [**eAVEncVideoOutputFrameRateConversion**](/windows/win32/codecapi/?branch=master)     | Specifies whether the encoder converts the frame rate.                                                    |
| [**eAVEncVideoOutputScanType**](/windows/win32/codecapi/?branch=master)                           | Specifies how the encoder interlaces the output video.                                                    |
| [**eAVEncVideoSourceScanType**](/windows/win32/codecapi/ne-codecapi-eavencvideosourcescantype?branch=master)                           | Specifies whether the input frames for an encoder are progressive or interlaced.                          |
| [**eAVFastDecodeMode**](/windows/win32/codecapi/ne-codecapi-eavfastdecodemode?branch=master)                                           | Specifies the video decoding speed.                                                                       |



 

## Related topics

<dl> <dt>

[Codec API Reference](codec-api-reference.md)
</dt> <dt>

[**ICodecAPI**](/windows/win32/Strmif/nn-strmif-icodecapi?branch=master)
</dt> </dl>

 

 



