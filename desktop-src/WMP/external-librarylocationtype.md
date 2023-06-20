---
title: External.libraryLocationType
description: Note This topic describes functionality designed for use by online stores. | External.libraryLocationType
ms.assetid: aaf20147-8331-40bd-a5cd-5ee9b8e2d022
keywords:
- External.libraryLocationType Windows Media Player
topic_type:
- apiref
api_name:
- External.libraryLocationType
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# External.libraryLocationType

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **libraryLocationType** property retrieves a [library location constant](library-location-constants.md) that indicates the type of the current view in Windows Media Player.

``` syntax
window.external.libraryLocationType
      
```

## Possible Values

This property is a read-only **String** that contains one of the library location constants.

## Remarks

This property works in combination with the [External.libraryLocationID](external-librarylocationid.md) property. For example, suppose **libraryLocationType** is equal to CPAlbumID and **libraryLocationID** is equal to 3. That means the current view in Windows Media Player is showing the album that has an ID of 3. For more information about how Windows Media Player characterizes views of online store content, see [Location and Selected Item](location-and-selected-item.md).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> <dt>

[**External.libraryLocationID**](external-librarylocationid.md)
</dt> <dt>

[**Location and Selected Item**](location-and-selected-item.md)
</dt> </dl>

 

 





