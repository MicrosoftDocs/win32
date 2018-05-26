---
Description: Contains the pinhole camera intrinsics for the sample.
ms.assetid: AF7EA6A0-90C5-49A8-AD68-776BF770A448
title: MFSampleExtension\_PinholeCameraIntrinsics attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFSampleExtension\_PinholeCameraIntrinsics attribute

Contains the pinhole camera intrinsics for the sample.

## Data type

Byte array

## Get/set

To get this attribute, call [**IMFAttributes::GetBlob**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getblob?branch=master).

To set this attribute, call [**IMFAttributes::SetBlob**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setblob?branch=master).

## Applies to

[**IMFSample**](/windows/win32/mfobjects/nn-mfobjects-imfsample?branch=master)

## Remarks

The value of the attribute is a [**MFPinholeCameraIntrinsics**](/windows/win32/mfapi/ns-mfapi-_mfpinholecameraintrinsics?branch=master).

This attribute is optional to support cameras that are not calibrated.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



 

 




