---
title: External.play method
description: Note This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The play method instructs Windows Media Player to play a set of media items.
ms.assetid: 3e1f45db-9e7f-4a1b-aaa2-513a19c46f70
keywords:
- play method Windows Media Player
- play method Windows Media Player , External class
- External class Windows Media Player , play method
topic_type:
- apiref
api_name:
- External.play
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# External.play method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **play** method instructs Windows Media Player to play a set of media items.

## Syntax


```JScript
External.play(
  LibraryLocationType,
  LibraryLocationIDs
)
```



## Parameters

<dl> <dt>

*LibraryLocationType* \[in\]
</dt> <dd>

A [library location constant](library-location-constants.md) that specifies the type of the media items to be played. For example, CPAlbumID specifies that one or more albums are to be played.

</dd> <dt>

*LibraryLocationIDs* \[in\]
</dt> <dd>

**String** containing the identifiers, delimited by semicolons, of the media items to be played.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> </dl>

 

 





