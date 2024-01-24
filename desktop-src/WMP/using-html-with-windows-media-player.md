---
title: Using HTML with Windows Media Player
description: Using HTML with Windows Media Player
ms.assetid: 321d4396-511b-4f0d-9ee9-8bdddceedc0e
keywords:
- Windows Media Player,HTML
- Windows Media Player object model,HTML
- object model,HTML
- Windows Media Player ActiveX control,HTML for object model
- ActiveX control,HTML for object model
- Windows Media Player Mobile ActiveX control,HTML for object model
- Windows Media Player Mobile,HTML for object model
- HTML with Windows Media Player
- Web page embedding,HTML
- embedding,Web pages
- script commands
- URL flipping
- rich media streaming
- browser support
- displaying webpages
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using HTML with Windows Media Player

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

## Overview

Using HTML with Windows Media Player is an excellent way to combine audio and video with text and graphics. You can embed the Windows Media Player control in a webpage when you want to supplement your static content or create Web applications with digital media. When you want to supplement your digital media with HTML, on the other hand, you can display webpages in the full mode of the Player by referencing them in Windows Media metafile playlists.

If you write custom programs that embed the Windows Media Player control in remote mode, you can also control the webpages displayed in the various panes of the full mode of the Player when your users undock the control. This lets you preserve continuity between the docked and undocked states.

## Web Embedding

You can use the Windows Media Player control as part of a webpage you create. See [Embedding the Windows Media Player Control in a Web Page](embedding-the-windows-media-player-control-in-a-web-page.md).

## Script Commands and URL Flipping

Script commands are text/value pairs you can embed in your digital media files or streams. You might use custom script commands solely to trigger script code, while letting Windows Media Player handle other script commands automatically.

When you have several webpages that accompany a digital media presentation, URL script commands can automatically change the page in one frame while the Windows Media Player control continues playing digital media in another frame. This is called URL flipping, and is an excellent way to create a multimedia slide show. Other automatically handled script commands let you switch playback to a different media file or stream, display captioning text, or trigger events such as ad insertions defined in a Windows Media metafile playlist.

For more information about URL flipping, see [Creating Web-Based Presentations](creating-web-based-presentations.md).

## Rich Media Streaming

URL flipping works best with simple pages that load rapidly. With more complex pages, multiple components are transferred individually, making it difficult to synchronize page display with digital media. To allow complex rich media presentations, webpages can be added to a media stream and delivered to the Player in the same way as audio and video. This lets you synchronize the components of your presentation much more easily, especially over low-speed connections.

For more information about rich media streaming, see [Creating Web-Based Presentations](creating-web-based-presentations.md).

## Browser Support

You can embed the Windows Media Player control in Microsoft Internet Explorer, Firefox, and Netscape Navigator, although the process is slightly different for each. You can also create webpages designed to work with all three browsers.

With Internet Explorer and Firefox, you embed the control using the HTML OBJECT element. Navigator requires a different approach, however, because it doesn't directly support ActiveX controls. With Navigator, you use the APPLET element to embed a special Java applet into the page. This applet handles communication with the Player ActiveX control.

For more information about Firefox support, see [Using the Windows Media Player Control with Firefox](using-the-windows-media-player-control-with-firefox.md).

For more information about Netscape Navigator support, see [Using Windows Media Player with Netscape 7.1](using-windows-media-player-with-netscape-7-1.md).

## Displaying Web Pages in the Full Mode of the Player

You can extend the functionality of Windows Media Player or provide a custom view of information that accompanies your digital media by displaying webpages in the full mode of the Player. This is the HTMLView feature of Windows Media metafiles. Metafiles give you great control over playlist content, allowing you to seamlessly transition between clips, insert advertisements, and display still images in Windows Media Player. To display webpages in the full mode of the Player, you use the PARAM element to add URL references to your playlist entries or to entire playlists.

For more information about using webpages in metafiles, see [Displaying Web Pages in Windows Media Player](displaying-web-pages-in-windows-media-player.md).

## Related topics

<dl> <dt>

[**About the Player Object Model**](about-the-player-object-model.md)
</dt> </dl>

 

 




