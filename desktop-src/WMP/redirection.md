---
title: Redirection
description: Redirection
ms.assetid: c8e3b43f-c11a-4ca7-b85c-038f0bfc3eb3
keywords:
- Windows Media metafile playlists,redirection
- playlists,redirection
- metafile playlists,redirection
- Windows Media Player,redirection
- redirection
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Redirection

The playlist will redirect the browser to Windows Media Player to play the designated media stream or media file. The most basic metafile playlist contains only the Uniform Resource Locator (URL) of a media file.

To create a basic metafile playlist, open your favorite text editor, such as Microsoft Notepad, and type the following example code.


```XML
<ASX version="3.0">
   <ENTRY>
      <REF HREF="PathToYourFile"/>
   </ENTRY>
</ASX>

```



Substitute a valid path to your Windows Media file using the syntax in the following table.



| Source of content                                                                                 | Syntax                                    |
|---------------------------------------------------------------------------------------------------|-------------------------------------------|
| Content is a file on a Windows Media server                                                       | mms://ServerName/Path/FileName.wma        |
| Content is a broadcast multicast that is accessed from a Windows Media station                    | https://WebServerName/Stations/kxyz.nsc    |
| Content is a broadcast unicast that is accessed from a publishing point on a Windows Media server | mms://ServerName/PublishingPointAlias     |
| Content is a file on a web server                                                                 | https://WebServerName/Path/Filename.wma    |
| Content is a file on a local hard disk                                                            | file://c:\\Path\\Filename.wma             |
| Content is a file on a network share                                                              | file://\\\\ServerName\\Path\\Filename.wma |
| Content is a file on a Windows Media server                                                       | mms://ServerName/Path/FileName.wmv        |



 

Save the file you have created with a file name and extension as described in [File Name Extensions](file-name-extensions.md). Double-click it in Windows Explorer. Windows Media Player should open and start streaming the content. You can save the file to your web server, along with your webpages, and link to it with an **HREF** element, or embed it in a webpage using the Windows Media Player **OBJECT** tag.

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

 

 




