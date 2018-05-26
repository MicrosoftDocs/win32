---
Description: Contains a pointer to the DXGI Device Manager for the Sink Writer.
ms.assetid: 0328FC02-2D32-480B-BB03-9C78BF317AF5
title: MF\_SINK\_WRITER\_D3D\_MANAGER attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_SINK\_WRITER\_D3D\_MANAGER attribute

Contains a pointer to the DXGI Device Manager for the [Sink Writer](sink-writer.md).

## Data type

**IMFDXGIDeviceManager\*** stored as **IUnknown\***

## Remarks

The value of this attribute is a pointer to the [**IMFDXGIDeviceManager**](/windows/win32/mfobjects/nn-mfobjects-imfdxgidevicemanager?branch=master) interface.

Use this attribute to provide a Direct3D device for any video encoders or media sinks loaded by the Sink Writer.

Use this attribute with the following functions:

-   [**MFCreateSinkWriterFromMediaSink**](/windows/win32/mfreadwrite/nf-mfreadwrite-mfcreatesinkwriterfrommediasink?branch=master)
-   [**MFCreateSinkWriterFromURL**](/windows/win32/mfreadwrite/nf-mfreadwrite-mfcreatesinkwriterfromurl?branch=master)

## Requirements



|                                     |                                                                                          |
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

 

 




