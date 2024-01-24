---
title: ENDMARKER Element
description: The ENDMARKER element specifies a marker at which Windows Media Player will stop rendering the stream.
ms.assetid: 554f0612-1669-4da4-9c5f-cc8984ef897c
keywords:
- ENDMARKER Element Windows Media Player
topic_type:
- apiref
api_name:
- ENDMARKER Element
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# ENDMARKER Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **ENDMARKER** element specifies a marker at which Windows Media Player will stop rendering the stream.

``` syntax
<ENDMARKER
   NUMBER = "marker number" |
   NAME = "marker name"
/>
```

## Attributes

**NUMBER**

The number of a numeric marker in the index. The default value is the end of the content.

**NAME**

The name of a named marker in the index. The default value is the end of the content.

## Parent/Child Elements



| Hierarchy       | Elements           |
|-----------------|--------------------|
| Parent elements | **ENTRY**, **REF** |
| Child elements  | None               |



 

## Remarks

This element specifies the marker where Windows Media Player is to stop rendering the stream defined in the parent **ENTRY** or **REF** element.

Note

Use the **ENDMARKER** element with either the **NUMBER** or **NAME** attribute, but not both.

In preview mode, reaching an end marker stops the preview, even if the time specified by the **PREVIEWDURATION** element has not elapsed. The **ENDMARKER** element also takes precedence over the **DURATION** element.

An **ENDMARKER** element defined within a **REF** element takes precedence over an **ENDMARKER** defined within the **REF** element's parent **ENTRY** element.

If the marker specified by an **ENDMARKER** element occurs earlier in the stream than the marker defined by a **STARTMARKER** element, no content plays, but no error is generated.

## Examples


```XML
<ENDMARKER NUMBER="17" />
<ENDMARKER NAME="Marker_StopHere" />

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

 

 





