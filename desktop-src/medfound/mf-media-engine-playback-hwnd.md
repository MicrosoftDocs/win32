---
description: Sets a handle to a video playback window for the Media Engine.
ms.assetid: 63889D81-12C5-47C1-B52A-6358E68830C3
title: MF_MEDIA_ENGINE_PLAYBACK_HWND attribute (Mfmediaengine.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MEDIA\_ENGINE\_PLAYBACK\_HWND attribute

Sets a handle to a video playback window for the Media Engine.

## Data type

**HWND** stored as **UINT64**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT64**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint64).

To set this attribute, call [**IMFAttributes::SetUINT64**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint64).

## Remarks

This attribute is used with the [**IMFMediaEngineClassFactory::CreateInstance**](/windows/desktop/api/mfmediaengine/nf-mfmediaengine-imfmediaengineclassfactory-createinstance) method to initialize the Media Engine.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                                |
| Header<br/>                   | <dl> <dt>Mfmediaengine.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




