---
title: PARAM Elements in an OBJECT Element
description: PARAM Elements in an OBJECT Element
ms.assetid: f9229d92-3a7e-4ba4-a84c-20e60f2482dc
keywords:
- Windows Media Player,PARAM elements in OBJECT element
- Windows Media Player object model,PARAM elements in OBJECT element
- object model,PARAM elements in OBJECT element
- Windows Media Player Mobile,PARAM elements in OBJECT element
- Windows Media Player ActiveX control,PARAM elements in OBJECT element
- Windows Media Player Mobile ActiveX control,PARAM elements in OBJECT element
- ActiveX control,PARAM elements in OBJECT element
- embedding,Web pages
- Web page embedding,PARAM elements in OBJECT element
- PARAM elements in OBJECT element
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PARAM Elements in an OBJECT Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Windows Media Player uses the PARAM element to define specific startup conditions for the control. The PARAM element is embedded inside the OBJECT element.

For example, if you want to define whether the **autoStart** property is True, you would embed the PARAM element inside the OBJECT element.


```HTML
<OBJECT ID="Player"
  CLASSID="CLSID:6BF52A52-394A-11d3-B153-00C04F79FAA6">
    <PARAM name="autoStart" value="True">
</OBJECT>
```



You can have as many PARAM elements in an OBJECT element as you want. PARAM has two attributes, name and value. Both attributes must be set.

The supported PARAM attributes vary slightly among browsers and mime types. The following table shows the attributes supported by the Internet Explorer and Firefox browsers. The preferred mime type for the Firefox browser is application/x-ms-wmp, however, there are several other mime types that you can use to embed the Player control in a webpage hosted by the Firefox browser. The fourth column of the table shows the attributes that are supported when you use a mime type other than application/x-ms-wmp.



| PARAM name                                            | Internet Explorer | Firefox with mime type application/x-ms-wmp | Firefox with any other mime type |
|-------------------------------------------------------|-------------------|---------------------------------------------|----------------------------------|
| [autoStart](settings-autostart.md)                   | yes               | yes                                         | yes                              |
| [balance](settings-balance.md)                       | yes               | yes                                         | yes                              |
| [baseURL](settings-baseurl.md)                       | yes               | yes                                         | yes                              |
| [captioningID](closedcaption-captioningid.md)        | yes               | yes                                         | yes                              |
| [currentMarker](controls-currentmarker.md)           | yes               | yes                                         | yes                              |
| [currentPosition](controls-currentposition.md)       | yes               | yes                                         | yes                              |
| [defaultFrame](settings-defaultframe.md)             | yes               | no                                          | no                               |
| [enableContextMenu](player-enablecontextmenu.md)     | yes               | yes                                         | yes                              |
| [enabled](player-enabled.md)                         | yes               | yes                                         | yes                              |
| [enableErrorDialogs](settings-enableerrordialogs.md) | yes               | yes                                         | no                               |
| **fileName**                                          | no                | yes                                         | yes                              |
| [fullScreen](player-fullscreen.md)                   | yes               | no                                          | no                               |
| [invokeURLs](settings-invokeurls.md)                 | yes               | no                                          | no                               |
| [mute](settings-mute.md)                             | yes               | yes                                         | yes                              |
| [playCount](settings-playcount.md)                   | yes               | yes                                         | no                               |
| [rate](settings-rate.md)                             | yes               | yes                                         | yes                              |
| [SAMIFileName](closedcaption-samifilename.md)        | yes               | yes                                         | yes                              |
| [SAMILang](closedcaption-samilang.md)                | yes               | yes                                         | yes                              |
| [SAMIStyle](closedcaption-samistyle.md)              | yes               | yes                                         | yes                              |
| **SRC**                                               | no                | yes                                         | yes                              |
| [stretchToFit](player-stretchtofit.md)               | yes               | yes                                         | no                               |
| [URL](player-url.md)                                 | yes               | yes                                         | yes                              |
| [volume](settings-volume.md)                         | yes               | yes                                         | yes                              |
| [windowlessVideo](player-windowlessvideo.md)         | yes               | yes                                         | yes                              |



 

> [!Note]  
> The **fileName** and **SRC** PARAM elements are supported by the Firefox plug-in, but not by Internet Explorer. They both perform the same function as the **URL** PARAM element.

 

See the [Object Model Reference for Scripting](object-model-reference-for-scripting.md) for more details about the values for each name attribute.

## Related topics

<dl> <dt>

[**Using the Windows Media Player Control in a Web Page**](using-the-windows-media-player-control-in-a-web-page.md)
</dt> </dl>

 

 




