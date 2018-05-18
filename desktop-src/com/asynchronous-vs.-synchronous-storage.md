---
title: Asynchronous and Synchronous Storage
description: Asynchronous and Synchronous Storage
ms.assetid: 'de8c50f8-1733-439f-ab53-f98ac21a1fae'
---

# Asynchronous and Synchronous Storage

Asynchronous monikers may also return an [Asynchronous Storage](https://msdn.microsoft.com/library/windows/desktop/aa378862) object in the [**IBindStatusCallback::OnDataAvailable**](_inet_IBindStatusCallback_OnDataAvailable_Method) notification. This storage object may allow access to some of the object's persistent data while the binding is still in progress. A client can choose between two modes for the storage: blocking and nonblocking.

In blocking mode, which is compatible with current implementations of storage objects, if data is unavailable, the call blocks until data arrives. In nonblocking mode, rather than blocking the call, the storage object returns a new error E\_PENDING when data is unavailable. A client aware of asynchronous binding and storage notes this error and waits for further notifications ([**OnDataAvailable**](_inet_IBindStatusCallback_OnDataAvailable_Method)) to retry the operation. A client can choose between a synchronous (blocking) and asynchronous (nonblocking) storage by choosing whether to set the BINDF\_ASYNCSTORAGE flag in the *grfBINDF* value returned to [**IBindStatusCallback::GetBindInfo**](_inet_IBindStatusCallback_GetBindInfo_Method).

## Related topics

<dl> <dt>

[Asynchronous Monikers](asynchronous-monikers.md)
</dt> </dl>

 

 




