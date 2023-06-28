---
title: DownloadCollection.count
description: Note This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The count property retrieves the number of pending downloads in the collection.
ms.assetid: 8f9245aa-6d92-4dd3-9b45-97ee37de680d
keywords:
- DownloadCollection.count Windows Media Player
topic_type:
- apiref
api_name:
- DownloadCollection.count
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DownloadCollection.count

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **count** property retrieves the number of pending downloads in the collection.

## Syntax

``` syntax
DownloadManager.getDownloadCollection(
        collectionId
        ).count
      
```

## Possible Values

This property is a read-only **Number** (**long**).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/>                                  |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**DownloadCollection Object**](downloadcollection-object.md)
</dt> </dl>

 

 





