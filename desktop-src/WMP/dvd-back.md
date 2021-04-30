---
title: DVD.back method
description: The back method returns the display from a submenu to its parent menu.
ms.assetid: 4b6c3562-6484-4ef0-8c5c-c24d88e02096
keywords:
- back method Windows Media Player
- back method Windows Media Player , DVD class
- DVD class Windows Media Player , back method
topic_type:
- apiref
api_name:
- DVD.back
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# DVD.back method

The **back** method returns the display from a submenu to its parent menu.

## Syntax


```JScript
DVD.back()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Every DVD is authored differently. Some DVDs are authored so that the **back** method is available from the root menu, but when invoked, it will do nothing.

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
</dt> </dl>

 

 





