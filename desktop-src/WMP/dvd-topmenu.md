---
title: DVD.topMenu method
description: The topMenu method stops title playback and displays the top (or root) menu for the current title.
ms.assetid: 9998e8d1-e5e7-4003-bf27-da319a1a3058
keywords:
- topMenu method Windows Media Player
- topMenu method Windows Media Player , DVD class
- DVD class Windows Media Player , topMenu method
topic_type:
- apiref
api_name:
- DVD.topMenu
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# DVD.topMenu method

The **topMenu** method stops title playback and displays the top (or root) menu for the current title.

## Syntax


```JScript
DVD.topMenu()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Every DVD is authored differently. The DVD must contain a menu for this method to work. Some DVDs are authored so that the **topMenu** and **titleMenu** methods open the same menu. The **topMenu** method usually invokes the top (or root) menu but it may invoke the title menu instead, if there is no root menu available.

**Windows Media Player 10 Mobile:** This method always succeeds, but does not perform the intended operation.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Version<br/>                  | Windows Media Player for Windows XP or later.<br/>                           |
| DLL<br/>                      | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**DVD Object**](dvd-object.md)
</dt> <dt>

[**DVD.titleMenu**](dvd-titlemenu.md)
</dt> </dl>

 

 





