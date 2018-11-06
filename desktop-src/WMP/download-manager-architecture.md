---
title: Download Manager Architecture
description: Download Manager Architecture
ms.assetid: cbd46bf2-613f-40ae-8506-2f3c5eb84ada
keywords:
- Windows Media Player online stores,Download Manager
- online stores,Download Manager
- type 2 online stores,Download Manager
- Windows Media Player,Download Manager
- Windows Media Player Download Manager
- Download Manager
- architecture for Download Manager
ms.topic: article
ms.date: 05/31/2018
---

# Download Manager Architecture

The Windows Media Player Download Manager uses COM technology. The functionality is distilled into a set of programming interfaces; you can write programming code that uses these interfaces by using Microsoft JScript or C++.

The scripting languages use the concept of objects to divide programming functionality. The **DownloadManager** object model uses several objects to divide the methods and properties into a logical organization that groups semantically related functions together. The following sections contain information about the Download Manager objects.



| Section                                                                     | Description                                                                                              |
|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [About the DownloadManager Object](#about-the-downloadmanager-object)       | The **DownloadManager** object represents the root object for the Windows Media Player Download Manager. |
| [About the DownloadCollection Object](#about-the-downloadcollection-object) | The **DownloadCollection** object represents a collection of download items.                             |
| [About the DownloadItem Object](#about-the-downloaditem-object)             | The **DownloadItem** object represents an individual download request.                                   |



 

## About the DownloadManager Object

**DownloadManager** is the root object for the Windows Media Player Download Manager. All other objects are accessed through this object. To gain access to the **DownloadManager** object, use the following JScript syntax:


```C++
var DownloadManager = external.DownloadManager;
```



This creates an instance of the **DownloadManager** object, which can then be used to retrieve the child objects. For example, the following syntax retrieves the first item from the download collection that has id number 253675:


```C++
var firstItem = DownloadManager.getDownloadCollection(253675).item(0);
```



## About the DownloadCollection Object

The **DownloadCollection** object represents a collection of files to be downloaded. You can use this object to determine how many downloads are in the collection, remove items from the collection, retrieve a specific download item, and to start a new download. Starting a new download automatically adds the download to the collection.

## About the DownloadItem Object

The **DownloadItem** object represents an individual download. Download items always exist as part of a download collection. Use this object to retrieve information about the download item and to pause, resume, or cancel the download in progress.

When you cancel a download, the download item remains in place in its download collection. In this case, **downloadCollection**.**downloadState** retrieves a value of 4, meaning canceled.

You can use **downloadItem**.**progress** to inform the user about how much of the file has been transferred or how much remains to be downloaded. You might use this value to estimate the time remaining as well.

## Related topics

<dl> <dt>

[**Download Manager**](download-manager.md)
</dt> </dl>

 

 




