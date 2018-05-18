---
title: How Asynchronous Binding and Storage Work
description: Asynchronous storage enhances the COM structured storage specification to support downloading of storage objects on high-latency, slow-link networks such as the Internet.
ms.assetid: '891152c3-5abd-45e4-a7bb-0aac23262b03'
keywords: ["How Asynchronous Binding and Storage Work"]
---

# How Asynchronous Binding and Storage Work

Asynchronous storage enhances the COM structured storage specification to support downloading of storage objects on high-latency, slow-link networks such as the Internet. Asynchronous storage works together with asynchronous monikers to provide complete asynchronous binding behavior.

## Document object embedded in a Web page

When a user clicks a link representing a document embedded in a Web page, the following events occur:

1.  The browser calls the [**MkParseDisplayName**](_com_mkparsedisplayname) function, passing the link URL.
2.  [**MkParseDisplayName**](_com_mkparsedisplayname) parses the URL, creates a corresponding asynchronous moniker, and returns a pointer to the moniker's [**IMoniker**](_com_imoniker) interface.
3.  The browser calls [**IsAsyncMoniker**](_inet_isasyncmoniker_function_cpp) to determine if the moniker is asynchronous, creates a bind context, registers the [**IBindStatusCallback**](_inet_ibindstatuscallback_interface_cpp) interface with the bind context, only if the moniker is asynchronous, and calls [**IMoniker::BindToObject**](_com_imoniker_bindtoobject), passing the bind context.
4.  The moniker binds to the object and queries it for the [**IPersistMoniker**](_inet_ipersistmoniker_interface_cpp) interface, which indicates whether the object supports asynchronous binding and storage. If the object returns a pointer to **IPersistMoniker**:

    1.  The URL moniker calls [**IPersistMoniker::Load**](_inet_ipersistmoniker_interface_inet_ipersistmoniker_load_method_cpp), passing its own [**IMoniker**](_com_imoniker) pointer to the object.
    2.  The object modifies the bind context, chooses whether it wants a blocking or nonblocking storage, registers its own [**IBindStatusCallback**](_inet_ibindstatuscallback_interface_cpp) and calls [**IMoniker::BindToStorage**](_com_imoniker_bindtostorage) on the pointer it received through [**IPersistMoniker::Load**](_inet_ipersistmoniker_interface_inet_ipersistmoniker_load_method_cpp).
    3.  The moniker creates an asynchronous storage, keeps a reference to the wrapper object's [**IFillLockBytes**](ifilllockbytes.md) interface, registers the [**IProgressNotify**](_com_iprogressnotify) interface on the root storage, and calls [**IPersistStorage::Load**](_com_ipersiststorage_load), passing the asynchronous storage's [**IStorage**](istorage.md) pointer. As data arrives (on a background thread) the moniker calls **IFillLockBytes** to fill the [**ILockBytes**](ilockbytes.md) on the temp file.
    4.  The object reads data from the storage and returns from [**IPersistMoniker::Load**](_inet_ipersistmoniker_interface_inet_ipersistmoniker_load_method_cpp) when it has received sufficient data to consider itself initialized. If the object attempts to read data that has not yet been downloaded, the downloader receives a notification on [**IProgressNotify**](_com_iprogressnotify). Inside the [**IProgressNotify::OnProgress**](_com_iprogressnotify_onprogress) method, the downloading thread either blocks in a modal message loop, or causes the asynchronous storage to return E\_PENDING, depending on whether the object has requested a blocking or nonblocking storage.

5.  If the object does not implement [**IPersistMoniker**](_inet_ipersistmoniker_interface_cpp), the moniker queries for [**IPersistStorage**](_com_ipersiststorage), which indicates that the object's persistent state is stored in a storage object. If the object returns a pointer to **IPersistStorage**:

    1.  The Moniker calls [**IMoniker::BindToStorage**](_com_imoniker_bindtostorage) on itself, requesting a blocking [**IStorage**](istorage.md) (because the object is not asynchronous-aware), creates an asynchronous storage, keeps a reference to the wrapper object's [**IFillLockBytes**](ifilllockbytes.md) interface, registers the [**IProgressNotify**](_com_iprogressnotify) interface on the root storage, and calls [**IPersistStorage::Load**](_com_ipersiststorage_load), passing the asynchronous storage's **IStorage** pointer. As data arrives (on a background thread) the moniker calls [**IFillLockBytes**](ifilllockbytes.md) to fill the [**ILockBytes**](ilockbytes.md) on the temporary file.
    2.  The object reads data from storage and returns from [**IPersistStorage::Load**](_com_ipersiststorage_load) when it has received sufficient data to consider itself initialized. If the object attempts to read data that has not yet been downloaded, it receives a notification on [**IProgressNotify**](_com_iprogressnotify). Inside the [**IProgressNotify::OnProgress**](_com_iprogressnotify_onprogress) method, the downloading thread always blocks in a modal message loop.

6.  Regardless of whether the download is synchronous or asynchronous, the moniker returns from [**IMoniker::BindToObject**](_com_imoniker_bindtoobject), and the browser receives the initialized object it requested.
7.  The browser queries for [**IOleObject**](_ole_ioleobject) and hosts the object as a Document Object. (At this point the object may not be initialized completely, but enough to display something useful, in which case downloading continues in the background.)

 

 




