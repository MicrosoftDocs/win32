---
Description: Codec API Enumerations
ms.assetid: '5d6e48cb-d181-448e-a96e-e5ab500427d7'
title: Codec API Enumerations
---

# Codec API Enumerations



| Enumeration                                                                              | Description                                                                                               |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [**eAVAudioChannelConfig**](eavaudiochannelconfig.md)                                   | Specifies the speaker configuration for the audio channels in the audio bit stream.                       |
| [**eAVDDSurroundMode**](eavddsurroundmode.md)                                           | Specifies whether the audio is encoded in Dolby Surround.                                                 |
| [**eAVDecAACDownmixMode**](eavdecaacdownmixmode.md)                                     | Specifies whether an AAC decoder uses standard MPEG-2/MPEG-4 stereo downmix equations.                    |
| [**eAVDecAudioDualMono**](eavdecaudiodualmono.md)                                       | Specifies whether the input audio stream is stereo or dual mono.                                          |
| [**eAVDecAudioDualMonoReproMode**](eavdecaudiodualmonorepromode.md)                     | Specifies how the decoder reproduces dual mono audio.                                                     |
| [**eAVDecDDOperationalMode**](eavdecddoperationalmode.md)                               | Specifies the compression control mode for a Dolby AC-3 audio stream.                                     |
| [**eAVDecHEAACDynamicRangeControl**](eavdecheaacdynamicrangecontrol.md)                 | Specifies whether an AAC decoder performs dynamic range control.                                          |
| [**eAVDecVideoInputScanType**](eavdecvideoinputscantype.md)                             | Specifies how the decoded video stream is interlaced.                                                     |
| [**eAVDecVideoSoftwareDeinterlaceMode**](eavdecvideosoftwaredeinterlacemode.md)         | Specifies a video decoder's software deinterlace mode.                                                    |
| [**eAVDecVideoSWPowerLevel**](eavdecvideoswpowerlevel.md)                               | Specifies the power-saving level of a video decoder.                                                      |
| [**eAVDSPLoudnessEqualization**](eavdsploudnessequalization.md)                         | Specifies whether loudness equalization is enabled in an audio decoder or digital signal processor (DSP). |
| [**eAVDSPSpeakerFill**](eavdspspeakerfill.md)                                           | Specifies whether speaker fill is enabled in an audio decoder or DSP.                                     |
| [**eAVEncAudioDualMono**](eavencaudiodualmono.md)                                       | Specifies whether 2-channel audio is encoded as stereo or dual mono.                                      |
| [**eAVEncAudioInputContent Enumeration**](eavencaudioinputcontent.md)                   | Specifies whether the audio content contains music or voice.                                              |
| [**eAVEncCommonRateControlMode**](eavenccommonratecontrolmode.md)                       | Specifies the rate control mode.                                                                          |
| [**eAVEncCommonStreamEndHandling**](eavenccommonstreamendhandling.md)                   | Specifies whether the encoder discards partial groups of pictures (GOPs) at the end of the stream.        |
| [**eAVEncDDAtoDConverterType**](eavencddatodconvertertype.md)                           | Specifies the type of analog-to-digital (A/D) conversion for a Dolby Digital audio stream.                |
| [**eAVEncDDDynamicRangeCompressionControl**](eavencdddynamicrangecompressioncontrol.md) | Specifies the dynamic range control profile in a Dolby Digital audio stream.                              |
| [**eAVEncDDHeadphoneMode**](eavencddheadphonemode.md)                                   | Specifies headphone mode for a Dolby Digital audio stream.                                                |
| [**eAVEncDDPreferredStereoDownMixMode**](eavencddpreferredstereodownmixmode.md)         | Specifies the preferred stereo downmix mode for a Dolby Digital audio stream.                             |
| [**eAVEncDDProductionRoomType**](eavencddproductionroomtype.md)                         | Specifies the room type for a Dolby Digital audio stream.                                                 |
| [**eAVEncDDService**](eavencddservice.md)                                               | Specifies the audio service contained in a Dolby Digital audio stream.                                    |
| [**eAVEncDDSurroundExMode**](eavencddsurroundexmode.md)                                 | Specifies whether a Dolby Digital audio stream is encoded in Dolby Digital Surround EX.                   |
| [**eAVEncInputVideoSystem**](eavencinputvideosystem.md)                                 | Specifies the nominal range for a video source.                                                           |
| [**eAVEncMPACodingMode**](eavencmpacodingmode.md)                                       | Specifies the MPEG audio encoding mode.                                                                   |
| [**eAVEncMPAEmphasisType**](eavencmpaemphasistype.md)                                   | Specifies the type of de-emphasis filter that should be used when decoding.                               |
| [**eAVEncMPALayer**](eavencmpalayer.md)                                                 | Specifies the MPEG audio layer.                                                                           |
| [**eAVEncMPVFrameFieldMode**](eavencmpvframefieldmode.md)                               | Specifies whether the encoder produces encoded fields or encoded frames.                                  |
| [**eAVEncMPVIntraVLCTable**](eavencmpvintravlctable.md)                                 | Specifies which variable-length coding (VLC) table to use for entropy coding.                             |
| [**eAVEncMPVLevel**](eavencmpvlevel.md)                                                 | Specifies the MPEG-2 profile.                                                                             |
| [**eAVEncMPVProfile**](eavencmpvprofile.md)                                             | Specifies the MPEG-2 profile.                                                                             |
| [**eAVEncMPVQScaleType**](eavencmpvqscaletype.md)                                       | Specifies whether the quantizer scale is linear or non-linear.                                            |
| [**eAVEncMPVScanPattern**](eavencmpvscanpattern.md)                                     | Specifies the macroblock scan pattern.                                                                    |
| [**eAVEncMPVSceneDetection**](eavencmpvscenedetection.md)                               | Specifies how the encoder behaves when it detects a new scene.                                            |
| [**eAVEncMuxOutput**](eavencmuxoutput.md)                                               | Specifies the type of output stream produced by a multiplexer.                                            |
| [**eAVEncVideoChromaResolution**](eavencvideochromaresolution.md)                       | Specifies chroma resolution.                                                                              |
| [**eAVEncVideoChromaSubsampling**](eavencvideochromasubsampling.md)                     | Specifies chroma siting.                                                                                  |
| [**eAVEncVideoColorLighting**](eavencvideocolorlighting.md)                             | Specifies the intended lighting conditions for viewing a video source.                                    |
| [**eAVEncVideoColorNominalRange**](eavencvideocolornominalrange.md)                     | Specifies the nominal range for a video source.                                                           |
| [**eAVEncVideoColorPrimaries**](eavencvideocolorprimaries.md)                           | Specifies the color primaries of the video.                                                               |
| [**eAVEncVideoColorTransferFunction**](eavencvideocolortransferfunction.md)             | Specifies the conversion function from R'G'B' to RGB.                                                     |
| [**eAVEncVideoColorTransferMatrix**](eavencvideocolortransfermatrix.md)                 | Specifies the conversion matrix from the Y'Cb'Cr' color space to the R'G'B' color space.                  |
| [**eAVEncVideoFilmContent**](eavencvideofilmcontent.md)                                 | Specifies whether the original source of the input video was film or video.                               |
| [**eAVEncVideoOutputFrameRateConversion**](eavencvideooutputframerateconversion.md)     | Specifies whether the encoder converts the frame rate.                                                    |
| [**eAVEncVideoOutputScanType**](eavencvideooutputscantype.md)                           | Specifies how the encoder interlaces the output video.                                                    |
| [**eAVEncVideoSourceScanType**](eavencvideosourcescantype.md)                           | Specifies whether the input frames for an encoder are progressive or interlaced.                          |
| [**eAVFastDecodeMode**](eavfastdecodemode.md)                                           | Specifies the video decoding speed.                                                                       |



 

## Related topics

<dl> <dt>

[Codec API Reference](codec-api-reference.md)
</dt> <dt>

[**ICodecAPI**](icodecapi.md)
</dt> </dl>

 

 



