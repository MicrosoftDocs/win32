---
description: Video Interlacing
ms.assetid: 2911ae57-1703-4a9d-bd33-94af1e0f8804
title: Video Interlacing
ms.topic: article
ms.date: 05/31/2018
---

# Video Interlacing

This topic describes how media sources and decoders should handle interlaced video content.

To decode and render interlaced video correctly, the following information is needed:

-   Progressive or interlaced. A video stream can contain progressive frames, interlaced frames, or a mix of both.

-   Field dominance. Field dominance describes which field appears first, the upper field or the lower field.

-   Repeat first field. This flag is used in 3:2 pulldown, when the frame is progressive but the stream is interlaced. In this context, the first field can be the upper or lower field.

-   Interleaved fields or single field. A sample can hold either a single field, or two interleaved fields. If a sample contains a single field, the sample height is half the frame height, because the sample contains only half of the scan lines for a frame. Interleaved fields are recommended unless the characteristics of the source content dictate otherwise.

Any of these characteristics can change from one sample to the next. However, video components need to know something about the overall content before streaming begins. For example, if the video is interlaced, the enhanced video renderer (EVR) needs to reserve video memory for the deinterlacing. If the video is entirely progressive frames, on the other hand, the EVR can optimize the rendering pipeline. Adding a deinterlacing step to the pipeline increases the rendering latency.

Information about interlacing is stored in two places:

-   General information about the interlacing in a stream is placed in the media type. For more information about media types, see [Media Types](media-types.md).

-   Information that can change with each sample is placed on the sample as an attribute. For more information about samples, see [Media Samples](media-samples.md).

## Interlace Information in the Media Type

The [**MF\_MT\_INTERLACE\_MODE**](mf-mt-interlace-mode-attribute.md) attribute on the media type describes how the stream as a whole is interlaced. The value of this attribute is a member of the [**MFVideoInterlaceMode**](/windows/desktop/api/mfobjects/ne-mfobjects-mfvideointerlacemode) enumeration. A video media type should always have this attribute.

-   If the stream contains only progressive frames, with no interlaced frames, use MFVideoInterlace\_Progressive.
-   If the stream contains only interlaced frames, and every sample contains two interleaved fields, use MFVideoInterlace\_FieldInterleavedUpperFirst or MFVideoInterlace\_FieldInterleavedLowerFirst.
-   If the stream contains only interlaced frames, and every sample contains a single field, use MFVideoInterlace\_FieldSingleUpper or MFVideoInterlace\_FieldSingleLower. If the fields alternate between upper and lower, then it does not matter which of these two values is used. If the format contains just upper fields, or just lower fields, then set the value that corresponds to the content.
-   If the stream contains a mix of interlaced and progressive frames, or if the field dominance switches, set the media type to MFVideoInterlace\_MixedInterlaceOrProgressive. Use sample attributes to describe each frame.

The following table summarizes this attribute.



| MF\_MT\_INTERLACE\_MODE                       | Interlaced? | Samples                                  | First field    |
|-----------------------------------------------|-------------|------------------------------------------|----------------|
| MFVideoInterlace\_Progressive                 | No          | Progressive frame                        | Not applicable |
| MFVideoInterlace\_FieldInterleavedUpperFirst  | Yes         | Interleaved fields                       | Upper first    |
| MFVideoInterlace\_FieldInterleavedLowerFirst  | Yes         | Interleaved fields                       | Lower first    |
| MFVideoInterlace\_FieldSingleUpper            | Yes         | Single field                             | Upper first    |
| MFVideoInterlace\_FieldSingleLower            | Yes         | Single field                             | Lower first    |
| MFVideoInterlace\_MixedInterlaceOrProgressive | Can vary    | Interleaved fields or progressive frames | Can vary       |



 

Interleaved fields and single fields cannot be mixed. Switching from one to another requires a media type change.

## Interlace Flags on Samples

Information that can change from one sample to the next is indicated using sample attributes. Use the [**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample) interface to get or set these attributes.

All of the interlacing attributes listed in this section have Boolean values. Effectively, each of these attributes can have three values: either **TRUE**, **FALSE**, or not set. If an attribute is not set, the value is taken from the media type. If an attribute is set, the value overrides the media type. Some combinations of flags and media types are not valid.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="mfsampleextension-interlaced-attribute.md">MFSampleExtension_Interlaced</a></td>
<td>If <strong>TRUE</strong>, the frame is interlaced. If <strong>FALSE</strong>, the frame is progressive.<br/> Set this attribute on every sample if the media type is MFVideoInterlace_MixedInterlaceOrProgressive.<br/></td>
</tr>
<tr class="even">
<td><a href="mfsampleextension-bottomfieldfirst-attribute.md">MFSampleExtension_BottomFieldFirst</a></td>
<td>The meaning of this flag depends on whether the samples contain interleaved fields or single fields.<br/>
<ul>
<li>Interleaved fields: If <strong>TRUE</strong>, the lower field is first. If <strong>FALSE</strong>, the upper field is first.<br/></li>
<li>Single fields: If <strong>TRUE</strong>, the sample contains a lower field. If <strong>FALSE</strong>, the sample contains an upper field.<br/></li>
</ul>
Set this attribute on every interlace sample if the media type is MFVideoInterlace_FieldSingleUpper, MFVideoInterlace_FieldSingleLower, or MFVideoInterlace_MixedInterlaceOrProgressive.<br/></td>
</tr>
<tr class="odd">
<td><a href="mfsampleextension-repeatfirstfield-attribute.md">MFSampleExtension_RepeatFirstField</a></td>
<td>If <strong>TRUE</strong>, the first field is repeated. If <strong>FALSE</strong> or not set, the first field is not repeated.</td>
</tr>
<tr class="even">
<td><a href="mfsampleextension-singlefield-attribute.md">MFSampleExtension_SingleField</a></td>
<td>If <strong>TRUE</strong>, the sample contains a single field. If <strong>FALSE</strong>, the sample contains interleaved fields.</td>
</tr>
</tbody>
</table>



 

The following table shows which flags are required, optional, or prohibited, based on the media type.



| Media Type         | Interlaced Flag                      | BottomFieldFirst Flag                    | RepeatFirstField Flag | SingleField Flag                     |
|--------------------|--------------------------------------|------------------------------------------|-----------------------|--------------------------------------|
| Progressive        | Optional; if set, must be **FALSE**. | Do not set.                              | Do not set.           | Do not set.                          |
| Interleaved fields | Optional; if set, must be **TRUE**.  | Optional; if set, must match media type. | Do not set.           | Optional; if set, must be **FALSE**. |
| Single fields      | Optional; if set, must be **TRUE**.  | Required.                                | Do not set.           | Set to **TRUE**.                     |
| Mixed              | Required.                            | Required.                                | Required.             | Optional; if set, must be **FALSE**. |



 

In the cases where the attribute is optional, the media type already defines the information. It is valid to set the attribute to match, but not required.

For example, if the media type is MFVideoInterlace\_Progressive, it implies that all frames in the stream are progressive. Therefore, you can either set the **MFSampleExtension\_Interlaced** attribute to **FALSE**, or leave the attribute unset.

## Recommendations

This section contains recommendations for various types of content.

1. The video is all progressive frames.

-   Set the media type to MFVideoInterlace\_Progressive.

-   Do not set the **MFSampleExtension\_Interlaced** attribute, or set it to **FALSE** on every frame.

-   Do not set the **MFSampleExtension\_BottomFieldFirst**, **MFSampleExtension\_RepeatFirstField**, or **MFSampleExtension\_SingleField** attributes.

2. The video is all interlaced fields with the same field dominance. Samples contain interleaved fields.

-   Set the media type to MFVideoInterlace\_FieldInterleavedUpperFirst or MFVideoInterlace\_FieldInterleavedLowerFirst.

-   Do not set the **MFSampleExtension\_Interlaced** attribute, or set it to **TRUE** on every frame.

-   Do not set the **MFSampleExtension\_BottomFieldFirst** attribute, or set the value on every frame to match the media type.

-   Do not set the **MFSampleExtension\_RepeatFirstField** attribute, or set it to **FALSE** on every frame.

-   Do not set the **MFSampleExtension\_SingleField** attribute, or set it to **FALSE** on every frame.

3. The video contains a mix of interlaced and progressive frames, with repeated fields and varying field dominance (for example, DVD video).

-   Set the media type to MFVideoInterlace\_MixedInterlaceOrProgressive.

-   On every frame, set the **MFSampleExtension\_Interlaced**, **MFSampleExtension\_BottomFieldFirst**, and **MFSampleExtension\_RepeatFirstField** attributes.

-   Do not set the **MFSampleExtension\_SingleField** attribute, or set it to **FALSE** on every frame.

4. The video is interlaced and samples contain single fields.

-   Set the media type to MFVideoInterlace\_FieldSingleUpper or MFVideoInterlace\_FieldSingleLower.

-   On every frame, set the **MFSampleExtension\_BottomFieldFirst** attribute.

-   Do not set the **MFSampleExtension\_Interlaced** attribute, or set it to **TRUE** on every frame.

-   Do not set the **MFSampleExtension\_RepeatFirstField** attribute, or set it to **FALSE** on every frame.

-   Do not set the **MFSampleExtension\_SingleField** attribute, or set it to **TRUE** on every frame.

Most video content falls into one of these categories.

## MPEG-2 Mappings

For MPEG-2 content, use the following mappings to convert the MPEG-2 flags to Media Foundation sample attributes.

**picture\_structure**



| Value         | Sample Attribute                                                                                                        |
|---------------|-------------------------------------------------------------------------------------------------------------------------|
| frame         | **MFSampleExtension\_SingleField** = **FALSE**                                                                          |
| top\_field    | **MFSampleExtension\_SingleField** = **TRUE**<br/> **MFSampleExtension\_BottomFieldFirst** = **FALSE**<br/> |
| bottom\_field | **MFSampleExtension\_SingleField** = **TRUE**<br/> **MFSampleExtension\_BottomFieldFirst** = **TRUE**<br/>  |



 

**progressive\_frame**



| Value | Sample Attribute                              |
|-------|-----------------------------------------------|
| 0     | **MFSampleExtension\_Interlaced** = **TRUE**  |
| 1     | **MFSampleExtension\_Interlaced** = **FALSE** |



 

**top\_field\_first**



| Value | Sample Attribute                                    |
|-------|-----------------------------------------------------|
| 0     | **MFSampleExtension\_BottomFieldFirst** = **TRUE**  |
| 1     | **MFSampleExtension\_BottomFieldFirst** = **FALSE** |



 

**repeat\_first\_field**



| Value | Sample Attribute                                    |
|-------|-----------------------------------------------------|
| 0     | **MFSampleExtension\_RepeatFirstField** = **FALSE** |
| 1     | **MFSampleExtension\_RepeatFirstField** = **TRUE**  |



 

## Single-Field Samples

If the media type is MFVideoInterlace\_FieldSingleUpper or MFVideoInterlace\_FieldSingleLower, it means that each sample contains a single field. However, the media type describes the entire frame. Therefore, each buffer contains only half the number of field lines given in the media type. For example, if the media type describes the video as 720 × 480, each field contains 240 scan lines, and therefore each buffer contains only 240 rows of pixels. If you write a component that accepts media types with single-field samples, you must take this fact into account when you access the data in the buffer.

The same rule applies to the geometric aperture ([MF\_MT\_GEOMETRIC\_APERTURE](mf-mt-geometric-aperture-attribute.md) attribute) and minimum display aperture ([MF\_MT\_MINIMUM\_DISPLAY\_APERTURE](mf-mt-minimum-display-aperture-attribute.md) attribute). These regions are specified in terms of the entire frame, not the individual fields.

## DirectShow Mappings

In DirectShow, per-sample interlacing information is contained in the **dwTypeSpecificFlags** member of the **AM\_SAMPLE2\_PROPERTIES** structure. The following table shows the equivalent attributes for Media Foundation.



| DirectShow sample flag              | Media Foundation sample attribute                                                                                                                                                  |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AM\_VIDEO\_FLAG\_INTERLEAVED\_FRAME | **MFSampleExtension\_SingleField** = **FALSE**.                                                                                                                                    |
| AM\_VIDEO\_FLAG\_FIELD1             | **MFSampleExtension\_Interlaced** = **TRUE**.<br/> **MFSampleExtension\_SingleField** = **TRUE**.<br/> **MFSampleExtension\_BottomFieldFirst** = **FALSE**.<br/> |
| AM\_VIDEO\_FLAG\_FIELD2             | **MFSampleExtension\_Interlaced** = **TRUE**.<br/> **MFSampleExtension\_SingleField** = **TRUE**.<br/> **MFSampleExtension\_BottomFieldFirst** = **TRUE**.<br/>  |
| AM\_VIDEO\_FLAG\_WEAVE              | **MFSampleExtension\_Interlaced** = **FALSE**. (This flag indicates that the driver should not deinterlace the two fields.)                                                        |
| AM\_VIDEO\_FLAG\_FIELD1FIRST        | **MFSampleExtension\_BottomFieldFirst** = **FALSE**. If the content is interlaced and the AM\_VIDEO\_FLAG\_FIELD1FIRST flag is not present, set this attribute to **TRUE**.        |
| AM\_VIDEO\_FLAG\_REPEAT\_FIELD      | **MFSampleExtension\_RepeatFirstField** = **TRUE**. If the AM\_VIDEO\_FLAG\_REPEAT\_FIELD flag is not present, set this attribute to **FALSE**.                                    |



 

If the DirectShow sample does not contain sample flags, use the value of **dwInterlaceFlags** from the **VIDEOINFOHEADER2** structure:



| DirectShow interlace flag    | Media Foundation sample attribute                    |
|------------------------------|------------------------------------------------------|
| AMINTERLACE\_IsInterlaced    | **MFSampleExtension\_Interlaced** = **TRUE**.        |
| AMINTERLACE\_1FieldPerSample | **MFSampleExtension\_SingleField** = **TRUE**.       |
| AMINTERLACE\_Field1First     | **MFSampleExtension\_BottomFieldFirst** = **FALSE**. |



 

## Related topics

<dl> <dt>

[Video Media Types](video-media-types.md)
</dt> <dt>

[Media Types](media-types.md)
</dt> </dl>

 

 




