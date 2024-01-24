---
title: Using PARAM Elements in a Web Page Displayed by Firefox
description: Using PARAM Elements in a Web Page Displayed by Firefox
ms.assetid: 8403c6f4-f221-4411-b49c-f0c9c22943df
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
- Windows Media Player,Firefox
- Windows Media Player object model,Firefox
- object model,Firefox
- Windows Media Player Mobile,Firefox
- Windows Media Player ActiveX control,Firefox
- Windows Media Player Mobile ActiveX control,Firefox
- ActiveX control,Firefox
- Firefox,PARAM elements in OBJECT element
- Web page embedding,Firefox
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using PARAM Elements in a Web Page Displayed by Firefox

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can use PARAM elements inside an OBJECT element to set the initial state of the Player control. For example, the PARAM elements in the following example specify that the control should play seattle.wmv automatically.


```HTML
<OBJECT id="Player" type="application/x-ms-wmp" width="300" height="200">
  <PARAM name="url" value="c:\MediaFiles\seattle.wmv" />
  <PARAM name="autostart" value="true" />
</OBJECT>

```



Most PARAM elements can be interpreted by Internet Explorer and by Firefox. However, there are a few PARAM elements that the Firefox plug-in does not support. For information about which PARAM elements are supported by the Firefox plug-in, see [PARAM Elements in an OBJECT Element](param-elements-in-an-object-element.md).

## Related topics

<dl> <dt>

[**Using the Windows Media Player Control with Firefox**](using-the-windows-media-player-control-with-firefox.md)
</dt> </dl>

 

 




