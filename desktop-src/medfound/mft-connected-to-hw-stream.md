---
Description: Specifies whether a hardware-based Media Foundation transform (MFT) is connected to another hardware-based MFT.
ms.assetid: 9166c43f-d2ae-4dc7-84e9-02146b67efe2
title: MFT\_CONNECTED\_TO\_HW\_STREAM attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFT\_CONNECTED\_TO\_HW\_STREAM attribute

Specifies whether a hardware-based Media Foundation transform (MFT) is connected to another hardware-based MFT.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master).

## Remarks

Applications typically do not use this attribute.

This attribute is used with hardware-based MFTs. When two hardware MFTs are connected within a topology, the topology loader sets this attribute to **TRUE** on the following objects:

-   The output stream of the upstream MFT
-   The input stream of the downstream MFT

To get the attribute store for the output stream, the topology loader calls [**IMFTransform::GetOutputStreamAttributes**](/windows/win32/mftransform/nf-mftransform-imftransform-getoutputstreamattributes?branch=master) on the upstream MFT. To get the attribute store for the input stream, the topology loader calls [**IMFTransform::GetInputStreamAttributes**](/windows/win32/mftransform/nf-mftransform-imftransform-getinputstreamattributes?branch=master) on the downstream MFT.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Hardware MFTs](hardware-mfts.md)
</dt> <dt>

[Transform Attributes](transform-attributes.md)
</dt> </dl>

 

 




