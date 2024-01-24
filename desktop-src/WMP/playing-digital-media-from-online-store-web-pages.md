---
title: Playing Digital Media from Online Store Web Pages
description: Playing Digital Media from Online Store Web Pages
ms.assetid: 519a6a0d-96cd-4bf9-b5a3-b7604d137fc1
keywords:
- Windows Media Player online stores,playing digital media
- online stores,playing digital media
- type 1 online stores,playing digital media
- type 2 online stores,playing digital media
- Windows Media Player online stores,digital media playing
- online stores,digital media playing
- type 1 online stores,digital media playing
- type 2 online stores,digital media playing
- Windows Media Player online stores,Web page digital media playing
- online stores,Web page digital media playing
- type 1 online stores,Web page digital media playing
- type 2 online stores,Web page digital media playing
- Web page digital media playing
- playing digital media
- digital media playing
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Playing Digital Media from Online Store Web Pages

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can play digital media content from your online store webpages. Simply embed the Windows Media Player control as described in [Using the Windows Media Player Control in a Web Page](using-the-windows-media-player-control-in-a-web-page.md). When you do this in a service task pane, the embedded control connects to the Windows Media Player program in a fashion similar to remote mode (see [Remoting the Windows Media Player Control](remoting-the-windows-media-player-control.md)). This means that users can use the transport controls of the full mode Player to control playback of digital media in the webpage.

We recommend that you set **uiMode** to "none" or "invisible" when embedding the Player control in a service task pane webpage.

## Related topics

<dl> <dt>

[**Information Common to Type 1 and Type 2 Online Stores**](information-common-to-type-1-and-type-2-online-stores.md)
</dt> <dt>

[**Player.uiMode**](player-uimode.md)
</dt> </dl>

 

 




