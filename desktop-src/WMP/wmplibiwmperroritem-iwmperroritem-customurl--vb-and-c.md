---
title: IWMPErrorItem customUrl property
description: The customUrl property gets the URL of a website that displays specific information about codec download failure.
ms.assetid: 638491da-f1e6-4d25-840e-24e6e2027c37
keywords:
- customUrl property Windows Media Player
- customUrl property Windows Media Player , IWMPErrorItem interface
- IWMPErrorItem interface Windows Media Player , customUrl property
topic_type:
- apiref
api_name:
- IWMPErrorItem.customUrl
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPErrorItem::customUrl property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **customUrl** property gets the URL of a website that displays specific information about codec download failure.

## Syntax


```CSharp
public System.String customUrl {get; set;}
```


```VB

Public ReadOnly Property customUrl As System.String
```





## Property value

A **System.String** that is the custom URL.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPErrorItem Interface (VB and C#)**](iwmperroritem--vb-and-c.md)
</dt> </dl>

 

 





