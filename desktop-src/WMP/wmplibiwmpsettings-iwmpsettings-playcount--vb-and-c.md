---
title: IWMPSettings playCount property
description: The playCount property gets or sets the number of times a media item will play.
ms.assetid: 5d18909d-8b7a-448e-b54a-23a312041066
keywords:
- playCount property Windows Media Player
- playCount property Windows Media Player , IWMPSettings interface
- IWMPSettings interface Windows Media Player , playCount property
topic_type:
- apiref
api_name:
- IWMPSettings.playCount
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPSettings::playCount property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **playCount** property gets or sets the number of times a media item will play.

## Syntax


```CSharp
public System.Int32 playCount {get; set;}
```


```VB

Public Property playCount As System.Int32
```





## Property value

A **System.Int32** that is the play count, with a minimum value of 1 and a default value of 1.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPSettings Interface (VB and C#)**](iwmpsettings--vb-and-c.md)
</dt> </dl>

 

 





