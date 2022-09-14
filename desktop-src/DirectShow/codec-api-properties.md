---
description: Codec API Properties
ms.assetid: 5d527af7-07cf-42e2-99bb-d56c856cc1bc
title: Codec API Properties
ms.topic: article
ms.date: 05/31/2018
---

# Codec API Properties

-   [Common Audio Properties](#common-audio-properties)
-   [Common Decoder Properties](#common-decoder-properties)
-   [Common Encoder Properties](#common-encoder-properties)
-   [Video Decoder Properties](#video-decoder-properties)
-   [Audio Decoder Properties](#audio-decoder-properties)
-   [Video Encoder Properties](#video-encoder-properties)
-   [Audio Encoder Properties](#audio-encoder-properties)
-   [MPEG Video Encoder Properties](#mpeg-video-encoder-properties)
-   [MPEG Audio Encoder Properties](#mpeg-audio-encoder-properties)
-   [Dolby Digital Audio Decoder Properties](#dolby-digital-audio-decoder-properties)
-   [Dolby Digital Audio Encoder Properties](#dolby-digital-audio-encoder-properties)
-   [Digital Signal Processing (DSP) Properties](#digital-signal-processing-dsp-properties)

### Common Audio Properties

These properties apply to both audio encoders and audio decoders.



| Property                                                      | Description                                                                    |
|---------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**AVAudioChannelConfig**](avaudiochannelconfig-property.md) | Gets the speaker configuration for the audio channels in the audio bit stream. |
| [**AVAudioChannelCount**](avaudiochannelcount-property.md)   | Gets the number of channels in the audio bit stream.                           |
| [**AVAudioSampleRate**](avaudiosamplerate-property.md)       | Gets the sample rate of the audio bit stream, in samples per seconds.          |
| [**AVDDSurroundMode**](avddsurroundmode-property.md)         | Specifies whether the audio is encoded in Dolby Surround.                      |



 

### Common Decoder Properties

These properties apply to both audio decoders and video decoders.



| Property                                                            | Description                                                                             |
|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**AVDecCommonInputFormat**](avdeccommoninputformat-property.md)   | Specifies the current input format for the decoder.                                     |
| [**AVDecCommonMeanBitRate**](avdeccommonmeanbitrate.md)            | Gets the current mean bit rate of the decoder.                                          |
| [**AVDecCommonOutputFormat**](avdeccommonoutputformat-property.md) | Specifies the output format for the decoder.                                            |
| [**AVDecMmcssClass**](avdecmmcss-property.md)                      | Specifies the Multimedia Class Scheduler Service (MMCSS) class for the decoding thread. |



 

### Common Encoder Properties

These properties apply to both audio encoders and video encoders.



| Property                                                                          | Description                                                                                                     |
|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [**AVEncCodecType**](avenccodectype-property.md)                                 | Specifies the encoding scheme.                                                                                  |
| [**AVEncCommonBufferInLevel**](avenccommonbufferinlevel-property.md)             | Specifies the initial level of the encoding buffer.                                                             |
| [**AVEncCommonBufferOutLevel**](avenccommonbufferoutlevel-property.md)           | Specifies the final level of the encoding buffer at the end of the encoding process.                            |
| [**AVEncCommonBufferSize**](avenccommonbuffersize-property.md)                   | Specifies the size of the buffer used during encoding.                                                          |
| [**AVEncCommonFormatConstraint**](avenccommonformatconstraint-property.md)       | Specifies the target format for an encoder.                                                                     |
| [**AVEncCommonLowLatency**](avenccommonlowlatency-property.md)                   | Specifies whether the output stream should be structured so that the encoded stream has a low decoding latency. |
| [**AVEncCommonMaxBitRate**](avenccommonmaxbitrate-property.md)                   | Specifies the maximum bit rate.                                                                                 |
| [**AVEncCommonMeanBitRate**](avenccommonmeanbitrate-property.md)                 | Specifies the average bit rate.                                                                                 |
| [**AVEncCommonMeanBitRateInterval**](avenccommonmeanbitrateinterval-property.md) | Specifies the time interval over which the average bit rate applies.                                            |
| [**AVEncCommonMinBitRate**](avenccommonminbitrate-property.md)                   | Specifies the minimum bit rate.                                                                                 |
| [**AVEncCommonMultipassMode**](avenccommonmultipassmode-property.md)             | Specifies the number of encoding passes that the encoder supports.                                              |
| [**AVEncCommonPassEnd**](avenccommonpassend-property.md)                         | Stops the current encoding pass, or queries whether the current encoding pass is the last one.                  |
| [**AVEncCommonPassStart**](avenccommonpassstart-property.md)                     | Starts the first encoding pass.                                                                                 |
| [**AVEncCommonQuality**](avenccommonquality-property.md)                         | Specifies the quality level for encoding.                                                                       |
| [**AVEncCommonQualityVsSpeed**](avenccommonqualityvsspeed-property.md)           | Specifies the tradeoff between encoding quality and speed.                                                      |
| [**AVEncCommonRateControlMode**](avenccommonratecontrolmode-property.md)         | Specifies the rate control mode.                                                                                |
| [**AVEncCommonRealTime**](avenccommonrealtime-property.md)                       | Specifies whether the application requires real-time encoding performance.                                      |
| [**AVEncCommonStreamEndHandling**](avenccommonstreamendhandling-property.md)     | Specifies whether the encoder discards partial groups of pictures (GOPs) at the end of the stream.              |
| [**AVEncMuxOutputStreamType**](avencmuxoutputstreamtype.md)                      | Specifies the type of output stream produced by a multiplexer.                                                  |
| [**AVEncStatCommonCompletedPasses**](avencstatcommoncompletedpasses-property.md) | Specifies the number of completed encoding passes.                                                              |



 

### Video Decoder Properties



| Property                                                                                | Description                                                                     |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [**AVDecVideoAcceleration\_H264**](avdecvideoacceleration-h264-property.md)            | Enables or disables hardware acceleration for H.264 video decoding.             |
| [**AVDecVideoAcceleration\_MPEG2**](avdecvideoacceleration-mpeg2-property.md)          | Enables or disables hardware acceleration for MPEG-2 video decoding.            |
| [**AVDecVideoAcceleration\_VC1**](avdecvideoacceleration-vc1-property.md)              | Enables or disables hardware acceleration for VC-1 video decoding.              |
| [**AVDecVideoDropPicWithMissingRef**](avdecvideodroppicwithmissingref-property.md)     | Specifies whether the decoder drops intra frames with missing reference frames. |
| [**AVDecVideoFastDecodeMode**](avdecvideofastdecodemode.md)                            | Gets or sets the video decoding speed.                                          |
| [**AVDecVideoImageSize**](avdecvideoimagesize.md)                                      | Gets the size of the decoded image, in pixels.                                  |
| [**AVDecVideoInputScanType**](avdecvideoinputscantype-property.md)                     | Specifies how the decoded video stream is interlaced.                           |
| [**AVDecVideoPixelAspectRatio**](avdecvideopixelaspectratio-property.md)               | Specifies the pixel aspect ratio of the decoded video stream.                   |
| [**AVDecVideoSoftwareDeinterlaceMode**](avdecvideosoftwaredeinterlacemode-property.md) | Specifies the decoder's software deinterlace mode.                              |
| [**AVDecVideoSWPowerLevel**](avdecvideoswpowerlevel-property.md)                       | Specifies the power-saving level.                                               |
| [**AVDecVideoThumbnailGenerationMode**](avdecvideothumbnailgenerationmode-property.md) | Enables or disables thumbnail generation mode.                                  |



 

### Audio Decoder Properties



| Property                                                                        | Description                                                                                                            |
|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**AVDecAACDownmixMode**](avdecaacdownmixmode-property.md)                     | Specifies whether an AAC decoder uses standard MPEG-2/MPEG-4 stereo downmix equations, or uses a non-standard downmix. |
| [**AVDecAudioDualMono**](avdecaudiodualmono-property.md)                       | Specifies whether 2-channel audio is encoded as stereo or dual mono.                                                   |
| [**AVDecAudioDualMonoReproMode**](avdecaudiodualmonorepromode-property.md)     | Specifies how the decoder reproduces dual mono audio.                                                                  |
| [**AVDecHEAACDynamicRangeControl**](avdecheaacdynamicrangecontrol-property.md) | Enables or disables dynamic range control in an AAC decoder.                                                           |



 

### Video Encoder Properties



| Property                                                                                        | Description                                                                                                           |
|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [**AVEncInputVideoSystem**](avencinputvideosystem-property.md)                                 | Specifies the video system of the source content.                                                                     |
| [**AVEncStatVideoCodedFrames**](avencstatvideocodedframes-property.md)                         | Returns the number of video frames that were encoded.                                                                 |
| [**AVEncStatVideoOutputFrameRate**](avencstatvideooutputframerate-property.md)                 | Returns the average frame rate of the video content.                                                                  |
| [**AVEncStatVideoTotalFrames**](avencstatvideototalframes-property.md)                         | Returns the number of video frames that the encoder received.                                                         |
| [**AVEncVideoCBRMotionTradeoff**](avencvideocbrmotiontradeoff-property.md)                     | Specifies the tradeoff between motion and still images.                                                               |
| [**AVEncVideoCodedVideoAccessUnitSize**](avencvideocodedvideoaccessunitsize-property.md)       | Specifies the size of the video access units.                                                                         |
| [**AVEncVideoDefaultUpperFieldDominant**](avencvideodefaultupperfielddominant-property.md)     | Specifies which field is displayed first.                                                                             |
| [**AVEncVideoDisplayDimension**](avencvideodisplaydimension-property.md)                       | Specifies the size of the video stream when it is decoded.                                                            |
| [**AVEncVideoEncodeDimension**](avencvideoencodedimension-property.md)                         | Specifies the width and height of the encoded video, if the video is cropped.                                         |
| [**AVEncVideoEncodeOffsetOrigin**](avencvideoencodeoffsetorigin-property.md)                   | Specifies the left and top corners of the clipping rectangle, if the video is cropped.                                |
| [**AVEncVideoFieldSwap**](avencvideofieldswap-property.md)                                     | Reverses the order of the interlaced fields in the source video.                                                      |
| [**AVEncVideoForceSourceScanType**](avencvideoforcesourcescantype-property.md)                 | Specifies whether the input frames are progressive or interlaced.                                                     |
| [**AVEncVideoHeaderDropFrame**](avencvideoheaderdropframe-property.md)                         | Specifies the value of drop-frame flag in the GOP header.                                                             |
| [**AVEncVideoHeaderFrames**](avencvideoheaderframes-property.md)                               | Specifies the starting frame number in the GOP header.                                                                |
| [**AVEncVideoHeaderHours**](avencvideoheaderhours-property.md)                                 | Specifies the starting hour number in the GOP header.                                                                 |
| [**AVEncVideoHeaderMinutes**](avencvideoheaderminutes-property.md)                             | Specifies the starting minute number in the GOP header.                                                               |
| [**AVEncVideoHeaderSeconds**](avencvideoheaderseconds-property.md)                             | Specifies the starting second number in the GOP header.                                                               |
| [**AVEncVideoInputChromaResolution**](avencvideoinputchromaresolution-property.md)             | Specifies the chroma resolution of the input video.                                                                   |
| [**AVEncVideoInputChromaSubsampling**](avencvideoinputchromasubsampling-property.md)           | Specifies the chroma siting for the input video.                                                                      |
| [**AVEncVideoInputColorLighting**](avencvideoinputcolorlighting-property.md)                   | Specifies the intended lighting conditions for viewing the input video.                                               |
| [**AVEncVideoInputColorNominalRange**](avencvideoinputcolornominalrange-property.md)           | Specifies the nominal range for the input video.                                                                      |
| [**AVEncVideoInputColorPrimaries**](avencvideoinputcolorprimaries-property.md)                 | Specifies the color primaries for the input video.                                                                    |
| [**AVEncVideoInputColorTransferFunction**](avencvideoinputcolortransferfunction-property.md)   | Specifies the conversion function from RGB to R'G'B' for input video                                                  |
| [**AVEncVideoInputColorTransferMatrix**](avencvideoinputcolortransfermatrix-property.md)       | Specifies the conversion matrix from the Y'Cb'Cr' color space to the R'G'B' color space, for the input video.         |
| [**AVEncVideoInverseTelecineEnable**](avencvideoinversetelecineenable-property.md)             | Specifies whether the encoder performs inverse telecine.                                                              |
| [**AVEncVideoInverseTelecineThreshold**](avencvideoinversetelecinethreshold-property.md)       | Sets the threshold at which the encoder considers a video field redundant.                                            |
| [**AVEncVideoMaxKeyframeDistance**](avencvideomaxkeyframedistance-property.md)                 | Specifies the maximum number of frames between key frames.                                                            |
| [**AVEncVideoNoOfFieldsToEncode**](avencvideonooffieldstoencode-property.md)                   | Specifies the number of fields to encode.                                                                             |
| [**AVEncVideoNoOfFieldsToSkip**](avencvideonooffieldstoskip-property.md)                       | Specifies the number of fields to skip during encoding.                                                               |
| [**AVEncVideoOutputChromaResolution**](avencvideooutputchromaresolution-property.md)           | Specifies the chroma resolution of the encoded video.                                                                 |
| [**AVEncVideoOutputChromaSubsampling**](avencvideooutputchromasubsampling-property.md)         | Specifies the chroma siting for the encoded video.                                                                    |
| [**AVEncVideoOutputColorLighting**](avencvideooutputcolorlighting-property.md)                 | Specifies the intended lighting conditions for viewing the encoded video.                                             |
| [**AVEncVideoOutputColorNominalRange**](avencvideooutputcolornominalrange-property.md)         | Specifies the nominal range for the encoded video.                                                                    |
| [**AVEncVideoOutputColorPrimaries**](avencvideooutputcolorprimaries-property.md)               | Specifies the color primaries for the encoded video.                                                                  |
| [**AVEncVideoOutputColorTransferFunction**](avencvideooutputcolortransferfunction-property.md) | Specifies the conversion function from RGB to R'G'B' for encoded video.                                               |
| [**AVEncVideoOutputColorTransferMatrix**](avencvideooutputcolortransfermatrix-property.md)     | Specifies the conversion matrix from the Y'Cb'Cr' color space to the R'G'B' color space, for the encoded video.       |
| [**AVEncVideoOutputFrameRate**](avencvideooutputframerate-property.md)                         | Specifies the frame rate on the encoder's output stream, in frames per second.                                        |
| [**AVEncVideoOutputFrameRateConversion**](avencvideooutputframerateconversion-property.md)     | Specifies whether the encoder converts the frame rate when the output frame rate does not match the input frame rate. |
| [**AVEncVideoOutputScanType**](avencvideooutputscantype-property.md)                           | Specifies how the encoder interlaces the output video.                                                                |
| [**AVEncVideoPixelAspectRatio**](avencvideopixelaspectratio-property.md)                       | Specifies the pixel aspect ratio.                                                                                     |
| [**AVEncVideoSourceFilmContent**](avencvideosourcefilmcontent-property.md)                     | Specifies whether the original source of the input video was film or video.                                           |
| [**AVEncVideoSourceIsBW**](avencvideosourceisbw-property.md)                                   | Specifies whether the video is monochrome (black and white) or contains color.                                        |



 

### Audio Encoder Properties



| Property                                                                        | Description                                                                         |
|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [**AVEncAudioDualMono**](avencaudiodualmono-property.md)                       | Specifies whether 2-channel audio is encoded as stereo or dual mono.                |
| [**AVEncAudioInputContent**](avencaudioinputcontent-property.md)               | Specifies whether the audio content contains music or voice.                        |
| [**AVEncAudioIntervalToEncode**](avencaudiointervaltoencode-property.md)       | Specifies the number of audio samples to encode.                                    |
| [**AVEncAudioIntervalToSkip**](avencaudiointervaltoskip-property.md)           | Specifies the number of audio samples for the encoder to skip.                      |
| [**AVEncAudioMapDestChannel N**](avencaudiomapdestchanneln-property.md)        | Specifies which audio channel is mapped to channel *N* in the encoded audio stream. |
| [**AVEncAudioMeanBitRate**](avencaudiomeanbitrate.md)                          | Specifies the average bit rate of the encoded audio stream.                         |
| [**AVEncStatAudioAverageBPS**](avencstataudioaveragebps-property.md)           | Returns the average bits per second of the encoded audio.                           |
| [**AVEncStatAudioAveragePCMValue**](avencstataudioaveragepcmvalue-property.md) | Returns the average volume level of the audio content.                              |
| [**AVEncStatAudioPeakPCMValue**](avencstataudiopeakpcmvalue-property.md)       | Returns the highest volume level that was present in the audio content.             |



 

### MPEG Video Encoder Properties



| Property                                                                                    | Description                                                                          |
|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**AVEncMPVAddSeqEndCode**](avencmpvaddseqendcode-property.md)                             | Specifies whether the encoder adds a sequence end code at the end of the stream.     |
| [**AVEncMPVDefaultBPictureCount**](avencmpvdefaultbpicturecount-property.md)               | Specifies the default number of consecutive B frames between I and P frames.         |
| [**AVEncMPVFrameFieldMode**](avencmpvframefieldmode-property.md)                           | Specifies whether the encoder produces encoded fields or encoded frames.             |
| [**AVEncMPVGenerateHeaderPicDispExt**](avencmpvgenerateheaderpicdispext-property.md)       | Specifies whether the encoder generates picture display extension headers.           |
| [**AVEncMPVGenerateHeaderPicExt**](avencmpvgenerateheaderpicext-property.md)               | Specifies whether the encoder generates picture extension headers.                   |
| [**AVEncMPVGenerateHeaderSeqDispExt**](avencmpvgenerateheaderseqdispext-property.md)       | Specifies whether the encoder generates sequence display extension headers.          |
| [**AVEncMPVGenerateHeaderSeqExt**](avencmpvgenerateheaderseqext-property.md)               | Specifies whether the encoder generates sequence extension headers.                  |
| [**AVEncMPVGenerateHeaderSeqScaleExt**](avencmpvgenerateheaderseqscaleext-property.md)     | Specifies whether the encoder generates sequence scalable extension headers.         |
| [**AVEncMPVGOPOpen**](avencmpvgopopen-property.md)                                         | Specifies whether the encoder produces open GOPs or closed GOPs.                     |
| [**AVEncMPVGOPSInSeq**](avencmpvgopsinseq-property.md)                                     | Specifies the number of GOPs between sequence headers.                               |
| [**AVEncMPVGOPSize**](avencmpvgopsize-property.md)                                         | Specifies the maximum number of pictures from one GOP header to the next GOP header. |
| [**AVEncMPVIntraDCPrecision**](avencmpvintradcprecision-property.md)                       | Specifies the precision of the DC coefficients.                                      |
| [**AVEncMPVIntraVLCTable**](avencmpvintravlctable-property.md)                             | Specifies which variable-length coding (VLC) table to use for entropy coding.        |
| [**AVEncMPVLevel**](avencmpvlevel-property.md)                                             | Specifies the MPEG-2 level.                                                          |
| [**AVEncMPVProfile**](avencmpvprofile-property.md)                                         | Specifies the MPEG-2 profile.                                                        |
| [**AVEncMPVQScaleType**](avencmpvqscaletype-property.md)                                   | Specifies whether the quantizer scale is linear or non-linear.                       |
| [**AVEncMPVQuantMatrixChromaIntra**](avencmpvquantmatrixchromaintra-property.md)           | Specifies the chroma quantization matrix for intra macroblocks.                      |
| [**AVEncMPVQuantMatrixChromaNonIntra**](avencmpvquantmatrixchromanonintra-property.md)     | Specifies the chroma quantization matrix for non-intra macroblocks.                  |
| [**AVEncMPVQuantMatrixIntra**](avencmpvquantmatrixintra-property.md)                       | Specifies the luma quantization matrix for intra macroblocks.                        |
| [**AVEncMPVQuantMatrixNonIntra**](avencmpvquantmatrixnonintra-property.md)                 | Specifies the luma quantization matrix for non-intra macroblocks.                    |
| [**AVEncMPVScanPattern**](avencmpvscanpattern-property.md)                                 | Specifies the macroblock scan pattern.                                               |
| [**AVEncMPVSceneDetection**](avencmpvscenedetection-property.md)                           | Specifies how the encoder behaves when it detects a new scene.                       |
| [**AVEncMPVUseConcealmentMotionVectors**](avencmpvuseconcealmentmotionvectors-property.md) | Specifies whether the encoder uses concealment motion vectors.                       |



 

### MPEG Audio Encoder Properties



| Property                                                                                  | Description                                                                   |
|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [**AVEncMPACodingMode**](avencmpacodingmode-property.md)                                 | Specifies the MPEG-1 audio encoding mode.                                     |
| [**AVEncMPACopyright**](avencmpacopyright-property.md)                                   | Specifies the default setting for the copyright bit.                          |
| [**AVEncMPAEmphasisType**](avencmpaemphasistype-property.md)                             | Specifies the type of de-emphasis filter that should be used when decoding.   |
| [**AVEncMPAEnableRedundancyProtection**](avencmpaenableredundancyprotection-property.md) | Specifies whether to add a cyclic redundancy check (CRC) to the frame header. |
| [**AVEncMPALayer**](avencmpalayer-property.md)                                           | Specifies the MPEG audio layer.                                               |
| [**AVEncMPAOriginalBitstream**](avencmpaoriginalbitstream-property.md)                   | Specifies the default setting for the original bit.                           |
| [**AVEncMPAPrivateUserBit**](avencmpaprivateuserbit-property.md)                         | Sets the value of the private user bit.                                       |



 

### Dolby Digital Audio Decoder Properties



| Property                                                                      | Description                                                                    |
|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**AVDecDDDynamicRangeScaleHigh**](avdecdddynamicrangescalehigh-property.md) | Specifies the high-level cut when the decoder performs dynamic range control.  |
| [**AVDecDDDynamicRangeScaleLow**](avdecdddynamicrangescalelow-property.md)   | Specifies the low-level boost when the decoder performs dynamic range control. |
| [**AVDecDDOperationalMode**](avdecddoperationalmode-property.md)             | Specifies the compression control mode.                                        |



 

### Dolby Digital Audio Encoder Properties



| Property                                                                                        | Description                                                                               |
|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [**AVEncDDAtoDConverterType**](avencddatodconvertertype-property.md)                           | Specifies the type of analog-to-digital (A/D) conversion.                                 |
| [**AVEncDDCentreDownMixLevel**](avencddcentredownmixlevel-property.md)                         | Specifies the center downmix level.                                                       |
| [**AVEncDDChannelBWLowPassFilter**](avencddchannelbwlowpassfilter-property.md)                 | Specifies whether a low pass filter is applied to the main input channels.                |
| [**AVEncDDCopyright**](avencddcopyright-property.md)                                           | Specifies the copyright flag.                                                             |
| [**AVEncDDDCHighPassFilter**](avencdddchighpassfilter-property.md)                             | Specifies whether a DC-blocking high pass filter is applied.                              |
| [**AVEncDDDialogNormalization**](avencdddialognormalization-property.md)                       | Specifies the dialog normalization level.                                                 |
| [**AVEncDDDigitalDeemphasis**](avencdddigitaldeemphasis-property.md)                           | Specifies whether digital de-emphasis.                                                    |
| [**AVEncDDDynamicRangeCompressionControl**](avencdddynamicrangecompressioncontrol-property.md) | Specifies the dynamic range control profile.                                              |
| [**AVEncDDHeadphoneMode**](avencddheadphonemode-property.md)                                   | Specifies the headphone mode.                                                             |
| [**AVEncDDLFELowPassFilter**](avencddlfelowpassfilter-property.md)                             | Specifies whether a low pass filter is applied to the low frequency effect (LFE) channel. |
| [**AVEncDDLoRoCenterMixLvl\_x10**](avencddlorocentermixlvl-x10-property.md)                    | Specifies the level shift that is applied to the center channel for Lo/Ro downmixing.     |
| [**AVEncDDLoRoSurroundMixLvl\_x10**](avencddlorosurroundmixlvl-x10-property.md)                | Specifies the level shift that is applied to the Surround channels for Lo/Ro downmixing.  |
| [**AVEncDDLtRtCenterMixLvl\_x10**](avencddltrtcentermixlvl-x10-property.md)                    | Specifies the level shift that is applied to the center channel for Lt/Rt downmixing.     |
| [**AVEncDDLtRtSurroundMixLvl\_x10**](avencddltrtsurroundmixlvl-x10-property.md)                | Specifies the level shift that is applied to the Surround channels for Lt/Rt downmixing.  |
| [**AVEncDDOriginalBitstream**](avencddoriginalbitstream-property.md)                           | Specifies the original bitstream flag.                                                    |
| [**AVEncDDPreferredStereoDownMixMode**](avencddpreferredstereodownmixmode-property.md)         | Specifies the preferred stereo downmix mode.                                              |
| [**AVEncDDProductionInfoExists**](avencddproductioninfoexists-property.md)                     | Specifies the audio production information flag.                                          |
| [**AVEncDDProductionMixLevel**](avencddproductionmixlevel-property.md)                         | Specifies the mixing level.                                                               |
| [**AVEncDDProductionRoomType**](avencddproductionroomtype-property.md)                         | Specifies the room type.                                                                  |
| [**AVEncDDRFPreEmphasisFilter**](avencddrfpreemphasisfilter-property.md)                       | Specifies the RF overmodulation protection setting.                                       |
| [**AVEncDDService**](avencddservice-property.md)                                               | Specifies the audio service.                                                              |
| [**AVEncDDSurround3dBAttenuation**](avencddsurround3dbattenuation-property.md)                 | Specifies whether the Surround channels are attenuated before encoding.                   |
| [**AVEncDDSurround90DegreeePhaseShift**](avencddsurround90degreeephaseshift-property.md)       | Specifies whether a 90-degree phase shift is applied to the Surround channels.            |
| [**AVEncDDSurroundDownMixLevel**](avencddsurrounddownmixlevel-property.md)                     | Specifies the Surround down mix level.                                                    |
| [**AVEncDDSurroundExMode**](avencddsurroundexmode-property.md)                                 | Specifies whether the audio stream is encoded in Surround EX.                             |



 

### Digital Signal Processing (DSP) Properties



| Property                                                                | Description                               |
|-------------------------------------------------------------------------|-------------------------------------------|
| [**AVDSPLoudnessEqualization**](avdsploudnessequalization-property.md) | Enables or disables loudness equalization |
| [**AVDSPSpeakerFill**](avdspspeakerfill-property.md)                   | Enables or disables speaker fill          |



 

## Related topics

<dl> <dt>

[Codec API Reference](codec-api-reference.md)
</dt> </dl>

 

 



