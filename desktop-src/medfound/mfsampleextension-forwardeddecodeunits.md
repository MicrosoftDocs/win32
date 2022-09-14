---
description: Gets an object of type IMFCollection containing IMFSample objects which contain network abstraction layer units (NALUs) and Supplemental Enhancement Information (SEI) units forwarded by a decoder.
ms.assetid: F9FD7959-A78A-4C72-8326-EE8FF9066E6C
title: MFSampleExtension_ForwardedDecodeUnits attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFSampleExtension\_ForwardedDecodeUnits attribute

Gets an object of type [**IMFCollection**](/windows/desktop/api/mfobjects/nn-mfobjects-imfcollection) containing [**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample) objects which contain network abstraction layer units (NALUs) and Supplemental Enhancement Information (SEI) units forwarded by a decoder.

## Data type

**IUnknown**

## Remarks

The collection contains all custom NALU/SEI units since previous frame with emulation prevention bytes removed.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



 

 




