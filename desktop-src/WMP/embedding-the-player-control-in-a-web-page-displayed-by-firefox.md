---
title: Embedding the Player Control in a Web Page Displayed by Firefox
description: Embedding the Player Control in a Web Page Displayed by Firefox
ms.assetid: 57e725dc-6430-43ec-a39c-c17854a7d8db
keywords:
- Windows Media Player,embedding ActiveX control
- Windows Media Player object model,embedding ActiveX control
- object model,embedding ActiveX control
- Windows Media Player Mobile,embedding ActiveX control
- Windows Media Player ActiveX control,embedding
- Windows Media Player Mobile ActiveX control,embedding
- ActiveX control,embedding
- Windows Media Player ActiveX control,Web pages
- Windows Media Player Mobile ActiveX control,Web pages
- ActiveX control,Web pages
- Windows Media Player,Firefox
- Windows Media Player object model,Firefox
- object model,Firefox
- Windows Media Player Mobile,Firefox
- Windows Media Player ActiveX control,Firefox
- Windows Media Player Mobile ActiveX control,Firefox
- ActiveX control,Firefox
- Firefox,about webpage embedding
- embedding,Web pages
- Web page embedding,Firefox
ms.topic: article
ms.date: 05/31/2018
---

# Embedding the Player Control in a Web Page Displayed by Firefox

To embed the Windows Media Player control in a webpage that can be displayed by a Firefox browser, create an OBJECT element or an EMBED element that has one of the following mime types as its **type** attribute:

-   application/x-ms-wmp
-   application/asx
-   video/x-ms-asf-plugin
-   application/x-mplayer2
-   video/x-ms-asf
-   video/x-ms-wm
-   audio/x-ms-wma
-   audio/x-ms-wax
-   video/x-ms-wmv
-   video/x-ms-wvx

The preferred mime type is application/x-ms-wmp.

The following examples show how to embed the Player control using an OBJECT element or an EMBED element.


```HTML
<OBJECT id="Player"
  type="application/x-ms-wmp" 
  width="320" height="320">
  <PARAM name="autostart" value="false"/>
</OBJECT>

<EMBED id="Player"
  type="application/x-ms-wmp" 
  width="320" height="320"
  autostart="false"/>

```



The preceeding examples work in Firefox but not in Internet Explorer. To embed the Player control in a webpage that can be displayed by Internet Explorer, you must create an OBJECT element that has a **classid** attribute set to the class ID of the Windows Media Player control.

The following example shows how to embed the Windows Media Player control in a webpage that can be displayed correctly by both Internet Explorer and Firefox. Script on the page detects the browser type and generates the appropriate OBJECT tag.


```HTML
<HTML>
  <BODY>
    <SCRIPT type="text/javascript">
      if(-1 != navigator.userAgent.indexOf("MSIE"))
      {
        document.write('<OBJECT id="Player"');
        document.write(' classid="clsid:6BF52A52-394A-11d3-B153-00C04F79FAA6"');
        document.write(' width=300 height=200></OBJECT>');
      }
      else if(-1 != navigator.userAgent.indexOf("Firefox"))
      {
        document.write('<OBJECT id="Player"'); 
        document.write(' type="application/x-ms-wmp"'); 
        document.write(' width=300 height=200></OBJECT>');
      }         
    </SCRIPT>
  </BODY>
</HTML>

```



## Related topics

<dl> <dt>

[**Using the Windows Media Player Control with Firefox**](using-the-windows-media-player-control-with-firefox.md)
</dt> </dl>

 

 




