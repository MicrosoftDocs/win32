---
title: DownloadManager Object
description: DownloadManager Object
ms.assetid: e6b07f3c-9254-41bb-9480-8167c3cd655b
keywords:
- Windows Media Player online stores,DownloadManager object
- online stores,DownloadManager object
- type 2 online stores,DownloadManager object
- DownloadManager
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# DownloadManager Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **DownloadManager** object is the root object for the Windows Media Player Download Manager. It can be used by webpages that are hosted in online store service task panes.

The **DownloadManager** object supports the following methods.



| Method                                                                   | Description                                  |
|--------------------------------------------------------------------------|----------------------------------------------|
| [createDownloadCollection](downloadmanager-createdownloadcollection.md) | Creates an empty download collection.        |
| [getDownloadCollection](downloadmanager-getdownloadcollection.md)       | Retrieves the specified download collection. |



 

The **DownloadManager** object is accessed by using **external.DownloadManager**. For illustration purposes, it is assumed that this value has been assigned to a variable named "DownloadManager", which will be used to identify this object in the reference syntax sections.

In Windows Media Player 10 or later, the **DownloadManager** property and object are accessible only from online store service task panes. You cannot use the **DownloadManager** from other features where the **External** object is available, such as HTMLView, Info Center View, and album information.

## Related topics

<dl> <dt>

[**Reference for Type 2 Online Stores**](reference-for-type-2-online-stores.md)
</dt> </dl>

 

 




