---
title: Using Relative Links in Metafiles
description: Using Relative Links in Metafiles
ms.assetid: 8f6c40fc-e025-43d5-a43a-c162f28bbd71
keywords:
- Windows Media metafile playlists,relative links
- playlists,relative links
- metafile playlists,relative links
- metafiles,relative links
- Windows Media metafiles,relative links
- relative links
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Using Relative Links in Metafiles

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Relative links are a fully supported feature of Windows Media metafiles. You can use relative links in metafiles much like you use them in HTML documents. The use of relative links enables you to create metafiles that are portable, meaning you can copy or move an entire directory structure to another server without updating the paths to graphic files used as banners or the **HREF** attributes of **MOREINFO** elements (if they reference files on the same web server as the stored metafile). Relative links work, in any application that supports them, because the parts of the URL not included in the **HREF** attribute of an element are included in the URL sent by the application to the server when that URL is requested. This means that the protocol (such as https://), the server name, and the virtual directory in which the file containing the relative link is located are all included in the URL that is sent to the server. If the media file, or URL you link to using a relative link does not reside on the same server as the metafile, the relative link is not valid.

> [!Note]  
> This information on relative links is correct only when using a link to metafiles that are opened in the stand-alone Windows Media Player. When you use the embedded Windows Media Player control, all links are relative to the page on which the control is hosted, unless the **BASE** child element of the **ASX** element is used to redirect the relative path.

 

All relative links in the metafile must be fully relative, not drive-relative, for streaming media. When a URL begins with a "\\" character, the link is drive-relative. Windows Media Player attempts to open the file linked to on the drive where the metafile was opened from, usually a web server. Because web servers use virtual directories, Windows Media Player tries to find the specified stream or media file in a subdirectory of a virtual directory on the web server where the metafile was opened from. A user would not have access to a server directory. The example in this section illustrates the use of a fully relative link.

You can use drive-relative links when using metafiles on a single computer where all media files linked to in the metafile playlist exist on a storage device in that computer. However, you cannot stream media in this manner.

When you use a link to another metafile to allow for relative links, the name displayed as the Title by Windows Media Player is the Title in the original metafile.

Relative links cannot be used for URLs to a streaming media server because different protocols are used for accessing streaming media content.

In the following example playlist, the first **ENTRYREF** contains a URL for another playlist, relative.wax.


```XML
<ASX>
    <ENTRYREF HREF="https://example.microsoft.com/metafiles/relative.wax"/>
</ASX>

```



The following example is the file relative.wax, which contains relative links.


```XML
<ASX version = "3.0">
    <BANNER HREF = "graphics/logo1.jpg">
        <MOREINFO HREF = "category1/category1.htm" />
    </BANNER>
    <ENTRY>
        <REF HREF = "mms://samples.microsoft.com/myfile.wma" />
    </ENTRY>
</ASX>

```



The URL containing the reference to the playlist, relative.wax, can exist in a metafile playlist anywhere that is accessible to the user. For the URL to be processed successfully, there must be a web server named "example.microsoft.com". That web server must have a virtual directory defined as "metafiles". The referenced playlist, relative.wax, must exist on the web server named "example.microsoft.com" in the virtual directory "metafiles".

For the referenced media files in the playlist relative.wax to be successfully accessed and played, there must be a directory named "Graphics" which is a subdirectory of the server's virtual directory "metafiles". The graphics file Logo1.jpg, referenced in the **BANNER** element, must be the subdirectory named Graphics.

Similarly a document named Category1.htm must reside in a subdirectory named Category1. The directory named Category1 must exist as a subdirectory of the virtual directory "metafiles" on the web server example.microsoft.com.

## Related topics

<dl> <dt>

[**Creating Metafile Playlists**](creating-metafile-playlists.md)
</dt> <dt>

[**Metafile Playlists**](metafile-playlists.md)
</dt> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> <dt>

[**Windows Media Metafile Guide**](windows-media-metafile-guide.md)
</dt> </dl>

 

 




