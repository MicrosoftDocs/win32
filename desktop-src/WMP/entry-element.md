---
title: ENTRY Element
description: The ENTRY element specifies a Windows Media file to render as a clip.
ms.assetid: 7fd16aff-2eed-4f95-92b3-b48a9d785e7c
keywords:
- ENTRY Element Windows Media Player
topic_type:
- apiref
api_name:
- ENTRY Element
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ENTRY Element

The **ENTRY** element specifies a Windows Media file to render as a clip.

``` syntax
<ENTRY
   CLIENTSKIP = "YES" | "NO"
   SKIPIFREF = "YES" | "NO"
>
</ENTRY>
```

## Attributes

**CLIENTSKIP**

Value indicating whether the user can skip forward past the clip.

Possible values include the following.



| Value | Description                                   |
|-------|-----------------------------------------------|
| YES   | Default. User can skip forward past the clip. |
| NO    | User cannot skip forward past the clip.       |



 

**SKIPIFREF**

Value indicating whether Windows Media Player should skip this clip when the **ENTRY** element is included in a second metafile through the use of an **ENTRYREF** element.

Possible values include the following.



| Value | Description                                                                                 |
|-------|---------------------------------------------------------------------------------------------|
| YES   | Windows Media Player will ignore this entry, if referenced through an **ENTRYREF** element. |
| NO    | Default. Windows Media Player will not ignore this entry.                                   |



 

## Parent/Child Elements



| Hierarchy       | Elements                                                                                                                                                                                     |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parent elements | **ASX**, **EVENT**, **REPEAT**                                                                                                                                                               |
| Child elements  | **ABSTRACT**, **AUTHOR**, **BANNER**, **BASE**, **COPYRIGHT**, **DURATION**, **ENDMARKER**, **MOREINFO**, **PARAM**, **PREVIEWDURATION**, **REF**, **STARTMARKER**, **STARTTIME**, **TITLE** |



 

## Remarks

This element is the fundamental construct in a Windows Media metafile. The **ENTRY** element and its associated attributes define meta-information for a single, logical piece of content, called a clip. Child elements within the scope of an **ENTRY** element define media content for Windows Media Player to open (**REF**), information about the clip that Windows Media Player will display as text (**AUTHOR**, **COPYRIGHT**, **TITLE**), and other settings related to the clip. The **REF** child element links the content to be streamed for the parent **ENTRY** element. Though the script will not break, the **ENTRY** is meaningless without a **REF** child.

If the value of the **CLIENTSKIP** attribute is NO, the user cannot skip forward past the piece of content defined by the **ENTRY** element. This does not work if the child **REF** element references another metafile. Nested metafiles should be referenced using the **ENTRYREF** element.

The **SKIPIFREF** attribute pertains only to **ENTRY** elements that are included in a second metafile through the use of an **ENTRYREF** element. The **ENTRYREF** element references another metafile for logical inclusion in the current file. If the value of the **SKIPIFREF** attribute for an **ENTRY** element from the referenced metafile file is YES, Windows Media Player ignores this pulled-in entry, and moves on to the next **ENTRY** element, if any. The next **ENTRY** element can be the next entry in the original file, or the next entry in the metafile referenced in the **ENTRYREF** element.

## Examples


```XML
<ASX VERSION="3.0">
   <TITLE>Example Windows Media Player Show</TITLE>
   
   <ENTRY>
      <TITLE>Example Clip</TITLE>
      <REF HREF="https://example.microsoft.com/media.asf" />
   </ENTRY>
   
   <ENTRY>
      <TITLE>Another Clip</TITLE>
      <REF HREF="https://example.microsoft.com/more_media.asf" />
   </ENTRY>
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

 

 





