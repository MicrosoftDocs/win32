---
description: Marks the current frame as a LTR frame.
ms.assetid: D70A54D6-DA9B-40E5-B130-0AA9C5363DF0
title: CODECAPI_AVEncVideoMarkLTRFrame property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# CODECAPI\_AVEncVideoMarkLTRFrame property

Marks the current frame as a LTR frame.

## Data type

**ULONG** (VT\_UI4)

## Property GUID

**CODECAPI\_AVEncVideoMarkLTRFrame**

## Remarks

**H.264/AVC encoders:**

The value of this control is the value of H.264 syntax *LongTermFramIdx* associated with the current frame. If the current frame is not in the base layer, for example syntax element *temporal\_id* is not equal to 0, this property applies to the next base layer frame in encoding order.

This property should not be called if a pending call to mark an LTR frame has been issued using the CODECAPI\_AVEncVideoMarkLTRFrame property and the encoder has not yet marked a frame as LTR. In other words, the encoder should not queue up CODECAPI\_AVEncVideoMarkLTRFrame requests. If a CODECAPI\_AVEncVideoMarkLTRFrame request is submitted while another CODECAPI\_AVEncVideoMarkLTRFrame request is still pending, the older request should be dropped.

The CODECAPI\_AVEncVideoMarkLTRFrame property is dynamic and can be set during the encoding session.

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

 

 




