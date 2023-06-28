---
title: IWMPDVD topMenu method
description: The topMenu method stops playback and displays the top (or root) menu for the current title.
ms.assetid: d6eb6311-167d-4cc1-b445-4e3d3e111e43
keywords:
- topMenu method Windows Media Player
- topMenu method Windows Media Player , IWMPDVD interface
- IWMPDVD interface Windows Media Player , topMenu method
topic_type:
- apiref
api_name:
- IWMPDVD.topMenu
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPDVD::topMenu method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **topMenu** method stops playback and displays the top (or root) menu for the current title.

## Syntax


```CSharp
public void topMenu();
```


```VB

Public Sub topMenu()
Implements IWMPDVD.topMenu
```





## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Every DVD is authored differently. The DVD must contain a menu for this method to work. Some DVDs are authored so that the **topMenu** and **IWMPDVD.titleMenu** methods open the same menu. The **topMenu** method usually invokes the top (or root) menu, but it may invoke the title menu if there is no root menu available.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPDVD Interface (VB and C#)**](iwmpdvd--vb-and-c.md)
</dt> <dt>

[**IWMPDVD.titleMenu (VB and C#)**](wmplibiwmpdvd-iwmpdvd-titlemenu--vb-and-c.md)
</dt> </dl>

 

 





