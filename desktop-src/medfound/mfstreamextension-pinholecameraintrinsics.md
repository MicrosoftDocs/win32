---
Description: Contains the pinhole camera intrinsics for the stream.
ms.assetid: 7E5E7C60-9C3F-406B-A7DD-A953181CD314
title: MFStreamExtension\_PinholeCameraIntrinsics attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFStreamExtension\_PinholeCameraIntrinsics attribute

Contains the pinhole camera intrinsics for the stream.

## Data type

Byte array

## Get/set

To get this attribute, call [**IMFMediaSourceEx::GetStreamAttributes**](/windows/win32/mfidl/nf-mfidl-imfmediasourceex-getstreamattributes?branch=master).

## Remarks

The value of the attribute is a [**MFPinholeCameraIntrinsics**](/windows/win32/mfapi/ns-mfapi-_mfpinholecameraintrinsics?branch=master).

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



 

 




