---
title: AxWindowsMediaPlayer.closedCaption property
description: The closedCaption property gets an IWMPClosedCaption interface for the current media item.
ms.assetid: 459a04fd-daf5-46f9-925b-02011bbbf640
keywords:
- closedCaption property Windows Media Player
- closedCaption property Windows Media Player , AxWindowsMediaPlayer class
- AxWindowsMediaPlayer class Windows Media Player , closedCaption property
topic_type:
- apiref
api_name:
- AxWindowsMediaPlayer.closedCaption
api_location:
- AxInterop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AxWindowsMediaPlayer.closedCaption property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The closedCaption property gets an **IWMPClosedCaption** interface for the current media item.

This property is read-only.

## Syntax


```CSharp
public IWMPClosedCaption closedCaption {get;}
```


```VB

Public ReadOnly Property closedCaption As IWMPClosedCaption
```





## Property value

The WMPLIB.IWMPClosedCaption interface.

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

[**IWMPClosedCaption Interface (VB and C#)**](iwmpclosedcaption--vb-and-c.md)
</dt> </dl>

 

 





