---
title: How Asynchronous Binding and Storage Work
description: Asynchronous storage enhances the COM structured storage specification to support downloading of storage objects on high-latency, slow-link networks such as the Internet.
ms.assetid: 891152c3-5abd-45e4-a7bb-0aac23262b03
keywords:
- How Asynchronous Binding and Storage Work
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How Asynchronous Binding and Storage Work

Asynchronous storage enhances the COM structured storage specification to support downloading of storage objects on high-latency, slow-link networks such as the Internet. Asynchronous storage works together with asynchronous monikers to provide complete asynchronous binding behavior.

## Document object embedded in a Web page

When a user clicks a link representing a document embedded in a Web page, the following events occur:

1.  The browser calls the [**MkParseDisplayName**](ada46dd3-e2c5-4ff5-89bd-3805f98b247b) function, passing the link URL.
2.  [**MkParseDisplayName**](ada46dd3-e2c5-4ff5-89bd-3805f98b247b) parses the URL, creates a corresponding asynchronous moniker, and returns a pointer to the moniker's [**IMoniker**](17f4c1df-7a9c-42ef-a888-70cd8d85f070) interface.
3.  The browser calls [**IsAsyncMoniker**](https://www.bing.com/search?q=**IsAsyncMoniker**) to determine if the moniker is asynchronous, creates a bind context, registers the [**IBindStatusCallback**](https://www.bing.com/search?q=**IBindStatusCallback**) interface with the bind context, only if the moniker is asynchronous, and calls [**IMoniker::BindToObject**](b5ce39ff-3387-4f72-9aea-5a26eed3810c), passing the bind context.
4.  The moniker binds to the object and queries it for the [**IPersistMoniker**](https://www.bing.com/search?q=**IPersistMoniker**) interface, which indicates whether the object supports asynchronous binding and storage. If the object returns a pointer to **IPersistMoniker**:

    1.  The URL moniker calls [**IPersistMoniker::Load**](https://www.bing.com/search?q=**IPersistMoniker::Load**), passing its own [**IMoniker**](17f4c1df-7a9c-42ef-a888-70cd8d85f070) pointer to the object.
    2.  The object modifies the bind context, chooses whether it wants a blocking or nonblocking storage, registers its own [**IBindStatusCallback**](https://www.bing.com/search?q=**IBindStatusCallback**) and calls [**IMoniker::BindToStorage**](94c8219f-8131-45dd-b350-878ffd6161ea) on the pointer it received through [**IPersistMoniker::Load**](https://www.bing.com/search?q=**IPersistMoniker::Load**).
    3.  The moniker creates an asynchronous storage, keeps a reference to the wrapper object's [**IFillLockBytes**](/windows/desktop/api/Objidl/nn-objidl-ifilllockbytes) interface, registers the [**IProgressNotify**](3f90437d-df8f-42b2-af81-519bfb9577b1) interface on the root storage, and calls [**IPersistStorage::Load**](34379b8d-4e00-49cd-9fd1-65f88746c61a), passing the asynchronous storage's [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) pointer. As data arrives (on a background thread) the moniker calls **IFillLockBytes** to fill the [**ILockBytes**](/windows/desktop/api/Objidl/nn-objidl-ilockbytes) on the temp file.
    4.  The object reads data from the storage and returns from [**IPersistMoniker::Load**](https://www.bing.com/search?q=**IPersistMoniker::Load**) when it has received sufficient data to consider itself initialized. If the object attempts to read data that has not yet been downloaded, the downloader receives a notification on [**IProgressNotify**](3f90437d-df8f-42b2-af81-519bfb9577b1). Inside the [**IProgressNotify::OnProgress**](07b3e629-a558-4a0e-8307-ca922f56e00c) method, the downloading thread either blocks in a modal message loop, or causes the asynchronous storage to return E\_PENDING, depending on whether the object has requested a blocking or nonblocking storage.

5.  If the object does not implement [**IPersistMoniker**](https://www.bing.com/search?q=**IPersistMoniker**), the moniker queries for [**IPersistStorage**](1c1a20fc-c101-4cbc-a7a6-30613aa387d7), which indicates that the object's persistent state is stored in a storage object. If the object returns a pointer to **IPersistStorage**:

    1.  The Moniker calls [**IMoniker::BindToStorage**](94c8219f-8131-45dd-b350-878ffd6161ea) on itself, requesting a blocking [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) (because the object is not asynchronous-aware), creates an asynchronous storage, keeps a reference to the wrapper object's [**IFillLockBytes**](/windows/desktop/api/Objidl/nn-objidl-ifilllockbytes) interface, registers the [**IProgressNotify**](3f90437d-df8f-42b2-af81-519bfb9577b1) interface on the root storage, and calls [**IPersistStorage::Load**](34379b8d-4e00-49cd-9fd1-65f88746c61a), passing the asynchronous storage's **IStorage** pointer. As data arrives (on a background thread) the moniker calls [**IFillLockBytes**](/windows/desktop/api/Objidl/nn-objidl-ifilllockbytes) to fill the [**ILockBytes**](/windows/desktop/api/Objidl/nn-objidl-ilockbytes) on the temporary file.
    2.  The object reads data from storage and returns from [**IPersistStorage::Load**](34379b8d-4e00-49cd-9fd1-65f88746c61a) when it has received sufficient data to consider itself initialized. If the object attempts to read data that has not yet been downloaded, it receives a notification on [**IProgressNotify**](3f90437d-df8f-42b2-af81-519bfb9577b1). Inside the [**IProgressNotify::OnProgress**](07b3e629-a558-4a0e-8307-ca922f56e00c) method, the downloading thread always blocks in a modal message loop.

6.  Regardless of whether the download is synchronous or asynchronous, the moniker returns from [**IMoniker::BindToObject**](b5ce39ff-3387-4f72-9aea-5a26eed3810c), and the browser receives the initialized object it requested.
7.  The browser queries for [**IOleObject**](58b32c87-39b6-4d64-9174-cf798ed302c2) and hosts the object as a Document Object. (At this point the object may not be initialized completely, but enough to display something useful, in which case downloading continues in the background.)

 

 




