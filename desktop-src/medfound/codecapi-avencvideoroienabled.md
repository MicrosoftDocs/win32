---
description: Indicates whether MFSampleExtension\_ROIRectangle attribute set on the input sample will be honored or not.
ms.assetid: 6B3CB513-43E8-4D30-B5A0-CD2E9C9F46BA
title: CODECAPI_AVEncVideoROIEnabled property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# CODECAPI\_AVEncVideoROIEnabled property

Indicates whether [MFSampleExtension\_ROIRectangle](mfsampleextension-roirectangle.md) attribute set on the input sample will be honored or not.

## Data type

**ULONG** (VT\_UI4)

## Property GUID

**CODECAPI\_AVEncVideoROIEnabled**

## Remarks

Default value is 0.

If an encoder MFT accepts a non-zero value, it is expected that the encoder will honor the [MFSampleExtension\_ROIRectangle](mfsampleextension-roirectangle.md) attribute set on the input sample.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>                                   |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Codecapi.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




