---
title: AxWindowsMediaPlayer.dvd property
description: The dvd property gets an IWMPDVD interface that provides properties and methods for working with DVDs.
ms.assetid: a1cafa04-33b6-42ff-86db-3ffc7f056907
keywords:
- dvd property Windows Media Player
- dvd property Windows Media Player , AxWindowsMediaPlayer class
- AxWindowsMediaPlayer class Windows Media Player , dvd property
topic_type:
- apiref
api_name:
- AxWindowsMediaPlayer.dvd
api_location:
- AxInterop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AxWindowsMediaPlayer.dvd property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The dvd property gets an IWMPDVD interface that provides properties and methods for working with DVDs.

This property is read-only.

## Syntax


```CSharp
public IWMPDVD dvd {get;}
```


```VB

Public ReadOnly Property dvd As IWMPDVD
```





## Property value

The WMPLib.IWMPDVD interface.

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

[**IWMPDVD Interface (VB and C#)**](iwmpdvd--vb-and-c.md)
</dt> </dl>

 

 





