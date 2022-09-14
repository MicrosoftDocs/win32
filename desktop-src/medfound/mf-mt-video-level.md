---
description: Specifies the MPEG-2 or H.264 level in a video media type. This is an alias of MF\_MT\_MPEG2\_LEVEL.
ms.assetid: 23786FC8-ACA4-4F6A-98BA-57A8C76BD4C6
title: MF_MT_VIDEO_LEVEL attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_VIDEO\_LEVEL attribute

Specifies the MPEG-2 or H.264 level in a video media type. This is an alias of [MF\_MT\_MPEG2\_LEVEL](mf-mt-mpeg2-level-attribute.md).

## Data type

**UINT32**

## Remarks

**H.264 encoders:**

Supported levels are extended to include the [**eAVEncH264VLevel5\_2**](/windows/desktop/api/codecapi/ne-codecapi-eavench264vlevel).

Default : Recommended default is to select the minimum level to match video encoding configuration including resolution, frame rate etc.

Recommended default: select the minimum level to match video encoding configuration including resolution, frame rate, etc.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




