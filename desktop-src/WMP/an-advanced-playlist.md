---
title: An Advanced Playlist
description: An Advanced Playlist
ms.assetid: 3f27562f-bc3b-4b7f-a83b-78317d3ad612
keywords:
- Windows Media metafile playlists,playlist examples
- playlists,playlist examples
- metafile playlists,playlist examples
- Windows Media metafile playlists,example playlists
- playlists,example playlists
- metafile playlists,example playlists
- Windows Media metafile playlists,sample playlists
- playlists,sample playlists
- metafile playlists,sample playlists
- Windows Media metafile playlists,code example
- playlists,code example
- metafile playlists,code example
- Windows Media metafile playlists,advanced playlist example
- playlists,advanced playlist example
- metafile playlists,advanced playlist example
- Windows Media Player,playlist examples
- Windows Media Player,example playlists
- Windows Media Player,sample playlists
- Windows Media Player,advanced playlist example
- playlist examples
- example playlists
- sample playlists
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# An Advanced Playlist

The following playlist example shows how to use a more complete set of playlist elements. When writing your own code, you will need to change all URLs and file names to valid file names that are accessible to your Windows Media Player.

Example Code


```XML
<ASX version = "3.0">
    <TITLE>Advanced Playlist Demo</TITLE>
    <ABSTRACT>More Information at this website</ABSTRACT>
    <MOREINFO HREF="http://www.microsoft.com/windows/windowsmedia" />
    <BANNER HREF = "..\samples\home.gif">
        <ABSTRACT>MSN website</ABSTRACT>
        <MOREINFO HREF = "http://www.msn.com" />
    </BANNER>
    <PARAM name="track" value="1"/>
    <ENTRY ClientSkip="no">
        <BANNER HREF = "..\sample\contact.gif">
            <ABSTRACT>Visit Our website</ABSTRACT>
            <MOREINFO HREF = "http://www.msn.com" />
        </BANNER>
        <MOREINFO HREF = "http://www.msn.com" />
        <!-- This is the ToolTip text for Title/Author/Copyright text -->
        <ABSTRACT>Visit the YourImage website</ABSTRACT>
        <TITLE>The first entry in an advanced playlist</TITLE>
        <AUTHOR>YourImage</AUTHOR>
        <COPYRIGHT>(c)2000 YourImage</COPYRIGHT>
        <!-- This is a comment.  Change the following path to point to 
            your Windows Media file -->
         <REF HREF = "..\media\laure.wma" />
    </ENTRY>

    <ENTRY>
        <TITLE>The second entry in the advanced playlist</TITLE>
        <AUTHOR>Microsoft Corporation</AUTHOR>
        <COPYRIGHT>(c)2000 Microsoft Corporation</COPYRIGHT>
        <!-- This is the ToolTip text for Title text -->
        <ABSTRACT>This is where you can include your tool tips</ABSTRACT>
        <!-- This is a comment.  Change the following path to point to 
            your Windows Media file -->
        <REF HREF = "..\media\mellow.wma" />
    </ENTRY>
</ASX>

```



The following table describes the preceding advanced playlist.



| Line                                                                                            | Description                                                                                                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| &lt;ASX version = "3.0"&gt;                                                                     | The [ASX](asx-element.md) element identifies for the client (Windows Media Player) that this is a Windows Media metafile playlist. The **version** attribute specifies the version number of the metafile elements.                                                                                                                    |
| &lt;TITLE&gt;Advanced Playlist Demo&lt;/TITLE&gt;                                               | The [TITLE](title-element--metafile.md) element identifies the title of the playlist as a whole. Windows Media Player displays this metadata as the show title.                                                                                                                                                                        |
| &lt;ABSTRACT&gt;More Information at this Web Site&lt; /ABSTRACT&gt;                             | The [ABSTRACT](abstract-element.md) element provides the ToolTip for the show title.                                                                                                                                                                                                                                                   |
| &lt;MOREINFO HREF ="http://www.microsoft.com/windows/windowsmedia" /&gt;                        | The [MOREINFO](moreinfo-element.md) element links the show title to an URL. Pausing the mouse pointer over the show title accesses the ToolTip, if defined. Selecting the show title will then open the designated URL.                                                                                                                |
| &lt;BANNER HREF = "..\\samples\\home.gif"&gt;                                                   | The [BANNER](banner-element.md) element creates an advertising banner in Windows Media Player. The **HREF** attribute specifies the banner graphic (which must be 194 pixels wide by 32 pixels tall).                                                                                                                                  |
| &lt;ABSTRACT&gt;MSN website&lt;/ABSTRACT&gt;                                                    | The [ABSTRACT](abstract-element.md) element provides the ToolTip for the **BANNER**.                                                                                                                                                                                                                                                   |
| &lt;MOREINFO HREF = "http://www.msn.com" &lt;/ABSTRACT&gt;                                      | The [MOREINFO](moreinfo-element.md) element links the **BANNER** graphic to a URL. Holding the mouse pointer over the **BANNER** accesses a ToolTip, if defined. Selecting the **BANNER** will open the designated URL.                                                                                                                |
| &lt;PARAM name = "track" value="1"/&gt;                                                         | The [PARAM](param-element.md) element defines a custom parameter. The **name** attribute defines the name of the custom parameter as "track". The **value** attribute defines the value of "track" to be "1".                                                                                                                          |
| &lt;/BANNER&gt;                                                                                 | Closes the **BANNER** element                                                                                                                                                                                                                                                                                                           |
| &lt;ENTRY ClientSkip="no"&gt;                                                                   | Begins the [ENTRY](entry-element.md) element block. This element defines a clip in a playlist by specifying a link in the **REF** element. Setting **ClientSkip** to "no" means that the user cannot fast forward or jump to the next clip                                                                                             |
| &lt;BANNER HREF = "..\\samples\\contact.gif"&gt;                                                | Creates an advertising banner. The **HREF** is the banner graphic (194x32 pixels).                                                                                                                                                                                                                                                      |
| &lt;ABSTRACT&gt;Visit Our website&lt; /ABSTRACT&gt;                                             | Provides the ToolTip for the banner.                                                                                                                                                                                                                                                                                                    |
| &lt;MOREINFO HREF = "http://www.msn.com" /&gt;                                                  | Provides a link to the URL for the banner. Selecting the banner connects to the URL.                                                                                                                                                                                                                                                    |
| &lt;/BANNER&gt;                                                                                 | Closes the **BANNER** element                                                                                                                                                                                                                                                                                                           |
| &lt;MOREINFO HREF = "http://www.msn.com" /&gt;                                                  | Provides a link to the URL for the clip **Title** text.                                                                                                                                                                                                                                                                                 |
| &lt;!--This is the ToolTip text for the Title text --&gt;                                       | A comment. [Comments](comments.md) are only be visible when the code is viewed.                                                                                                                                                                                                                                                        |
| &lt;Abstract&gt;Visit the YourImage website&lt;/abstract&gt;                                    | Provides the ToolTip for the clip **Title** text.                                                                                                                                                                                                                                                                                       |
| &lt;TITLE&gt;The first entry in an advanced playlist&lt;/TITLE&gt;                              | Identifies the title of the clip. It is the clip **TITLE** because it is nested within an **ENTRY** element. Windows Media Player displays this metadata as the clip title.                                                                                                                                                             |
| &lt;AUTHOR&gt;YourImage&lt;/AUTHOR&gt;                                                          | Identifies the author of the media clip. This metadata is displayed as the clip **AUTHOR** by Windows Media Player.                                                                                                                                                                                                                     |
| &lt;COPYRIGHT&gt;(c)2000 YourImage&lt;/COPYRIGHT&gt;                                            | The [COPYRIGHT](copyright-element.md) element specifies the copyrights associated with the media clip. Windows Media Player displays this metadata as the clip COPYRIGHT.                                                                                                                                                              |
| &lt;!-- This is a comment. Change the following path to point to your Windows Media file --&gt; | A comment, in the same format as **XML** comments.                                                                                                                                                                                                                                                                                      |
| &lt;REF HREF = "..\\media\\laure.wma" /&gt;                                                     | URL for the media content. The [REF](ref-element.md) element identifies the line as a pointer to media content. The **HREF** attribute is the URL to the file.Note the use of the XML-like closing of the element , "/&gt;" instead of "&lt;/REF&gt;". Because this element does not have child elements, it closes itself.<br/> |
| &lt;/ENTRY&gt;                                                                                  | Specifies the end of the of the first **ENTRY** element.                                                                                                                                                                                                                                                                                |
| &lt;ENTRY&gt;                                                                                   | Begins the second **ENTRY** element.                                                                                                                                                                                                                                                                                                    |
| &lt;TITLE&gt;The second Entry in the advanced playlist&lt;/TITLE&gt;                            | Identifies the title of the second clip.                                                                                                                                                                                                                                                                                                |
| &lt;AUTHOR&gt;Microsoft Corporation&lt;/AUTHOR&gt;                                              | Identifies the author of the second media clip.                                                                                                                                                                                                                                                                                         |

| &lt;!--This is the ToolTip text for the Title/Author/Copyright text --&gt;                      | A comment. It will only be visible when the code is viewed.                                                                                                                                                                                                                                                                             |
| &lt;ABSTRACT&gt;This is where you can include your tool tips&lt;/ABSTRACT&gt;                   | This is the ToolTip text for the **TITLE** text of the clip.                                                                                                                                                                                                                                                                            |
| &lt;!-- This is a comment. Change the following path to point to your Windows Media file --&gt; | A comment. It will only be visible when the code is viewed.                                                                                                                                                                                                                                                                             |
| &lt;REF HREF = ..\\media\\mellow.wma" /&gt;                                                     | Identifies the line as a pointer to media content. The **HREF** attribute is the URL to the file.                                                                                                                                                                                                                                       |
| &lt;/ENTRY&gt;                                                                                  | Specifies the end of the second **ENTRY** element.                                                                                                                                                                                                                                                                                      |
| &lt;/ASX&gt;                                                                                    | Specifies the end of the playlist.                                                                                                                                                                                                                                                                                                      |



 

## Related topics

<dl> <dt>

[**Creating Metafile Playlists**](creating-metafile-playlists.md)
</dt> <dt>

[**Example Playlists**](example-playlists.md)
</dt> <dt>

[**Metafile Playlists**](metafile-playlists.md)
</dt> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> <dt>

[**Windows Media Metafile Guide**](windows-media-metafile-guide.md)
</dt> </dl>

 

 





