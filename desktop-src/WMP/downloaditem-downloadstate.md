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
ms.date: 05/31/2018
---

# DownloadItem.downloadState

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

 

 





