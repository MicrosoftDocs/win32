---
Description: Enables the source reader or sink writer to use hardware-based Media Foundation transforms (MFTs).
ms.assetid: 03f2fa76-b828-40b1-929d-60e7d5ab49bb
title: MF\_READWRITE\_ENABLE\_HARDWARE\_TRANSFORMS attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_READWRITE\_ENABLE\_HARDWARE\_TRANSFORMS attribute

Enables the source reader or sink writer to use hardware-based Media Foundation transforms (MFTs).

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master).

## Remarks

By default, the source reader and sink writer do not use hardware decoders or encoders. To enable the use of hardware MFTs, set this attribute to **TRUE** when you create the source reader or sink writer.

Use this attribute with the following functions:

-   [**MFCreateSourceReaderFromByteStream**](/windows/win32/mfreadwrite/nf-mfreadwrite-mfcreatesourcereaderfrombytestream?branch=master)
-   [**MFCreateSourceReaderFromMediaSource**](/windows/win32/mfreadwrite/nf-mfreadwrite-mfcreatesourcereaderfrommediasource?branch=master)
-   [**MFCreateSourceReaderFromURL**](/windows/win32/mfreadwrite/nf-mfreadwrite-mfcreatesourcereaderfromurl?branch=master)
-   [**MFCreateSinkWriterFromMediaSink**](/windows/win32/mfreadwrite/nf-mfreadwrite-mfcreatesinkwriterfrommediasink?branch=master)
-   [**MFCreateSinkWriterFromURL**](/windows/win32/mfreadwrite/nf-mfreadwrite-mfcreatesinkwriterfromurl?branch=master)

There is one exception to the default behavior. The source reader and sink writer automatically use MFTs that are registered locally in the caller's process. To register an MFT locally, call [**MFTRegisterLocal**](/windows/win32/mfapi/nf-mfapi-mftregisterlocal?branch=master) or [**MFTRegisterLocalByCLSID**](/windows/win32/mfapi/nf-mfapi-mftregisterlocalbyclsid?branch=master). Hardware MFTs that are registered locally are used even if the **MF\_READWRITE\_ENABLE\_HARDWARE\_TRANSFORMS** attribute is not set.

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

 

 




