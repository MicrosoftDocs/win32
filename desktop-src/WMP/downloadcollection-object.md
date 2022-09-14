---
title: DownloadCollection Object
description: DownloadCollection Object
ms.assetid: e943b391-386e-43c5-a314-55ea31b2eefa
keywords:
- Windows Media Player online stores,DownloadCollection object
- online stores,DownloadCollection object
- type 2 online stores,DownloadCollection object
- DownloadCollection
ms.topic: article
ms.date: 05/31/2018
---

# DownloadCollection Object

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **DownloadCollection** object contains properties and methods to handle collections of download items. It can be used by webpages that are hosted in the full mode Windows Media Player and that have access to the **External** object, such as online stores.

The **DownloadCollection** object supports the following properties.



| Property                              | Description                                  |
|---------------------------------------|----------------------------------------------|
| [count](downloadcollection-count.md) | Retrieves the number of pending downloads.   |
| [id](downloadcollection-id.md)       | Retrieves the ID of the download collection. |



 

The **DownloadCollection** object supports the following methods.



| Method                                                | Description                                   |
|-------------------------------------------------------|-----------------------------------------------|
| [Clear](downloadcollection-clear.md)                 | Removes all items from a download collection. |
| [item](downloadcollection-item.md)                   | Retrieves a pending download object.          |
| [removeItem](downloadcollection-removeitem.md)       | Removes a download item from a collection.    |
| [startDownload](downloadcollection-startdownload.md) | Queues a download.                            |



 

The **DownloadCollection** object is accessed through the following methods.



| Object                                        | Method                                                                   |
|-----------------------------------------------|--------------------------------------------------------------------------|
| [DownloadManager](downloadmanager-object.md) | [createDownloadCollection](downloadmanager-createdownloadcollection.md) |
| [DownloadManager](downloadmanager-object.md) | [getDownloadCollection](downloadmanager-getdownloadcollection.md)       |



 

For purposes of illustration, **DownloadManager**.**getDownloadCollection**(*collectionId*) is used in the reference syntax sections.

## Related topics

<dl> <dt>

[**Reference for Type 2 Online Stores**](reference-for-type-2-online-stores.md)
</dt> </dl>

 

 




