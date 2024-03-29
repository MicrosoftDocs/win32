---
title: STARTTIME Element
description: The STARTTIME element defines a time index from which Windows Media Player will start rendering the stream.
ms.assetid: 9b0199c8-5c95-4b4e-a943-e3bd037bf0bc
keywords:
- STARTTIME Element Windows Media Player
topic_type:
- apiref
api_name:
- STARTTIME Element
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# STARTTIME Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **STARTTIME** element defines a time index from which Windows Media Player will start rendering the stream.

``` syntax
<STARTTIME
   VALUE = "hh:mm:ss.fract"
/>
```

## Attributes

**VALUE** (required)

The time index (in hours, minutes, seconds, and hundredths of a second) from which Windows Media Player starts playing a stream defined in the associated element.

## Parent/Child Elements



| Hierarchy       | Elements           |
|-----------------|--------------------|
| Parent elements | **ENTRY**, **REF** |
| Child elements  | None               |



 

## Remarks

This element defines a time index into the content where Windows Media Player is to start rendering the stream. This element can be used only with stored, on-demand content that has been indexed.

## Examples


```XML
<STARTTIME VALUE="1:30.0" />
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

 

 





