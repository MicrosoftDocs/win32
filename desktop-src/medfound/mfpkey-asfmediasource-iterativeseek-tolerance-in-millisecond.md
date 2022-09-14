---
description: Sets the tolerance, in milliseconds, that is used when the ASF media source performs iterative seeking.
ms.assetid: 3ee4410f-857c-4978-a308-87decfba0e2f
title: MFPKEY_ASFMediaSource_IterativeSeek_Tolerance_In_MilliSecond property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_ASFMediaSource\_IterativeSeek\_Tolerance\_In\_MilliSecond property

Sets the tolerance, in milliseconds, that is used when the ASF media source performs iterative seeking.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**ULONG**

VT\_UI4

**ulVal**



## Remarks

Use this property to configure the ASF media source. To set the property, pass an **IPropertyStore** pointer to the source resolver. For more information, see [Configuring a Media Source](configuring-a-media-source.md).

This property applies only when iterative seeking is enabled. For more information, see [MFPKEY\_ASFMediaSource\_IterativeSeekIfNoIndex](mfpkey-asfmediasource-iterativeseekifnoindex.md).

The iterative seeking algorithm halts if it finds a packet whose distance from the seek time is within the specified tolerance. The default value is 8000 milliseconds.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                     |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




