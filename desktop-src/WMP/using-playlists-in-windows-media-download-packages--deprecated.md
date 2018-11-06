---
title: Using Playlists in Windows Media Download Packages (deprecated)
description: Using Playlists in Windows Media Download Packages (deprecated)
ms.assetid: c40efe24-aaed-47fc-8a8a-f412dfc36af7
keywords:
- Windows Media metafiles,Windows Media Download packages
- Windows Media Player,Windows Media Download packages
- metafiles,Windows Media Download packages
- Windows Media,Windows Media Download packages
- playlists,Windows Media Download packages
- metafile playlists,Windows Media Download packages
- Windows Media metafile playlists,Windows Media Download packages
- Windows Media Download packages,playlists
- Windows Media Download packages,metafile playlists
- Windows Media Download packages,Windows Media metafile playlists
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Using Playlists in Windows Media Download Packages (deprecated)

This page documents a feature that may be unavailable in future versions of Windows Media Player and the Windows Media Player SDK.

Playlists are Windows Media metafiles with an .asx file name extension that provide information that tells Windows Media Player how to play the packaged content. By combining multiple content files into a single Windows Media Download package, you can control and customize your Windows Media Download package by using the playlist.

> [!Note]  
> In general, metafile playlists are used by Windows Media Download packages to reference the multimedia content in the package rather than a stream from a server on an intranet or the Internet. However, URL references within the .asx file are supported.

 

Using XML, the metafile provides the information Windows Media Player uses to play and display content. Playlists are made up of various XML code elements with their associated tags and attributes. Each element in a Windows Media metafile playlist defines a particular setting or action in Windows Media Player.

The user's computer associates a Windows Media metafile that has an .asx file name extension with Windows Media Player. Windows Media Player opens and parses the XML code in the metafile, which contains the path for locating the packaged audio or video files. The metafile script then controls the audio, video, and graphical experience. The metafile also contains information that Windows Media Player processes and displays in the playlist drop-down box. Immediately after the list is displayed, the first item in the list is played.

A metafile playlist is a shortcut to the files that contain your packaged content. The following code is an example of a metafile that specifies the border to display by using the **SKIN** element, two songs to be played, and the playlist information for each song.


```XML
<ASX Version="3.0">
<AUTHOR>Name of content creator goes here</AUTHOR>
<TITLE>Album Title goes here</TITLE>
<PARAM name="Album" value="Album Title "/>
<PARAM name="Artist" value="Artist Name"/>
<PARAM name="Genre" value="Genre"/>
<SKIN HREF="myborder.wmz"/>
    <ENTRY>
        <REF HREF="song1.wma"/>
        <AUTHOR>Creator's name</AUTHOR>
        <COPYRIGHT>Copyright information</COPYRIGHT>
        <TITLE>Song #1 title</TITLE>
    </ENTRY>
    <ENTRY>
        <REF HREF="song2.wma"/>
        <AUTHOR>Creator's name</AUTHOR>
        <COPYRIGHT>Copyright information</COPYRIGHT>
        <TITLE>Song #2 name</TITLE>
    </ENTRY>
</ASX>

```



## Related topics

<dl> <dt>

[**Borders for Windows Media Player (deprecated)**](borders-for-windows-media-player--deprecated.md)
</dt> <dt>

[**Windows Media Download Packages (deprecated)**](windows-media-download-packages--deprecated.md)
</dt> <dt>

[**Windows Media Metafiles**](windows-media-metafiles.md)
</dt> </dl>

 

 




