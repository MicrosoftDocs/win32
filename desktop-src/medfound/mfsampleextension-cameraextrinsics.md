---
Description: 'Contains the camera extrinsics for the sample.'
ms.assetid: 'C970E958-3866-491A-9806-DB300834360E'
title: 'MFSampleExtension\_CameraExtrinsics attribute'
---

# MFSampleExtension\_CameraExtrinsics attribute

Contains the camera extrinsics for the sample.

## Data type

Byte array

## Get/set

To get this attribute, call [**IMFAttributes::GetBlob**](imfattributes-getblob.md).

To set this attribute, call [**IMFAttributes::SetBlob**](imfattributes-setblob.md).

## Applies to

[**IMFSample**](imfsample.md)

## Remarks

The value of the attribute is a [**MFCameraExtrinsics**](mfcameraextrinsics.md).

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

 

 




