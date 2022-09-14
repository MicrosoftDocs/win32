---
description: Contains the camera extrinsics for the stream.
ms.assetid: 2236C135-BA3D-4C1B-8A39-5E23EF67425A
title: MFStreamExtension_CameraExtrinsics attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFStreamExtension\_CameraExtrinsics attribute

Contains the camera extrinsics for the stream.

## Data type

Byte array

## Get/set

To get this attribute, call [**IMFMediaSourceEx::GetStreamAttributes**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasourceex-getstreamattributes).

## Remarks

The value of the attribute is a [**MFCameraExtrinsics**](/windows/desktop/api/mfapi/ns-mfapi-mfcameraextrinsics).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



 

 




