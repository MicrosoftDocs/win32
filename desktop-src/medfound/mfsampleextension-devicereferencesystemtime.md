---
description: Specifies the original device timestamp on the sample.
ms.assetid: 93BB6E41-308E-4527-A04B-C685C818FEC4
title: MFSampleExtension_DeviceReferenceSystemTime attribute (Mfcaptureengine.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFSampleExtension\_DeviceReferenceSystemTime attribute

Specifies the original device timestamp on the sample.

## Data type

**UINT64**

## Remarks

This is the a device reference time stamp of media samples in 100ns resolution. This time stamp may or may not carry the actual value of the query performance counter (QPC), depending on the source producing the samples. This value may be modified by other components in the media pipeline. This value is not available to MFTs inserted into the capture pipeline.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                   |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                        |
| Header<br/>                   | <dl> <dt>Mfcaptureengine.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mfcaptureengine.idl</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




