---
description: Specifies the maximum number of coded sequences which the MPEG4 sink will place in each fragment when operating in fragmented mode.
title: MF_MPEG4SINK_MAX_CODED_SEQUENCES_PER_FRAGMENT attribute (Mfidl.h)
ms.topic: reference
ms.date: 10/31/2025
---

# MF\_MPEG4SINK\_MAX\_CODED\_SEQUENCES\_PER\_FRAGMENT attribute

Specifies the maximum number of coded sequences which the MPEG4 sink will place in each fragment when operating in fragmented mode.

## Data type

**UINT32**

## Remarks

A coded sequence is a group of [IMFSample](/windows/win32/api/mfobjects/nn-mfobjects-imfsample) objects where the first **IMFSample** has the non-zero value for the [MFSampleExtension_CleanPoint](mfsampleextension-cleanpoint-attribute.md) attribute, followed by zero or more **IMFSamples** that have a zero value, or no value, for the **MFSampleExtension_CleanPoint** attribute.

## Requirements

| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 version 1709                                |
| Minimum supported server | Windows Server version 1709                        |
| Header               | Mfidl.h |




## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 




