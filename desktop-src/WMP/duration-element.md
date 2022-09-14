---
title: DURATION Element
description: The DURATION element defines the length of time Windows Media Player will render the associated playlist entry.
ms.assetid: fe5c242e-08c9-44f0-a6fc-3f0fa432ba38
keywords:
- DURATION Element Windows Media Player
topic_type:
- apiref
api_name:
- DURATION Element
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# DURATION Element

The **DURATION** element defines the length of time Windows Media Player will render the associated playlist entry.

``` syntax
<DURATION
    VALUE = "hh:mm:ss.fract"
/>
```

## Attributes

**VALUE** (required)

The length of time, in hours, minutes, seconds, and hundredths of a second, that an entry is rendered by Windows Media Player. The default value is the entire length of the entry. If the entry is a graphic file, a duration value must be specified.

## Parent/Child Elements



| Hierarchy       | Elements           |
|-----------------|--------------------|
| Parent elements | **ENTRY**, **REF** |
| Child elements  | None               |



 

## Remarks

This element defines the length of time a stream is to be rendered. If the **VALUE** attribute exceeds the length of the content stream, the stream terminates at its normal end-point.

This element can appear either within a **REF** element or within an **ENTRY** element. However, a **DURATION** element defined within a **REF** element overrides one that appears within the **REF** element's parent **ENTRY** element.

The **DURATION** element overrides a **PREVIEWDURATION** element.

## Examples


```XML
<DURATION VALUE="00:00:30" />   <!-- 30 seconds -->
<DURATION VALUE="1:01.5" />     <!-- 61.5 seconds -->

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> <dt>

[**Windows Media Metafile Reference**](windows-media-metafile-reference.md)
</dt> </dl>

 

 





