---
title: Adding an Embedded Windows Media Player Control
description: Adding an Embedded Windows Media Player Control
ms.assetid: e002bf2a-c51a-448a-80a0-a35d6f32e9c0
keywords:
- Windows Media metafile playlists,adding embedded Windows Media Player controls
- playlists,adding embedded Windows Media Player controls
- metafile playlists,adding embedded Windows Media Player controls
- Windows Media metafile playlists,embedded Windows Media Player controls
- playlists,embedded Windows Media Player controls
- metafile playlists,embedded Windows Media Player controls
- adding embedded Windows Media Player controls
- embedded Windows Media Player controls
- Windows Media Player,adding embedded controls
- Windows Media Player,embedded controls
- HTMLView,adding embedded Windows Media Player controls
- HTMLView,embedded Windows Media Player controls
- HTMLView,Windows Media Player object model
- HTMLView,Player object model
- Windows Media Player object model,about
- object model,about
- Player object
- Windows Media,Player object model
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Adding an Embedded Windows Media Player Control

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

There are two reasons you might consider adding an embedded instance of Windows Media Player to your HTMLView presentation. First, if you want to display video content, you need to use the Windows Media Player ActiveX control. Second, if you want to take advantage of features of the Windows Media Player object model from within your HTMLView webpage, you must use an instance the Player control to do so.

## Using the Player control to display video in HTMLView content

Usually, Windows Media Player displays video using the Video and Visualization pane of the **Now Playing** feature. Since HTMLView uses this area to display your webpage, you must supply an additional video display area if you want the Player to play video. This is easy to do by using the Windows Media Player ActiveX control.

To use the Player control to display video, embed the control in your HTMLView webpage by using the **OBJECT** tag. This is the same technique you use to embed the Player control into any webpage in which you want to display video. The following example code shows the basic syntax for embedding the Player control in Internet Explorer:


```XML
<OBJECT id = "Player" 
    CLASSID = "CLSID:6BF52A52-394A-11d3-B153-00C04F79FAA6"> 
        <PARAM Name = "autoStart"  Value = "true">
        <PARAM Name = "uiMode" Value = "none">
</OBJECT>

```



The *autoStart* parameter ensures that content plays automatically whenever a new URL is specified. The value you specify for *uiMode* is up to you, but you will usually want to specify "none" when creating content for HTMLView presentations. When you embed the Windows Media Player control to display video in this manner, the user can control playback using the controls of the full-mode Player, so there's no need to provide additional transport controls in the webpage. You can use the space you would usually allocate for transport controls to display more text, graphics, or links to other content.

Do not specify a *URL* parameter when embedding the Windows Media Player control in a webpage designed to display in an HTMLView presentation. Instead, specify the digital media files in the .asx file that opens the content.

Because you provide the video display region in your HTMLView webpage, you can decide where to position the video and how large you want the display region to be. For example, you can contain the **Player** object within an HTML **DIV** element and then specify the position for the **DIV** to situate the video display on the webpage. You can change the dimensions of the video display by specifying values for the height and width attributes of the **OBJECT** element. You can also specify these values using script code.

## Using the Player object model

The Windows Media Player object model exposes properties, methods, and events that you can use in your HTMLView webpages. When you embed the Windows Media Player ActiveX control in your HTMLView webpage, you automatically have access to the Player object model.

If you embed the Windows Media Player control in your HTMLView webpage, do not use the Player object model to specify the digital media file to be played. For example, if you use script code to specify a value for the **URL** property of the embedded control, your HTMLView webpage will be unloaded from the **Now Playing** feature when the digital media file plays. To prevent this from happening, always open .asx files that include HTMLView parameters when you need to use script to open digital media content from your HTMLView webpage.

## Related topics

<dl> <dt>

[**Displaying Web Pages in Windows Media Player**](displaying-web-pages-in-windows-media-player.md)
</dt> <dt>

[**Player.uiMode**](player-uimode.md)
</dt> <dt>

[**Player.URL**](player-url.md)
</dt> <dt>

[**Settings.autoStart**](settings-autostart.md)
</dt> </dl>

 

 




