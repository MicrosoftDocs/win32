---
title: PREVIEWDURATION Element
description: The PREVIEWDURATION element defines the length of time a clip plays in preview mode.
ms.assetid: 428a4e3d-9c08-4b6c-acc7-b630aab37de3
keywords:
- PREVIEWDURATION Element Windows Media Player
topic_type:
- apiref
api_name:
- PREVIEWDURATION Element
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# PREVIEWDURATION Element

The **PREVIEWDURATION** element defines the length of time a clip plays in preview mode.

``` syntax
<PREVIEWDURATION
   VALUE = "hh:mm:ss.fract"
/>
```

## Attributes

**VALUE** (required)

Length of time (in hours, minutes, seconds, and hundredths of a second) that the clip plays in preview mode.

## Parent/Child Elements



| Hierarchy       | Elements                    |
|-----------------|-----------------------------|
| Parent elements | **ASX**, **ENTRY**, **REF** |
| Child elements  | None                        |



 

## Remarks

This element defines the length of time that a clip plays in preview mode. If this element appears within an **ENTRY** element or a **REF** element, it applies to the clip defined by that element. If it appears within the scope of an **ASX** element, it applies to every clip in the metafile. A **PREVIEWDURATION** element in a **REF** element takes precedence over one in an ENTRY **element**, and either takes precedence over a **PREVIEWDURATION** element in an **ASX** element. If no **PREVIEWDURATION** element is defined for a clip, the default preview time is 10 seconds.

If there is a **STARTTIME** or **STARTMARKER** element for the clip, Windows Media Player renders the clip starting at the point defined by one of these elements; otherwise it renders from the beginning of the clip. The clip stops normally if it is shorter than the time defined by the **PREVIEWDURATION** element.

The **DURATION** element overrides a **PREVIEWDURATION** element.

## Examples


```XML
<PREVIEWDURATION VALUE="0:30.0" />
```



## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------|
| Version<br/> | Windows Media Player version 70 or later<br/> |



## See also

<dl> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> <dt>

[**Windows Media Metafile Reference**](windows-media-metafile-reference.md)
</dt> </dl>

 

 





