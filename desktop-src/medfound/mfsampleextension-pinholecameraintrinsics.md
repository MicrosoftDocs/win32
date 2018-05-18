---
Description: 'Contains the pinhole camera intrinsics for the sample.'
ms.assetid: 'AF7EA6A0-90C5-49A8-AD68-776BF770A448'
title: 'MFSampleExtension\_PinholeCameraIntrinsics attribute'
---

# MFSampleExtension\_PinholeCameraIntrinsics attribute

Contains the pinhole camera intrinsics for the sample.

## Data type

Byte array

## Get/set

To get this attribute, call [**IMFAttributes::GetBlob**](imfattributes-getblob.md).

To set this attribute, call [**IMFAttributes::SetBlob**](imfattributes-setblob.md).

## Applies to

[**IMFSample**](imfsample.md)

## Remarks

The value of the attribute is a [**MFPinholeCameraIntrinsics**](mfpinholecameraintrinsics.md).

This attribute is optional to support cameras that are not calibrated.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



 

 




