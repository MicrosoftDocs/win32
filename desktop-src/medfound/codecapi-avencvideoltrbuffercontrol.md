---
description: Specifies the maximum number of Long Term Reference (LTR) frames controlled by application.
ms.assetid: C34AD867-5F94-4414-A282-ECC392678635
title: CODECAPI_AVEncVideoLTRBufferControl property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# CODECAPI\_AVEncVideoLTRBufferControl property

Specifies the maximum number of Long Term Reference (LTR) frames controlled by application.

## Data type

**ULONG** (VT\_UI4)

## Property GUID

**CODECAPI\_AVEncVideoLTRBufferControl**

## Property value

The value of this control includes two fields, where each field has 16 bits.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="The_first_field"></span><span id="the_first_field"></span><span id="THE_FIRST_FIELD"></span><dl> <dt><strong>The first field</strong></dt> <dt>Bits[0..15]</dt> </dl></td>
<td>The number of LTR frames controlled by the application.<br/> <strong>H.264/AVC encoders:</strong><br/> Assuming the value is N and N is non-zero value, at each IDR frame the encoder must automatically mark the frames following the IDR frame (and including the IDR frame) as LTR frames as long as all 3 of the following apply:
<ul>
<li>The frame is not already set to be marked as a long term reference frame.</li>
<li>The frame is a base layer frame. For example, syntax element <strong>temporal_id</strong> equal to 0.</li>
<li>The number of frames currently marked as LTR is less than N.</li>
</ul>
<br/></td>
</tr>
<tr class="even">
<td><span id="The_second_field"></span><span id="the_second_field"></span><span id="THE_SECOND_FIELD"></span><dl> <dt><strong>The second field</strong></dt> <dt>Bits[16..31]</dt> </dl></td>
<td>The trust mode of LTR control.<br/> <strong>H.264/AVC encoders:</strong><br/> 1 (Trust Until) means the encoder may use an LTR frame unless the app explicitly invalidates it through the <a href="codecapi-avencvideouseltrframe.md">CODECAPI_AVEncVideoUseLTRFrame</a> control. <br/> Other values are invalid and reserved for future use.<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

This is a static API.

Default value shall be 0

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

 

 




