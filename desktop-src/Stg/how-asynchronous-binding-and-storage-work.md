---
title: How Asynchronous Binding and Storage Work
description: Asynchronous storage enhances the COM structured storage specification to support downloading of storage objects on high-latency, slow-link networks such as the Internet.
ms.assetid: 891152c3-5abd-45e4-a7bb-0aac23262b03
keywords:
- How Asynchronous Binding and Storage Work
ms.topic: article
ms.date: 05/31/2018
---

# How Asynchronous Binding and Storage Work

Asynchronous storage enhances the COM structured storage specification to support downloading of storage objects on high-latency, slow-link networks such as the Internet. Asynchronous storage works together with asynchronous monikers to provide complete asynchronous binding behavior.

## Document object embedded in a Web page

When a user clicks a link representing a document embedded in a Web page, the following events occur:

1.  The browser calls the [**MkParseDisplayName**](/windows/win32/api/objbase/nf-objbase-mkparsedisplayname) function, passing the link URL.
2.  [**MkParseDisplayName**](/windows/win32/api/objbase/nf-objbase-mkparsedisplayname) parses the URL, creates a corresponding asynchronous moniker, and returns a pointer to the moniker's [**IMoniker**](/windows/win32/api/objidl/nn-objidl-imoniker) interface.
3.  The browser calls [**IsAsyncMoniker**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775110(v=vs.85)) to determine if the moniker is asynchronous, creates a bind context, registers the [**IBindStatusCallback**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775060(v=vs.85)) interface with the bind context, only if the moniker is asynchronous, and calls [**IMoniker::BindToObject**](/windows/win32/api/objidl/nf-objidl-imoniker-bindtoobject), passing the bind context.
4.  The moniker binds to the object and queries it for the [**IPersistMoniker**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775042(v=vs.85)) interface, which indicates whether the object supports asynchronous binding and storage. If the object returns a pointer to **IPersistMoniker**:

    1.  The URL moniker calls [**IPersistMoniker::Load**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775044(v=vs.85)), passing its own [**IMoniker**](/windows/win32/api/objidl/nn-objidl-imoniker) pointer to the object.
    2.  The object modifies the bind context, chooses whether it wants a blocking or nonblocking storage, registers its own [**IBindStatusCallback**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775060(v=vs.85)) and calls [**IMoniker::BindToStorage**](/windows/win32/api/objidl/nf-objidl-imoniker-bindtostorage) on the pointer it received through [**IPersistMoniker::Load**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775044(v=vs.85)).
    3.  The moniker creates an asynchronous storage, keeps a reference to the wrapper object's [**IFillLockBytes**](/windows/desktop/api/Objidl/nn-objidl-ifilllockbytes) interface, registers the [**IProgressNotify**](/windows/win32/api/objidl/nn-objidl-iprogressnotify) interface on the root storage, and calls [**IPersistStorage::Load**](/windows/win32/api/objidl/nf-objidl-ipersiststorage-load), passing the asynchronous storage's [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) pointer. As data arrives (on a background thread) the moniker calls **IFillLockBytes** to fill the [**ILockBytes**](/windows/desktop/api/Objidl/nn-objidl-ilockbytes) on the temp file.
    4.  The object reads data from the storage and returns from [**IPersistMoniker::Load**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775044(v=vs.85)) when it has received sufficient data to consider itself initialized. If the object attempts to read data that has not yet been downloaded, the downloader receives a notification on [**IProgressNotify**](/windows/win32/api/objidl/nn-objidl-iprogressnotify). Inside the [**IProgressNotify::OnProgress**](/windows/win32/api/objidl/nf-objidl-iprogressnotify-onprogress) method, the downloading thread either blocks in a modal message loop, or causes the asynchronous storage to return E\_PENDING, depending on whether the object has requested a blocking or nonblocking storage.

5.  If the object does not implement [**IPersistMoniker**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775042(v=vs.85)), the moniker queries for [**IPersistStorage**](/windows/win32/api/objidl/nn-objidl-ipersiststorage), which indicates that the object's persistent state is stored in a storage object. If the object returns a pointer to **IPersistStorage**:

    1.  The Moniker calls [**IMoniker::BindToStorage**](/windows/win32/api/objidl/nf-objidl-imoniker-bindtostorage) on itself, requesting a blocking [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) (because the object is not asynchronous-aware), creates an asynchronous storage, keeps a reference to the wrapper object's [**IFillLockBytes**](/windows/desktop/api/Objidl/nn-objidl-ifilllockbytes) interface, registers the [**IProgressNotify**](/windows/win32/api/objidl/nn-objidl-iprogressnotify) interface on the root storage, and calls [**IPersistStorage::Load**](/windows/win32/api/objidl/nf-objidl-ipersiststorage-load), passing the asynchronous storage's **IStorage** pointer. As data arrives (on a background thread) the moniker calls [**IFillLockBytes**](/windows/desktop/api/Objidl/nn-objidl-ifilllockbytes) to fill the [**ILockBytes**](/windows/desktop/api/Objidl/nn-objidl-ilockbytes) on the temporary file.
    2.  The object reads data from storage and returns from [**IPersistStorage::Load**](/windows/win32/api/objidl/nf-objidl-ipersiststorage-load) when it has received sufficient data to consider itself initialized. If the object attempts to read data that has not yet been downloaded, it receives a notification on [**IProgressNotify**](/windows/win32/api/objidl/nn-objidl-iprogressnotify). Inside the [**IProgressNotify::OnProgress**](/windows/win32/api/objidl/nf-objidl-iprogressnotify-onprogress) method, the downloading thread always blocks in a modal message loop.

6.  Regardless of whether the download is synchronous or asynchronous, the moniker returns from [**IMoniker::BindToObject**](/windows/win32/api/objidl/nf-objidl-imoniker-bindtoobject), and the browser receives the initialized object it requested.
7.  The browser queries for [**IOleObject**](/windows/win32/api/oleidl/nn-oleidl-ioleobject) and hosts the object as a Document Object. (At this point the object may not be initialized completely, but enough to display something useful, in which case downloading continues in the background.)

 

 