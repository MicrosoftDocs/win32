---
title: IWMPSettings balance property
description: The balance property gets or sets the current stereo balance.
ms.assetid: 6b9b6305-3bab-418d-a172-d47ca4dbaba5
keywords:
- balance property Windows Media Player
- balance property Windows Media Player , IWMPSettings interface
- IWMPSettings interface Windows Media Player , balance property
topic_type:
- apiref
api_name:
- IWMPSettings.balance
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPSettings::balance property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **balance** property gets or sets the current stereo balance.

## Syntax


```CSharp
public System.Int32 balance {get; set;}
```


```VB

Public Property balance As System.Int32
```





## Property value

A **System.Int32** that is the balance value. This value can range from  100 to 100. The default value is zero.

## Remarks

The value zero indicates that the audio plays at equal volume on both left and right channels. A value of  100 indicates that audio plays only on the left channel. A value of 100 indicates that audio plays only on the right channel.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later.<br/>                                                                     |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPSettings Interface (VB and C#)**](iwmpsettings--vb-and-c.md)
</dt> </dl>

 

 





