---
title: Creating an HTMLView Presentation
description: Creating an HTMLView Presentation
ms.assetid: 70203160-2dd9-4096-be6a-c704db757f7f
keywords:
- Windows Media metafile playlists,HTMLView presentations
- playlists,HTMLView presentations
- metafile playlists,HTMLView presentations
- Windows Media metafile playlists,creating HTMLView presentations
- playlists,creating HTMLView presentations
- metafile playlists,creating HTMLView presentations
- creating HTMLView presentations
- Windows Media Player,creating HTMLView presentations
- Windows Media Player,HTMLView presentations
- HTMLView,creating presentations
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Creating an HTMLView Presentation

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To create a basic HTMLView presentation, you need at least three elements:

-   **Digital media content.** This is one or more audio or video files that Windows Media Player plays.
-   **A webpage.** This is the Web-based content that displays in the **Now Playing** feature of the Player UI.
-   **A Windows Media metafile.** This is the metafile playlist that directs Windows Media Player to combine the digital media content with the webpage.

An .asx file is a text file that provides information about a file stream and its presentation. Based on Extensible Markup Language (XML) syntax, .asx files can contain a variety of elements, each identified by a tag with associated attributes. The **PARAM** element provides a way to associate a custom parameter with either a particular entry in a metafile playlist or the entire metafile. One of the predefined parameter names available for your use is "HTMLView". This is the parameter that causes the webpage specified by the URL value to be displayed in Windows Media Player.

The following example code shows an .asx file that combines a single digital media file with a single webpage:


```XML
<ASX version="3.0">
<PARAM name="HTMLView" value="https://www.proseware.com/htmlview.htm"/>

<ENTRY>
   <REF href="rtsp://www.proseware.com/content1.wma"/>
</ENTRY>

</ASX>

```



When Windows Media Player opens the .asx file in the preceding example, it plays the audio from the file named content1.wma and opens the webpage named htmlview.htm in the **Now Playing** feature of the full-mode Player. The user can pause, seek, and stop the audio content using the Windows Media Player controls.

You can easily change the webpage that is displayed for each piece of content by associating a **PARAM** element with each entry, as the following code example shows:


```XML
<ASX version="3.0">

<ENTRY>
   <PARAM name="HTMLView" value="https://www.proseware.com/htmlview1.htm"/>
   <REF href="rtsp://www.proseware.com/content1.wma"/>
</ENTRY>

<ENTRY>
   <PARAM name="HTMLView" value="https://www.proseware.com/htmlview2.htm"/>
   <REF href="rtsp://www.proseware.com/content2.wma"/>
</ENTRY>

</ASX>

```



In the preceding example, Windows Media Player first displays the webpage htmlview1.htm while playing the digital audio file content1.wma. When the Player opens the next entry in the playlist, content2.wma, the webpage displayed in **Now Playing** changes to htmlview2.htm. In this way, you can specify which webpage the user sees for each piece of digital media content.

## Related topics

<dl> <dt>

[**Displaying Web Pages in Windows Media Player**](displaying-web-pages-in-windows-media-player.md)
</dt> <dt>

[**PARAM Element**](param-element.md)
</dt> </dl>

 

 




