---
description: Codec and DSP IPropertyBag constants.
ms.assetid: 078b0eea-16dd-4427-b984-9e52a43de559
title: Codec and DSP IPropertyBag Constants
ms.topic: article
ms.date: 05/31/2018
---

# Codec and DSP IPropertyBag Constants

There are two methods of setting properties on the codec and DSP objects programmatically, using either the **IPropertyBag** interface or the **IPropertyStore** interface. Most common properties are available through both interfaces. Use of the **IPropertyStore** interface is preferred over **IPropertyBag**.



| IPropertyBag string constant          | IPropertyStore property key                                                                         |
|---------------------------------------|-----------------------------------------------------------------------------------------------------|
| g\_wszAvgFrameRate                    | [MFPKEY\_ASFOVERHEADPERFRAME](mfpkey-asfoverheadperframeproperty.md)                               |
| g\_wszWMACAvgBytesPerSecond           | [MFPKEY\_WMAENC\_AVGBYTESPERSEC](mfpkey-wmaenc-avgbytespersecproperty.md)                          |
| g\_wszWMACDRCSetting                  | [MFPKEY\_WMADEC\_DRCMODE](mfpkey-wmadec-drcmodeproperty.md)                                        |
| g\_wszWMACHiResOutput                 | [MFPKEY\_WMADEC\_HIRESOUTPUT](mfpkey-wmadec-hiresoutputproperty.md)                                |
| g\_wszWMACMusicSpeechClassMode        | [MFPKEY\_WMAVOICE\_ENC\_MusicSpeechClassMode](mfpkey-wmavoice-enc-musicspeechclassmodeproperty.md) |
| g\_wszWMACOriginalWaveFormat          | [MFPKEY\_WMAENC\_ORIGWAVEFORMAT](mfpkey-wmaenc-origwaveformatproperty.md)                          |
| g\_wszWMACSpeakerConfig               | [MFPKEY\_WMADEC\_SPKRCFG](mfpkey-wmadec-spkrcfgproperty.md)                                        |
| g\_wszWMACVoiceBuffer                 | [MFPKEY\_WMAVOICE\_ENC\_BufferWindow](mfpkey-wmavoice-enc-bufferwindowproperty.md)                 |
| g\_wszWMACVoiceBuffer                 | [MFPKEY\_WMAVOICE\_ENC\_EDL](mfpkey-wmavoice-enc-edlproperty.md)                                   |
| g\_wszWMADRCAverageReference          | [MFPKEY\_WMADRC\_AVGREF](mfpkey-wmadrc-avgrefproperty.md)                                          |
| g\_wszWMADRCAverageTarget             | [MFPKEY\_WMADRC\_AVGTARGET](mfpkey-wmadrc-avgtargetproperty.md)                                    |
| g\_wszWMADRCPeakReference             | [MFPKEY\_WMADRC\_PEAKREF](mfpkey-wmadrc-peakrefproperty.md)                                        |
| g\_wszWMADRCPeakTarget                | [MFPKEY\_WMADRC\_PEAKTARGET](mfpkey-wmadrc-peaktargetproperty.md)                                  |
| g\_wszWMCPAudioVBRQuality             | [MFPKEY\_VBRQUALITY](mfpkey-vbrqualityproperty.md)                                                 |
| g\_wszWMCPAudioVBRSupported           | [MFPKEY\_VBRENABLED](mfpkey-vbrenabledproperty.md)                                                 |
| g\_wszWMCPMaxPasses                   | [MFPKEY\_PASSESRECOMMENDED](mfpkey-passesrecommendedproperty.md)                                   |
| g\_wszWMVCAvgBitrate                  | [MFPKEY\_RAVG](mfpkey-ravgproperty.md)                                                             |
| g\_wszWMVCBAvg                        | [MFPKEY\_BAVG](mfpkey-bavgproperty.md)                                                             |
| g\_wszWMVCBDeltaQP                    | [MFPKEY\_BDELTAQP](mfpkey-bdeltaqpproperty.md)                                                     |
| g\_wszWMVCBMax                        | [MFPKEY\_BMAX](mfpkey-bmaxproperty.md)                                                             |
| g\_wszWMVCBufferFullnessInFirstByte   | [MFPKEY\_BUFFERFULLNESSINFIRSTBYTE](mfpkey-bufferfullnessinfirstbyteproperty.md)                   |
| g\_wszWMVCCodedFrames                 | [MFPKEY\_CODEDFRAMES](mfpkey-codedframesproperty.md)                                               |
| g\_wszWMVCComplexityEx                | [MFPKEY\_COMPLEXITYEX](mfpkey-complexityexproperty.md)                                             |
| g\_wszWMVCComplexityMode              | [MFPKEY\_COMPLEXITY](mfpkey-complexityproperty.md)                                                 |
| g\_wszWMVCCompressionOptimizationType | [MFPKEY\_COMPRESSIONOPTIMIZATIONTYPE](mfpkey-compressionoptimizationtypeproperty.md)               |
| g\_wszWMVCCrisp                       | [MFPKEY\_CRISP](mfpkey-crispproperty.md)                                                           |
| g\_wszWMVCDecoderComplexityProfile    | [MFPKEY\_DECODERCOMPLEXITYPROFILE](mfpkey-decodercomplexityprofileproperty.md)                     |
| g\_wszWMVCDecoderComplexityRequested  | [MFPKEY\_DECODERCOMPLEXITYREQUESTED](mfpkey-decodercomplexityrequestedproperty.md)                 |
| g\_wszWMVCDecoderDeinterlacing        | [MFPKEY\_DECODER\_DEINTERLACING](mfpkey-decoder-deinterlacingproperty.md)                          |
| g\_wszWMVCDenoiseOption               | [MFPKEY\_DENOISEOPTION](mfpkey-denoiseoptionproperty.md)                                           |
| g\_wszWMVCEndOfPass                   | [MFPKEY\_ENDOFPASS](mfpkey-endofpassproperty.md)                                                   |
| g\_wszWMVCForceFrameHeight            | [MFPKEY\_FORCEFRAMEHEIGHT](mfpkey-forceframeheightproperty.md)                                     |
| g\_wszWMVCForceFrameWidth             | [MFPKEY\_FORCEFRAMEWIDTH](mfpkey-forceframewidthproperty.md)                                       |
| g\_wszWMVCForceMedianSetting          | [MFPKEY\_FORCEMEDIANSETTING](mfpkey-forcemediansettingproperty.md)                                 |
| g\_wszWMVCFOURCC                      | [MFPKEY\_FOURCC](mfpkey-fourccproperty.md)                                                         |
| g\_wszWMVCInterlacedCodingEnabled     | [MFPKEY\_INTERLACEDCODINGENABLED](mfpkey-interlacedcodingenabledproperty.md)                       |
| g\_wszWMVCLookAhead                   | [MFPKEY\_LOOKAHEAD](mfpkey-lookaheadproperty.md)                                                   |
| g\_wszWMVCLoopFilter                  | [MFPKEY\_LOOPFILTER](mfpkey-loopfilterproperty.md)                                                 |
| g\_wszWMVCMacroblockModeCostMethod    | [MFPKEY\_MACROBLOCKMODECOSTMETHOD](mfpkey-macroblockmodecostmethodproperty.md)                     |
| g\_wszWMVCMaxBitrate                  | [MFPKEY\_RMAX](mfpkey-rmaxproperty.md)                                                             |
| g\_wszWMVCMotionMatchMethod           | [MFPKEY\_MOTIONMATCHMETHOD](mfpkey-motionmatchmethodproperty.md)                                   |
| g\_wszWMVCMotionSearchLevel           | [MFPKEY\_MOTIONSEARCHLEVEL](mfpkey-motionsearchlevelproperty.md)                                   |
| g\_wszWMVCMotionSearchRange           | [MFPKEY\_MOTIONSEARCHRANGE](mfpkey-motionsearchrangeproperty.md)                                   |
| g\_wszWMVCNoiseEdgeRemoval            | [MFPKEY\_NOISEEDGEREMOVAL](mfpkey-noiseedgeremovalproperty.md)                                     |
| g\_wszWMVCNumThreads                  | [MFPKEY\_NUMTHREADS](mfpkey-numthreadsproperty.md)                                                 |
| g\_wszWMVCPassesRecommended           | [MFPKEY\_PASSESRECOMMENDED](mfpkey-passesrecommendedproperty.md)                                   |
| g\_wszWMVCPassesUsed                  | [MFPKEY\_PASSESUSED](mfpkey-passesusedproperty.md)                                                 |
| g\_wszWMVCPerceptualOptLevel          | [MFPKEY\_PERCEPTUALOPTLEVEL](mfpkey-perceptualoptlevelproperty.md)                                 |
| g\_wszWMVCProduceDummyFrames          | [MFPKEY\_PRODUCEDUMMYFRAMES](mfpkey-producedummyframesproperty.md)                                 |
| g\_wszWMVCRangeRedux                  | [MFPKEY\_RANGEREDUX](mfpkey-rangereduxproperty.md)                                                 |
| g\_wszWMVCTotalFrames                 | [MFPKEY\_TOTALFRAMES](mfpkey-totalframesproperty.md)                                               |
| g\_wszWMVCVBREnabled                  | [MFPKEY\_VBRENABLED](mfpkey-vbrenabledproperty.md)                                                 |
| g\_wszWMVCVBRQuality                  | [MFPKEY\_VBRQUALITY](mfpkey-vbrqualityproperty.md)                                                 |
| g\_wszWMVCVideoScaling                | [MFPKEY\_VIDEOSCALING](mfpkey-videoscalingproperty.md)                                             |
| g\_wszWMVCVType                       | [MFPKEY\_VTYPE](mfpkey-vtypeproperty.md)                                                           |
| g\_wszWMVCZeroByteFrames              | [MFPKEY\_ZEROBYTEFRAMES](mfpkey-zerobyteframesproperty.md)                                         |



 

## Related topics

<dl> <dt>

[Windows Media Codecs](windows-media-codecs.md)
</dt> </dl>

 

 



