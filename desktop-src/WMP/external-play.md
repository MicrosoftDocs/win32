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
ms.date: 05/31/2018
---

# External.play method

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

 

 





