---
title: BANNER Element
description: The BANNER element defines a URL to a graphic file that will appear in the display panel.
ms.assetid: 8b4a3369-a687-40a8-b5df-afb0e0518cd1
keywords:
- BANNER Element Windows Media Player
topic_type:
- apiref
api_name:
- BANNER Element
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# BANNER Element

The **BANNER** element defines a URL to a graphic file that will appear in the display panel.

``` syntax
<BANNER
   HREF = "URL"
>
</BANNER>
```

## Attributes

**HREF** (required)

URL to a graphic file that is displayed in the display panel.

## Parent/Child Elements



| Hierarchy       | Elements                   |
|-----------------|----------------------------|
| Parent elements | **ASX**, **ENTRY**         |
| Child elements  | **ABSTRACT**, **MOREINFO** |



 

## Remarks

This element defines a URL to a graphic file that appears in the Windows Media Player display panel, beneath the video content. If the media is audio only, the banner graphic is displayed by itself. Windows Media Player reserves a space 32 pixels high by 194 pixels wide (the banner bar) for the graphic. If the graphic defined in the URL is smaller than that, it displays at its original size. If the graphic is larger than the reserved space, Windows Media Player will crop the image to fit the space.

You can use an **ABSTRACT** element within the scope of the **BANNER** element to display text as a ToolTip when the user pauses the mouse pointer over the banner graphic. A **MOREINFO** element within a **BANNER** element defines a URL to which the user is taken when the user clicks the banner graphic. (The URL can be any path or protocol, such as an email link, a Hypertext Transfer Protocol (HTTP) URL to a website, or even a Microsoft JScript command.) When the pointer is moved over the graphic, the graphic becomes embossed and looks like a button.

A **BANNER** element defined for an **ASX** element displays while all clips in the playlist are playing. A **BANNER** element defined in an **ENTRY** element displays only while that clip is playing, and during that time overrides any banner defined within the parent **ASX** element. You can specify how Windows Media Player reserves space for the banner by setting the **BANNERBAR** attribute of the **ASX** element.

Banner images are not supported with DRM files or when Windows Media Player is embedded in a webpage.

## Examples

The following is an example of a **BANNER** element without child elements:


```XML
<BANNER HREF="https://sample.microsoft.com/art/banner1.bmp" />
```



The following is an example of a **BANNER** element containing **ABSTRACT** and **MOREINFO** elements.


```XML
<BANNER HREF="https://www.proseware.com/logos/banner1.bmp">
    <ABSTRACT>Click here to go to our website.</ABSTRACT>
    <MOREINFO HREF="https://sample.microsoft.com" />
    <!-- The text in the Abstract element displays as a 
         ToolTip when the mouse hovers over the banner 
         graphic. When a user clicks the banner, the URL 
         given in the MoreInfo element opens in the 
         browser. -->
</BANNER>
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

 

 





