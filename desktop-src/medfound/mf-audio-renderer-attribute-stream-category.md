---
Description: Specifies the audio stream category for the Streaming Audio Renderer (SAR).
ms.assetid: 88E79DE6-2062-4471-A939-D1D4DD2EC42D
title: MF\_AUDIO\_RENDERER\_ATTRIBUTE\_STREAM\_CATEGORY attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_AUDIO\_RENDERER\_ATTRIBUTE\_STREAM\_CATEGORY attribute

Specifies the audio stream category for the [Streaming Audio Renderer](streaming-audio-renderer.md) (SAR).

## Data type

**UINT32**

## Remarks

You can use this attribute to configure the audio renderer. The usage depends on which function you call to create the audio renderer.



| Function                                                               | How to Set the attribute                                                                                                                                                                       |
|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MFCreateAudioRenderer**](/windows/win32/mfidl/nf-mfidl-mfcreateaudiorenderer?branch=master)                 | Use the [**IMFAttributes**](/windows/win32/mfobjects/nn-mfobjects-imfattributes?branch=master) pointer specified in the *pAudioAttributes* parameter.                                                                                          |
| [**MFCreateAudioRendererActivate**](/windows/win32/mfidl/nf-mfidl-mfcreateaudiorendereractivate?branch=master) | Use the [**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master) pointer returned in the *ppActivate* parameter. Set the attribute before calling [**IMFActivate::ActivateObject**](/windows/win32/mfobjects/nf-mfobjects-imfactivate-activateobject?branch=master). |



 

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

 

 




