---
title: ASFLeakyBucketPairs
description: The ASFLeakyBucketPairs attribute is an optional attribute that describes the buffering requirements for a variable bit rate file.
ms.assetid: d1b3e8cc-c082-4283-88bc-172f58adf2d9
keywords:
- ASFLeakyBucketPairs windows Media Format
topic_type:
- apiref
api_name:
- ASFLeakyBucketPairs
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# ASFLeakyBucketPairs

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **ASFLeakyBucketPairs** attribute is an optional attribute that describes the buffering requirements for a variable bit rate file.

## Global Constant

g\_wszASFLeakyBucketPairs

## Data Type

**WMT\_TYPE\_BINARY**

## Remarks

This attribute has the following format:

``` syntax
struct
{
    WORD wReserved;
    WM_LEAKY_BUCKET_PAIR bucket[2];
};
```

Where *wReserved* must equal zero, and *bucket* is an array of [**WM\_LEAKY\_BUCKET\_PAIR**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_leaky_bucket_pair) structures. The array must contain at least two entries, but can be larger. The reader object uses this attribute to determine the amount of content to buffer before playback.

## See also

<dl> <dt>

[**Attribute List**](attribute-list.md)
</dt> </dl>

 

 




