---
title: IWMPCdromRip ripState property
description: The ripState property gets an enumeration value that indicates the current state of the ripping process.
ms.assetid: eacf36d9-725c-47cf-9f90-6241feeb67bc
keywords:
- ripState property Windows Media Player
- ripState property Windows Media Player , IWMPCdromRip interface
- IWMPCdromRip interface Windows Media Player , ripState property
topic_type:
- apiref
api_name:
- IWMPCdromRip.ripState
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPCdromRip::ripState property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **ripState** property gets an enumeration value that indicates the current state of the ripping process.

## Syntax


```CSharp
public WMPRipState ripState {get; set;}
```


```VB

Public ReadOnly Property ripState As WMPRipState
```





## Property value

A **WMPLib.WMPRipState** that is a value from the **WMPRipState** enumeration that indicates the current state.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11.<br/>                                                                                    |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPCdromRip Interface (VB and C#)**](iwmpcdromrip--vb-and-c.md)
</dt> <dt>

[**Ripping a CD**](ripping-a-cd.md)
</dt> <dt>

[**WMPRipState**](/previous-versions/windows/desktop/api/wmp/ne-wmp-wmpripstate)
</dt> </dl>

 

 





