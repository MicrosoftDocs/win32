---
Description: Specifies the audio policy class for the audio renderer.
ms.assetid: 80b028f5-7756-4bb8-b5e3-ebc8343e168c
title: MF\_AUDIO\_RENDERER\_ATTRIBUTE\_SESSION\_ID attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_AUDIO\_RENDERER\_ATTRIBUTE\_SESSION\_ID attribute

Specifies the audio policy class for the audio renderer.

## Data type

**GUID**

## Remarks

This attribute associates the audio renderer with an audio policy class. Each policy class has its own volume and policy control. If this attribute is not set, the new SAR joins the application's default audio session. For more information, see [**IAudioClient::Initialize**](coreaudio.iaudioclient_initialize) in the core audio API documentation.

You can use this attribute to configure the audio renderer. The usage depends on which function you call to create the audio renderer:

-   [**MFCreateAudioRenderer**](/windows/win32/mfidl/nf-mfidl-mfcreateaudiorenderer?branch=master): Set this attribute using the [**IMFAttributes**](/windows/win32/mfobjects/nn-mfobjects-imfattributes?branch=master) interface pointer specified in the *pAudioAttributes* parameter.
-   [**MFCreateAudioRendererActivate**](/windows/win32/mfidl/nf-mfidl-mfcreateaudiorendereractivate?branch=master): Set this attribute using the [**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master) interface pointer retrieved in the *ppActivate* parameter. Set the attribute before calling [**IMFActivate::ActivateObject**](/windows/win32/mfobjects/nf-mfobjects-imfactivate-activateobject?branch=master).

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
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

[**IMFAttributes::GetGUID**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getguid?branch=master)
</dt> <dt>

[**IMFAttributes::SetGUID**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setguid?branch=master)
</dt> <dt>

[Streaming Audio Renderer](streaming-audio-renderer.md)
</dt> </dl>

 

 




