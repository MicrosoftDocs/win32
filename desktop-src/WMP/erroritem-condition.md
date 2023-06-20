---
title: ErrorItem.condition
description: The condition property retrieves a value indicating the condition for the error.
ms.assetid: efb54b48-cfaa-479f-9ee6-ce6724dca24c
keywords:
- ErrorItem.condition Windows Media Player
topic_type:
- apiref
api_name:
- ErrorItem.condition
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# ErrorItem.condition

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **condition** property retrieves a value indicating the condition for the error.

``` syntax
player.error.item(
        index
        ).condition
      
```

## Possible Values

This property is a read-only **Number** (**long**) that represents the condition code.

## Remarks

The condition code is a value that is used by Microsoft to provide additional information for technical support personnel.

**Windows Media Player 10 Mobile:** This property always returns 0.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**ErrorItem Object**](erroritem-object.md)
</dt> </dl>

 

 





