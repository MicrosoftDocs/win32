---
title: Player.ScriptCommand event
description: The ScriptCommand event occurs when a synchronized command or URL is received. | Player.ScriptCommand event
ms.assetid: d3aec4e2-1b0e-414e-8113-0af4fcd37e3b
keywords:
- ScriptCommand event Windows Media Player
- ScriptCommand event Windows Media Player , Player class
- Player class Windows Media Player , ScriptCommand event
topic_type:
- apiref
api_name:
- Player.ScriptCommand
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Player.ScriptCommand event

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **ScriptCommand** event occurs when a synchronized command or URL is received.

## Syntax


```JScript
Player.ScriptCommand(
  scType,
  Param
)
```



## Parameters

<dl> <dt>

*scType* 
</dt> <dd>

String specifying the type of script command.

</dd> <dt>

*Param* 
</dt> <dd>

**String** specifying the script command.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

Commands can be embedded among the sounds and images of a Windows Media file or stream. The commands are a pair of Unicode strings associated with a designated time in the stream. When the stream reaches the time associated with the command, the Windows Media Player control sends a **ScriptCommand** event with two parameters. One parameter specifies the type of command being sent, and the other parameter specifies the command. The type of parameter is used to determine how the command parameter is processed. Any type of command can be embedded in a file or stream to be handled by the **ScriptCommand** event.

The following table lists script command types that are automatically processed by Windows Media Player.



| Type                   | Description                                                                                                                                                         |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CAPTION                | The control displays the associated text in the DIV specified by *ClosedCaption*.**captioningID**.                                                                  |
| EVENT                  | Tells the control to execute instructions defined for the specified event.                                                                                          |
| FILENAME               | The control resets its **URL** property, attempts to open the specified file, and begins playing the new stream immediately.                                        |
| OPENEVENT              | Buffers the associated EVENT type command for timely execution of the EVENT script.                                                                                 |
| SYNCHRONIZEDLYRICLYRIC | The *Param* parameter contains the synchronized lyric text. Windows Media Player displays the lyric text in the closed caption area of the **Now Playing** feature. |
| TEXT                   | The control displays the associated text in the DIV specified by *ClosedCaption*.**captioningID**.                                                                  |
| URL                    | The control automatically opens the URL specified using the default Internet browser if the *Settings*.**invokeURLs** property is set to true.                      |



 

You can embed any other type of command as long as you provide reciprocal code to handle the command. Though unknown commands are ignored by the Windows Media Player control, they are still handed off to the **ScriptCommand** event.

URL commands received by the Windows Media Player control are invoked automatically in your default Web browser if the *Settings*.**invokeURLs** property is set to true. You can use the *Settings*.**defaultFrame** property to specify the target frame in which the webpage appears.

The URL sent to Windows Media Player is processed relative to the base URL specified by the *Settings*.**baseURL** property. The base URL is concatenated with the relatively specified URL, resulting in a fully specified URL that is passed as the command parameter by the **ScriptCommand** event.

The Windows Media Player control always processes incoming URL-type commands in the following manner:

1.  A URL-type command is received.
2.  *Settings*.**baseURL** is used to create a full URL from the relative URL specified in the script command.
3.  *ScriptCommand* is called.
4.  After *ScriptCommand* returns, *Settings*.**invokeURLs** is checked.
5.  If *Settings*.**invokeURLs** is true and the command is a URL-type, the specified URL is invoked. If *Settings*.**invokeURLs** is false or if the command is not a URL-type, the command is ignored.

When authoring a Windows Media file, you can specify which frame the new URL is displayed in by concatenating two ampersands and the name of the frame in the parameter field. The example below illustrates typical *ScriptCommand* parameters. It specifies that the URL *mypage* must be launched in the *myframe* frame.


```JScript
scType = "URL"
Param = https://myweb/mypage.html&&myframe

```



The ScriptCommand event is not called if the file is being scanned (fast-forwarded or fast-reversed).

The value of event parameters is specified by Windows Media Player, and can be accessed or passed to a method in an imported JScript file using the parameter name given. This parameter name must be typed exactly as shown, including capitalization.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> <dt>

[**Player.URL**](player-url.md)
</dt> <dt>

[**Settings.baseURL**](settings-baseurl.md)
</dt> <dt>

[**Settings.defaultFrame**](settings-defaultframe.md)
</dt> <dt>

[**Settings.invokeURLs**](settings-invokeurls.md)
</dt> </dl>

 

 





