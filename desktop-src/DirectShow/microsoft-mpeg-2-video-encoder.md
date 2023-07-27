---
description: The Microsoft MPEG-2 Video Encoder filter encodes MPEG-2 and MPEG-1 video.
ms.assetid: d52c1299-0641-405c-8960-edd738b56823
title: Microsoft MPEG-2 Video Encoder (Wmcodecdsp.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Microsoft MPEG-2 Video Encoder

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Microsoft MPEG-2 Video Encoder filter encodes MPEG-2 and MPEG-1 video.

To encode and multiplex audio/video streams, use the [**Microsoft MPEG-2 Encoder**](microsoft-mpeg-2-encoder.md) filter, which encapsulates the functions of both this filter and the [**Microsoft MPEG-2 Audio Encoder**](microsoft-mpeg-2-audio-encoder.md) filter.

> [!Note]  
> This filter is not supported on IA-64-based platforms.

 



Filter Information

Filter Interfaces

[**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter)<br/> [**ICodecAPI**](/windows/desktop/api/Strmif/nn-strmif-icodecapi)<br/> **IEncoderAPI**<br/> [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking)<br/> [**IVideoEncoder**](/windows/win32/api/strmif/nn-strmif-ivideoencoder)<br/>

Input Pin Media Types

**MEDIATYPE\_Video**, **MEDIASUBTYPE\_I420**<br/> **MEDIATYPE\_Video**, **MEDIASUBTYPE\_IYUV**<br/> **MEDIATYPE\_Video**, **MEDIASUBTYPE\_RGB24**<br/> **MEDIATYPE\_Video**, **MEDIASUBTYPE\_UYVY**<br/> **MEDIATYPE\_Video**, **MEDIASUBTYPE\_YUY2**<br/> **MEDIATYPE\_Video**, **MEDIASUBTYPE\_YV12**<br/>

Input Pin Interfaces

[**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin)<br/> [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin)<br/> [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)<br/>

Output Pin Media Types

**MEDIATYPE\_Stream**, **MEDIASUBTYPE\_MPEG2\_VIDEO**<br/> **MEDIATYPE\_Stream**, **MEDIASUBTYPE\_MPEG2\_PROGRAM**<br/> **MEDIATYPE\_Stream**, **MEDIASUBTYPE\_MPEG2\_TRANSPORT**<br/> **MEDIATYPE\_Video**, **MEDIASUBTYPE\_MPEG2\_VIDEO**<br/>

Output Pin Interfaces

[**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking)<br/> [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin)<br/> [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)<br/>

Filter CLSID

**CLSID\_CMPEG2EncoderVideoDS** (declared in wmcodecdsp.h)

Executable

msmpeg2enc.dll

[Merit](merit.md)

**MERIT\_DO\_NOT\_USE**

[Filter Category](filter-categories.md)

**CLSID\_LegacyAmFilterCategory**



 

## Remarks

The MPEG-2 Video Encoder can produce the following kinds of output:

-   Video elementary stream
-   Video in an MPEG-2 program stream
-   Video in an MPEG-2 transport stream

It supports the following MPEG-2 profiles and levels:



| Profile        | Levels                     | Remarks                                            |
|----------------|----------------------------|----------------------------------------------------|
| Simple Profile | Main                       |                                                    |
| Main Profile   | Low, Main, High, High-1440 |                                                    |
| High Profile   | Main, High, High-1440      | No scalability or 4:2:2/4:4:4 support (only 4:2:0) |
| 4:2:2 Profile  | Main, High                 | No scalability or 4:2:2 support (only 4:2:0)       |



 

### Codec Properties

The filter supports the following properties through [**ICodecAPI**](/windows/desktop/api/Strmif/nn-strmif-icodecapi).



| Property                                                                                      | Default                                                          | Supported Values                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AVEncCodecType**](avenccodectype-property.md)                                             | MPEG-2 video                                                     | **CODECAPI\_GUID\_AVEncMPEG1Video**<br/> **CODECAPI\_GUID\_AVEncMPEG2Video**<br/>                                                                                                                        |
| [**AVEncCommonBufferInLevel**](avenccommonbufferinlevel-property.md)                         | 12222464 bits                                                    |                                                                                                                                                                                                                      |
| [**AVEncCommonBufferOutLevel**](avenccommonbufferoutlevel-property.md)                       | 12222464 bits                                                    |                                                                                                                                                                                                                      |
| [**AVEncCommonBufferSize**](avenccommonbuffersize-property.md)                               | 12222464 bits                                                    |                                                                                                                                                                                                                      |
| [**AVEncCommonFormatConstraint**](avenccommonformatconstraint-property.md)                   | Unspecified                                                      | **CODECAPI\_GUID\_AVEncCommonFormatUnSpecified** (No format constraint)<br/> **CODECAPI\_GUID\_AVEncCommonFormatDVD\_V** (DVD-Video)<br/> **CODECAPI\_GUID\_AVEncCommonFormatVCD** (Video CD)<br/> |
| [**AVEncCommonMaxBitRate**](avenccommonmaxbitrate-property.md)                               | 9800000 (9.8 Mbits/second)                                       |                                                                                                                                                                                                                      |
| [**AVEncCommonMeanBitRate**](avenccommonmeanbitrate-property.md)                             | 7000000 (7.0 Mbits/second)                                       |                                                                                                                                                                                                                      |
| [**AVEncCommonMinBitRate**](avenccommonminbitrate-property.md)                               | 128                                                              |                                                                                                                                                                                                                      |
| [**AVEncCommonMultipassMode**](avenccommonmultipassmode-property.md)                         | 1                                                                | 1                                                                                                                                                                                                                    |
| [**AVEncCommonQuality**](avenccommonquality-property.md)                                     | 100                                                              | 1 — 100                                                                                                                                                                                                              |
| [**AVEncCommonQualityVsSpeed**](avenccommonqualityvsspeed-property.md)                       | 75                                                               | 0 — 100                                                                                                                                                                                                              |
| [**AVEncCommonRateControlMode**](avenccommonratecontrolmode-property.md)                     | CBR                                                              | **eAVEncCommonRateControlMode\_CBR**<br/> **eAVEncCommonRateControlMode\_PeakConstrainedVBR**<br/> **eAVEncCommonRateControlMode\_Quality**<br/>                                                   |
| [**AVEncInputVideoSystem**](avencinputvideosystem-property.md)                               | Unspecified                                                      | eAVEncInputVideoSystem\_Unspecified<br/> eAVEncInputVideoSystem\_PAL<br/> eAVEncInputVideoSystem\_NTSC<br/>                                                                                        |
| [**AVEncMPVDefaultBPictureCount**](avencmpvdefaultbpicturecount-property.md)                 | 2                                                                | 0 — 2                                                                                                                                                                                                                |
| [**AVEncMPVFrameFieldMode**](avencmpvframefieldmode-property.md)                             | Frame mode                                                       |                                                                                                                                                                                                                      |
| [**AVEncMPVGenerateHeaderSeqDispExt**](avencmpvgenerateheaderseqdispext-property.md)         | **TRUE**                                                         |                                                                                                                                                                                                                      |
| [**AVEncMPVGenerateHeaderSeqExt**](avencmpvgenerateheaderseqext-property.md)                 | **TRUE**                                                         |                                                                                                                                                                                                                      |
| [**AVEncMPVGOPOpen**](avencmpvgopopen-property.md)                                           | **FALSE**                                                        |                                                                                                                                                                                                                      |
| [**AVEncMPVGOPSInSeq**](avencmpvgopsinseq-property.md)                                       | 1                                                                | 0 — 1                                                                                                                                                                                                                |
| [**AVEncMPVGOPSize**](avencmpvgopsize-property.md)                                           | 18 frames (36 fields) for NTSC; 15 frames (30 fields) otherwise. | 1 — 30; see Remarks                                                                                                                                                                                                  |
| [**AVEncMPVIntraDCPrecision**](avencmpvintradcprecision-property.md)                         | 9                                                                | 8 — 10                                                                                                                                                                                                               |
| [**AVEncMPVLevel**](avencmpvlevel-property.md)                                               | High                                                             |                                                                                                                                                                                                                      |
| [**AVEncMPVProfile**](avencmpvprofile-property.md)                                           | Main                                                             |                                                                                                                                                                                                                      |
| [**AVEncVideoDefaultUpperFieldDominant**](avencvideodefaultupperfielddominant-property.md)   | **TRUE**                                                         |                                                                                                                                                                                                                      |
| [**AVEncVideoForceSourceScanType**](avencvideoforcesourcescantype-property.md)               | Interlaced                                                       | **eAVEncVideoSourceScan\_Interlaced**<br/> **eAVEncVideoSourceScan\_Progressive**<br/>                                                                                                                   |
| [**AVEncVideoInputChromaResolution**](avencvideoinputchromaresolution-property.md)           | 4:2:0                                                            | **eAVEncVideoChromaResolution\_420** (4:2:0)<br/> **eAVEncVideoChromaResolution\_SameAsSource**<br/>                                                                                                     |
| [**AVEncVideoInputChromaSubsampling**](avencvideoinputchromasubsampling-property.md)         | Same as source                                                   |                                                                                                                                                                                                                      |
| [**AVEncVideoInputColorNominalRange**](avencvideoinputcolornominalrange-property.md)         | Same as source                                                   |                                                                                                                                                                                                                      |
| [**AVEncVideoInputColorPrimaries**](avencvideoinputcolorprimaries-property.md)               | Same as source                                                   |                                                                                                                                                                                                                      |
| [**AVEncVideoInputColorTransferFunction**](avencvideoinputcolortransferfunction-property.md) | Same as source                                                   |                                                                                                                                                                                                                      |
| [**AVEncVideoInputColorTransferMatrix**](avencvideoinputcolortransfermatrix-property.md)     | Same as source                                                   |                                                                                                                                                                                                                      |
| [**AVEncVideoMaxKeyframeDistance**](avencvideomaxkeyframedistance-property.md)               | [**AVEncMPVGOPSize**](avencmpvgopsize-property.md) - 1          | 0 or [**AVEncMPVGOPSize**](avencmpvgopsize-property.md) - 1                                                                                                                                                         |
| [**AVEncVideoNoOfFieldsToEncode**](avencvideonooffieldstoencode-property.md)                 | 0                                                                |                                                                                                                                                                                                                      |
| [**AVEncVideoOutputChromaResolution**](avencvideooutputchromaresolution-property.md)         | 4:2:0                                                            | **eAVEncVideoChromaResolution\_420** (4:2:0)<br/> **eAVEncVideoChromaResolution\_SameAsSource**<br/>                                                                                                     |
| [**AVEncVideoOutputFrameRate**](avencvideooutputframerate-property.md)                       |                                                                  | Must be the same as the input frame rate.                                                                                                                                                                            |
| [**AVEncVideoOutputScanType**](avencvideooutputscantype-property.md)                         | Same as input                                                    | **eAVEncVideoOutputScan\_SameAsInput**                                                                                                                                                                               |
| [**AVEncVideoPixelAspectRatio**](avencvideopixelaspectratio-property.md)                     | 1:1                                                              |                                                                                                                                                                                                                      |



 

It is recommended to set properties in the following order:

1.  [**AVEncCommonFormatConstraint**](avenccommonformatconstraint-property.md)
2.  [**AVEncCodecType**](avenccodectype-property.md)
3.  [**AVEncMPVProfile**](avencmpvprofile-property.md)
4.  [**AVEncMPVLevel**](avencmpvlevel-property.md)
5.  [**AVEncInputVideoSystem**](avencinputvideosystem-property.md)

Set the remaining properties in any order. (However, see [GOP Structure](#gop-structure).)

It is possible to set properties while the filter graph is running. There is a delay of at least one GOP before the new settings take effect.

### Encoder Operation

When encoding MPEG-1 video, the encoder automatically sets the 1-bit **constrained\_parameters\_flag** code in the sequence header if all constraints are met.

If needed, the encoder rounds up the input video dimensions so that the output video dimensions match the MPEG requirements. For progressive video, the output dimensions are rounded up to a multiple of 16 in both width and height. For interlaced video, width is rounded up to a multiple of 16, and height is rounded up to a multiple of 32. This round-up operation uses padding as needed.

If the video is interlaced, the encoder performs automatic telecine (3:2 pull-down) detection. The input video can contain field picture pairs, in addition to interlaced frames.

The encoder's internal format is 4:2:0 IYUV (identical to I420). It can perform color conversion from YUY2, YV12, UYVY, and RGB-24 video formats.

To constrain the bitstream to a target format (DVD or VCD), set the [**AVEncCommonFormatConstraint**](avenccommonformatconstraint-property.md) property. If this property has a value other than **GUID\_AVEncCommonFormatUnSpecified**, the encoder limits the MPEG syntax to that allowed by the target format.

For live encoding, set the [**AVEncCommonQualityVsSpeed**](avenccommonqualityvsspeed-property.md) property to zero. This causes the encoder to optimize for speed.

### Encoding Modes

The encoder supports several encoding modes:

-   One-pass constant bit rate (CBR).
-   One-pass quality-based variable bit rate (VBR), using a constant quantizer step size. In this mode, the encoder attempts to meet a target quality level, up to a maximum bit rate.
-   One-pass peak-constrained VBR. In this mode, the encoder attempts to achieve a target average bit rate within certain internal limits.

To configure the encoding mode, set the following properties:




| Mode | Properties | 
|------|------------|
| CBR | <a href="avenccommonratecontrolmode-property.md"><strong>AVEncCommonRateControlMode</strong></a> = <strong>eAVEncCommonRateControlMode_CBR</strong><br /><a href="avenccommonqualityvsspeed-property.md"><strong>AVEncCommonQualityVsSpeed</strong></a><br /><a href="avenccommonmeanbitrate-property.md"><strong>AVEncCommonMeanBitRate</strong></a><br /> | 
| Quality-based VBR | <a href="avenccommonratecontrolmode-property.md"><strong>AVEncCommonRateControlMode</strong></a> = <strong>eAVEncCommonRateControlMode_Quality</strong><br /><a href="avenccommonquality-property.md"><strong>AVEncCommonQuality</strong></a><br /><a href="avenccommonmaxbitrate-property.md"><strong>AVEncCommonMaxBitRate</strong></a><br /><blockquote>[!Note]<br />In this mode, the <a href="avenccommonmeanbitrate-property.md"><strong>AVEncCommonMeanBitRate</strong></a> and <a href="avenccommonminbitrate-property.md"><strong>AVEncCommonMinBitRate</strong></a> properties are not used. The minimum bit rate is assumed to be zero.</blockquote><br /> | 
| Peak-constrained VBR | <a href="avenccommonratecontrolmode-property.md"><strong>AVEncCommonRateControlMode</strong></a> = <strong>eAVEncCommonRateControlMode_PeakConstrainedVBR</strong><br /><a href="avenccommonmultipassmode-property.md"><strong>AVEncCommonMultipassMode</strong></a> = 1<br /><a href="avenccommonminbitrate-property.md"><strong>AVEncCommonMinBitRate</strong></a><br /><a href="avenccommonmaxbitrate-property.md"><strong>AVEncCommonMaxBitRate</strong></a><br /><a href="avenccommonmeanbitrate-property.md"><strong>AVEncCommonMeanBitRate</strong></a><br /> | 




 

> [!Note]  
> Two-pass VBR is not supported.

 

### Aspect Ratio

The display aspect ratio and pixel aspect ratio (PAR) are related by the following formula:

<dl> Display aspect ratio = PAR × (picture width / picture height)  
</dl>

The encoder uses this formula to calculate the value of pel\_aspect\_ratio for MPEG-1 bitstreams or aspect\_ratio\_information for MPEG-2 bitstreams. (See ISO/IEC 11172 and ISO/IEC 138181-2, respectively.)

The encoder tries the following settings, in order:

1.  If the application sets the [**AVEncVideoPixelAspectRatio**](avencvideopixelaspectratio-property.md) property at any time before the filter graph runs, this property is used for the PAR.
2.  Otherwise, if the **dwPictAspectRatioX** and **dwPictAspectRatioY** members of the [**VIDEOINFOHEADER2**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-videoinfoheader2) structure are non-zero, these members are used for the display aspect ratio, and the PAR is calculated from the display aspect ratio.
3.  If none of these values is present, the PAR is assumed to be 1.0, and the display aspect ratio is calculated accordingly.

In live encoding mode ([**AVEncCommonQualityVsSpeed**](avenccommonqualityvsspeed-property.md) equal to zero), the display aspect ratio must be either 4:3 or 16:9, with a default value of 4:3. If the computed display aspect ratio is not 4:3 or 16:9, the encoder uses the value 4:3.

### GOP Structure

To specify the group of picture (GOP) structure, set the following properties in order:

1.  [**AVEncMPVGOPSize**](avencmpvgopsize-property.md)
2.  [**AVEncVideoMaxKeyframeDistance**](avencvideomaxkeyframedistance-property.md)
3.  [**AVEncMPVDefaultBPictureCount**](avencmpvdefaultbpicturecount-property.md)

Based on these settings, the encoder produces one of the following GOP structures:



| [**AVEncVideoMaxKeyframeDistance**](avencvideomaxkeyframedistance-property.md) | [**AVEncMPVDefaultBPictureCount**](avencmpvdefaultbpicturecount-property.md) | GOP Structure |
|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------|---------------|
| 0                                                                               | 0                                                                             | IIII...       |
| [**AVEncMPVGOPSize**](avencmpvgopsize-property.md) - 1                         | 0                                                                             | IPPP...       |
| [**AVEncMPVGOPSize**](avencmpvgopsize-property.md) - 1                         | 1                                                                             | IBPBP...      |
| [**AVEncMPVGOPSize**](avencmpvgopsize-property.md) - 1                         | 2                                                                             | IBBPBBP...    |



 

The default GOP structure is IBBPBBP... with a GOP size of 15 frames.

If the application constrains the target format to DVD (through the [**AVEncCommonFormatConstraint**](avenccommonformatconstraint-property.md) property) and sets the [**AVEncInputVideoSystem**](avencinputvideosystem-property.md) property to NTSC or PAL, the encoder supports the following GOP sizes:



| Video System | Valid GOP Sizes | Default GOP Size |
|--------------|-----------------|------------------|
| NTSC         | 1-18            | 18 (36 fields)   |
| PAL          | 1-15            | 15 (30 fields)   |



 

### Codec Property Change Lists

Setting the value of one codec property can change the valid range of another property. (For example, constraining the target format restricts the average bit rate.) Whenever the application sets a property, the encoder checks if any other properties now fall outside their valid range. If so, the encoder resets that property to its new default value. To receive notifications when this occurs, do the following:

1.  Call [**ICodecAPI::RegisterForEvent**](/windows/desktop/api/Strmif/nf-strmif-icodecapi-registerforevent) with the value **CODECAPI\_CHANGELISTS**.
2.  Use the [**IMediaEventEx**](/windows/desktop/api/Control/nn-control-imediaeventex) interface to monitor events from the filter graph.
3.  If the range or default value of a property changes, the encoder sends an [**EC\_CODECAPI\_EVENT**](ec-codecapi-event.md) event with a list of changed properties.

### IEncoderAPI Support

For backward compatibility, the filter supports the following properties through the **IEncoderAPI** interface:



| Property                       | Description                                                                              |
|--------------------------------|------------------------------------------------------------------------------------------|
| **ENCAPIPARAM\_BITRATE**       | Equivalent to [**AVEncCommonMeanBitRate**](avenccommonmeanbitrate-property.md).         |
| **ENCAPIPARAM\_PEAK\_BITRATE** | Equivalent to [**AVEncCommonMaxBitRate**](avenccommonmaxbitrate-property.md).           |
| **ENCAPIPARAM\_BITRATE\_MODE** | Equivalent to [**AVEncCommonRateControlMode**](avenccommonratecontrolmode-property.md). |



 

When setting the **ENCAPIPARAM\_BITRATE\_MODE** property, the values are mapped as follows:



| **ENCAPIPARAM\_BITRATE\_MODE** | [**AVEncCommonRateControlMode**](avenccommonratecontrolmode-property.md) |
|--------------------------------|---------------------------------------------------------------------------|
| **ConstantBitRate**            | **eAVEncCommonRateControlMode\_CBR**                                      |
| **VariableBitRateAverage**     | See Note.                                                                 |
| **VariableBitRatePeak**        | **eAVEncCommonRateControlMode\_PeakConstrainedVBR**                       |



 

> [!Note]  
> Currently, the MPEG-2 video encoder does not support the **VariableBitRateAverage** encoding mode. If you set this value, the encoder defaults to CBR encoding (**eAVEncCommonRateControlMode\_CBR**).

 

When getting the **ENCAPIPARAM\_BITRATE\_MODE** property, the values are mapped as follows:



| [**AVEncCommonRateControlMode**](avenccommonratecontrolmode-property.md) | **ENCAPIPARAM\_BITRATE\_MODE** |
|---------------------------------------------------------------------------|--------------------------------|
| **eAVEncCommonRateControlMode\_CBR**                                      | **ConstantBitRate**            |
| **eAVEncCommonRateControlMode\_Quality**                                  | **VariableBitRatePeak**        |
| **eAVEncCommonRateControlMode\_PeakConstrainedVBR**                       | **VariableBitRatePeak**        |



 

### Limitations

Currently the encoder does not support any of the following features:

-   Generation of packetized elementary stream (PES) packets.
-   Frame-rate conversion. The input stream must have a frame rate that is valid for an MPEG-2 bitstream.
-   Frame-rate extensions for MPEG-2 (**frame\_rate\_extension\_n**, **frame\_rate\_extension\_d**).
-   Entry/exit buffer (VBV) positions for a clip.
-   Insertion of line-21 data (Closed Caption information) into the video elementary stream.
-   Setting the 25-bit **time\_code** field in the GOP header for MPEG-2.
-   Denoise filter.
-   Digital rights management (DRM).

The encoder introduces an encoding latency of at least one GOP.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista Home Premium, Windows Vista Ultimate, Windows 7 Home Premium, Windows 7 Professional, Windows 7 Enterprise, Windows 7 Ultimate \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                                                                                                                                     |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl>                                                                                       |



## See also

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> <dt>

[**MPEG-2 Demultiplexer Media Types**](mpeg-2-demultiplexer-media-types.md)
</dt> </dl>

 

 
