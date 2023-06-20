---
title: External.saveCurrentViewToLibrary method
description: The saveCurrentViewToLibrary method creates a playlist from the media items in the current view and saves the playlist in the local library.
ms.assetid: cd87e932-d599-4298-bbee-6755999dda15
keywords:
- saveCurrentViewToLibrary method Windows Media Player
- saveCurrentViewToLibrary method Windows Media Player , External class
- External class Windows Media Player , saveCurrentViewToLibrary method
topic_type:
- apiref
api_name:
- External.saveCurrentViewToLibrary
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# External.saveCurrentViewToLibrary method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **saveCurrentViewToLibrary** method creates a playlist from the media items in the current view and saves the playlist in the local library.

## Syntax


```JScript
External.saveCurrentViewToLibrary(
  FriendlyListName,
  Local
)
```



## Parameters

<dl> <dt>

*FriendlyListName* \[in\]
</dt> <dd>

**String** that specifies a friendly name for the playlist. Windows Media Player displays this name in its user interface.

</dd> <dt>

*Local* \[in\]
</dt> <dd>

**Boolean** that specifies whether the playlist is dynamic or static. **TRUE** specifies dynamic, and **FALSE** specifies static.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11<br/>                                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> </dl>

 

 





