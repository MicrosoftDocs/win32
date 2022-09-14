---
title: DownloadItem Object
description: DownloadItem Object
ms.assetid: 668ee632-0a3d-426b-baab-08e88b9fc607
keywords:
- Windows Media Player online stores,DownloadItem object
- online stores,DownloadItem object
- type 2 online stores,DownloadItem object
- DownloadItem
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# DownloadItem Object

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **DownloadItem** object represents a file download request. It can be used by webpages that are hosted in the full mode Windows Media Player and that have access to the **External** object, such as premium services.

The **DownloadItem** object supports the following properties.



| Property                                        | Description                                      |
|-------------------------------------------------|--------------------------------------------------|
| [downloadState](downloaditem-downloadstate.md) | Retrieves the state of the download.             |
| [progress](downloaditem-progress.md)           | Retrieves the progress of the download in bytes. |
| [size](downloaditem-size.md)                   | Retrieves the size of the download.              |
| [sourceURL](downloaditem-sourceurl.md)         | Retrieves the source URL of the download.        |
| [type](downloaditem-type.md)                   | Retrieves the type of the download.              |



 

The **DownloadItem** object supports the following methods.



| Method                                      | Description                                                |
|---------------------------------------------|------------------------------------------------------------|
| [cancel](downloaditem-cancel.md)           | Cancels the download.                                      |
| [getItemInfo](downloaditem-getiteminfo.md) | Retrieves the value of an attribute for the download item. |
| [pause](downloaditem-pause.md)             | Pauses the download.                                       |
| [resume](downloaditem-resume.md)           | Resumes the download.                                      |



 

The **DownloadItem** object is accessed through the following property.



| Object                                              | Property                            |
|-----------------------------------------------------|-------------------------------------|
| [DownloadCollection](downloadcollection-object.md) | [item](downloadcollection-item.md) |



 

For purposes of illustration, **DownloadManager**.**getDownloadCollection**(*collectionId*).**item**(*itemId*) is used in the reference syntax sections.

## Related topics

<dl> <dt>

[**Reference for Type 2 Online Stores**](reference-for-type-2-online-stores.md)
</dt> </dl>

 

 




