---
title: Creating Web-Based Presentations
description: Creating Web-Based Presentations
ms.assetid: 60d8be10-ebed-4a4f-b17f-700475b51b34
keywords:
- Windows Media Player,Web-based presentations
- Windows Media Player object model,Web-based presentations
- object model,Web-based presentations
- Windows Media Player Mobile,Web-based presentations
- Windows Media Player ActiveX control,Web-based presentations
- Windows Media Player Mobile ActiveX control,Web-based presentations
- ActiveX control,Web-based presentations
- Web-based presentations,creating
- creating Web-based presentations,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Creating Web-Based Presentations

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media Player control lets you easily create Web-based slide-show presentations that combine audio and video with HTML. By adding URL-type script commands to your media files, you can cause specified webpages to display in a specified Web browser frame at specific times during digital media playback.

Windows Media Player also features rich media streaming to enable efficient delivery of HTML data over a network inside a single Windows Media stream or file. The Player and server handle the smooth, timely delivery of audio, video, and HTML to the browser. Just as in Web presentations that do not use rich media streaming, embedded script commands render the presentation in a specified browser frame at specified times.

A typical layout for Web-based presentations uses two frames. One frame contains a webpage that embeds the Windows Media Player control and displays the video part of a presentation. The other frame displays webpages that change at various times as the video plays.

If the digital media accompanying your webpages contains audio only, you can hide the frame that contains the Windows Media Player control by setting its width to zero. This way, the audio can play uninterrupted in the background while your webpages display in the full browser window.

The following sections describe common techniques for enabling Web-based presentations:

-   [URL Flipping](url-flipping.md)
-   [Rich Media Streaming](rich-media-streaming.md)

## Related topics

<dl> <dt>

[**Player Control Guide**](player-control-guide.md)
</dt> </dl>

 

 




