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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DownloadItem.type

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





