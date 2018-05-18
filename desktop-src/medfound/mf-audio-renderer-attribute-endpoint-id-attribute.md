---
Description: 'Specifies the identifier for the audio endpoint device.'
ms.assetid: 'f145fb80-c136-421c-9a65-e69c52109348'
title: 'MF\_AUDIO\_RENDERER\_ATTRIBUTE\_ENDPOINT\_ID attribute'
---

# MF\_AUDIO\_RENDERER\_ATTRIBUTE\_ENDPOINT\_ID attribute

Specifies the identifier for the audio endpoint device.

## Data type

Wide-character string

## Remarks

You can use this attribute to configure the audio renderer. The usage depends on which function you call to create the audio renderer:

-   [**MFCreateAudioRenderer**](mfcreateaudiorenderer.md): Set this attribute using the [**IMFAttributes**](imfattributes.md) interface pointer specified in the *pAudioAttributes* parameter.
-   [**MFCreateAudioRendererActivate**](mfcreateaudiorendereractivate.md): Set this attribute using the [**IMFActivate**](imfactivate.md) interface pointer retrieved in the *ppActivate* parameter. Set the attribute before calling [**IMFActivate::ActivateObject**](imfactivate-activateobject.md).

An audio endpoint device is a hardware device that lies at one end of an audio data path, such as a headphone or a speaker. To obtain the audio endpoint identifier, use the following core audio APIs:

-   Use the [**IMMDeviceEnumerator**](coreaudio.immdeviceenumerator) interface to enumerate the devices on the system.
-   Call [**IMMDevice::GetId**](coreaudio.immdevice_getid) to get the identifier for the device.

For more information, see the [Core Audio](coreaudio.core_audio_apis_in_windows_vista) API documentation. If this attribute is not set, the audio renderer uses the default endpoint device.

If this attribute is set, do not set the [**MF\_AUDIO\_RENDERER\_ATTRIBUTE\_ENDPOINT\_ROLE**](mf-audio-renderer-attribute-endpoint-role-attribute.md) attribute. If both attributes are set, a failure will occur when the audio renderer is created.

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

[**IMFAttributes::GetString**](imfattributes-getstring.md)
</dt> <dt>

[**IMFAttributes::SetString**](imfattributes-setstring.md)
</dt> <dt>

[Streaming Audio Renderer](streaming-audio-renderer.md)
</dt> </dl>

 

 




