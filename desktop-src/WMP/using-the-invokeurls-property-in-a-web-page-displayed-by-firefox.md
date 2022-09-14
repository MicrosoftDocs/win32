---
title: Using the invokeURLs Property in a Web Page Displayed by Firefox
description: Using the invokeURLs Property in a Web Page Displayed by Firefox
ms.assetid: cec2ba89-b08f-4c83-bcb2-a4df1ce6f179
keywords:
- Windows Media Player,embedding ActiveX control
- Windows Media Player object model,embedding ActiveX control
- object model,embedding ActiveX control
- Windows Media Player Mobile,embedding ActiveX control
- Windows Media Player ActiveX control,embedding
- Windows Media Player Mobile ActiveX control,embedding
- Windows Media Player ActiveX control,Web pages
- Windows Media Player Mobile ActiveX control,Web pages
- Windows Media Player ActiveX control,invokeURLs property
- Windows Media Player Mobile ActiveX control,invokeURLs property
- embedding,Web pages
- Web page embedding,invokeURLs property
- Windows Media Player,Firefox
- Windows Media Player object model,Firefox
- object model,Firefox
- Windows Media Player ActiveX control,Firefox
- ActiveX control,Firefox
- Firefox,invokeURLs property
- Web page embedding,Firefox
ms.topic: article
ms.date: 05/31/2018
---

# Using the invokeURLs Property in a Web Page Displayed by Firefox

Some media files contain embedded URLs for which Windows Media Player displays webpages in a Web browser window or frame as the media file plays. In Windows Internet Explorer, you can use the [Settings.invokeURLs](settings-invokeurls.md) property to specify whether pages are displayed for embedded URLs, and you can use the [Settings.defaultFrame](settings-defaultframe.md) property to specify a frame for displaying such pages.

In Firefox, some workarounds are required to set the **invokeURLs** property and to specify a frame for displaying pages for embedded URLs.

## Setting the invokeURLs property

The default value of the **Settings.invokeURLs** property is true, so if you want the value to be false, you must set it explicitly. In Internet Explorer, you can set **invokeURLs** to false in a PARAM element inside the Player control's OBJECT element.

The Firefox plug-in does not support setting the **invokeURLs** property in a PARAM element.

You can work around this limitation by setting the **invokeURLs** property in script. The following code shows how to set the **invokeURLs** property to false in a webpage that can be displayed by both Internet Explorer and Firefox.


```HTML
<HTML>
  <BODY OnLoad="Initialize()">

    <SCRIPT type="text/javascript">

      document.write('<OBJECT id="Player"'); 

      if(-1 != navigator.userAgent.indexOf("MSIE"))
      {               
        document.write(' classid="clsid:6BF52A52-394A-11d3-B153-00C04F79FAA6"');       
      }
      else if(-1 != navigator.userAgent.indexOf("Firefox"))
      {      
        document.write(' type="application/x-ms-wmp"');        
      }  

      document.write(' width=300 height=200>');
      document.write('<PARAM name="autoStart" value="false"/>');
      document.write('<PARAM name="url" value="c:\\MediaFiles\\Glass.wmv"/>');
      document.write('</OBJECT>'); 
      
    </SCRIPT>

    <SCRIPT>
      function Initialize()
      {
        Player.settings.invokeURLs = false;
        Player.controls.play();
      }
    </SCRIPT>

  </BODY>
</HTML>

```



## Displaying webpages in a frame

A media file can contain URLs that display webpages in a browser window or frame as the media file is played. In Internet Explorer, you can use the [Settings.defaultFrame](settings-defaultframe.md) property to specify the frame in which those pages are displayed. If you do not set the **defaultFrame** property, URLs are displayed in a separate window of the default browser. However, the Firefox plug-in does not support the **Settings.defaultFrame** property. To work around this limitation, set the **Settings.invokeURLs** property to false and write a [ScriptCommand](player-player-scriptcommand.md) event handler that sets the location of the target frame. The following example, which works in Internet Explorer and Firefox, illustrates this technique. Assume that the webpage shown in the example is in frames\[0\] and you want the URL's page to be displayed in frames\[1\].


```HTML
<HTML>
  <BODY OnLoad="Initialize()">

    <SCRIPT type="text/javascript">

      document.write('<OBJECT id="Player"'); 

      if(-1 != navigator.userAgent.indexOf("MSIE"))
      {               
        document.write(' classid="clsid:6BF52A52-394A-11d3-B153-00C04F79FAA6"');       
      }
      else if(-1 != navigator.userAgent.indexOf("Firefox"))
      {      
        document.write(' type="application/x-ms-wmp"');        
      }  

      document.write(' width=300 height=200>');
      document.write('<PARAM name="autoStart" value="false"/>');
      document.write('<PARAM name="url" value="c:\\MediaFiles\\Glass.wmv"/>');
      document.write('</OBJECT>'); 
      
    </SCRIPT>

    <SCRIPT>
      function Initialize()
      {
        Player.settings.invokeURLs = false;
        Player.controls.play();
      }
    </SCRIPT>

    <SCRIPT for="Player" event="ScriptCommand(scType, scParam)">
      if( scType == "URL" )
      {
        parent.frames[1].location = scParam;
      }
    </script>

  </BODY>
</HTML>

```



## Related topics

<dl> <dt>

[**Using the Windows Media Player Control with Firefox**](using-the-windows-media-player-control-with-firefox.md)
</dt> </dl>

 

 




