---
description: Contains a pointer to the stream attributes of the connected stream on a hardware-based Media Foundation transform (MFT).
ms.assetid: 7e14a02e-4cbf-45aa-a6f5-2c53b2437127
title: MFT_CONNECTED_STREAM_ATTRIBUTE attribute (Mftransform.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFT\_CONNECTED\_STREAM\_ATTRIBUTE attribute

Contains a pointer to the stream attributes of the connected stream on a hardware-based Media Foundation transform (MFT).

## Data type

**IMFAttributes\*** stored as **IUnknown\***

## Get/set

To get this attribute, call [**IMFAttributes::GetUnknown**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getunknown).

To set this attribute, call [**IMFAttributes::SetUnknown**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setunknown).

## Remarks

Applications typically do not use this attribute.

This attribute is used for MFTs that act as proxies to a hardware device. For details, see [Hardware MFTs](hardware-mfts.md).

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[MFT\_CONNECTED\_TO\_HW\_STREAM](mft-connected-to-hw-stream.md)
</dt> <dt>

[Hardware MFTs](hardware-mfts.md)
</dt> <dt>

[Transform Attributes](transform-attributes.md)
</dt> </dl>

 

 




