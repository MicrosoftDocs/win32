---
title: DownloadItem.sourceURL
description: Note This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The sourceURL property retrieves the source URL of the download.
ms.assetid: 87af20a5-5721-498d-8417-3e7dbbec38a2
keywords:
- DownloadItem.sourceURL Windows Media Player
topic_type:
- apiref
api_name:
- DownloadItem.sourceURL
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# DownloadItem.sourceURL

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **sourceURL** property retrieves the source URL of the download.

## Syntax

``` syntax
DownloadManager.getDownloadCollection(
        collectionId
        ).item(
        itemId
        ).sourceURL
      
```

## Possible Values

This property is a read-only **String**.

## Remarks

Only the following digital media formats can be downloaded:

-   Advanced Systems Format (ASF)
-   MP3
-   Windows Media Audio (WMA)
-   Windows Media Video (WMV)

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**DownloadItem Object**](downloaditem-object.md)
</dt> </dl>

 

 





