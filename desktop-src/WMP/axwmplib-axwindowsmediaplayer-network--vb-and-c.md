---
title: AxWindowsMediaPlayer.network property
description: The network property gets an IWMPNetwork interface that provides access to network information and settings.
ms.assetid: 0a6c4a8c-8759-47d4-be03-9909a8460e71
keywords:
- network property Windows Media Player
- network property Windows Media Player , AxWindowsMediaPlayer class
- AxWindowsMediaPlayer class Windows Media Player , network property
topic_type:
- apiref
api_name:
- AxWindowsMediaPlayer.network
api_location:
- AxInterop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AxWindowsMediaPlayer.network property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The network property gets an IWMPNetwork interface that provides access to network information and settings.

This property is read-only.

## Syntax


```CSharp
public IWMPNetwork network {get;}
```


```VB

Public ReadOnly Property network As IWMPNetwork
```





## Property value

The WMPLib.IWMPNetwork interface.

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

[**IWMPNetwork Interface (VB and C#)**](iwmpnetwork--vb-and-c.md)
</dt> </dl>

 

 





