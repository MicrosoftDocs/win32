---
description: Contains flags to configure the audio renderer.
ms.assetid: 07433904-1bf6-4e8d-9571-8d663bf4fd13
title: MF_AUDIO_RENDERER_ATTRIBUTE_FLAGS attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_AUDIO\_RENDERER\_ATTRIBUTE\_FLAGS attribute

Contains flags to configure the audio renderer.

## Data type

**UINT32**

## Remarks

The value of this attribute is a bitwise **OR** of the following flags.



| Value                                                   | Description                                                                                                                                                                                                                                                                                                                       |
|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **MF\_AUDIO\_RENDERER\_ATTRIBUTE\_FLAGS\_CROSSPROCESS** | The audio renderer is uses a cross-process audio session. This flag enables audio renderers in multiple processes to share the same audio session, along with the associated volume and policy controls.<br/> If this flag is not set, the audio session cannot be shared by audio renderers in other processes.<br/> |
| **MF\_AUDIO\_RENDERER\_ATTRIBUTE\_FLAGS\_NOPERSIST**    | The Windows audio session API (WASAPI) will not persist the properties for this audio session, such as the session volume.<br/> If this flag is not set, WASAPI will persist the audio session properties.<br/>                                                                                                       |



 

You can use this attribute to configure the audio renderer. The usage depends on which function you call to create the audio renderer:

-   [**MFCreateAudioRenderer**](/windows/desktop/api/mfidl/nf-mfidl-mfcreateaudiorenderer): Set this attribute using the [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) interface pointer specified in the *pAudioAttributes* parameter.
-   [**MFCreateAudioRendererActivate**](/windows/desktop/api/mfidl/nf-mfidl-mfcreateaudiorendereractivate): Set this attribute using the [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) interface pointer retrieved in the *ppActivate* parameter. Set the attribute before calling [**IMFActivate::ActivateObject**](/windows/desktop/api/mfobjects/nf-mfobjects-imfactivate-activateobject).

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Audio Renderer Attributes](audio-renderer-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[Streaming Audio Renderer](streaming-audio-renderer.md)
</dt> </dl>

 

 




