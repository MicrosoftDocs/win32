---
title: Handling Events in a Web Page Displayed by Firefox
description: Handling Events in a Web Page Displayed by Firefox
ms.assetid: 361c46ff-36e2-4497-a511-86b0439e9437
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
- Windows Media Player ActiveX control,event handling
- Windows Media Player Mobile ActiveX control,event handling
- ActiveX control,event handling
- embedding,Web pages
- Web page embedding,event handling
- Windows Media Player,Firefox
- Windows Media Player object model,Firefox
- object model,Firefox
- Windows Media Player Mobile,Firefox
- Windows Media Player ActiveX control,Firefox
- Windows Media Player Mobile ActiveX control,Firefox
- ActiveX control,Firefox
- Firefox,event handling
- Web page embedding,Firefox
- events,Firefox
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Handling Events in a Web Page Displayed by Firefox

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When you embed the Windows Media Player control in a webpage, you can write script that handles events. For a list of events raised by the Player control, see [Player Object](player-object.md).

If the mime type associated with an embedded Player control is application/x-ms-wmp, you can write event handlers that have the following format:


```HTML
<SCRIPT for="Player" language="jscript" event="EventName(Params)">
  ...
</SCRIPT>
```



where *EventName* is the name of a Windows Media Player event, and *Params* is a list of the event's parameters. For example, the following code has a handler for the [PlayStateChange](player-player-playstatechange.md) event.


```HTML
<OBJECT id="Player" type="application/x-ms-wmp" width="300" height="200">
  <PARAM name="URL" value="c:\MediaFiles\Seattle.wmv"/>
</OBJECT>

<P id="p1">...</P>

<SCRIPT for="Player" event="PlayStateChange(NewState)">
  document.getElementById("p1").innerHTML = "Play state: " + NewState;
</SCRIPT>
```



If you have several instances of the Player control on a webpage and if you use the format shown in the preceeding example, then each event handler is tied to a specific instance of the Player control. In the preceeding example, the event handler is called only when the play state changes for the control that has id="Player".

If the mime type associated with an embedded Player control is not application/x-ms-wmp, you can write event handlers that have the following format:


```HTML
<SCRIPT language="jscript">
  function OnDSEventNameEvt(Params)
  {...}
</SCRIPT>
```



where *EventName* is the name of a Windows Media Player event, and *Params* is a list of the event's parameters. For example, the following code has a handler for the **PlayStateChange** event.


```HTML
<OBJECT id="Player" type="application/asx" width="300" height="200">
  <PARAM name="URL" value="c:\MediaFiles\Test.asx"/>
</OBJECT>

<P id="p1">...</P>

<SCRIPT>
  function OnDSPlayStateChangeEvt(NewState)
  {
    p1.innerHTML = "Play state: " + NewState;
  }
</SCRIPT>

```



If you have several instances of the Player control on a webpage and if you use the format shown in the preceeding example, then each event handler is tied to all instances of the Player control and the event handler is called when the play state changes for any Player control on the page.

> [!Note]  
> If the mime type is not application/x-ms-wmp, the **DoubleClick** event is sent as OnDSDblClickEvt (not OnDSDoubleClickEvt) for compatibility with version 6.4 of the Player control.

 

## Related topics

<dl> <dt>

[**Using the Windows Media Player Control with Firefox**](using-the-windows-media-player-control-with-firefox.md)
</dt> </dl>

 

 




