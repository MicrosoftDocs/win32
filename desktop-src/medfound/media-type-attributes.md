---
description: Media Type Attributes
ms.assetid: e84ba3f6-4857-4340-baca-5847650ea7b8
title: Media Type Attributes
ms.topic: article
ms.date: 05/31/2018
---

# Media Type Attributes

The following attributes apply to media types. Some of these attributes are intended only for converting legacy media type formats into Media Foundation media types.

## General Format Attributes

These attributes can be applied to all media types.



| Attribute                                                                            | Description                                                                            |
|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**MF\_MT\_ALL\_SAMPLES\_INDEPENDENT**](mf-mt-all-samples-independent-attribute.md) | Specifies whether each sample is independent of the other samples in the stream.       |
| [**MF\_MT\_AM\_FORMAT\_TYPE**](mf-mt-am-format-type-attribute.md)                   | Format GUID.                                                                           |
| [**MF\_MT\_COMPRESSED**](mf-mt-compressed-attribute.md)                             | Specifies whether the media data is compressed                                         |
| [**MF\_MT\_FIXED\_SIZE\_SAMPLES**](mf-mt-fixed-size-samples-attribute.md)           | Specifies whether the samples have a fixed size.                                       |
| [**MF\_MT\_MAJOR\_TYPE**](mf-mt-major-type-attribute.md)                            | Major type GUID.                                                                       |
| [**MF\_MT\_SAMPLE\_SIZE**](mf-mt-sample-size-attribute.md)                          | Size of each sample, in bytes.                                                         |
| [**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md)                                   | Subtype GUID.                                                                          |
| [**MF\_MT\_USER\_DATA**](mf-mt-user-data-attribute.md)                              | Contains user data for a media type that was converted from a legacy format structure. |
| [**MF\_MT\_WRAPPED\_TYPE**](mf-mt-wrapped-type-attribute.md)                        | Contains a media type that has been wrapped in another media type.                     |



 

## Audio Format Attributes

These attributes can be applied to media types whose major type equals MFMediaType\_Audio.



| Attribute                                                                                            | Description                                                                                 |
|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [MF\_MT\_AAC\_AUDIO\_PROFILE\_LEVEL\_INDICATION](mf-mt-aac-audio-profile-level-indication.md)       | Specifies the audio profile and level of an Advanced Audio Coding (AAC) stream.             |
| [MF\_MT\_AAC\_PAYLOAD\_TYPE](mf-mt-aac-payload-type.md)                                             | Specifies the payload type for an Advanced Audio Coding (AAC) stream.                       |
| [**MF\_MT\_AUDIO\_AVG\_BYTES\_PER\_SECOND**](mf-mt-audio-avg-bytes-per-second-attribute.md)         | Average number of bytes per second.                                                         |
| [**MF\_MT\_AUDIO\_BITS\_PER\_SAMPLE**](mf-mt-audio-bits-per-sample-attribute.md)                    | Number of bits per audio sample.                                                            |
| [**MF\_MT\_AUDIO\_BLOCK\_ALIGNMENT**](mf-mt-audio-block-alignment-attribute.md)                     | Block alignment, in bytes.                                                                  |
| [**MF\_MT\_AUDIO\_CHANNEL\_MASK**](mf-mt-audio-channel-mask-attribute.md)                           | Specifies the assignment of audio channels to speaker positions.                            |
| [**MF\_MT\_AUDIO\_FLOAT\_SAMPLES\_PER\_SECOND**](mf-mt-audio-float-samples-per-second-attribute.md) | Number of audio samples per second (floating-point value).                                  |
| [**MF\_MT\_AUDIO\_FOLDDOWN\_MATRIX**](mf-mt-audio-folddown-matrix-attribute.md)                     | Specifies how an audio decoder should transform multichannel audio to stereo output.        |
| [**MF\_MT\_AUDIO\_NUM\_CHANNELS**](mf-mt-audio-num-channels-attribute.md)                           | Number of audio channels.                                                                   |
| [**MF\_MT\_AUDIO\_PREFER\_WAVEFORMATEX**](mf-mt-audio-prefer-waveformatex-attribute.md)             | Specifies the preferred legacy format structure to use when converting an audio media type. |
| [**MF\_MT\_AUDIO\_SAMPLES\_PER\_BLOCK**](mf-mt-audio-samples-per-block-attribute.md)                | Number of audio samples contained in one compressed block of audio data.                    |
| [**MF\_MT\_AUDIO\_SAMPLES\_PER\_SECOND**](mf-mt-audio-samples-per-second-attribute.md)              | Number of audio samples per second (integer value).                                         |
| [**MF\_MT\_AUDIO\_VALID\_BITS\_PER\_SAMPLE**](mf-mt-audio-valid-bits-per-sample-attribute.md)       | Number of valid bits of audio data in each audio sample.                                    |
| [**MF\_MT\_AUDIO\_WMADRC\_AVGREF**](mf-mt-audio-wmadrc-avgref-attribute.md)                         | Reference average volume level of a Windows Media Audio file.                               |
| [**MF\_MT\_AUDIO\_WMADRC\_AVGTARGET**](mf-mt-audio-wmadrc-avgtarget-attribute.md)                   | Target average volume level of a Windows Media Audio file.                                  |
| [**MF\_MT\_AUDIO\_WMADRC\_PEAKREF**](mf-mt-audio-wmadrc-peakref-attribute.md)                       | Reference peak volume level of a Windows Media Audio file.                                  |
| [**MF\_MT\_AUDIO\_WMADRC\_PEAKTARGET**](mf-mt-audio-wmadrc-peaktarget-attribute.md)                 | Target peak volume level of a Windows Media Audio file.                                     |
| [MF\_MT\_ORIGINAL\_WAVE\_FORMAT\_TAG](mf-mt-original-wave-format-tag.md)                            | Contains the original WAVE format tag for an audio stream.                                  |



 

## Video Format Attributes

These attributes can be applied to media types whose major type equals MFMediaType\_Video.



| Attribute                                                                              | Description                                                                                                                             |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [**MF\_MT\_AVG\_BIT\_ERROR\_RATE**](mf-mt-avg-bit-error-rate-attribute.md)            | Data error rate.                                                                                                                        |
| [**MF\_MT\_AVG\_BITRATE**](mf-mt-avg-bitrate-attribute.md)                            | Approximate data rate of the video stream.                                                                                              |
| [**MF\_MT\_CUSTOM\_VIDEO\_PRIMARIES**](mf-mt-custom-video-primaries-attribute.md)     | Custom color primaries.                                                                                                                 |
| [**MF\_MT\_DEFAULT\_STRIDE**](mf-mt-default-stride-attribute.md)                      | Default surface stride.                                                                                                                 |
| [**MF\_MT\_DRM\_FLAGS**](mf-mt-drm-flags-attribute.md)                                | Specifies whether the video requires enforcing copy protection.                                                                         |
| [**MF\_MT\_FRAME\_RATE**](mf-mt-frame-rate-attribute.md)                              | Frame rate.                                                                                                                             |
| [MF\_MT\_FRAME\_RATE\_RANGE\_MAX](mf-mt-frame-rate-range-max.md)                      | The maximum frame rate supported by a video capture device.                                                                             |
| [MF\_MT\_FRAME\_RATE\_RANGE\_MIN](mf-mt-frame-rate-range-min.md)                      | The minimum frame rate supported by a video capture device.                                                                             |
| [**MF\_MT\_FRAME\_SIZE**](mf-mt-frame-size-attribute.md)                              | Width and height of the video frame.                                                                                                    |
| [**MF\_MT\_GEOMETRIC\_APERTURE**](mf-mt-geometric-aperture-attribute.md)              | Geometric aperture.                                                                                                                     |
| [**MF\_MT\_INTERLACE\_MODE**](mf-mt-interlace-mode-attribute.md)                      | Describes how the frames are interlaced.                                                                                                |
| [**MF\_MT\_MAX\_KEYFRAME\_SPACING**](mf-mt-max-keyframe-spacing-attribute.md)         | Maximum number of frames from one key frame to the next.                                                                                |
| [**MF\_MT\_MINIMUM\_DISPLAY\_APERTURE**](mf-mt-minimum-display-aperture-attribute.md) | Minimum display aperture.                                                                                                               |
| [**MF\_MT\_MPEG\_SEQUENCE\_HEADER**](mf-mt-mpeg-sequence-header-attribute.md)         | MPEG-1 or MPEG-2 sequence header.                                                                                                       |
| [**MF\_MT\_MPEG\_START\_TIME\_CODE**](mf-mt-mpeg-start-time-code-attribute.md)        | Group-of-pictures (GOP) start time code.                                                                                                |
| [**MF\_MT\_MPEG2\_FLAGS**](mf-mt-mpeg2-flags-attribute.md)                            | Miscellaneous flags for MPEG-2 video.                                                                                                   |
| [**MF\_MT\_MPEG2\_LEVEL**](mf-mt-mpeg2-level-attribute.md)                            | MPEG-2 or H.264 level.                                                                                                                  |
| [**MF\_MT\_MPEG2\_PROFILE**](mf-mt-mpeg2-profile-attribute.md)                        | MPEG-2 or H.264 profile.                                                                                                                |
| [MF\_MT\_ORIGINAL\_4CC](mf-mt-original-4cc.md)                                        | Contains the original codec FOURCC for a video stream.                                                                                  |
| [**MF\_MT\_PAD\_CONTROL\_FLAGS**](mf-mt-pad-control-flags-attribute.md)               | Aspect ratio of the output rectangle.                                                                                                   |
| [**MF\_MT\_PALETTE**](mf-mt-palette-attribute.md)                                     | Palette entries.                                                                                                                        |
| [**MF\_MT\_PAN\_SCAN\_APERTURE**](mf-mt-pan-scan-aperture-attribute.md)               | Defines the 4×3 region of video that should be displayed in pan/scan mode.                                                              |
| [**MF\_MT\_PAN\_SCAN\_ENABLED**](mf-mt-pan-scan-enabled-attribute.md)                 | Specifies whether pan/scan mode is enabled.                                                                                             |
| [**MF\_MT\_PIXEL\_ASPECT\_RATIO**](mf-mt-pixel-aspect-ratio-attribute.md)             | Pixel aspect ratio.                                                                                                                     |
| [**MF\_MT\_SOURCE\_CONTENT\_HINT**](mf-mt-source-content-hint-attribute.md)           | Intended aspect ratio.                                                                                                                  |
| [**MF\_MT\_TRANSFER\_FUNCTION**](mf-mt-transfer-function-attribute.md)                | Conversion function from RGB to R'G'B'.                                                                                                 |
| [MF\_MT\_VIDEO\_3D](mf-mt-video-3d.md)                                                | Specifies whether a video stream contains 3D content.                                                                                   |
| [**MF\_MT\_VIDEO\_CHROMA\_SITING**](mf-mt-video-chroma-siting-attribute.md)           | Describes how chroma was sampled for Y'Cb'Cr' video.                                                                                    |
| [**MF\_MT\_VIDEO\_LIGHTING**](mf-mt-video-lighting-attribute.md)                      | Optimal lighting conditions for viewing.                                                                                                |
| [**MF\_MT\_VIDEO\_NOMINAL\_RANGE**](mf-mt-video-nominal-range-attribute.md)           | Nominal range of the color information                                                                                                  |
| [**MF\_MT\_VIDEO\_PRIMARIES**](mf-mt-video-primaries-attribute.md)                    | Color primaries.                                                                                                                        |
| [MF\_MT\_VIDEO\_ROTATION](mf-mt-video-rotation.md)                                    | Specifies the rotation of a video frame in the counter-clockwise direction.                                                             |
| [**MF\_MT\_YUV\_MATRIX**](mf-mt-yuv-matrix-attribute.md)                              | Conversion matrix from the Y'Cb'Cr' color space to the R'G'B' color space.                                                              |
| [MF\_XVP\_CALLER\_ALLOCATES\_OUTPUT](mf-xvp-caller-allocates-output.md)               | Specifies whether that the caller will allocate the textures used for output by the [**Video Processor MFT**](video-processor-mft.md). |
| [MF\_XVP\_DISABLE\_FRC](mf-xvp-disable-frc.md)                                        | Disables frame-rate conversion in the [**Video Processor MFT**](video-processor-mft.md).                                               |



 

## Other Format Attributes

The following attributes apply to interleaved DV video.



| Attribute                                                                      | Description                                                           |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [**MF\_MT\_DV\_AAUX\_CTRL\_PACK\_0**](mf-mt-dv-aaux-ctrl-pack-0-attribute.md) | Audio auxiliary (AAUX) source control pack for the first audio block. |
| [**MF\_MT\_DV\_AAUX\_CTRL\_PACK\_1**](mf-mt-dv-aaux-ctrl-pack-1-attribute.md) | AAUX source control pack for the second audio block.                  |
| [**MF\_MT\_DV\_AAUX\_SRC\_PACK\_0**](mf-mt-dv-aaux-src-pack-0-attribute.md)   | AAUX source pack for the first audio block.                           |
| [**MF\_MT\_DV\_AAUX\_SRC\_PACK\_1**](mf-mt-dv-aaux-src-pack-1-attribute.md)   | AAUX source pack for the second audio block.                          |
| [**MF\_MT\_DV\_VAUX\_CTRL\_PACK**](mf-mt-dv-vaux-ctrl-pack-attribute.md)      | Video auxiliary (VAUX) source control pack.                           |
| [**MF\_MT\_DV\_VAUX\_SRC\_PACK**](mf-mt-dv-vaux-src-pack-attribute.md)        | VAUX source pack.                                                     |



 

The following attributes apply to Advanced Streaming Format (ASF) files.



| Attribute                                                      | Description                                                      |
|----------------------------------------------------------------|------------------------------------------------------------------|
| [MF\_MT\_ARBITRARY\_FORMAT](mf-mt-arbitrary-format.md)        | Additional format data for a binary stream in an ASF file.       |
| [MF\_MT\_ARBITRARY\_HEADER](mf-mt-arbitrary-header.md)        | Type-specific data for a binary stream in an ASF file.           |
| [MF\_MT\_IMAGE\_LOSS\_TOLERANT](mf-mt-image-loss-tolerant.md) | Specifies whether an ASF image stream is a degradable JPEG type. |



 

The following attributes apply to MPEG-4 files.



| Attribute                                                                     | Description                                                   |
|-------------------------------------------------------------------------------|---------------------------------------------------------------|
| [MF\_MT\_MPEG4\_CURRENT\_SAMPLE\_ENTRY](mf-mt-mpeg4-current-sample-entry.md) | The index of the current entry in the sample description box. |
| [MF\_MT\_MPEG4\_SAMPLE\_DESCRIPTION](mf-mt-mpeg4-sample-description.md)      | The sample description box.                                   |



 

## Related topics

<dl> <dt>

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)
</dt> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> <dt>

[Media Types](media-types.md)
</dt> <dt>

[Audio Media Types](audio-media-types.md)
</dt> <dt>

[Video Media Types](video-media-types.md)
</dt> </dl>

 

 



