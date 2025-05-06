---
description: Specifies that the Source Reader or Sink Writer should load only hardware-based Media Foundation transforms (MFTs) that match the passed-in D3D device manager.
title: MF_READWRITE_USE_ONLY_HARDWARE_TRANSFORMS attribute (Mfreadwrite.h)
ms.topic: reference
ms.date: 05/06/2025
---


# MF\_READWRITE\_USE\_ONLY\_HARDWARE\_TRANSFORMS attribute

Specifies that the Source Reader or Sink Writer should load only hardware-based Media Foundation transforms (MFTs) that match the passed-in D3D device manager.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Remarks

By default, the Source Reader and Sink Writer will use any transform that matches the media type, including software decoders and encoders.  Set this attribute to TRUE to ensure that the Source Reader or Sink Writer use only hardware MFTs that match the passed in D3D device manager through the [MF\_SOURCE\_READER\_D3D\_MANAGER](mf-source-reader-d3d-manager.md) or [MF\_SINK\_WRITER\_D3D\_MANAGER](mf-sink-writer-d3d-manager.md) attributes. If a matching hardware MFT is not found, then the Source Reader or Sink Writer API attempting to create the transform chain will fail with an appropriate error code.  

If the D3D device manager is not passed in or if the [MF\_READWRITE\_ENABLE\_HARDWARE\_TRANSFORMS](mf-readwrite-enable-hardware-transforms.md) attribute is not set, this attribute has no effect.

Use this attribute with the following functions:

-   [**MFCreateSourceReaderFromByteStream**](/windows/desktop/api/mfreadwrite/nf-mfreadwrite-mfcreatesourcereaderfrombytestream)
-   [**MFCreateSourceReaderFromMediaSource**](/windows/desktop/api/mfreadwrite/nf-mfreadwrite-mfcreatesourcereaderfrommediasource)
-   [**MFCreateSourceReaderFromURL**](/windows/desktop/api/mfreadwrite/nf-mfreadwrite-mfcreatesourcereaderfromurl)
-   [**MFCreateSinkWriterFromMediaSink**](/windows/desktop/api/mfreadwrite/nf-mfreadwrite-mfcreatesinkwriterfrommediasink)
-   [**MFCreateSinkWriterFromURL**](/windows/desktop/api/mfreadwrite/nf-mfreadwrite-mfcreatesinkwriterfromurl)

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 11 Version 25H2 |
| Minimum supported server | Windows Server Version 25H2 |
| Header                   | Mfreadwrite.h |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Sink Writer Attributes](sink-writer-attributes.md)
</dt> <dt>

[Source Reader Attributes](source-reader-attributes.md)
</dt> </dl>
