---
title: Asynchronous and Synchronous Storage
description: Asynchronous and Synchronous Storage
ms.assetid: de8c50f8-1733-439f-ab53-f98ac21a1fae
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous and Synchronous Storage

Asynchronous monikers may also return an [Asynchronous Storage](https://msdn.microsoft.com/library/windows/desktop/aa378862) object in the [**IBindStatusCallback::OnDataAvailable**](9755eda0-4d33-49e1-9bdd-f50a906e826f) notification. This storage object may allow access to some of the object's persistent data while the binding is still in progress. A client can choose between two modes for the storage: blocking and nonblocking.

In blocking mode, which is compatible with current implementations of storage objects, if data is unavailable, the call blocks until data arrives. In nonblocking mode, rather than blocking the call, the storage object returns a new error E\_PENDING when data is unavailable. A client aware of asynchronous binding and storage notes this error and waits for further notifications ([**OnDataAvailable**](9755eda0-4d33-49e1-9bdd-f50a906e826f)) to retry the operation. A client can choose between a synchronous (blocking) and asynchronous (nonblocking) storage by choosing whether to set the BINDF\_ASYNCSTORAGE flag in the *grfBINDF* value returned to [**IBindStatusCallback::GetBindInfo**](a402c6a2-bae3-4874-8fc9-67d04b67687e).

## Related topics

<dl> <dt>

[Asynchronous Monikers](asynchronous-monikers.md)
</dt> </dl>

 

 




