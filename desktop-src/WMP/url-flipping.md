---
title: URL Flipping
description: URL Flipping
ms.assetid: 2921dff1-f740-491c-9b5e-79b7638e2065
keywords:
- Windows Media Player,Web-based presentations
- Windows Media Player object model,Web-based presentations
- object model,Web-based presentations
- Windows Media Player Mobile,Web-based presentations
- Windows Media Player ActiveX control,Web-based presentations
- Windows Media Player Mobile ActiveX control,Web-based presentations
- ActiveX control,Web-based presentations
- Windows Media Player,URL flipping
- Windows Media Player object model,URL flipping
- object model,URL flipping
- Windows Media Player Mobile,URL flipping
- Windows Media Player ActiveX control,URL flipping
- Windows Media Player Mobile ActiveX control,URL flipping
- ActiveX control,URL flipping
- Web-based presentations,URL flipping
- creating Web-based presentations,URL flipping
- URL flipping
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# URL Flipping

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Using webpages for slide shows is called URL flipping, and is handled automatically by Windows Media Player when it encounters URL script commands embedded in the digital media stream it is playing. You can specify a target frame for your pages in each script command, or you can specify it by setting the **Settings.defaultFrame** property. You can set this property in script code or by using a PARAM element within the OBJECT element that embeds the Windows Media Player control.

You are free to handle the URL script commands in your JScript code just as you would handle custom script commands. If you want the Windows Media Player control to ignore URL script commands so that you can handle them entirely by yourself, set the *Settings*.**invokeURLs** property to false either in script code or using a PARAM element as previously described.

The following example illustrates a typical frameset for URL flipping. First, create a page that describes the frameset:


```HTML
<HTML>
<FRAMESET cols="300,*">
  <FRAME name="player" src="player.html">
  <FRAME name="content">
</FRAMESET>
</HTML>

```



Next, create the player.html file referenced in the frameset by using the following code (the video.wmv file is assumed to exist in the same directory as the HTML files):


```HTML
<HTML>
<BODY>
<OBJECT ID="Player" CLASSID="CLSID:6BF52A52-394A-11d3-B153-00C04F79FAA6">
  <PARAM name="URL" value="https://www.proseware.com/Media/video.wmv"/>
  <PARAM name="defaultFrame" value="content"/>
</OBJECT>
</BODY>
</HTML>

```



If your webpages are small enough to load rapidly, this setup may be sufficient for your needs. If, on the other hand, your webpages are complex, rich media streaming may be more effective depending on the connection speed of your audience.

> [!Note]  
> URL flipping does not work correctly with pages viewed in Netscape Navigator. Instead of appearing in the frame specified by **defaultFrame**, each URL script command received in Navigator displays the URL in a new browser window.

 

## Related topics

<dl> <dt>

[**Creating Web-Based Presentations**](creating-web-based-presentations.md)
</dt> <dt>

[**Using Script to Control URL Flipping**](using-script-to-control-url-flipping.md)
</dt> </dl>

 

 




