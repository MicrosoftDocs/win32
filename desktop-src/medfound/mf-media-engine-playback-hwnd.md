---
Description: 'Sets a handle to a video playback window for the Media Engine.'
ms.assetid: '63889D81-12C5-47C1-B52A-6358E68830C3'
title: 'MF\_MEDIA\_ENGINE\_PLAYBACK\_HWND attribute'
---

# MF\_MEDIA\_ENGINE\_PLAYBACK\_HWND attribute

Sets a handle to a video playback window for the Media Engine.

## Data type

**HWND** stored as **UINT64**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT64**](imfattributes-getuint64.md).

To set this attribute, call [**IMFAttributes::SetUINT64**](imfattributes-setuint64.md).

## Remarks

This attribute is used with the [**IMFMediaEngineClassFactory::CreateInstance**](imfmediaengineclassfactory-createinstance.md) method to initialize the Media Engine.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                                |
| Header<br/>                   | <dl> <dt>Mfmediaengine.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




