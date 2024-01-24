---
title: AxWindowsMediaPlayer.Ctlenabled property
description: The Ctlenabled property gets or sets a value indicating whether the Windows Media Player control is enabled.
ms.assetid: 2091e529-551a-4c02-9384-51b774c82ee6
keywords:
- Ctlenabled property Windows Media Player
- Ctlenabled property Windows Media Player , AxWindowsMediaPlayer class
- AxWindowsMediaPlayer class Windows Media Player , Ctlenabled property
topic_type:
- apiref
api_name:
- AxWindowsMediaPlayer.Ctlenabled
api_location:
- AxInterop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AxWindowsMediaPlayer.Ctlenabled property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Ctlenabled property gets or sets a value indicating whether the Windows Media Player control is enabled.

## Syntax


```CSharp
public System.Boolean Ctlenabled {get; set;}
```


```VB

Public Property Ctlenabled As System.Boolean
```





## Property value

A System.Boolean value that indicates whether the Windows Media Player control is enabled. The default value is true.

## Remarks

If the **Ctlenabled** property is set to false, then Windows Media Player hides the user controls during full-screen playback.

## Requirements



| Requirement | Value |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                          |
| Namespace<br/> | **AxWMPLib**<br/>                                                                                                    |
| Assembly<br/>  | <dl> <dt>AxInterop.WMPLib.dll (AxInterop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer Object (VB and C#)**](axwindowsmediaplayer-object--vb-and-c.md)
</dt> </dl>

 

 





