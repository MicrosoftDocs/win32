---
Description: Specifies the device role for the audio stream.
ms.assetid: E4B7660D-5F41-495A-B77D-94B7981F4C2C
title: MF\_MEDIA\_ENGINE\_AUDIO\_ENDPOINT\_ROLE attribute
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MF\_MEDIA\_ENGINE\_AUDIO\_ENDPOINT\_ROLE attribute

Specifies the device role for the audio stream.

## Data type

**[**ERole**](https://msdn.microsoft.com/en-us/library/Dd370842(v=VS.85).aspx)** stored as **UINT32**

## Remarks

The value of this attribute is a member of the [**ERole**](https://msdn.microsoft.com/en-us/library/Dd370842(v=VS.85).aspx) enumeration.

This attribute is used with the [**IMFMediaEngineClassFactory::CreateInstance**](/windows/desktop/api/mfmediaengine/nf-mfmediaengine-imfmediaengineclassfactory-createinstance) method to initialize the Media Engine. The attribute is optional.

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

 

 




