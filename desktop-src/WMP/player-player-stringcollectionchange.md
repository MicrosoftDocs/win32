---
title: Player.StringCollectionChange event
description: The StringCollectionChange event occurs when a string collection changes. | Player.StringCollectionChange event
ms.assetid: 465ec694-afd1-4baa-b559-3ab75874388f
keywords:
- StringCollectionChange event Windows Media Player
- StringCollectionChange event Windows Media Player , Player class
- Player class Windows Media Player , StringCollectionChange event
topic_type:
- apiref
api_name:
- Player.StringCollectionChange
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Player.StringCollectionChange event

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The StringCollectionChange event occurs when a string collection changes.

## Syntax


```JScript
Player.StringCollectionChange(
  pdispStringCollection,
  change,
  lCollectionIndex
)
```



## Parameters

<dl> <dt>

*pdispStringCollection* 
</dt> <dd>

**StringCollection** object that changed.

</dd> <dt>

*change* 
</dt> <dd>

Number (long)indicating the type of change that occurred to the string collection. Includes one of the following values.



| Number | Description                        |
|--------|------------------------------------|
| 0      | Unknown. (Not a valid value)       |
| 1      | An item was inserted.              |
| 2      | The string collection changed.     |
| 3      | An item was deleted.               |
| 4      | The string collection was cleared. |
| 5      | Bulk updates are beginning.        |
| 6      | Bulk updates have ended.           |



 

</dd> <dt>

*lCollectionIndex* 
</dt> <dd>

Number (long) containing the index of the string collection item that changed.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

**Windows Media Player 10 Mobile:** This event is not supported.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> <dt>

[**StringCollection Object**](stringcollection-object.md)
</dt> </dl>

 

 





