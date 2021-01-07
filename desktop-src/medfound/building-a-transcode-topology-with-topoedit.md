---
description: This topic describes how to create a transcoding topology in TopoEdit.
ms.assetid: 9a7b57f9-f606-4874-9fd3-aa37215f6f20
title: Building a Transcode Topology with TopoEdit
ms.topic: article
ms.date: 05/31/2018
---

# Building a Transcode Topology with TopoEdit

This topic describes how to create a transcoding topology in TopoEdit.

> [!Note]  
> This feature requires Windows 7

 

## To build a transcoding topology

1.  On the **File** menu, click **Render Transcode**.

2.  In the **Select Media Source** dialog box, select the source file for transcoding.
3.  Click **Open**.
4.  In the **Choose Transcode Profile** dialog box, select one of the encoding profiles from the drop-down list.
    > [!Note]  
    > The profiles are loaded from the file TranscodeProfiles.xml.

     

5.  In the **Choose target file** dialog, select the name of the output file.
6.  TopoEdit creates the transcode topology and displays the topology nodes in main application window.
7.  Click the **Play** button on the toolbar to run the media session. Wait for encoding to complete.

## TranscodeProfiles.xml

TopoEdit loads the encoding profiles from the file TranscodeProfiles.xml. This file is located in the Bin directory of the Windows SDK.

The file begins with a **TedTranscodeProfiles** element. Each profile begins with a **TedTranscodeProfile** element. Each profile consists of a set of values of the format `<VALUE_NAME Value="VALUE"/>`. The following values are defined:



| Value                                                                                                                                                                                                    | Description                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="AudioAvgBytesPerSecond"></span><span id="audioavgbytespersecond"></span><span id="AUDIOAVGBYTESPERSECOND"></span>**AudioAvgBytesPerSecond**<br/>                                         | The average bytes per second for the audio stream. Equivalent to the [**MF\_MT\_AUDIO\_AVG\_BYTES\_PER\_SECOND**](mf-mt-audio-avg-bytes-per-second-attribute.md) attribute.<br/>                                                |
| <span id="AudioBitsPerSample"></span><span id="audiobitspersample"></span><span id="AUDIOBITSPERSAMPLE"></span>**AudioBitsPerSample**<br/>                                                         | The number of bits per sample for the audio stream. Equivalent to the [**MF\_MT\_AUDIO\_BITS\_PER\_SAMPLE**](mf-mt-audio-bits-per-sample-attribute.md) attribute.<br/>                                                          |
| <span id="AudioBlockAlignment"></span><span id="audioblockalignment"></span><span id="AUDIOBLOCKALIGNMENT"></span>**AudioBlockAlignment**<br/>                                                     | The block alignment for the audio stream. Equivalent to the [**MF\_MT\_AUDIO\_BLOCK\_ALIGNMENT**](mf-mt-audio-block-alignment-attribute.md) attribute.<br/>                                                                     |
| <span id="AudioEncodingProfile"></span><span id="audioencodingprofile"></span><span id="AUDIOENCODINGPROFILE"></span>**AudioEncodingProfile**<br/>                                                 | A codec-specific value that defines the audio profile. Equivalent to the [MF\_TRANSCODE\_ENCODINGPROFILE](mf-transcode-encodingprofile.md) attribute. <br/>                                                                     |
| <span id="AudioFormat"></span><span id="audioformat"></span><span id="AUDIOFORMAT"></span>**AudioFormat**<br/>                                                                                     | The encoded audio subtype. Equivalent to the [**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md) attribute.<br/>                                                                                                                  |
| <span id="AudioNumChannels"></span><span id="audionumchannels"></span><span id="AUDIONUMCHANNELS"></span>**AudioNumChannels**<br/>                                                                 | The number of channels in the audio stream. Equivalent to the [**MF\_MT\_AUDIO\_NUM\_CHANNELS**](mf-mt-audio-num-channels-attribute.md) attribute.<br/>                                                                         |
| <span id="AudioSamplesPerSecond"></span><span id="audiosamplespersecond"></span><span id="AUDIOSAMPLESPERSECOND"></span>**AudioSamplesPerSecond**<br/>                                             | The sample rate of the audio stream, in samples per second. Equivalent to the [**MF\_MT\_AUDIO\_SAMPLES\_PER\_SECOND**](mf-mt-audio-samples-per-second-attribute.md) attribute.<br/>                                            |
| <span id="ContainerType"></span><span id="containertype"></span><span id="CONTAINERTYPE"></span>**ContainerType**<br/>                                                                             | The file container type. Equivalent to the [MF\_TRANSCODE\_CONTAINERTYPE](mf-transcode-containertype.md) attribute. <br/>                                                                                                       |
| <span id="ProfileName"></span><span id="profilename"></span><span id="PROFILENAME"></span>**ProfileName**<br/>                                                                                     | The display name of the profile.<br/>                                                                                                                                                                                            |
| <span id="SkipMetadataTransfer"></span><span id="skipmetadatatransfer"></span><span id="SKIPMETADATATRANSFER"></span>**SkipMetadataTransfer**<br/>                                                 | Specify 1 if metadata should not be transferred to the output file, or 0 if metadata should be transferred. Equivalent to the [MF\_TRANSCODE\_SKIP\_METADATA\_TRANSFER](mf-transcode-skip-metadata-transfer.md) attribute.<br/> |
| <span id="VideoBitrate"></span><span id="videobitrate"></span><span id="VIDEOBITRATE"></span>**VideoBitrate**<br/>                                                                                 | The average video bitrate. Equivalent to the [**MF\_MT\_AVG\_BITRATE**](mf-mt-avg-bitrate-attribute.md) attribute. <br/>                                                                                                        |
| <span id="VideoEncodeComplexity"></span><span id="videoencodecomplexity"></span><span id="VIDEOENCODECOMPLEXITY"></span>**VideoEncodeComplexity**<br/>                                             | A codec-specific value that defines the encode quality. Equivalent to the [MF\_TRANSCODE\_QUALITYVSSPEED](mf-transcode-qualityvsspeed.md) attribute. <br/>                                                                      |
| <span id="VideoEncodingProfile"></span><span id="videoencodingprofile"></span><span id="VIDEOENCODINGPROFILE"></span>**VideoEncodingProfile**<br/>                                                 | A codec-specific value that defines the video profile. Equivalent to the [MF\_TRANSCODE\_ENCODINGPROFILE](mf-transcode-encodingprofile.md) attribute. <br/>                                                                     |
| <span id="VideoFormat"></span><span id="videoformat"></span><span id="VIDEOFORMAT"></span>**VideoFormat**<br/>                                                                                     | The encoded video subtype. Equivalent to the [**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md) attribute.<br/>                                                                                                                  |
| <span id="VideoFrameHeight"></span><span id="videoframeheight"></span><span id="VIDEOFRAMEHEIGHT"></span>**VideoFrameHeight**<br/>                                                                 | The height of the output video. Equivalent to the [**MF\_MT\_FRAME\_SIZE**](mf-mt-frame-size-attribute.md) attribute.<br/>                                                                                                      |
| <span id="VideoFrameRateDenominator"></span><span id="videoframeratedenominator"></span><span id="VIDEOFRAMERATEDENOMINATOR"></span>**VideoFrameRateDenominator**<br/>                             | The denominator of the frame rate of the output video. Equivalent to the [**MF\_MT\_FRAME\_RATE**](mf-mt-frame-rate-attribute.md) attribute.<br/>                                                                               |
| <span id="VideoFrameRateNumerator"></span><span id="videoframeratenumerator"></span><span id="VIDEOFRAMERATENUMERATOR"></span>**VideoFrameRateNumerator**<br/>                                     | The numerator of the frame rate of the output video. Equivalent to the [**MF\_MT\_FRAME\_RATE**](mf-mt-frame-rate-attribute.md) attribute.<br/>                                                                                 |
| <span id="VideoFrameWidth"></span><span id="videoframewidth"></span><span id="VIDEOFRAMEWIDTH"></span>**VideoFrameWidth**<br/>                                                                     | The width of the output video. Equivalent to the [**MF\_MT\_FRAME\_SIZE**](mf-mt-frame-size-attribute.md) attribute.<br/>                                                                                                       |
| <span id="VideoPixelAspectRatioDenominator"></span><span id="videopixelaspectratiodenominator"></span><span id="VIDEOPIXELASPECTRATIODENOMINATOR"></span>**VideoPixelAspectRatioDenominator**<br/> | The denominator of the pixel aspect ratio (PAR) of the output video. Equivalent to the [**MF\_MT\_PIXEL\_ASPECT\_RATIO**](mf-mt-pixel-aspect-ratio-attribute.md) attribute. <br/>                                               |
| <span id="VideoPixelAspectRatioNumerator"></span><span id="videopixelaspectrationumerator"></span><span id="VIDEOPIXELASPECTRATIONUMERATOR"></span>**VideoPixelAspectRatioNumerator**<br/>         | The numerator of the PAR of the output video. Equivalent to the [**MF\_MT\_PIXEL\_ASPECT\_RATIO**](mf-mt-pixel-aspect-ratio-attribute.md) attribute. <br/>                                                                      |



 

## Related topics

<dl> <dt>

[TopoEdit](topoedit.md)
</dt> </dl>

 

 




