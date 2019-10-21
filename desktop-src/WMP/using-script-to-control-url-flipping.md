---
title: Using Script to Control URL Flipping
description: Using Script to Control URL Flipping
ms.assetid: ec504ecf-10ef-4b90-bee6-8d149c251ee5
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
ms.date: 05/31/2018
---

# Using Script to Control URL Flipping

When a user connects to a rich media stream while the stream is already in progress, it is possible for the streamed webpage to display before all the elements have arrived and been cached if Windows Media Player automatically invokes the URL. When this happens, the user sees a blank or incomplete webpage until the next set of data arrives in the cache.

You can avoid displaying a blank or incomplete webpage by invoking the URL using script instead of letting Windows Media Player do it automatically. That way, you can ignore the first URL flip and then invoke subsequent URLs by using script code.

> [!Note]  
> This section assumes that you are streaming HTML using the Windows Media Encoder 9 Series SDK and that you have set the HTML stream to repeat.

 

First, you must create a frameset webpage to contain the frame with the embedded Player and the frame that displays the streaming HTML. Each of these two frames will display a separate webpage initially, so you will create a total of three webpages. The following example code demonstrates the frameset webpage:


```HTML
<HTML>
<HEAD>
</HEAD>

<FRAMESET cols = "350, *">
  <FRAME  name = "player" src = "embed_player.htm">
  <FRAME  name = "content" src = "blank.htm">

  <NOFRAMES>
  <BODY>

  <P>This page uses frames, but your browser doesn't support them.</P>

  </BODY>
  </NOFRAMES>

</FRAMESET>
</HTML>

```



The preceding webpage example incorporates two frames. The first frame displays in the left half of the browser window and displays the webpage named embed\_player.htm. The following example code creates this webpage:


```HTML
<HTML>
<HEAD>
</HEAD>
<BODY>

<!-- Embed Windows Media Player and disable the invokeURLs parameter -->
<OBJECT CLASSID = "CLSID:6BF52A52-394A-11D3-B153-00C04F79FAA6" ID = "Player">
  <PARAM name = "URL"  value = "https://www.proseware.com/Media/video.wmv">
  <PARAM name = "invokeURLs"  value = "false">
</OBJECT>

<SCRIPT LANGUAGE = "JScript">
  var bFirstURL = true; // Global flag for first URL flip.
</SCRIPT>

<!-- Create an event handler for script commands. -->
<SCRIPT LANGUAGE = "JScript"  FOR = "Player" EVENT = "ScriptCommand(scType, scParam)">

  if("URL" == scType)
  {
    if ( bFirstURL == false )
    {
      // Show the next URL flip.
      parent.content.location = scParam;
    }
    else
    {
      bFirstURL = false; // Set the flag.
    }
  }

</SCRIPT>

</BODY>
</HTML>

```



The second frame in the frameset displays in the right half of the browser window and displays a webpage named "blank.htm". The following example code creates this webpage:


```HTML
<HTML>
<HEAD>
</HEAD>
<BODY>

Loading...
</BODY>
</HTML>

```



When the frameset page loads in the browser, the left frame shows the embedded Player and the right frame shows the text "Loading..." to inform the user that more data is forthcoming. When the first URL script command arrives from the HTML stream, the event handler simply changes the value of the **Boolean** flag. When each subsequent URL script command arrives from the HTML stream, the script in the event handler loads the new URL into the frame named "content", and the complete webpage displays in the frame located in the right half of the browser window.

For more information about streaming HTML using Windows Media, see the Windows Media Encoder SDK.

## Related topics

<dl> <dt>

[**Rich Media Streaming**](rich-media-streaming.md)
</dt> <dt>

[**URL Flipping**](url-flipping.md)
</dt> </dl>

 

 




