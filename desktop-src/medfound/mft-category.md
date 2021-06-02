---
description: The following GUIDs define categories for Media Foundation transforms (MFTs). These categories are used to register and enumerate MFTs.
ms.assetid: eca3ae3b-e40a-407d-986c-d0a85b891f52
title: MFT_CATEGORY (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFT\_CATEGORY

The following GUIDs define categories for Media Foundation transforms (MFTs). These categories are used to register and enumerate MFTs.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Constant</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><span id="MFT_CATEGORY_AUDIO_DECODER"></span><span id="mft_category_audio_decoder"></span><dl> <dt><strong>MFT_CATEGORY_AUDIO_DECODER</strong></dt> </dl></td>
<td style="text-align: left;">Audio decoders.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="MFT_CATEGORY_AUDIO_EFFECT"></span><span id="mft_category_audio_effect"></span><dl> <dt><strong>MFT_CATEGORY_AUDIO_EFFECT</strong></dt> </dl></td>
<td style="text-align: left;">Audio effects.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="MFT_CATEGORY_AUDIO_ENCODER"></span><span id="mft_category_audio_encoder"></span><dl> <dt><strong>MFT_CATEGORY_AUDIO_ENCODER</strong></dt> </dl></td>
<td style="text-align: left;">Audio encoders.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="MFT_CATEGORY_DEMULTIPLEXER"></span><span id="mft_category_demultiplexer"></span><dl> <dt><strong>MFT_CATEGORY_DEMULTIPLEXER</strong></dt> </dl></td>
<td style="text-align: left;">Demultiplexers.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="MFT_CATEGORY_MULTIPLEXER"></span><span id="mft_category_multiplexer"></span><dl> <dt><strong>MFT_CATEGORY_MULTIPLEXER</strong></dt> </dl></td>
<td style="text-align: left;">Multiplexers.<br/>
<blockquote>
[!Note]<br />
In Windows Vista, the Media Foundation pipeline does not support MFTs with more than one input. Multiple-input MFTs are supported in Windows 7.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="MFT_CATEGORY_OTHER"></span><span id="mft_category_other"></span><dl> <dt><strong>MFT_CATEGORY_OTHER</strong></dt> </dl></td>
<td style="text-align: left;">Miscellaneous MFTs.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="MFT_CATEGORY_VIDEO_DECODER"></span><span id="mft_category_video_decoder"></span><dl> <dt><strong>MFT_CATEGORY_VIDEO_DECODER</strong></dt> </dl></td>
<td style="text-align: left;">Video decoders.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="MFT_CATEGORY_VIDEO_EFFECT"></span><span id="mft_category_video_effect"></span><dl> <dt><strong>MFT_CATEGORY_VIDEO_EFFECT</strong></dt> </dl></td>
<td style="text-align: left;">Video effects.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="MFT_CATEGORY_VIDEO_RENDERER_EFFECT"></span><span id="mft_category_video_renderer_effect"></span><dl> <dt><strong>MFT_CATEGORY_VIDEO_RENDERER_EFFECT</strong></dt> </dl></td>
<td style="text-align: left;">Video renderer effects.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="MFT_CATEGORY_VIDEO_ENCODER"></span><span id="mft_category_video_encoder"></span><dl> <dt><strong>MFT_CATEGORY_VIDEO_ENCODER</strong></dt> </dl></td>
<td style="text-align: left;">Video encoders.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="MFT_CATEGORY_VIDEO_PROCESSOR"></span><span id="mft_category_video_processor"></span><dl> <dt><strong>MFT_CATEGORY_VIDEO_PROCESSOR</strong></dt> </dl></td>
<td style="text-align: left;"><blockquote>
[!Note]<br />
Introduced in Windows 7.
</blockquote>
<br/> Video processors. <br/> This category is limited to MFTs that perform format conversions on uncompressed video, including color-space conversions. For video effects that modify the appearance of the image (such as a blur effect or a color-to-grayscale transform), use the <strong>MFT_CATEGORY_VIDEO_EFFECT</strong> category.<br/></td>
</tr>
</tbody>
</table>



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Constants](media-foundation-constants.md)
</dt> <dt>

[Media Foundation Transforms](media-foundation-transforms.md)
</dt> <dt>

[**MFTEnum**](/windows/desktop/api/mfapi/nf-mfapi-mftenum)
</dt> <dt>

[**MFTEnumEx**](/windows/desktop/api/mfapi/nf-mfapi-mftenumex)
</dt> <dt>

[**MFTRegister**](/windows/desktop/api/mfapi/nf-mfapi-mftregister)
</dt> </dl>

 

 




