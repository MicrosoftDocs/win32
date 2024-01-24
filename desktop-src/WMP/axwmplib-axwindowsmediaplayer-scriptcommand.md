---
title: ScriptCommand Event of the AxWindowsMediaPlayer Object
description: The ScriptCommand event occurs when a synchronized command or URL is received. | ScriptCommand Event of the AxWindowsMediaPlayer Object
ms.assetid: b6c613b2-f1b0-43d3-9992-c01d1e00e644
keywords:
- ScriptCommand Event of the AxWindowsMediaPlayer Object Windows Media Player
topic_type:
- apiref
api_name:
- ScriptCommand Event of the AxWindowsMediaPlayer Object
api_location:
- AxInterop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# ScriptCommand Event of the AxWindowsMediaPlayer Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The ScriptCommand event occurs when a synchronized command or URL is received.

``` syntax
[C#]
private void player_ScriptCommand(
  object sender,
  _WMPOCXEvents_ScriptCommandEvent e
)

[Visual Basic]
Private Sub player_ScriptCommand(  
  sender As Object, 
  e As _WMPOCXEvents_ScriptCommandEvent
) Handles player.ScriptCommand
```

## Event Data

The handler associated with this event is of type **AxWMPLib.\_WMPOCXEvents\_ScriptCommandEventHandler**. This handler receives an argument of type **AxWMPLib.\_WMPOCXEvents\_ScriptCommandEvent**, which contains the following properties related to this event.



| Property | Description                                                   |
|----------|---------------------------------------------------------------|
| scType   | System.StringSpecifies the type of script command.<br/> |
| param    | System.StringSpecifies the script command.<br/>         |



 

## Remarks

Commands can be embedded among the sounds and images of a Windows Media file or stream. The commands are a pair of Unicode strings associated with a designated time in the stream. When the stream reaches the time associated with the command, the Windows Media Player control sends a **ScriptCommand** event with two parameters. One parameter specifies the type of command being sent, and the other parameter specifies the command. The type of parameter is used to determine how the command parameter is processed. Any type of command can be embedded in a file or stream to be handled by the **ScriptCommand** event.

The following table lists script command types that are automatically processed by Windows Media Player.



| Type                   | Description                                                                                                                                                         |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CAPTION                | The control displays the associated text in the HTML element specified by IWMPClosedCaption.**captioningId**.                                                       |
| EVENT                  | The control executes instructions defined for the specified event.                                                                                                  |
| FILENAME               | The control resets its **URL** property, attempts to open the specified file, and begins playing the new stream immediately.                                        |
| OPENEVENT              | Buffers the associated EVENT type command for timely execution of the EVENT script.                                                                                 |
| SYNCHRONIZEDLYRICLYRIC | The *param* parameter contains the synchronized lyric text. Windows Media Player displays the lyric text in the closed caption area of the **Now Playing** feature. |
| TEXT                   | The control displays the associated text in the HTML element specified by IWMPClosedCaption.**captioningId**.                                                       |
| URL                    | The control automatically opens the URL specified using the default Internet browser if the IWMPSettings.**invokeURLs** property is set to true.                    |



 

You can embed any other type of command as long as you provide code to handle the command. Though unknown commands are ignored by the Windows Media Player control, they are still handed off to the **ScriptCommand** event.

The ScriptCommand event is not called if the file is being scanned in fast forward or rewind mode.

URL commands received by the Windows Media Player control are invoked automatically in your default Web browser if the IWMPSettings.**invokeURLs** property is set to true. You can use the IWMPSettings.**defaultFrame** property to specify the target frame in which the webpage appears.

The URL sent to Windows Media Player is processed relative to the base URL specified by the IWMPSettings.**baseURL** property. The base URL is concatenated with the relative URL, resulting in a fully specified URL that is passed as the command parameter by the **ScriptCommand** event.

The Windows Media Player control always processes incoming URL commands in the following manner:

1.  A URL-type command is received.
2.  IWMPSettings.**baseURL** is used to create a full URL from the relative URL specified in the script command.
3.  **ScriptCommand** is called.
4.  After **ScriptCommand** returns, IWMPSettings.**invokeURLs** is checked.
5.  If IWMPSettings.**invokeURLs** is true and the command is a URL command, the specified URL is invoked. If IWMPSettings.**invokeURLs** is false or if the command is not a URL command, the command is ignored.

When authoring a Windows Media file, you can specify which frame the new URL is displayed in by concatenating two ampersands and the name of the frame in the parameter field. The following example illustrates typical **ScriptCommand** parameters. It specifies that the URL *mypage* must be launched in the *myframe* frame.


```CSharp
scType = "URL"
Param = https://myweb/mypage.html&&myframe
```



The ScriptCommand event is not called if the file is being scanned (fast-forwarded or rewound).

## Requirements



| Requirement | Value |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                          |
| Namespace<br/> | **AxWMPLib**<br/>                                                                                                    |
| Assembly<br/>  | <dl> <dt>AxInterop.WMPLib.dll (AxInterop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer Object (VB and C#)**](axwindowsmediaplayer-object--vb-and-c.md)
</dt> <dt>

[**AxWindowsMediaPlayer.URL (VB and C#)**](axwmplib-axwindowsmediaplayer-url--vb-and-c.md)
</dt> <dt>

[**IWMPClosedCaption.captioningId (VB and C#)**](wmplibiwmpclosedcaption-iwmpclosedcaption-captioningid--vb-and-c.md)
</dt> <dt>

[**IWMPSettings.baseURL (VB and C#)**](wmplibiwmpsettings-iwmpsettings-baseurl--vb-and-c.md)
</dt> <dt>

[**IWMPSettings.defaultFrame (VB and C#)**](wmplibiwmpsettings-iwmpsettings-defaultframe--vb-and-c.md)
</dt> <dt>

[**IWMPSettings.invokeURLs (VB and C#)**](wmplibiwmpsettings-iwmpsettings-invokeurls--vb-and-c.md)
</dt> </dl>

 

 





