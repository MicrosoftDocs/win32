---
title: IWMPSettings defaultFrame property
description: The defaultFrame property gets or sets the name of the frame used to display a URL that is received in an AxWindowsMediaPlayer\_WMPOCXEvents\_ScriptCommandEvent event.
ms.assetid: 92c775ac-5ff1-4d21-b21d-491bc48a033f
keywords:
- defaultFrame property Windows Media Player
- defaultFrame property Windows Media Player , IWMPSettings interface
- IWMPSettings interface Windows Media Player , defaultFrame property
topic_type:
- apiref
api_name:
- IWMPSettings.defaultFrame
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPSettings::defaultFrame property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **defaultFrame** property gets or sets the name of the frame used to display a URL that is received in an **AxWindowsMediaPlayer\_WMPOCXEvents\_ScriptCommandEvent** event.

## Syntax


```CSharp
public System.String defaultFrame {get; set;}
```


```VB

Public Property defaultFrame As System.String
```





## Property value

A **System.String** that is the value of the name attribute of the target **FRAME** element.

## Remarks

If a target frame is specified in the **\_WMPOCXEvents\_ScriptCommandEvent** event itself, this property is ignored.

This property is ignored when using the Netscape Navigator Java applet. In Netscape Navigator, each URL script command received will display the URL in a new browser window, regardless of the value of **defaultFrame**.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer.ScriptCommand Event (VB and C#)**](axwmplib-axwindowsmediaplayer-scriptcommand.md)
</dt> <dt>

[**IWMPSettings Interface (VB and C#)**](iwmpsettings--vb-and-c.md)
</dt> </dl>

 

 





