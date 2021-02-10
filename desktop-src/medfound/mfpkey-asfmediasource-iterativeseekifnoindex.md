---
description: Configures the ASF media source to use iterative seeking if the source file has no index.
ms.assetid: 0dd6f202-cdbc-4a28-8907-5530a0a2141b
title: MFPKEY_ASFMediaSource_IterativeSeekIfNoIndex property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_ASFMediaSource\_IterativeSeekIfNoIndex property

Configures the ASF media source to use iterative seeking if the source file has no index.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**VARIANT\_BOOL**

VT\_BOOL

**boolVal**



## Remarks

Use this property to configure the ASF media source. To set the property, pass an **IPropertyStore** pointer to the *source resolver*. For more information, see [Configuring a Media Source](configuring-a-media-source.md).

*Iterative seeking* is an algorithm to find a position in an ASF file with no index. It uses a series of approximations, based on the average bit rate, to get progressively closer to the target seek time. (The algorithm is similar to a binary search.) Iterative seeking can take longer than seeking by index, so it is disabled by default.

If you set this property, use the following properties to set the search parameters:

-   [MFPKEY\_ASFMediaSource\_IterativeSeek\_Max\_Count](mfpkey-asfmediasource-iterativeseek-max-count.md)
-   [MFPKEY\_ASFMediaSource\_IterativeSeek\_Tolerance\_In\_MilliSecond](mfpkey-asfmediasource-iterativeseek-tolerance-in-millisecond.md)

These properties set the maximum number of iterations and the tolerance, respectively. The algorithm halts when it reaches the maximum number of iterations, or when it finds a packet whose distance from the seek time is within the specified tolerance.

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

 

 




