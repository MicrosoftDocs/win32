---
title: IWMPSettings invokeURLs property
description: The invokeURLs property gets or sets a value indicating whether URL events should launch a Web browser.
ms.assetid: e16c968d-a1b7-4c3a-9c1a-5748ed44cdac
keywords:
- invokeURLs property Windows Media Player
- invokeURLs property Windows Media Player , IWMPSettings interface
- IWMPSettings interface Windows Media Player , invokeURLs property
topic_type:
- apiref
api_name:
- IWMPSettings.invokeURLs
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPSettings::invokeURLs property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **invokeURLs** property gets or sets a value indicating whether URL events should launch a Web browser.

## Syntax


```CSharp
public System.Boolean invokeURLs {get; set;}
```


```VB

Public Property invokeURLs As System.Boolean
```





## Property value

A **System.Boolean** value indicating whether URL events should launch a Web browser. The default is **true**.

## Remarks

Digital media files and streams can contain URL script commands. When a URL script command is sent to the Windows Media Player control, it is passed first to the **AxWindowsMediaPlayer\_WMPOCXEvents\_ScriptCommandEvent** event handler regardless of the value retrieved by **invokeURLs**. After **\_WMPOCXEvents\_ScriptCommandEvent** exits, Windows Media Player checks **invokeURLs** to determine whether to launch the default Web browser with the URL. You can selectively display URLs by checking them in **\_WMPOCXEvents\_ScriptCommandEvent** and setting **invokeURLs** as desired.

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

 

 





