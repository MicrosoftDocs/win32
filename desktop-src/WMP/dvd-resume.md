---
title: DVD.resume method
description: The resume method returns to playback mode from menu mode at the same title position as when the menu was invoked.
ms.assetid: ba8b3c05-d33b-41b3-b5dd-a693a7b1fb4b
keywords:
- resume method Windows Media Player
- resume method Windows Media Player , DVD class
- DVD class Windows Media Player , resume method
topic_type:
- apiref
api_name:
- DVD.resume
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DVD.resume method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **resume** method returns to playback mode from menu mode at the same title position as when the menu was invoked.

## Syntax


```JScript
DVD.resume()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

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

 

 





