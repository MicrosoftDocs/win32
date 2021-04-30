---
description: Contains the pinhole camera intrinsics for the stream.
ms.assetid: 7E5E7C60-9C3F-406B-A7DD-A953181CD314
title: MFStreamExtension_PinholeCameraIntrinsics attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFStreamExtension\_PinholeCameraIntrinsics attribute

Contains the pinhole camera intrinsics for the stream.

## Data type

Byte array

## Get/set

To get this attribute, call [**IMFMediaSourceEx::GetStreamAttributes**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasourceex-getstreamattributes).

## Remarks

The value of the attribute is a [**MFPinholeCameraIntrinsics**](/windows/desktop/api/mfapi/ns-mfapi-mfpinholecameraintrinsics).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



 

 




