---
title: Callback Synchronization
description: Callback Synchronization
ms.assetid: 'e8268f18-49e7-4e09-9006-77858b734bf4'
---

# Callback Synchronization

The asynchronous [WinInet API](https://msdn.microsoft.com/library/windows/desktop/aa385331) (used for the most common protocols) leaves the synchronization of the callback mechanism and the calling application as an exercise for the client. This is intentional because it allows the greatest degree of flexibility. The default protocols and the URL moniker implementation perform this synchronization and guarantee that single-threaded and apartment-threaded applications never have to deal with free-thread-style contention. That is, the client's [**IEnumFORMATETC**](ienumformatetc.md) and [**IBindStatusCallback**](_inet_IBindStatusCallback_Interface_cpp) interfaces are called only on their proper threads. This feature is transparent to the user of the URL mMoniker as long each thread that calls [**IMoniker::BindToStorage**](imoniker-bindtostorage.md) and [**IMoniker::BindToObject**](imoniker-bindtoobject.md) has a message queue.

The asynchronous moniker specification requires more precise control over the prioritization and management of downloads than is allowed for by either WinSock or WinInet. Accordingly, a URL moniker manages all the downloads for any given caller's thread, using (as part of its synchronization) a priority scheme based on the [**IBinding**](_inet_IBinding_Interface_cpp) specification.

## Related topics

<dl> <dt>

[URL Monikers](url-monikers.md)
</dt> </dl>

 

 




