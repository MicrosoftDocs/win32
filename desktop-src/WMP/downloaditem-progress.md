---
title: DownloadItem.progress
description: Note This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The progress property retrieves the progress of the download in bytes.
ms.assetid: 58644eac-8dd0-4e9d-8055-03833c863a6e
keywords:
- DownloadItem.progress Windows Media Player
topic_type:
- apiref
api_name:
- DownloadItem.progress
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DownloadItem.progress

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **progress** property retrieves the progress of the download in bytes.

## Syntax

``` syntax
DownloadManager.getDownloadCollection(
        collectionId
        ).item(
        itemId
        ).progress
      
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

[**DownloadItem Object**](downloaditem-object.md)
</dt> <dt>

[**DownloadItem.size**](downloaditem-size.md)
</dt> </dl>

 

 





