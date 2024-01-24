---
title: IWMPNetwork maxBitRate property
description: The maxBitRate property gets the maximum possible video bit rate.
ms.assetid: 5a4c984a-a692-49f4-9539-d9bec269dba8
keywords:
- maxBitRate property Windows Media Player
- maxBitRate property Windows Media Player , IWMPNetwork interface
- IWMPNetwork interface Windows Media Player , maxBitRate property
topic_type:
- apiref
api_name:
- IWMPNetwork.maxBitRate
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPNetwork::maxBitRate property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **maxBitRate** property gets the maximum possible video bit rate.

## Syntax


```CSharp
public System.Int32 maxBitRate {get; set;}
```


```VB

Public ReadOnly Property maxBitRate As System.Int32
```





## Property value

A **System.Int32** that is the maximum bit rate.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPNetwork Interface (VB and C#)**](iwmpnetwork--vb-and-c.md)
</dt> </dl>

 

 





