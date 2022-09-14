---
title: DVD.titleMenu method
description: The titleMenu method stops title playback and displays the title menu.
ms.assetid: 3be3e7cd-5969-4051-ae63-ff070a19fe51
keywords:
- titleMenu method Windows Media Player
- titleMenu method Windows Media Player , DVD class
- DVD class Windows Media Player , titleMenu method
topic_type:
- apiref
api_name:
- DVD.titleMenu
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# DVD.titleMenu method

The **titleMenu** method stops title playback and displays the title menu.

## Syntax


```JScript
DVD.titleMenu()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Every DVD is authored differently. The DVD must contain a menu for this method to work. Some DVDs are authored so that the **topMenu** and **titleMenu** methods open the same menu. The **titleMenu** method usually invokes the title menu but it may invoke the top menu instead, if there is no title menu available.

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

[**DVD.topMenu**](dvd-topmenu.md)
</dt> </dl>

 

 





