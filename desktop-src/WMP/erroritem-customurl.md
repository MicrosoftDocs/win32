---
title: ErrorItem.customUrl
description: The customURL property retrieves the URL of a website that displays specific information about codec download failure.
ms.assetid: 51028f45-2ce6-4e57-86bd-d7c2d8fb3af8
keywords:
- ErrorItem.customUrl Windows Media Player
topic_type:
- apiref
api_name:
- ErrorItem.customUrl
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# ErrorItem.customUrl

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **customURL** property retrieves the URL of a website that displays specific information about codec download failure.

``` syntax
player.error.item(
        index
        ).customURL
      
```

## Possible Values

This property is a read-only **String**.

## Remarks

**Windows Media Player 10 Mobile:** This property always returns an empty string.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**ErrorItem Object**](erroritem-object.md)
</dt> </dl>

 

 





