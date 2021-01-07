---
description: The MP3 file source parses MP3 files.
ms.assetid: 37362642-1b8a-4fb3-950d-ed1afe3696e5
title: MP3 File Source
ms.topic: reference
ms.date: 05/31/2018
---

# MP3 File Source

The MP3 file source parses MP3 files.

The MP3 file source outputs buffers that contain MPEG-1 audio frames. It does not decode the audio.

## File Extensions and MIME Types

The MP3 file source is the default media source for the following file name extension:

-   .mp3

It is also the default media source for the following MIME types.

-   audio/mpeg
-   audio/x-mp3
-   audio/x-mpeg

## Media Types

The media type offered by the MP3 file source contains the following attributes.



| Attribute                                                                                    | Description                                                                                                                                        |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MF\_MT\_MAJOR\_TYPE**](mf-mt-major-type-attribute.md)                                    | Equal to **MFMediaType\_Audio**.                                                                                                                   |
| [**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md)                                           | Equal to **MFAudioFormat\_MP3** or **MFAudioFormat\_MPEG**.                                                                                        |
| [**MF\_MT\_AUDIO\_AVG\_BYTES\_PER\_SECOND**](mf-mt-audio-avg-bytes-per-second-attribute.md) | Average number of bytes per second.                                                                                                                |
| [**MF\_MT\_AUDIO\_BLOCK\_ALIGNMENT**](mf-mt-audio-block-alignment-attribute.md)             | Equal to 1.                                                                                                                                        |
| [**MF\_MT\_AUDIO\_NUM\_CHANNELS**](mf-mt-audio-num-channels-attribute.md)                   | Number of audio channels.                                                                                                                          |
| [**MF\_MT\_AUDIO\_SAMPLES\_PER\_SECOND**](mf-mt-audio-samples-per-second-attribute.md)      | Number of audio samples per second.                                                                                                                |
| [**MF\_MT\_USER\_DATA**](mf-mt-user-data-attribute.md)                                      | Contains the portion of a [**MPEGLAYER3WAVEFORMAT**](/windows/win32/api/mmreg/ns-mmreg-mpeglayer3waveformat) structure that appears after the **wfx** member of the structure. |



 

## Interfaces

The MP3 file source exposes the following interfaces through [**QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)):

-   [**IMFGetService**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice)
-   [**IMFMediaEventGenerator**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator)
-   [**IMFMediaSource**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasource)

In addition, it exposes the following interfaces through [**IMFGetService**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice):



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Service GUID</th>
<th>Interface</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>MF_METADATA_PROVIDER_SERVICE</strong></td>
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfmetadataprovider"><strong>IMFMetadataProvider</strong></a></td>
</tr>
<tr class="even">
<td><strong>MF_PROPERTY_HANDLER_SERVICE</strong></td>
<td><a href="/windows/desktop/api/propsys/nn-propsys-ipropertystore"><strong>IPropertyStore</strong></a>
<blockquote>
[!Note]<br />
See <a href="shell-metadata-providers.md">Shell Metadata Providers</a>.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td><strong>MF_RATE_CONTROL_SERVICE</strong></td>
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfratecontrol"><strong>IMFRateControl</strong></a></td>
</tr>
<tr class="even">
<td><strong>MF_RATE_CONTROL_SERVICE</strong></td>
<td><a href="/windows/desktop/api/mfidl/nn-mfidl-imfratesupport"><strong>IMFRateSupport</strong></a></td>
</tr>
</tbody>
</table>



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                           |
| DLL<br/>                      | <dl> <dt>Mf.dll</dt> </dl> |



## See also

<dl> <dt>

[Media Sources and Sinks](media-sources-and-sinks.md)
</dt> <dt>

[Media Sources](media-sources.md)
</dt> <dt>

[Source Resolver](source-resolver.md)
</dt> <dt>

[Supported Media Formats in Media Foundation](supported-media-formats-in-media-foundation.md)
</dt> </dl>

 

 
