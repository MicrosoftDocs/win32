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
ms.date: 05/31/2018
---

# ASFLeakyBucketPairs

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

 

 




