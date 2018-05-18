---
Description: 'Specifies the audio stream category for the Streaming Audio Renderer (SAR).'
ms.assetid: '88E79DE6-2062-4471-A939-D1D4DD2EC42D'
title: 'MF\_AUDIO\_RENDERER\_ATTRIBUTE\_STREAM\_CATEGORY attribute'
---

# MF\_AUDIO\_RENDERER\_ATTRIBUTE\_STREAM\_CATEGORY attribute

Specifies the audio stream category for the [Streaming Audio Renderer](streaming-audio-renderer.md) (SAR).

## Data type

**UINT32**

## Remarks

You can use this attribute to configure the audio renderer. The usage depends on which function you call to create the audio renderer.



| Function                                                               | How to Set the attribute                                                                                                                                                                       |
|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MFCreateAudioRenderer**](mfcreateaudiorenderer.md)                 | Use the [**IMFAttributes**](imfattributes.md) pointer specified in the *pAudioAttributes* parameter.                                                                                          |
| [**MFCreateAudioRendererActivate**](mfcreateaudiorendereractivate.md) | Use the [**IMFActivate**](imfactivate.md) pointer returned in the *ppActivate* parameter. Set the attribute before calling [**IMFActivate::ActivateObject**](imfactivate-activateobject.md). |



 

The value of the attribute is a member of the [**AUDIO\_STREAM\_CATEGORY**](coreaudio.audio_stream_category) enumeration. The audio service uses the stream category to determine audio policies when multiple applications play audio at the same time.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




