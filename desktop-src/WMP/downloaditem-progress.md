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
ms.date: 05/31/2018
---

# DownloadItem.progress

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

 

 





