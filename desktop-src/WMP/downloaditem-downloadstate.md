---
title: DownloadItem.downloadState
description: Note This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The downloadState property retrieves the state of the download.
ms.assetid: dde27f43-40ee-4eb9-b316-42312ee937d0
keywords:
- DownloadItem.downloadState Windows Media Player
topic_type:
- apiref
api_name:
- DownloadItem.downloadState
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DownloadItem.downloadState

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **downloadState** property retrieves the state of the download.

## Syntax

``` syntax
DownloadManager.getDownloadCollection(
        collectionId
        ).item(
        itemId
        ).downloadState
      
```

## Possible Values

This property is a read-only **Number** containing one of the following values.



| Value | Description |
|-------|-------------|
| 0     | Downloading |
| 1     | Paused      |
| 2     | Processing  |
| 3     | Completed   |
| 4     | Canceled    |



 

## Remarks

Download states can occur in any order. Do not write code that depends on the occurrence of any particular download state.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/>                                  |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**DownloadItem Object**](downloaditem-object.md)
</dt> </dl>

 

 





