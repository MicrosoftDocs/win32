---
title: Accessing Media
description: Accessing Media
ms.assetid: 18ea844d-98c9-4168-9af2-161dda52f6bd
keywords:
- Windows Media metafile playlists,accessing media
- playlists,accessing media
- metafile playlists,accessing media
- Windows Media metafile playlists,media access
- playlists,media access
- metafile playlists,media access
- Windows Media metafile playlists,controlling playback
- playlists,controlling playback
- metafile playlists,controlling playback
- Windows Media metafile playlists,setting duration
- playlists,setting duration
- metafile playlists,setting duration
- Windows Media Player,accessing media
- Windows Media Player,media access
- Windows Media Player,controlling playback
- Windows Media Player,setting duration
- accessing media
- media access
- controlling playback
- setting duration
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Accessing Media

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Use playlists to specify and to control the streaming media or media files that Windows Media Player plays.

Use the **ENTRY** element to specify a single media element (a media file or a live stream) and any child elements (such as images, **MOREINFO** links, and **ABSTRACT** text). Use an **ENTRYREF** element to specify a playlist. A playlist can contain one or more **ENTRY** or **ENTRYREF** elements. Windows Media Player executes a playlist by starting with the first entry and then playing each entry in turn until the list is finished.

An **ENTRY** element can point to any type of media that Windows Media Player can play. This includes not only .wma, .wmv, .asf, and .avi files, to name a few, but live streams as well. By using a series of **ENTRY** or **ENTRYREF** elements to reference media content, you can use a playlist to send a single stream that consists of multiple sources. The referenced streams will play sequentially and be seen as one continuous stream by the viewer. For example, the playlist can contain two **ENTRY** elements: a standard introduction from a Windows Media file with a .wma extension, and a live Windows Media stream.

> [!Note]  
> A playlist must not contain links to media files that have content created with different versions of Digital Rights Management (DRM). In a metafile playlist, if there are links for media files with DRM version 1 content and for media files created with later DRM versions, Windows Media Player will only play the DRM version 1 content.

 

## Controlling Playback

Use playlists to control not only which media clip is played, but also which portions of the clip are played and how. You can use playlists to define a set of clips to be looped or repeated, to set the duration of play, and to assign start times, and start and end markers for each entry. The **STARTTIME**, **STARTMARKER**, and **ENDMARKER** elements work in conjunction with markers in the media file.

For example, the following playlist uses an ad banner and the associated **MOREINFO** link in one **ENTRY**, and references a **STARTMARKER** and **ENDMARKER**.


```XML
<ASX version ="3.0">
<Title>Windows Media Example</Title>
<Abstract>Windows Media Technologies</Abstract>
<MoreInfo href = "https://www.proseware.com"/>
    <!--This is the first Entry -->
    <Entry>
        <Title>This is the ad</Title>
        <Author>Ad Department</Author>
        <Copyright>2000</Copyright>
        <Abstract>This is a description of the ad.</Abstract>
        <MoreInfo href = "https://www.proseware.com/"/>
        <Ref href="ad.wma"/>
        <Banner href ="purchase.gif">
           <Abstract>Click here to go to our website.</Abstract>
           <MoreInfo href = "https://www.litwareinc.com/" />
        </Banner>
     </Entry>        
    <!-- This is the second Entry -->
    <!-- The Windows Media file plays from Segment2 to Segment3 -->
    <Entry>
        <Title>Playlist Clip Number Two</Title>
        <Author>Windows Media</Author>
        <Copyright>2000</Copyright>
        <Ref href="show.wma"/>
        <StartMarker Name = "Segment2" />
        <EndMarker Name = "Segment3" />
    </Entry>
</ASX>

```



## Setting Duration

Use the **DURATION** element to specify how long to play a clip or set of clips. You can also use the **PREVIEWMODE** attribute of the **ASX** element in conjunction with the **PREVIEWDURATION** element to specify how long to play a clip or set of clips. Set the **PREVIEWMODE** attribute to YES to use the **PREVIEWDURATION** element to specify how long to play the associated clip. The **PREVIEWDURATION** and **DURATION** elements have the same behavior.

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

 

 




