---
title: Rich Media Streaming
description: Rich Media Streaming
ms.assetid: 3a48ee9a-5bf8-4cd0-9eed-07ec6da0f578
keywords:
- Windows Media Player,Web-based presentations
- Windows Media Player object model,Web-based presentations
- object model,Web-based presentations
- Windows Media Player Mobile,Web-based presentations
- Windows Media Player ActiveX control,Web-based presentations
- Windows Media Player Mobile ActiveX control,Web-based presentations
- ActiveX control,Web-based presentations
- Windows Media Player,rich media streaming
- Windows Media Player object model,rich media streaming
- object model,rich media streaming
- Windows Media Player Mobile,rich media streaming
- Windows Media Player ActiveX control,rich media streaming
- Windows Media Player Mobile ActiveX control,rich media streaming
- ActiveX control,rich media streaming
- Web-based presentations,rich media streaming
- creating Web-based presentations,rich media streaming
- rich media streaming
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Rich Media Streaming

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Complex webpages contain many different components that are normally transferred separately. On a slow connection, such pages display one piece at a time and may take several minutes to display completely. This may prevent you from effectively synchronizing webpages with your digital media. The solution to this problem is rich media streaming, which means adding your webpages to your digital media stream so that they are delivered at the same time as the audio or video data.

Rich media streaming uses a simple frameset layout and behaves exactly like normal URL flipping. Just as in URL flipping, URL script commands embedded in digital media streams are used to display the content in the target frame. Instead of pointing to pages on the Web, however, the URL script commands are used by Windows Media Player 9 Series or later to access files in the Internet Explorer cache where the streamed HTML content is placed as it is received. Just as with normal URL flipping, you can write event handlers that respond to these URL script commands, or you can let the Windows Media Player control handle everything automatically.

> [!Note]  
> Any HTML content delivered through rich media streaming is played back in the Internet security zone, and is subject to the user's browser security settings.

 

For more information on creating rich media presentations, see the Windows Media Format 9 Series or later SDK and the Windows Media Encoder 9 Series SDK.

## Related topics

<dl> <dt>

[**Creating Web-Based Presentations**](creating-web-based-presentations.md)
</dt> <dt>

[**Using Script to Control URL Flipping**](using-script-to-control-url-flipping.md)
</dt> </dl>

 

 




