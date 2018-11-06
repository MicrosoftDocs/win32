---
Description: Codec API Enumerations
ms.assetid: 5d6e48cb-d181-448e-a96e-e5ab500427d7
title: Codec API Enumerations
ms.topic: article
ms.date: 05/31/2018
---

# Codec API Enumerations



| Enumeration                                                                              | Description                                                                                               |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [**eAVAudioChannelConfig**](/windows/desktop/api/codecapi/ne-codecapi-eavaudiochannelconfig)                                   | Specifies the speaker configuration for the audio channels in the audio bit stream.                       |
| [**eAVDDSurroundMode**](/windows/desktop/api/codecapi/ne-codecapi-eavddsurroundmode)                                           | Specifies whether the audio is encoded in Dolby Surround.                                                 |
| [**eAVDecAACDownmixMode**](https://msdn.microsoft.com/en-us/library/Dd757608(v=VS.85).aspx)                                     | Specifies whether an AAC decoder uses standard MPEG-2/MPEG-4 stereo downmix equations.                    |
| [**eAVDecAudioDualMono**](/windows/desktop/api/codecapi/ne-codecapi-eavdecaudiodualmono)                                       | Specifies whether the input audio stream is stereo or dual mono.                                          |
| [**eAVDecAudioDualMonoReproMode**](/windows/desktop/api/codecapi/ne-codecapi-eavdecaudiodualmonorepromode)                     | Specifies how the decoder reproduces dual mono audio.                                                     |
| [**eAVDecDDOperationalMode**](/windows/desktop/api/codecapi/ne-codecapi-eavdecddoperationalmode)                               | Specifies the compression control mode for a Dolby AC-3 audio stream.                                     |
| [**eAVDecHEAACDynamicRangeControl**](/windows/desktop/api/codecapi/ne-codecapi-eavdecheaacdynamicrangecontrol)                 | Specifies whether an AAC decoder performs dynamic range control.                                          |
| [**eAVDecVideoInputScanType**](https://msdn.microsoft.com/en-us/library/Dd388763(v=VS.85).aspx)                             | Specifies how the decoded video stream is interlaced.                                                     |
| [**eAVDecVideoSoftwareDeinterlaceMode**](/windows/desktop/api/codecapi/ne-codecapi-eavdecvideosoftwaredeinterlacemode)         | Specifies a video decoder's software deinterlace mode.                                                    |
| [**eAVDecVideoSWPowerLevel**](/windows/desktop/api/codecapi/ne-codecapi-eavdecvideoswpowerlevel)                               | Specifies the power-saving level of a video decoder.                                                      |
| [**eAVDSPLoudnessEqualization**](/windows/desktop/api/codecapi/ne-codecapi-eavdsploudnessequalization)                         | Specifies whether loudness equalization is enabled in an audio decoder or digital signal processor (DSP). |
| [**eAVDSPSpeakerFill**](/windows/desktop/api/codecapi/ne-codecapi-eavdspspeakerfill)                                           | Specifies whether speaker fill is enabled in an audio decoder or DSP.                                     |
| [**eAVEncAudioDualMono**](https://msdn.microsoft.com/en-us/library/Dd388765(v=VS.85).aspx)                                       | Specifies whether 2-channel audio is encoded as stereo or dual mono.                                      |
| [**eAVEncAudioInputContent Enumeration**](https://msdn.microsoft.com/en-us/library/Dd388768(v=VS.85).aspx)                   | Specifies whether the audio content contains music or voice.                                              |
| [**eAVEncCommonRateControlMode**](https://msdn.microsoft.com/en-us/library/Dd388772(v=VS.85).aspx)                       | Specifies the rate control mode.                                                                          |
| [**eAVEncCommonStreamEndHandling**](https://msdn.microsoft.com/en-us/library/Dd388776(v=VS.85).aspx)                   | Specifies whether the encoder discards partial groups of pictures (GOPs) at the end of the stream.        |
| [**eAVEncDDAtoDConverterType**](https://msdn.microsoft.com/en-us/library/Dd388780(v=VS.85).aspx)                           | Specifies the type of analog-to-digital (A/D) conversion for a Dolby Digital audio stream.                |
| [**eAVEncDDDynamicRangeCompressionControl**](https://msdn.microsoft.com/en-us/library/Dd319379(v=VS.85).aspx) | Specifies the dynamic range control profile in a Dolby Digital audio stream.                              |
| [**eAVEncDDHeadphoneMode**](/windows/desktop/api/codecapi/ne-codecapi-eavencddheadphonemode)                                   | Specifies headphone mode for a Dolby Digital audio stream.                                                |
| [**eAVEncDDPreferredStereoDownMixMode**](/windows/desktop/api/codecapi/ne-codecapi-eavencddpreferredstereodownmixmode)         | Specifies the preferred stereo downmix mode for a Dolby Digital audio stream.                             |
| [**eAVEncDDProductionRoomType**](https://msdn.microsoft.com/en-us/library/Dd319390(v=VS.85).aspx)                         | Specifies the room type for a Dolby Digital audio stream.                                                 |
| [**eAVEncDDService**](/windows/desktop/api/codecapi/ne-codecapi-eavencddservice)                                               | Specifies the audio service contained in a Dolby Digital audio stream.                                    |
| [**eAVEncDDSurroundExMode**](/windows/desktop/api/codecapi/ne-codecapi-eavencddsurroundexmode)                                 | Specifies whether a Dolby Digital audio stream is encoded in Dolby Digital Surround EX.                   |
| [**eAVEncInputVideoSystem**](/windows/desktop/api/codecapi/ne-codecapi-eavencinputvideosystem)                                 | Specifies the nominal range for a video source.                                                           |
| [**eAVEncMPACodingMode**](/windows/desktop/api/codecapi/ne-codecapi-eavencmpacodingmode)                                       | Specifies the MPEG audio encoding mode.                                                                   |
| [**eAVEncMPAEmphasisType**](https://msdn.microsoft.com/en-us/library/Dd319403(v=VS.85).aspx)                                   | Specifies the type of de-emphasis filter that should be used when decoding.                               |
| [**eAVEncMPALayer**](https://msdn.microsoft.com/en-us/library/Dd319405(v=VS.85).aspx)                                                 | Specifies the MPEG audio layer.                                                                           |
| [**eAVEncMPVFrameFieldMode**](/windows/desktop/api/codecapi/ne-codecapi-eavencmpvframefieldmode)                               | Specifies whether the encoder produces encoded fields or encoded frames.                                  |
| [**eAVEncMPVIntraVLCTable**](/windows/desktop/api/codecapi/ne-codecapi-eavencmpvintravlctable)                                 | Specifies which variable-length coding (VLC) table to use for entropy coding.                             |
| [**eAVEncMPVLevel**](/windows/desktop/api/codecapi/ne-codecapi-eavencmpvlevel)                                                 | Specifies the MPEG-2 profile.                                                                             |
| [**eAVEncMPVProfile**](https://msdn.microsoft.com/en-us/library/Dd319417(v=VS.85).aspx)                                             | Specifies the MPEG-2 profile.                                                                             |
| [**eAVEncMPVQScaleType**](/windows/desktop/api/codecapi/ne-codecapi-eavencmpvqscaletype)                                       | Specifies whether the quantizer scale is linear or non-linear.                                            |
| [**eAVEncMPVScanPattern**](https://msdn.microsoft.com/en-us/library/Dd319423(v=VS.85).aspx)                                     | Specifies the macroblock scan pattern.                                                                    |
| [**eAVEncMPVSceneDetection**](https://msdn.microsoft.com/en-us/library/Dd319426(v=VS.85).aspx)                               | Specifies how the encoder behaves when it detects a new scene.                                            |
| [**eAVEncMuxOutput**](https://msdn.microsoft.com/en-us/library/Dd757614(v=VS.85).aspx)                                               | Specifies the type of output stream produced by a multiplexer.                                            |
| [**eAVEncVideoChromaResolution**](https://msdn.microsoft.com/en-us/library/Dd319429(v=VS.85).aspx)                       | Specifies chroma resolution.                                                                              |
| [**eAVEncVideoChromaSubsampling**](/windows/desktop/api/codecapi/ne-codecapi-eavencvideochromasubsampling)                     | Specifies chroma siting.                                                                                  |
| [**eAVEncVideoColorLighting**](/windows/desktop/api/codecapi/ne-codecapi-eavencvideocolorlighting)                             | Specifies the intended lighting conditions for viewing a video source.                                    |
| [**eAVEncVideoColorNominalRange**](/windows/desktop/api/codecapi/ne-codecapi-eavencvideocolornominalrange)                     | Specifies the nominal range for a video source.                                                           |
| [**eAVEncVideoColorPrimaries**](/windows/desktop/api/codecapi/ne-codecapi-eavencvideocolorprimaries)                           | Specifies the color primaries of the video.                                                               |
| [**eAVEncVideoColorTransferFunction**](/windows/desktop/api/codecapi/ne-codecapi-eavencvideocolortransferfunction)             | Specifies the conversion function from R'G'B' to RGB.                                                     |
| [**eAVEncVideoColorTransferMatrix**](/windows/desktop/api/codecapi/ne-codecapi-eavencvideocolortransfermatrix)                 | Specifies the conversion matrix from the Y'Cb'Cr' color space to the R'G'B' color space.                  |
| [**eAVEncVideoFilmContent**](https://msdn.microsoft.com/en-us/library/Dd319452(v=VS.85).aspx)                                 | Specifies whether the original source of the input video was film or video.                               |
| [**eAVEncVideoOutputFrameRateConversion**](https://msdn.microsoft.com/en-us/library/Dd319454(v=VS.85).aspx)     | Specifies whether the encoder converts the frame rate.                                                    |
| [**eAVEncVideoOutputScanType**](https://msdn.microsoft.com/en-us/library/Dd319457(v=VS.85).aspx)                           | Specifies how the encoder interlaces the output video.                                                    |
| [**eAVEncVideoSourceScanType**](/windows/desktop/api/codecapi/ne-codecapi-eavencvideosourcescantype)                           | Specifies whether the input frames for an encoder are progressive or interlaced.                          |
| [**eAVFastDecodeMode**](/windows/desktop/api/codecapi/ne-codecapi-eavfastdecodemode)                                           | Specifies the video decoding speed.                                                                       |



 

## Related topics

<dl> <dt>

[Codec API Reference](codec-api-reference.md)
</dt> <dt>

[**ICodecAPI**](/windows/desktop/api/Strmif/nn-strmif-icodecapi)
</dt> </dl>

 

 



