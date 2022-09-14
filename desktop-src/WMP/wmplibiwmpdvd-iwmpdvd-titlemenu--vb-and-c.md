---
title: IWMPDVD titleMenu method
description: The titleMenu method stops playback and displays the title menu.
ms.assetid: 28714644-12c4-46eb-95fc-70091624f6dd
keywords:
- titleMenu method Windows Media Player
- titleMenu method Windows Media Player , IWMPDVD interface
- IWMPDVD interface Windows Media Player , titleMenu method
topic_type:
- apiref
api_name:
- IWMPDVD.titleMenu
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPDVD::titleMenu method

The **titleMenu** method stops playback and displays the title menu.

## Syntax


```CSharp
public void titleMenu();
```


```VB

Public Sub titleMenu()
Implements IWMPDVD.titleMenu
```





## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Every DVD is authored differently. The DVD must contain a menu for this method to work. Some DVDs are authored so that the **IWMPDVD.topMenu** and **titleMenu** methods open the same menu. The **titleMenu** method usually invokes the title menu, but it may invoke the top menu if there is no title menu available.

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

[**IWMPDVD.topMenu (VB and C#)**](wmplibiwmpdvd-iwmpdvd-topmenu--vb-and-c.md)
</dt> </dl>

 

 





