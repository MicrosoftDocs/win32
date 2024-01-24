---
title: MOREINFO Element
description: The MOREINFO element specifies a URL to a website, email address, or script command associated with a show, clip, or banner.
ms.assetid: b817ef1d-4ca0-45f4-942b-695eaf537110
keywords:
- MOREINFO Element Windows Media Player
topic_type:
- apiref
api_name:
- MOREINFO Element
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# MOREINFO Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **MOREINFO** element specifies a URL to a website, email address, or script command associated with a show, clip, or banner.

``` syntax
<MOREINFO
   HREF = "URL"
   TARGET = "Frame"
/>
```

## Attributes

**HREF** (required)

URL to a website, email address, or script command.

**TARGET**

Value defining the frame or window in which the browser will open the page defined by the **HREF** attribute.

This can be a string containing a window name, or one of the following values.



| Value    | Description                                                                                                              |
|----------|--------------------------------------------------------------------------------------------------------------------------|
| \_blank  | The document loads in a new browser window.                                                                              |
| \_self   | The document loads in the same frame as the current document containing the Windows Media Player control.                |
| \_parent | The document loads in the immediate parent frame of the current frame, or the current frame if there is no parent frame. |
| \_top    | The document loads in the full browser window, replacing all other frames or documents.                                  |



 

## Parent/Child Elements



| Hierarchy       | Elements                       |
|-----------------|--------------------------------|
| Parent elements | **ASX**, **ENTRY**, **BANNER** |
| Child elements  | None                           |



 

## Remarks

This element specifies a URL to a website, email address, **or script command. The user can access the target of the URL by clicking on the graphic or text associated with the MOREINFO** element. The details depend on the parent element of the **MOREINFO** element:

-   If the **MOREINFO** element is the child of an **ASX** element, the user can access the URL by clicking the show title.
-   If the **MOREINFO** element is the child of an **ENTRY** element, the user can access the URL by clicking the clip title.
-   If the **MOREINFO** element is the child of a **BANNER** element, the user can access the URL by clicking the banner graphic.

If the **HREF** attribute specifies a URL to a website, the browser opens and navigates to the URL. If the **HREF** attribute specifies an email address, the user's email application starts. If the **HREF** attribute specifies a script command, the script command executes in the browser.

**Note**

If the **MOREINFO** element appears within an **ASX** or **ENTRY** element, when the mouse cursor is held over the title of the show (for an **ASX** element) or clip (for an **ENTRY** element), the URL defined in the **HREF** attribute can be selected and accessed by Windows Media Player.

The **TARGET** attribute defines the frame or window in which the browser will open the page defined by the **HREF** attribute. The values for this attribute follow standard HTML syntax and definitions. In the case of a control embedded in a webpage, if no **TARGET** attribute is defined, the URL loads the current browser window and replaces the existing page, which means the content stops playing. Therefore, it is recommended that you always specify a **TARGET** attribute when embedding the Windows Media Player control in a webpage.

If the metafile is opened in the stand-alone Windows Media Player, the **TARGET** attribute is ignored, and the URL loads in an existing browser window. If there is no browser window currently open, the URL loads in a new browser window.

## Examples


```XML
<ASX VERSION="3.0">

   <TITLE>Example Media Player Show</TITLE>
   <MOREINFO HREF="https://example.microsoft.com/info/show_info.htm" />
   
   <ENTRY>
      <TITLE>Example Clip</TITLE>
      <MOREINFO HREF="https://example.microsoft.com/info/clip1_info.htm" />
      <REF HREF="mms://example.microsoft.com/media.asf" />
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

 

 





