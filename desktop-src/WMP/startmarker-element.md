---
title: STARTMARKER Element
description: The STARTMARKER element specifies a marker from which Windows Media Player will start rendering the stream.
ms.assetid: b5c2422b-a59c-43f7-bac3-5722418192dc
keywords:
- STARTMARKER Element Windows Media Player
topic_type:
- apiref
api_name:
- STARTMARKER Element
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# STARTMARKER Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **STARTMARKER** element specifies a marker from which Windows Media Player will start rendering the stream.

``` syntax
<STARTMARKER
   NUMBER = "marker number"
   NAME = "marker name"
/>
```

## Attributes

**NUMBER**

The number of a numeric marker in the index. The default value is the beginning of on-demand content or the current position in a real-time stream.

**NAME**

The name of a named marker in the index. The default value is the beginning of on-demand content or the current position in a real-time stream.

## Parent/Child Elements



| Hierarchy       | Elements           |
|-----------------|--------------------|
| Parent elements | **ENTRY**, **REF** |
| Child elements  | None               |



 

## Remarks

This element specifies the marker from which Windows Media Player is to start rendering the stream defined in the parent **ENTRY** or **REF** element.

**Note**

Use this element with either the **NUMBER** or **NAME** attribute, but not both.

A **STARTMARKER** element defined within a **REF** element takes precedence over a **STARTMARKER** element defined within the **REF** element's parent **ENTRY** element. A **STARTMARKER** element also takes precedence over a **STARTTIME** element.

If the marker specified by a **STARTMARKER** element occurs later in the stream than the marker defined by an **ENDMARKER** element, no content plays, but no error is generated.

## Examples


```XML
<STARTMARKER NUMBER="14" />
<STARTMARKER NAME="Marker_StartHere" />
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

 

 





