---
description: Enables or disables read-ahead in a media source.
ms.assetid: b2b8711f-ba63-4fba-bb88-8d254135eb21
title: MFPKEY_MediaSource_DisableReadAhead property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_MediaSource\_DisableReadAhead property

Enables or disables read-ahead in a media source.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**VARIANT\_BOOL**

VT\_BOOL

**boolVal**



## Remarks

Applications can use this property to configure some media sources. To set the property, pass an **IPropertyStore** pointer to the source resolver. For more information, see [Configuring a Media Source](configuring-a-media-source.md).

If the value is **VARIANT\_TRUE**, the media source will not read ahead in the byte stream. This setting can optimize performance if you plan to read a limited amount of data from the media source—for example, to get a thumbnail image from a video file.

For typical audio/video playback, this property should be set to **VARIANT\_FALSE**. The default value is **VARIANT\_FALSE**.

Not every media source supports this property.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Client<br/> | Windows 7<br/>                                                               |
| Header<br/> | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




