---
title: SKIN Element (deprecated)
description: This page documents a feature that may be unavailable in future versions of Windows Media Player and the Windows Media Player SDK.
ms.assetid: 593244c1-f850-46d7-8b84-14dcd59b024e
keywords:
- SKIN Element (deprecated) Windows Media Player
topic_type:
- apiref
api_name:
- SKIN Element (deprecated)
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# SKIN Element (deprecated)

This page documents a feature that may be unavailable in future versions of Windows Media Player and the Windows Media Player SDK.

The **SKIN** element specifies a URL to a border.

``` syntax
<SKIN
   HREF = "URL"
/>
```

## Attributes

**HREF** (required)

URL for a compressed border file with a file name extension .wmz. For Windows Media Player 9 Series or later, this value can reference only border files on the user's hard disk located in the same directory as the metafile playlist. See the example code.

## Parent/Child Elements



| Hierarchy       | Elements |
|-----------------|----------|
| Parent elements | **ASX**  |
| Child elements  | None     |



 

## Remarks

The **SKIN** element is used to create a border, which is similar to a skin but is displayed in the **Now Playing** area of the full mode Windows Media Player. The **SKIN** element is used only for borders, which appear inside the full mode Windows Media Player, and not for regular skins, which entirely replace the compact mode Windows Media Player.

In a Windows Media Download Package (with a .wmd file name extension), the **SKIN** element enables a border to have content and link to other sites. The Windows Media Download Package is a compressed file that contains a border file and a Windows Media metafile. The border file (with a .wmz file name extension) is compressed, and includes a skin definition file (with a .wms file name extension).

A **SKIN** element has three components:

-   A skin
-   Some content
-   A metafile

Skins included with Windows Media Download Packages must be rectangular in shape. Creating borders with skins that are not rectangular may yield unexpected results.

## Examples


```XML
<ASX version = "3.0">
    <TITLE>A Skin Element</TITLE>
    <SKIN HREF = "YourTest.wmz" />

    <ENTRY>
        <PARAM name="YourAlbumTitle" value="YourTitle.jpg"/>
        <PARAM name="link" value="https://www.proseware.com"/>
        <TITLE>(The Artist)-YourTitle</TITLE>
        <REF HREF="(The Artist)-YourSongTitle.wma"/>
    </ENTRY>

</ASX>
```



## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------|
| Version<br/> | Windows Media Player version 70 or later<br/> |



## See also

<dl> <dt>

[**Borders for Windows Media Player (deprecated)**](borders-for-windows-media-player--deprecated.md)
</dt> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> <dt>

[**Windows Media Metafile Reference**](windows-media-metafile-reference.md)
</dt> </dl>

 

 





