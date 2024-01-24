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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DownloadItem.sourceURL

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





