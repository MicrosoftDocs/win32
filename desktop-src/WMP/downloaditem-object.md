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
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# DownloadItem Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




