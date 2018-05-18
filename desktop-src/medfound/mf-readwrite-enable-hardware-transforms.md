---
Description: 'Enables the source reader or sink writer to use hardware-based Media Foundation transforms (MFTs).'
ms.assetid: '03f2fa76-b828-40b1-929d-60e7d5ab49bb'
title: 'MF\_READWRITE\_ENABLE\_HARDWARE\_TRANSFORMS attribute'
---

# MF\_READWRITE\_ENABLE\_HARDWARE\_TRANSFORMS attribute

Enables the source reader or sink writer to use hardware-based Media Foundation transforms (MFTs).

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](imfattributes-getuint32.md).

To set this attribute, call [**IMFAttributes::SetUINT32**](imfattributes-setuint32.md).

## Remarks

By default, the source reader and sink writer do not use hardware decoders or encoders. To enable the use of hardware MFTs, set this attribute to **TRUE** when you create the source reader or sink writer.

Use this attribute with the following functions:

-   [**MFCreateSourceReaderFromByteStream**](mfcreatesourcereaderfrombytestream.md)
-   [**MFCreateSourceReaderFromMediaSource**](mfcreatesourcereaderfrommediasource.md)
-   [**MFCreateSourceReaderFromURL**](mfcreatesourcereaderfromurl.md)
-   [**MFCreateSinkWriterFromMediaSink**](mfcreatesinkwriterfrommediasink.md)
-   [**MFCreateSinkWriterFromURL**](mfcreatesinkwriterfromurl.md)

There is one exception to the default behavior. The source reader and sink writer automatically use MFTs that are registered locally in the caller's process. To register an MFT locally, call [**MFTRegisterLocal**](mftregisterlocal.md) or [**MFTRegisterLocalByCLSID**](mftregisterlocalbyclsid.md). Hardware MFTs that are registered locally are used even if the **MF\_READWRITE\_ENABLE\_HARDWARE\_TRANSFORMS** attribute is not set.

This attribute does not affect hardware-accelerated video decoding that uses DirectX Video Acceleration (DXVA). To enable DXVA decoding in the source reader, set the [MF\_SOURCE\_READER\_D3D\_MANAGER](mf-source-reader-d3d-manager.md) attribute.

If this attribute is **TRUE**, do not set the [MF\_READWRITE\_DISABLE\_CONVERTERS](mf-readwrite-disable-converters.md) attribute.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Mfreadwrite.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Sink Writer Attributes](sink-writer-attributes.md)
</dt> <dt>

[Source Reader Attributes](source-reader-attributes.md)
</dt> </dl>

 

 




