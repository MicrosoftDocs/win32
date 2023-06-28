---
title: IWMPCdromBurn burnState property
description: The burnState property gets an enumeration value that indicates the current burn state.
ms.assetid: 2bb543f9-9e4c-4425-99d6-ac89ef7f5807
keywords:
- burnState property Windows Media Player
- burnState property Windows Media Player , IWMPCdromBurn interface
- IWMPCdromBurn interface Windows Media Player , burnState property
topic_type:
- apiref
api_name:
- IWMPCdromBurn.burnState
- IWMPCdromBurn.get_burnState
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPCdromBurn::burnState property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **burnState** property gets an enumeration value that indicates the current burn state.

This property is read-only.

## Syntax


```CSharp
public WMPBurnState burnState {get;}
```


```VB

Public ReadOnly Property burnState As WMPBurnState
```





## Property value

A **WMPLib.WMPBurnState** that is a value from the **WMPBurnState** enumeration that indicates the current state.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11.<br/>                                                                                    |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPCdromBurn Interface (VB and C#)**](iwmpcdromburn--vb-and-c.md)
</dt> <dt>

[**WMPBurnState**](/previous-versions/windows/desktop/api/wmp/ne-wmp-wmpburnstate)
</dt> </dl>

 

 





