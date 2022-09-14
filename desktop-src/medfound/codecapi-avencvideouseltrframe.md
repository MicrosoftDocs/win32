---
description: Specifies that the current frame is encoded using one or multiple LTR frames.
ms.assetid: 51FD6E36-9CDF-4005-942F-7A92CA706F38
title: CODECAPI_AVEncVideoUseLTRFrame property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# CODECAPI\_AVEncVideoUseLTRFrame property

Specifies that the current frame is encoded using one or multiple LTR frames.

## Data type

**ULONG** (VT\_UI4)

## Property GUID

**CODECAPI\_AVEncVideoUseLTRFrame**

## Property value

The value of this control includes two fields, where each field has 16 bits.




| Value | Meaning | 
|-------|---------|
| <span id="The_first_field"></span><span id="the_first_field"></span><span id="THE_FIRST_FIELD"></span><dl><dt><strong>The first field</strong></dt><dt>Bits[0..15]</dt></dl> | Indicates which LTR frame(s) are allowed for encoding the current frame. <br /><strong>H.264/AVC encoders:</strong><br /> This is a bitmap that indicates which LTR frames can be used as a reference for this frame. The least significant bit corresponds to LTR index 0, the second least significant bit corresponds to LTR index 1, etc.<br /> This value shall not be 0.<br /> The highest index specified by this value shall not be greater than the maximum number of LTR frames specified in the <a href="codecapi-avencvideoltrbuffercontrol.md">CODECAPI_AVEncVideoLTRBufferControl</a> property less one.<br /> | 
| <span id="The_second_field"></span><span id="the_second_field"></span><span id="THE_SECOND_FIELD"></span><dl><dt><strong>The second field</strong></dt><dt>Bits[16..31]</dt></dl> | Flag that indicates whether additional limitations are required for encoding subsequent frames. <br /><strong>H.264/AVC encoders:</strong><br /> 1 is on the only valid value for this field. All other values are invalid and reserved for future use.<br /> When the flag is 1, the encoder shall encode subsequent frames in encoding order subject to the following constraints:<br /><ul><li>It shall not use short term reference frames in encoding order older than the current frame or future encoding in encoding order.</li><li>It shall not use LTR frames not described by the most recent CODECAPI_AVEncVideoUseLTRFrame control.</li><li>It may use LTR frames updated after the current frame.</li></ul> | 




 

## Remarks

**H.264/AVC encoders:**

This property should not be called if a pending call to use an LTR frame has been issued using the CODECAPI\_AVEncVideoUseLTRFrame property and the encoder has not yet generated a frame that has used the LTR. In other words, the encoder should not queue up CODECAPI\_AVEncVideoUseLTRFrame requests.

If a CODECAPI\_AVEncVideoUseLTRFrame request is submitted while another CODECAPI\_AVEncVideoUseLTRFrame request is still pending, then the older request should be dropped.

Calling CODECAPI\_AVEncVideoUseLTRFrame on a non-base layer frame is valid and shall apply to the non-base layer frame, without delay to a base layer frame.

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

 

 




