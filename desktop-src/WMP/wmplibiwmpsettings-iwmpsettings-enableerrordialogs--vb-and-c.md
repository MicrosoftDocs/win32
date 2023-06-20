---
title: IWMPSettings enableErrorDialogs property
description: The enableErrorDialogs property gets or sets a value indicating whether error dialog boxes are displayed automatically.
ms.assetid: 5310864b-e250-4fb1-8351-d1d7de312f21
keywords:
- enableErrorDialogs property Windows Media Player
- enableErrorDialogs property Windows Media Player , IWMPSettings interface
- IWMPSettings interface Windows Media Player , enableErrorDialogs property
topic_type:
- apiref
api_name:
- IWMPSettings.enableErrorDialogs
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPSettings::enableErrorDialogs property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **enableErrorDialogs** property gets or sets a value indicating whether error dialog boxes are displayed automatically.

## Syntax


```CSharp
public System.Boolean enableErrorDialogs {get; set;}
```


```VB

Public Property enableErrorDialogs As System.Boolean
```





## Property value

A **System.Boolean** value indicating whether error dialog boxes are displayed automatically. The default is **true**.

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

 

 





