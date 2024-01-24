---
title: DownloadManager.getDownloadCollection method
description: Note This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The getDownloadCollection method retrieves the specified download collection.
ms.assetid: 743d6bcf-2d5b-4a30-a4ef-4538cf7c901e
keywords:
- getDownloadCollection method Windows Media Player
- getDownloadCollection method Windows Media Player , DownloadManager class
- DownloadManager class Windows Media Player , getDownloadCollection method
topic_type:
- apiref
api_name:
- DownloadManager.getDownloadCollection
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DownloadManager.getDownloadCollection method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **getDownloadCollection** method retrieves the specified download collection.

## Syntax


```JScript
retVal = DownloadManager.getDownloadCollection(
  collectionId
)
```



## Parameters

<dl> <dt>

*collectionId* \[in\]
</dt> <dd>

**Number** (**long**) specifying the ID of the download collection to retrieve.

</dd> </dl>

## Return value

This method returns a **DownloadCollection** object.

## Remarks

You must first call *DownloadManager*.**createDownloadCollection** to create a new collection and retrieve its ID value.

An existing download collection may contain items that have been marked as cancelled.

Real-time download items not completed in a prior session are not retrieved as part of the collection. Background downloads that were completed prior to the current session remain in the download collection until removed.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/>                                  |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**DownloadManager Object**](downloadmanager-object.md)
</dt> <dt>

[**DownloadManager. createDownloadCollection**](downloadmanager-createdownloadcollection.md)
</dt> <dt>

[**DownloadCollection Object**](downloadcollection-object.md)
</dt> </dl>

 

 





