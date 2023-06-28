---
title: REPEAT Element
description: The REPEAT element defines the number of times Windows Media Player repeats one or more ENTRY or ENTRYREF elements.
ms.assetid: 1a825f2b-29a7-4180-93df-51b3b5dd14e5
keywords:
- REPEAT Element Windows Media Player
topic_type:
- apiref
api_name:
- REPEAT Element
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# REPEAT Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **REPEAT** element defines the number of times Windows Media Player repeats one or more **ENTRY** or **ENTRYREF** elements.

``` syntax
<REPEAT   
   COUNT = "integer"
>
</REPEAT>
```

## Attributes

**COUNT**

Integer representing the number of times Windows Media Player repeats the **ENTRY** and **ENTRYREF** elements within this element's scope.

## Parent/Child Elements



| Hierarchy       | Elements                |
|-----------------|-------------------------|
| Parent elements | **ASX**                 |
| Child elements  | **ENTRY**, **ENTRYREF** |



 

## Remarks

This element defines the number of times Windows Media Player repeats, or loops through, the clips defined by the **ENTRY** and **ENTRYREF** elements within this element's scope. Only the first **REPEAT** element in a metafile is valid; subsequent **REPEAT** elements are ignored.

If no **COUNT** attribute is defined, the content in the associated **ENTRY** and **ENTRYREF** elements repeats an infinite number of times. A value of zero causes Windows Media Player to ignore the **REPEAT** element and play the content once.

## Examples


```XML
<ASX VERSION="3.0">
   <ENTRY>
        <REF HREF="mms://example.microsoft.com/clip1.asf" />
<!-- This clip plays once. -->
   </ENTRY>

   <REPEAT COUNT="2">
      <ENTRY>
     <REF HREF="mms://example.microsoft.com/clip2.asf" />
     <REF HREF="mms://example.microsoft.com/clip3.asf" />
 <!-- These clips play twice. -->
      </ENTRY>
   </REPEAT>
</ASX>
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

 

 





