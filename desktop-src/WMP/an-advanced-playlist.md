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
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# An Advanced Playlist

The following playlist example shows how to use a more complete set of playlist elements. When writing your own code, you will need to change all URLs and file names to valid file names that are accessible to your Windows Media Player.

Example Code


``` XML
<ASX version = "3.0">
    <TITLE>Advanced Playlist Demo</TITLE>
    <ABSTRACT>More Information at this website</ABSTRACT>
    <MOREINFO HREF="https://www.microsoft.com/windows/windowsmedia" />
    <BANNER HREF = "..\samples\home.gif">
        <ABSTRACT>MSN website</ABSTRACT>
        <MOREINFO HREF = "https://www.msn.com" />
    </BANNER>
    <PARAM name="track" value="1"/>
    <ENTRY ClientSkip="no">
        <BANNER HREF = "..\sample\contact.gif">
            <ABSTRACT>Visit Our website</ABSTRACT>
            <MOREINFO HREF = "https://www.msn.com" />
        </BANNER>
        <MOREINFO HREF = "https://www.msn.com" />
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
| `<ASX version = "3.0">`                                                                     | The [ASX](asx-element.md) element identifies for the client (Windows Media Player) that this is a Windows Media metafile playlist. The **version** attribute specifies the version number of the metafile elements.                                                                                                                    |
| `<TITLE>Advanced Playlist Demo</TITLE>`                                               | The [TITLE](title-element--metafile.md) element identifies the title of the playlist as a whole. Windows Media Player displays this metadata as the show title.                                                                                                                                                                        |
| `<ABSTRACT>More Information at this Web Site< /ABSTRACT>`                             | The [ABSTRACT](abstract-element.md) element provides the ToolTip for the show title.                                                                                                                                                                                                                                                   |
| `<MOREINFO HREF ="https://www.microsoft.com/windows/windowsmedia" />`                        | The [MOREINFO](moreinfo-element.md) element links the show title to an URL. Pausing the mouse pointer over the show title accesses the ToolTip, if defined. Selecting the show title will then open the designated URL.                                                                                                                |
| `<BANNER HREF = "..\\samples\\home.gif">`                                                   | The [BANNER](banner-element.md) element creates an advertising banner in Windows Media Player. The **HREF** attribute specifies the banner graphic (which must be 194 pixels wide by 32 pixels tall).                                                                                                                                  |
| `<ABSTRACT>MSN website</ABSTRACT>`                                                    | The [ABSTRACT](abstract-element.md) element provides the ToolTip for the **BANNER**.                                                                                                                                                                                                                                                   |
| `<MOREINFO HREF = "https://www.msn.com" </ABSTRACT>`                                      | The [MOREINFO](moreinfo-element.md) element links the **BANNER** graphic to a URL. Holding the mouse pointer over the **BANNER** accesses a ToolTip, if defined. Selecting the **BANNER** will open the designated URL.                                                                                                                |
| \<PARAM name = "track" value="1"/>                                                         | The [PARAM](param-element.md) element defines a custom parameter. The **name** attribute defines the name of the custom parameter as "track". The **value** attribute defines the value of "track" to be "1".                                                                                                                          |
| `</BANNER>`                                                                                 | Closes the **BANNER** element                                                                                                                                                                                                                                                                                                           |
| `<ENTRY ClientSkip="no">`                                                                   | Begins the [ENTRY](entry-element.md) element block. This element defines a clip in a playlist by specifying a link in the **REF** element. Setting **ClientSkip** to "no" means that the user cannot fast forward or jump to the next clip                                                                                             |
| `<BANNER HREF = "..\\samples\\contact.gif">`                                                | Creates an advertising banner. The **HREF** is the banner graphic (194x32 pixels).                                                                                                                                                                                                                                                      |
| `<ABSTRACT>Visit Our website< /ABSTRACT>`                                             | Provides the ToolTip for the banner.                                                                                                                                                                                                                                                                                                    |
| `<MOREINFO HREF = "https://www.msn.com" />`                                                  | Provides a link to the URL for the banner. Selecting the banner connects to the URL.                                                                                                                                                                                                                                                    |
| `</BANNER>`                                                                                 | Closes the **BANNER** element                                                                                                                                                                                                                                                                                                           |
| `<MOREINFO HREF = "https://www.msn.com" />`                                                  | Provides a link to the URL for the clip **Title** text.                                                                                                                                                                                                                                                                                 |
| `<!--This is the ToolTip text for the Title text -->`                                       | A comment. [Comments](comments.md) are only be visible when the code is viewed.                                                                                                                                                                                                                                                        |
| `<Abstract>Visit the YourImage website</abstract>`                                    | Provides the ToolTip for the clip **Title** text.                                                                                                                                                                                                                                                                                       |
| `<TITLE>The first entry in an advanced playlist</TITLE>`                              | Identifies the title of the clip. It is the clip **TITLE** because it is nested within an **ENTRY** element. Windows Media Player displays this metadata as the clip title.                                                                                                                                                             |
| `<AUTHOR>YourImage</AUTHOR>`                                                          | Identifies the author of the media clip. This metadata is displayed as the clip **AUTHOR** by Windows Media Player.                                                                                                                                                                                                                     |
| `<COPYRIGHT>(c)2000 YourImage</COPYRIGHT>`                                            | The [COPYRIGHT](copyright-element.md) element specifies the copyrights associated with the media clip. Windows Media Player displays this metadata as the clip COPYRIGHT.                                                                                                                                                              |
| `<!-- This is a comment. Change the following path to point to your Windows Media file -->` | A comment, in the same format as **XML** comments.                                                                                                                                                                                                                                                                                      |
| `<REF HREF = "..\\media\\laure.wma" />`                                                     | URL for the media content. The [REF](ref-element.md) element identifies the line as a pointer to media content. The **HREF** attribute is the URL to the file.Note the use of the XML-like closing of the element , "/>" instead of "&lt;/REF&gt;". Because this element does not have child elements, it closes itself.<br/> |
| `</ENTRY>`                                                                                  | Specifies the end of the of the first **ENTRY** element.                                                                                                                                                                                                                                                                                |
| `<ENTRY>`                                                                                   | Begins the second **ENTRY** element.                                                                                                                                                                                                                                                                                                    |
| `<TITLE>The second Entry in the advanced playlist</TITLE>`                            | Identifies the title of the second clip.                                                                                                                                                                                                                                                                                                |
| `<AUTHOR>Microsoft Corporation</AUTHOR>`                                              | Identifies the author of the second media clip.                                                                                                                                                                                                                                                                                         |
| `<!--This is the ToolTip text for the Title/Author/Copyright text -->`                      | A comment. It will only be visible when the code is viewed.                                                                                                                                                                                                                                                                             |
| `<ABSTRACT>This is where you can include your tool tips</ABSTRACT>`                   | This is the ToolTip text for the **TITLE** text of the clip.                                                                                                                                                                                                                                                                            |
| `<!-- This is a comment. Change the following path to point to your Windows Media file -->` | A comment. It will only be visible when the code is viewed.                                                                                                                                                                                                                                                                             |
| `<REF HREF = ..\\media\\mellow.wma" />`                                                     | Identifies the line as a pointer to media content. The **HREF** attribute is the URL to the file.                                                                                                                                                                                                                                       |
| `</ENTRY>`                                                                                  | Specifies the end of the second **ENTRY** element.                                                                                                                                                                                                                                                                                      |
| `</ASX>`                                                                                    | Specifies the end of the playlist.                                                                                                                                                                                                                                                                                                      |



 

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

 

 





