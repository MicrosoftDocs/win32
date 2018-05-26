---
Description: Gets an object of type IMFCollection containing IMFSample objects which contain network abstraction layer units (NALUs) and Supplemental Enhancement Information (SEI) units forwarded by a decoder.
ms.assetid: F9FD7959-A78A-4C72-8326-EE8FF9066E6C
title: MFSampleExtension\_ForwardedDecodeUnits attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFSampleExtension\_ForwardedDecodeUnits attribute

Gets an object of type [**IMFCollection**](/windows/win32/mfobjects/nn-mfobjects-imfcollection?branch=master) containing [**IMFSample**](/windows/win32/mfobjects/nn-mfobjects-imfsample?branch=master) objects which contain network abstraction layer units (NALUs) and Supplemental Enhancement Information (SEI) units forwarded by a decoder.

## Data type

**IUnknown**

## Remarks

The collection contains all custom NALU/SEI units since previous frame with emulation prevention bytes removed.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



 

 




