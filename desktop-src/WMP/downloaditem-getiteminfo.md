---
title: DownloadItem.getItemInfo method
description: Note This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The getItemInfo method retrieves the value of an attribute for the download item.
ms.assetid: da885611-b4a0-4264-8b32-13cc6f87d6e9
keywords:
- getItemInfo method Windows Media Player
- getItemInfo method Windows Media Player , DownloadItem class
- DownloadItem class Windows Media Player , getItemInfo method
topic_type:
- apiref
api_name:
- DownloadItem.getItemInfo
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# DownloadItem.getItemInfo method

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **getItemInfo** method retrieves the value of an attribute for the download item.

## Syntax


```JScript
strRetVal = DownloadItem.getItemInfo(
  itemname
)
```



## Parameters

<dl> <dt>

*itemname* \[in\]
</dt> <dd>

**String** containing the attribute name. Supported values are AlbumArtist, Album, Duration, WM/Provider, Title, UserRating, and WM/TrackNumber.

</dd> </dl>

## Return value

This method returns a **String** containing the value of the attribute specified by *itemname*.

## Remarks

This method retrieves attributes specified using the BITS description string. See [Windows Media Player BITS Job Convention](windows-media-player-bits-job-convention.md).

This method is supported for background downloading. Your code should not call this method when using real-time downloading.

This method can retrieve information for BITS jobs added during the current Windows Media Player session only.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 10 or later<br/>                                        |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**DownloadItem.type**](downloaditem-type.md)
</dt> <dt>

[**DownloadItem Object**](downloaditem-object.md)
</dt> </dl>

 

 





