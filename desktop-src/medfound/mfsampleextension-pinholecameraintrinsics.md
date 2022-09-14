---
description: Contains the pinhole camera intrinsics for the sample.
ms.assetid: AF7EA6A0-90C5-49A8-AD68-776BF770A448
title: MFSampleExtension_PinholeCameraIntrinsics attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFSampleExtension\_PinholeCameraIntrinsics attribute

Contains the pinhole camera intrinsics for the sample.

## Data type

Byte array

## Get/set

To get this attribute, call [**IMFAttributes::GetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getblob).

To set this attribute, call [**IMFAttributes::SetBlob**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setblob).

## Applies to

[**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample)

## Remarks

The value of the attribute is a [**MFPinholeCameraIntrinsics**](/windows/desktop/api/mfapi/ns-mfapi-mfpinholecameraintrinsics).

This attribute is optional to support cameras that are not calibrated.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



 

 




