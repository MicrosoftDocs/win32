---
title: Modifying the Display
description: Modifying the Display
ms.assetid: 21d68a34-d3d8-4b5b-b8fe-0489dc6247ec
keywords:
- Windows Media metafile playlists,modifying displays
- playlists,modifying displays
- metafile playlists,modifying displays
- Windows Media metafile playlists,display modification
- playlists,display modification
- metafile playlists,display modification
- Windows Media Player,display modification
- Windows Media Player,modifying displays
- Windows Media Player,text properties
- Windows Media Player,image properties
- Windows Media Player,MOREINFO properties
- Windows Media Player,ABSTRACT text
- MOREINFO properties
- ABSTRACT text
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Modifying the Display

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Playlists can alter the Windows Media Player user interface in four main ways:

-   Text properties
-   Image properties
-   MOREINFO properties
-   ABSTRACT text

## Text properties

Windows Media Player enables the display of Title, Author, Copyright, and Description metadata text. Clip metadata can come from the stream or media file, or it can come from a playlist. Show metadata comes from the playlist. In general, playlists are a better method of passing text properties to Windows Media Player, especially if text elements are likely to change. It is easier to edit text in a playlist than to re-author a media file. And because properties read from a playlist override those contained in the media file, you can easily update display text by adding the new text to the corresponding property in a playlist. In the following example, the text of the Title and Author metadata in the playlist overrides the Title and Author text contained in the media file, sample.wma.

**DESCRIPTION** text is retrieved from a Windows Media file referenced in an **ENTRY** element unless there is an **ABSTRACT** element in a metafile playlist. If there is **ABSTRACT** text, it will be displayed, overriding the **DESCRIPTION** text.


```XML
<ASX version="3.0" BANNERBAR="AUTO" >
    <ENTRY>
        <BANNER HREF="YourPath\2.gif">
        </BANNER>
        <TITLE>Upgrade</TITLE>
        <AUTHOR>Ad Department</AUTHOR>
        <REF href="YourPath\sample.wma"/>
    </ENTRY>
</ASX>

```



## Image properties

Banner images can be added to the user interface of Windows Media Player. The graphic can be used for advertising, providing information, and providing access to websites, to name a few possibilities.

Use the **BANNER** element to specify a graphic image (32 pixels high by 194 pixels wide) for display by Windows Media Player. The graphic is displayed below any video content. A hyperlink can be added to the banner using the **MOREINFO** child element.

A ToolTip can be defined by an **ABSTRACT** element within the scope of the **BANNER** element. Any defined ToolTip text can be displayed by pausing the mouse pointer over the banner graphic. Selecting the banner graphic with the mouse pointer will activate any hyperlink defined with the **MOREINFO** element.

The preferred **BANNER** graphics format is the GIF format. The JPG format can be used if the graphic is properly sized.

The previous example illustrates use of the **BANNER** element.

> [!Note]  
> **BANNER** images are not supported with DRM files or when Windows Media Player is embedded in a webpage.

 

For more information about banners, see [Custom Graphics in Windows Media Player](custom-graphics-in-windows-media-player.md).

## MOREINFO properties

Text and image areas of the user interface can be associated with URLs. During playback, users can select one of these sections to connect to the URL associated with it in their Web browser. For example, you can associate an advertiser's website with an ad banner image as shown in the following code snippet.


```XML
<BANNER HREF="YourPath\2.gif">
    <ABSTRACT>More Information.</ABSTRACT>
    <MOREINFO HREF="https://www.proseware.com" />
</BANNER>

```



## ABSTRACT text

**ABSTRACT** text is used to display a short pop-up description of the text or image areas of the user interface it is associated with. During playback, if the mouse pointer hovers over one of these areas, a ToolTip appears beside the mouse pointer displaying the **ABSTRACT** text associated with the area. **ABSTRACT** text is retrieved from a metafile and is defined with the **ABSTRACT** element. The **ABSTRACT** element can be a child element of either an **ENTRY** or a **BANNER** element.

## Related topics

<dl> <dt>

[**Metafile Playlists**](metafile-playlists.md)
</dt> <dt>

[**Using Metafile Playlists**](using-metafile-playlists.md)
</dt> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> <dt>

[**Windows Media Metafile Guide**](windows-media-metafile-guide.md)
</dt> </dl>

 

 




