---
description: Contains a pointer to the DXGI Device Manager for the Sink Writer.
ms.assetid: 0328FC02-2D32-480B-BB03-9C78BF317AF5
title: MF_SINK_WRITER_D3D_MANAGER attribute (Mfreadwrite.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_SINK\_WRITER\_D3D\_MANAGER attribute

Contains a pointer to the DXGI Device Manager for the [Sink Writer](sink-writer.md).

## Data type

**IMFDXGIDeviceManager\*** stored as **IUnknown\***

## Remarks

The value of this attribute is a pointer to the [**IMFDXGIDeviceManager**](/windows/desktop/api/mfobjects/nn-mfobjects-imfdxgidevicemanager) interface.

Use this attribute to provide a Direct3D device for any video encoders or media sinks loaded by the Sink Writer.

Use this attribute with the following functions:

-   [**MFCreateSinkWriterFromMediaSink**](/windows/desktop/api/mfreadwrite/nf-mfreadwrite-mfcreatesinkwriterfrommediasink)
-   [**MFCreateSinkWriterFromURL**](/windows/desktop/api/mfreadwrite/nf-mfreadwrite-mfcreatesinkwriterfromurl)

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                              |
| Header<br/>                   | <dl> <dt>Mfreadwrite.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Sink Writer](sink-writer.md)
</dt> </dl>

 

 




