---
title: External.filter
description: Note This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The filter property retrieves the search filter currently in use by Windows Media Player.
ms.assetid: 45084dd2-fe57-4ab1-86d8-c5f39c282573
keywords:
- External.filter Windows Media Player
topic_type:
- apiref
api_name:
- External.filter
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# External.filter

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **filter** property retrieves the search filter currently in use by Windows Media Player.

``` syntax
window.external.filter
      
```

## Possible Values

This property is a read-only **String**.

## Remarks

The search filter is the text that the user enters in the Player's word wheel control.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> </dl>

 

 





