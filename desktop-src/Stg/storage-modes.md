---
title: Storage Modes
description: Asynchronous storage supports two storage modes blocking and nonblocking, which a client (either a browser or the object itself) can specify by returning BINDF\_ASYNCSTORAGE from the moniker's call to IBindStatusCallback GetBindInfo.
ms.assetid: df8f9e2c-40d2-4997-b5f9-bdbc524437cf
ms.topic: article
ms.date: 05/31/2018
---

# Storage Modes

Asynchronous storage supports two storage modes: blocking and nonblocking, which a client (either a browser or the object itself) can specify by returning BINDF\_ASYNCSTORAGE from the moniker's call to [**IBindStatusCallback::GetBindInfo**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775058(v=vs.85)). If a client specifies BINDF\_ASYNCSTORAGE, it receives a pointer to a nonblocking asynchronous storage. Otherwise, it receives a pointer to a blocking asynchronous storage. Even if the client does not request an asynchronous binding operation (by not registering [**IBindStatusCallback**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775060(v=vs.85)) with the bind context), the moniker still returns a blocking asynchronous storage, enabling progressive loading for legacy applications.

In nonblocking mode, an asynchronous storage returns E\_PENDING when data is unavailable. Upon receiving this message, the client waits for notification that additional data is available before trying again to download it.

In blocking mode, instead of returning E\_PENDING, the asynchronous storage blocks the call until new data is available, then unblocks the call and returns the new data. The client must be ready to receive the data. While the thread is blocked, data already passed to the client is fully available to the user.

Blocking mode is necessary because clients unaware of asynchronous storage will not recognize E\_PENDING and will assume that an unrecoverable error has occurred. Blocking asynchronous storage enables existing clients to do progressive rendering.

 

 