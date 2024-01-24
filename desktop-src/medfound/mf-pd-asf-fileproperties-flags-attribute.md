---
description: Specifies whether an Advanced Systems Format (ASF) file is broadcast or seekable. This value corresponds to the Flags field of the File Properties Object, defined in the ASF specification.
ms.assetid: 427f0dca-f945-4c89-a87a-a7c86291b1c5
title: MF_PD_ASF_FILEPROPERTIES_FLAGS attribute (Wmcontainer.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_PD\_ASF\_FILEPROPERTIES\_FLAGS attribute

Specifies whether an Advanced Systems Format (ASF) file is broadcast or seekable. This value corresponds to the Flags field of the File Properties Object, defined in the ASF specification.

## Data type

**UINT32**

## Remarks

This attribute applies to presentation descriptors for ASF content. The value of the attribute is a bitwise OR of the following flags:



| Flag | Description                                                                                                                                                                                                                                                                                       |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x01 | Broadcast flag. The file is in the process of being created.                                                                                                                                                                                                                                      |
| 0x02 | Seekable flag. The file is seekable.<br/> A file is seekable if an audio stream is present and the maximum data packet size equals the minimum data packet size. It can also be seekable if the file has an audio stream and a video stream with a matching Simple Index Object.<br/> |



 

The [**IMFASFContentInfo::GeneratePresentationDescriptor**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-generatepresentationdescriptor) method generates this attribute from the ASF metadata.

If the broadcast flag is set, the following attributes in the presentation descriptor are not valid:

-   [**MF\_PD\_ASF\_FILEPROPERTIES\_FILE\_ID**](mf-pd-asf-fileproperties-file-id-attribute.md)
-   [**MF\_PD\_ASF\_FILEPROPERTIES\_CREATION\_TIME**](mf-pd-asf-fileproperties-creation-time-attribute.md)
-   [**MF\_PD\_ASF\_FILEPROPERTIES\_PACKETS**](mf-pd-asf-fileproperties-packets-attribute.md)
-   [**MF\_PD\_ASF\_FILEPROPERTIES\_PLAY\_DURATION**](mf-pd-asf-fileproperties-play-duration-attribute.md)
-   [**MF\_PD\_ASF\_FILEPROPERTIES\_SEND\_DURATION**](mf-pd-asf-fileproperties-send-duration-attribute.md)

In addition, the [**MF\_PD\_ASF\_FILEPROPERTIES\_MAX\_PACKET\_SIZE**](mf-pd-asf-fileproperties-max-packet-size-attribute.md) attribute and [**MF\_PD\_ASF\_FILEPROPERTIES\_MIN\_PACKET\_SIZE**](mf-pd-asf-fileproperties-min-packet-size-attribute.md) attribute values are set to the actual packet size.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Wmcontainer.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[**IMFPresentationDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfpresentationdescriptor)
</dt> <dt>

[Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
</dt> <dt>

[ASF Header Object](asf-file-structure.md)
</dt> <dt>

[Presentation Descriptors](presentation-descriptors.md)
</dt> </dl>

 

 




