---
Description: Indicates whether a media source supports hardware data flow.
ms.assetid: 32FEBC99-0AE0-4FE9-90AB-5FB204BD4C83
title: MF\_SOURCE\_STREAM\_SUPPORTS\_HW\_CONNECTION attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_SOURCE\_STREAM\_SUPPORTS\_HW\_CONNECTION attribute

Indicates whether a media source supports hardware data flow.

## Data type

**BOOL** stored as **UINT32**

## Remarks

This attribute is used when a media source proxies a hardware device and is able to transfer data downstream over a hardware bus, without sending data up to the CPU. For example, a webcam might deliver H.264-encoded video directly to an integrated hardware decoder.

In this scenario, the source and decoder are still represented in the Microsoft Media Foundation by a [media source](media-sources.md) object and a [Media Foundation transform](media-foundation-transforms.md) (MFT). However, no data flows between these two objects at the pipeline layer, only at the hardware layer, as shown in the following diagram.

![a diagram that shows a hardware proxy source.](images/proxy-mft3.png)

The connection between the media source and the MFT is negotiated as follows.

1.  The pipeline queries the media source for the [**IMFMediaSourceEx**](/windows/win32/mfidl/nn-mfidl-imfmediasourceex?branch=master) interface. (This interface is optional for media sources to support.)
2.  The pipeline calls [**IMFMediaSourceEx::GetStreamAttributes**](/windows/win32/mfidl/nf-mfidl-imfmediasourceex-getstreamattributes?branch=master) to get an [**IMFAttributes**](/windows/win32/mfobjects/nn-mfobjects-imfattributes?branch=master) pointer.
3.  The pipeline queries for the MF\_SOURCE\_STREAM\_SUPPORTS\_HW\_CONNECTION attribute. If the attribute is present and equal to **TRUE**, the media source supports hardware connections.
4.  The pipeline checks if the MFT is also a hardware proxy, by checking for the [MFT\_ENUM\_HARDWARE\_URL\_Attribute](mft-enum-hardware-url-attribute.md) attribute on the MFT. For details, see [Hardware MFTs](hardware-mfts.md).
5.  The pipeline sets the [MFT\_CONNECTED\_STREAM\_ATTRIBUTE](mft-connected-stream-attribute.md) attribute on the MFT. The value of this attribute is the [**IMFAttribute**](/windows/win32/mfobjects/nn-mfobjects-imfattributes?branch=master) pointer obtained from the media source in step 2.
6.  The pipeline sets the [MFT\_CONNECTED\_TO\_HW\_STREAM](mft-connected-to-hw-stream.md) attribute to **TRUE** on both the media source and the MFT.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Hardware MFTs](hardware-mfts.md)
</dt> </dl>

 

 




