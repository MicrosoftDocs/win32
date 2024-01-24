---
title: AxWindowsMediaPlayer.Ctlcontrols property
description: The Ctlcontrols property gets an IWMPControls interface that provides a way to manipulate the playback of a media item.
ms.assetid: 0f0067e5-91bb-4179-a054-51f709b90c01
keywords:
- Ctlcontrols property Windows Media Player
- Ctlcontrols property Windows Media Player , AxWindowsMediaPlayer class
- AxWindowsMediaPlayer class Windows Media Player , Ctlcontrols property
topic_type:
- apiref
api_name:
- AxWindowsMediaPlayer.Ctlcontrols
api_location:
- AxInterop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AxWindowsMediaPlayer.Ctlcontrols property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Ctlcontrols property gets an IWMPControls interface that provides a way to manipulate the playback of a media item.

This property is read-only.

## Syntax


```CSharp
public IWMPControls Ctlcontrols {get;}
```


```VB

Public ReadOnly Property Ctlcontrols As IWMPControls
```





## Property value

The WMPLIB.IWMPControls interface.

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

[**IWMPControls Interface (VB and C#)**](iwmpcontrols--vb-and-c.md)
</dt> </dl>

 

 





