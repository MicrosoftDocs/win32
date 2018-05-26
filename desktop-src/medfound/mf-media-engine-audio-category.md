---
Description: Specifies the category of the audio stream.
ms.assetid: 0F2DB9A7-64ED-4952-BCB3-F2B15BA37D2A
title: MF\_MEDIA\_ENGINE\_AUDIO\_CATEGORY attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MEDIA\_ENGINE\_AUDIO\_CATEGORY attribute

Specifies the category of the audio stream.

## Data type

**[**AUDIO\_STREAM\_CATEGORY**](coreaudio.audio_stream_category)**

## Remarks

The value of this attribute is a member of the [**AUDIO\_STREAM\_CATEGORY**](coreaudio.audio_stream_category) enumeration.

This attribute is used with the [**IMFMediaEngineClassFactory::CreateInstance**](/windows/win32/mfmediaengine/nf-mfmediaengine-imfmediaengineclassfactory-createinstance?branch=master) method to initialize the Media Engine. The attribute is optional.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Mfmediaengine.idl</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




