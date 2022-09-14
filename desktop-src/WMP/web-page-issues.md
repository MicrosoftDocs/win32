---
title: Web Page Issues
description: Web Page Issues
ms.assetid: fd97540e-21e9-443e-99ec-ed29f4a2570a
keywords:
- Windows Media metafile playlists,Web pages
- playlists,Web pages
- metafile playlists,Web pages
- Windows Media metafile playlists,customizing HTMLView
- playlists,customizing HTMLView
- metafile playlists,customizing HTMLView
- Windows Media metafile playlists,HTMLView customizing
- playlists,HTMLView customizing
- metafile playlists,HTMLView customizing
- customizing HTMLView
- Windows Media Player,Web pages
- Windows Media Player,customizing HTMLView
- Windows Media Player,HTMLView customizing
- HTMLView,customizing
- HTMLView,Web pages
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Web Page Issues

There are some things to consider when you create a webpage to be displayed in the Windows Media Player **Now Playing** feature. This section discusses some of the issues you might encounter when creating your Web-based content.

## Customizing HTMLView

Your HTMLView webpage can be as simple or complex as you want. You can include any of the elements you usually use in your Web-based content. If you embed the Windows Media Player control, you can display one of the user interfaces supplied by the control, create your own user interface using HTML and script code, or provide no UI at all (which means that the user can use the transport controls of the full-mode Player).

The recommended size for webpages displayed by using the HTMLView feature is 575 x 345 pixels. The user, however, has the ability to resize Windows Media Player and choose the screen resolution. If the HTMLView webpage is larger than the size accommodated by the **Now Playing** feature, the Player displays horizontal and vertical scroll bars that enable the user to see the entire page. You should test your HTMLView content using a variety of screen resolutions and Player sizes to determine the best size for your webpage.

Windows Media Player does not provide a method that enables you to specify a size for the full-mode Player.

## Web page navigation

Windows Media Player does not provide a navigation toolbar for webpages displayed in the **Now Playing** feature. This means that you have complete control over whether users can navigate away from your HTMLView webpage. If you want to enable users to navigate to other webpages, you must include elements in your HTML code to provide that functionality.

## Retrieving the parent window

If your existing script code uses **window.parent** to retrieve the parent window object, this code will not work in your HTMLView webpage. When you use HTMLView, there is no parent window object; therefore, this scripting feature is unavailable.

## About the embedded browser

Because Windows Media Player uses an embedded instance of Internet Explorer to display HTMLView content, the user settings and policies for Internet Explorer apply to any webpages displayed in the Player. For example, if the user has configured Internet Explorer to prevent webpages from downloading cookies to the computer, your HTMLView webpage is also prevented from doing this.

Web pages opened by using the HTMLView feature always run in the Internet Explorer **Internet** security zone.

The embedded Web browser control uses the same rules to cache webpages as the stand-alone version of Internet Explorer. It's a good idea to use Active Server Pages (ASP) when creating your content to ensure that the content is delivered from your web server each time Windows Media Player accesses the HTMLView webpage. Using ASP pages can be as simple as renaming your webpage to use an .asp file name extension.

## About local Web content

The HTMLView feature does not allow you to open webpages that are stored on the user's computer.

## Prompting the user

You can use **window.prompt** to prompt the user for information. However, **window.alert** and **window.confirm** are not available when using HTMLView.

## Timing issues

You may encounter timing issues when using an embedded Windows Media Player control in your HTMLView webpage. In HTMLView, an embedded Player control shares its playback engine with the stand-alone Windows Media Player. It is possible that the stand-alone Player may open and begin playing the first playlist entry before the webpage (and, therefore, the Player control) finishes loading. This means that if you handle the **OpenStateChange** or **PlayStateChange** events, the script code will not receive event notifications for these events until the Player control and its associated objects are loaded.

You can take steps in your code to delay playback until the Windows Media Player control is instantiated. One way to do this is to make the first entry in your metafile playlist point to an image file and set the duration of the file to a length of time that allows the Player control to load. The following example code demonstrates this option:


```XML
<ASX version="3.0">
   <PARAM name="HTMLView" value="https://www.proseware.com/htmlview1.htm"/>

<ENTRY>
   <REF href="https://www.proseware.com/blank.jpg"/>
   <DURATION  VALUE = "1:00"/>
</ENTRY>

<ENTRY>
   <REF href="rtsp://www.proseware.com/content1.wma"/>
</ENTRY>

</ASX>

```



When the preceding playlist opens, Windows Media Player waits at the first entry in the playlist for up to one minute while the Player loads the HTMLView webpage.

Next, in your HTMLView webpage, write script code to handle the **onload** event for the **BODY** element. In the event handler function, call the Player **Controls.Next** method to begin playback of the second entry in the playlist.


```XML
<HTML>
<!-- Define the event handler function. -->
<BODY  onload = "OnLoad();">

<OBJECT id = "Player" 
    CLASSID = "CLSID:6BF52A52-394A-11d3-B153-00C04F79FAA6"> 
        <PARAM Name = "autoStart"  Value = "true">
        <PARAM Name = "uiMode" Value = "none">

</OBJECT>

<!-- Handle the BODY onload event. -->
<SCRIPT>
function OnLoad()
{
   // Advance to the second entry in the playlist.
   Player.controls.next();
}
</SCRIPT>

</BODY>
</HTML>

```



When the webpage in the preceding example finishes loading, Windows Media Player immediately advances to the second entry in the playlist. This overrides the duration specified for the first element in the playlist, meaning that the user doesn't have to wait the full one minute before seeing the desired content; he or she only has to wait for the webpage to finish loading. Because the Player control is completely instantiated at this point, the **OpenStateChange** and **PlayStateChange** events can be handled in the usual manner.

## Related topics

<dl> <dt>

[**Displaying Web Pages in Windows Media Player**](displaying-web-pages-in-windows-media-player.md)
</dt> <dt>

[**Player.PlayStateChange Event**](player-player-playstatechange.md)
</dt> <dt>

[**Player.OpenStateChange Event**](player-player-openstatechange.md)
</dt> </dl>

 

 




