---
Description: Specifies whether the Media Engine will play protected content.
ms.assetid: 2A593499-BF40-440E-AF1D-3B0E7732489A
title: MF\_MEDIA\_ENGINE\_CONTENT\_PROTECTION\_FLAGS attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MEDIA\_ENGINE\_CONTENT\_PROTECTION\_FLAGS attribute

Specifies whether the Media Engine will play protected content.

## Data type

**UINT32**

## Remarks

The value of this attribute is a bitwise **OR** of flags from the [**MF\_MEDIA\_ENGINE\_PROTECTION\_FLAGS**](/windows/win32/mfmediaengine/ne-mfmediaengine-mf_media_engine_protection_flags?branch=master) enumeration. To enable playback of protected content, set the **MF\_MEDIA\_ENGINE\_ENABLE\_PROTECTED\_CONTENT** flag.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                                |
| Header<br/>                   | <dl> <dt>Mfmediaengine.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Media Engine Attributes](media-engine-attributes.md)
</dt> <dt>

[**IMFMediaEngineClassFactory::CreateInstance**](/windows/win32/mfmediaengine/nf-mfmediaengine-imfmediaengineclassfactory-createinstance?branch=master)
</dt> </dl>

 

 




