---
Description: Specifies the offsets to the payload boundaries in a frame for protected samples.
ms.assetid: 8aa25afd-efa8-4fe0-92d4-8432f9d633c9
title: MFSampleExtension\_PacketCrossOffsets attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFSampleExtension\_PacketCrossOffsets attribute

Specifies the offsets to the payload boundaries in a frame for protected samples.

## Data type

Byte array

## Get/set

To get this attribute, call [**IMFAttributes::GetBlob**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getblob?branch=master).

To set this attribute, call [**IMFAttributes::SetBlob**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setblob?branch=master).

## Applies to

[**IMFSample**](/windows/win32/mfobjects/nn-mfobjects-imfsample?branch=master)

## Remarks

This attribute applies to media samples protected by Windows Media Digital Rights Management (DRM). The value of the attribute is an array of **DWORD**s. Each entry in the array is the offset of a payload boundary, relative to the start of the frame. An application can use these values when decrypting and reconstructing the frames.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                              |
| Header<br/>                   | <dl> <dt>Wmcontainer.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[ASF Splitter](asf-splitter.md)
</dt> <dt>

[Sample Attributes](sample-attributes.md)
</dt> <dt>

[Media Samples](media-samples.md)
</dt> </dl>

 

 




