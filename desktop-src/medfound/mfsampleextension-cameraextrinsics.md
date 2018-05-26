---
Description: Contains the camera extrinsics for the sample.
ms.assetid: C970E958-3866-491A-9806-DB300834360E
title: MFSampleExtension\_CameraExtrinsics attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFSampleExtension\_CameraExtrinsics attribute

Contains the camera extrinsics for the sample.

## Data type

Byte array

## Get/set

To get this attribute, call [**IMFAttributes::GetBlob**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getblob?branch=master).

To set this attribute, call [**IMFAttributes::SetBlob**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setblob?branch=master).

## Applies to

[**IMFSample**](/windows/win32/mfobjects/nn-mfobjects-imfsample?branch=master)

## Remarks

The value of the attribute is a [**MFCameraExtrinsics**](/windows/win32/mfapi/ns-mfapi-_mfcameraextrinsics?branch=master).

This attribute is optional to support cameras that are not calibrated.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




