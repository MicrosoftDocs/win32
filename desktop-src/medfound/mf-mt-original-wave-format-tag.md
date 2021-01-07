---
description: Contains the original WAVE format tag for an audio stream.
ms.assetid: 2b30a1c2-4a42-4b09-acb6-b76267cc7ed0
title: MF_MT_ORIGINAL_WAVE_FORMAT_TAG attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_ORIGINAL\_WAVE\_FORMAT\_TAG attribute

Contains the original WAVE format tag for an audio stream.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Applies to

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)

## Remarks

Depending on the source file, the AVI media source might set this attribute on the media types that it offers.

An AVI file contains a stream header for each stream in the file. The AVI media source translates the stream header into a media type. For audio streams, the stream header contains a format tag that identifies the audio format. (The format tag is contained in the **wFormatTag** member of the [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure.) In most cases, the AVI media source converts the format tag directly to a subtype GUID, as described in the topic [**Audio Subtype GUIDs**](audio-subtype-guids.md). In some cases, however, it maps the original format tag to another format tag that is equivalent. If so, the media source stores the original format tag in the media type, using the MF\_MT\_ORIGINAL\_WAVE\_FORMAT\_TAG attribute.

The format mappings are stored in the Registry under the following key:

**HKEY\_CLASSES\_ROOT**\\**MediaFoundation**\\**MapAudioFormatTag**

Each entry is a **DWORD** value. The name of the entry is the decimal representation of the format tag. The value of the entry is the equivalent format tag.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 
