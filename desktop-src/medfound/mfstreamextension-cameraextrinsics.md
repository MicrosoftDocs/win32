---
Description: Contains the camera extrinsics for the stream.
ms.assetid: 2236C135-BA3D-4C1B-8A39-5E23EF67425A
title: MFStreamExtension\_CameraExtrinsics attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFStreamExtension\_CameraExtrinsics attribute

Contains the camera extrinsics for the stream.

## Data type

Byte array

## Get/set

To get this attribute, call [**IMFMediaSourceEx::GetStreamAttributes**](/windows/win32/mfidl/nf-mfidl-imfmediasourceex-getstreamattributes?branch=master).

## Remarks

The value of the attribute is a [**MFCameraExtrinsics**](/windows/win32/mfapi/ns-mfapi-_mfcameraextrinsics?branch=master).

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



 

 




