---
title: AxWindowsMediaPlayer.Error property
description: The Error property gets the IWMPError interface that provides access to a collection of IWMPErrorItem interfaces.
ms.assetid: 9acc9252-d9c6-48a7-95a3-b1dddce93795
keywords:
- Error property Windows Media Player
- Error property Windows Media Player , AxWindowsMediaPlayer class
- AxWindowsMediaPlayer class Windows Media Player , Error property
topic_type:
- apiref
api_name:
- AxWindowsMediaPlayer.Error
api_location:
- AxInterop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AxWindowsMediaPlayer.Error property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Error property gets the IWMPError interface that provides access to a collection of IWMPErrorItem interfaces.

This property is read-only.

## Syntax


```CSharp
public IWMPError Error {get;}
```


```VB

Public ReadOnly Property Error As IWMPError
```





## Property value

The WMPLib.IWMPError interface.

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

[**IWMPError Interface (VB and C#)**](iwmperror--vb-and-c.md)
</dt> <dt>

[**IWMPErrorItem Interface (VB and C#)**](iwmperroritem--vb-and-c.md)
</dt> </dl>

 

 





