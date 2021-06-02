---
title: ASX Element
description: The ASX element defines a file as a metafile.
ms.assetid: 130220a0-959c-4c13-aa7d-06b6bbebc9cc
keywords:
- ASX Element Windows Media Player
topic_type:
- apiref
api_name:
- ASX Element
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ASX Element

The **ASX** element defines a file as a metafile.

``` syntax
<ASX
   VERSION = "number"
   PREVIEWMODE = "YES" | "NO"
   BANNERBAR = "AUTO" | "FIXED"
>
</ASX>
```

## Attributes

`VERSION` (required)

Decimal number representing the version number of the syntax for the metafile. Set to 3 or 3.0.

**PREVIEWMODE** (optional)

Value indicating whether Windows Media Player enters preview mode before playing the first clip.

Must be one of the following values.



| Value | Description                                                                                        |
|-------|----------------------------------------------------------------------------------------------------|
| YES   | Windows Media Player enters preview mode before playing the first clip.                            |
| NO    | The default value. Windows Media Player does not enter preview mode before playing the first clip. |



 

**BANNERBAR** (optional)

Value indicating whether Windows Media Player reserves space for a banner graphic.

Must be one of the following values.



| Value | Description                                                                                                                                |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------|
| AUTO  | The default value. Windows Media Player reserves space for the banner bar only when a piece of content includes one.                       |
| FIXED | Windows Media Player reserves a fixed space for a banner graphic for every piece of content played, whether there is an associated banner. |



 

## Parent/Child Elements



| Hierarchy       | Elements                                                                                                                                                               |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parent elements | None. The **ASX** element must be the first element in every metafile.                                                                                                 |
| Child elements  | **ABSTRACT**, **AUTHOR**, **BANNER**, **BASE**, **COPYRIGHT**, **ENTRY**, **ENTRYREF**, **EVENT**, **MOREINFO**, **PREVIEWDURATION**, **PARAM**, **REPEAT**, **TITLE** |



 

## Remarks

The first four characters of a metafile playlist must be "<ASX". Other elements defined within the scope of the **ASX** element, such as **TITLE** and **AUTHOR**, are associated with the show information displayed by Windows Media Player.

For Windows Media Player, the syntax version number is 3.0. Windows Media Player supports all previous versions of metafile syntax. Acceptable values for the **VERSION** attribute include both 3.0 and 3 (with no decimal point).

If the value of the **PREVIEWMODE** attribute is YES, Windows Media Player immediately enters preview mode before playing the first clip. When Windows Media Player enters preview mode, it previews each clip referenced in the metafile. The **PREVIEWDURATION** element determines the duration of each preview.

The **BANNERBAR** attribute defines whether Windows Media Player reserves space for a banner graphic. A banner is a graphic that is displayed in the video display area while media content is playing. (Use the **BANNER** element to add a banner to the content.) If the value of **BANNERBAR** is FIXED, Windows Media Player reserves banner space for every piece of media content, whether the media content has a banner. If a piece of media content does not have a banner associated with it, the space reserved for one is black. If the value of the **BANNERBAR** attribute is AUTO, Windows Media Player reserves space for the banner only when the media content includes one.

If you create a metafile with multiple clips (**ENTRY** or **ENTRYREF** elements) and set the value of the **BANNERBAR** attribute to AUTO, Windows Media Player might resize to allow space for a banner graphic for one clip, and then resize again if the next clip does not contain a banner graphic. If you want the size of the window to stay the same (except when the video size changes), use the FIXED value for the **BANNERBAR** attribute.

The space reserved for a banner graphic is 32 pixels high by 194 pixels wide. The reserved space appears below any rendered video content and 6 pixels above the lower edge of the video area, allowing space for the 6-pixel video area border. The reserved banner space is centered horizontally.

Windows Media Player renders the graphic beginning in the leftmost pixel of the banner space. If the graphic fills the entire space, it will appear centered horizontally. Otherwise there will be trailing space. Note that the minimum width of Windows Media Player is always wider than the size of the video clip, regardless of the value of the **BANNERBAR** attribute.

## Examples


```XML
<ASX VERSION="3.0" PREVIEWMODE="YES" BANNERBAR="auto"  >
   <ENTRY HREF="https://sample.microsoft.com/sample1.ASX" />
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

 

 





