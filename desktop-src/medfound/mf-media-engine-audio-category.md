---
description: Specifies the category of the audio stream.
ms.assetid: 0F2DB9A7-64ED-4952-BCB3-F2B15BA37D2A
title: MF_MEDIA_ENGINE_AUDIO_CATEGORY attribute
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MEDIA\_ENGINE\_AUDIO\_CATEGORY attribute

Specifies the category of the audio stream.

## Data type

**[**AUDIO\_STREAM\_CATEGORY**](/windows/win32/api/audiosessiontypes/ne-audiosessiontypes-audio_stream_category)**

## Remarks

The value of this attribute is a member of the [**AUDIO\_STREAM\_CATEGORY**](/windows/win32/api/audiosessiontypes/ne-audiosessiontypes-audio_stream_category) enumeration.

This attribute is used with the [**IMFMediaEngineClassFactory::CreateInstance**](/windows/desktop/api/mfmediaengine/nf-mfmediaengine-imfmediaengineclassfactory-createinstance) method to initialize the Media Engine. The attribute is optional.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Mfmediaengine.idl</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 
