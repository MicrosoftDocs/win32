---
description: Specifies Long Term Reference (LTR) frame info and is returned on the output sample.
ms.assetid: 0632D780-C56B-4FDB-8A76-B7A7DE414242
title: MFSampleExtension_LongTermReferenceFrameInfo attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFSampleExtension\_LongTermReferenceFrameInfo attribute

Specifies Long Term Reference (LTR) frame info and is returned on the output sample.

## Data type

**UINT32**

## Remarks

**H.264/AVC encoders:**

Encoders shall return this attribute on the output sample when the application controls LTR frames, which is specified by [CODECAPI\_AVEncVideoLTRBufferControl](codecapi-avencvideoltrbuffercontrol.md).

MFSampleExtension\_LongTermReferenceFrameInfo returns up to two fields.

The first field, bits\[0..15\], is *LongTermFrameIdx* associated with the output frame if it is marked as a LTR frame. The first value is 0xffff, if this output frame is a short term reference frame or a non-reference frame.

The second field, bits\[16..31\], is a bitmap consisting of *MaxNumLTRFrames* many bits that indicate which LTR frame(s) were used for encoding this output frame, starting from bit 16. The rest of bits shall be set to 0. The second value is 0 if this output frame is not encoded using any LTR frames. *MaxNumLTRFrames* is the maximum number of LTR frames set through [CODECAPI\_AVEncVideoLTRBufferControl](codecapi-avencvideoltrbuffercontrol.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>                                |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/>                     |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




