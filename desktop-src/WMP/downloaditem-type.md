---
title: DownloadItem.type
description: Note This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The type property retrieves the type of the download.
ms.assetid: 58ffb8a3-5410-492b-bb0f-9130ed209b78
keywords:
- DownloadItem.type Windows Media Player
topic_type:
- apiref
api_name:
- DownloadItem.type
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# DownloadItem.type

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **type** property retrieves the type of the download.

## Syntax

``` syntax
DownloadManager.getDownloadCollection(
        collectionId
        ).item(
        itemId
        ).type
      
```

## Possible Values

This property is a read-only **String** containing one of the following values.



| Value      | Description                                                                                                                                                                            |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| background | (Windows XP only.) The download occurs as a background process as processor time becomes available. Download states persist even when Windows Media Player or Windows XP is shut down. |
| real time  | (All supported operating systems.) The download occurs all at once. No download states persist between sessions.                                                                       |



 

## Remarks

Each type of download has advantages and disadvantages. Background downloading allows the user to proceed to other tasks and even restart Windows without cancelling the download, but takes more time overall to complete the download and is only supported for Windows XP. Real-time downloading takes less time to complete, but requires the user to finish all downloading before closing Windows Media Player.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/>                                  |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**DownloadItem Object**](downloaditem-object.md)
</dt> </dl>

 

 





