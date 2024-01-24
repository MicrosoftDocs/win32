---
title: Hiding the Windows Media Player Control
description: Hiding the Windows Media Player Control
ms.assetid: 754896af-b80d-4552-82c6-3fb65359accd
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
- embedding,Web pages
- Windows Media Player,hiding ActiveX control
- Windows Media Player object model,hiding ActiveX control
- object model,hiding ActiveX control
- Windows Media Player Mobile,hidingActiveX control
- Windows Media Player ActiveX control,hiding
- Windows Media Player Mobile ActiveX control,hiding
- ActiveX control,hiding
- Windows Media Player ActiveX control,Web pages
- Windows Media Player Mobile ActiveX control,Web pages
- ActiveX control,Web pages
- Web page embedding,hiding ActiveX control
- hiding Windows Media Player ActiveX control
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Hiding the Windows Media Player Control

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media Player ActiveX object is embedded in a webpage using the OBJECT element. Unlike earlier versions, the OBJECT element that defines Windows Media Player must be placed in the BODY section of a webpage, between the &lt;BODY&gt; and </BODY> tags. Placing the Windows Media Player ActiveX object in the HEAD section of a webpage to hide the user interface can produce unexpected results.

If you put the Windows Media Player ActiveX control in the BODY section of a webpage, the control user interface will be displayed. If you do not want it to be displayed, and wish to create your own user interface, set the height and width attributes of the OBJECT element to zero.

The control can also be made invisible by setting the *Player*.**uiMode** property to "invisible". This can be done using a PARAM tag as discussed in the next section. In this case, space is reserved for the control using height and width, but nothing is displayed in the reserved space until **uiMode** is changed to something other than "invisible".

## Related topics

<dl> <dt>

[**Using the Windows Media Player Control in a Web Page**](using-the-windows-media-player-control-in-a-web-page.md)
</dt> </dl>

 

 




