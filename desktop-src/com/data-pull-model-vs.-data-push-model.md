---
title: Data-Pull Model and Data-Push Model
description: Data-Pull Model and Data-Push Model
ms.assetid: ba0e8532-9c7b-4e15-9c27-8205d738fc4b
ms.topic: article
ms.date: 05/31/2018
---

# Data-Pull Model and Data-Push Model

A client of an asynchronous moniker can choose between a data-pull and data-push model for driving an asynchronous [**IMoniker::BindToStorage**](/windows/desktop/api/ObjIdl/nf-objidl-imoniker-bindtostorage) operation and receiving asynchronous notifications. In the data-pull model, the client drives the bind operation and the moniker provides data to the client only as it is read. In other words, after the first call to [**IBindStatusCallback::OnDataAvailable**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775061(v=vs.85)), the moniker does not provide any data to the client unless the client has consumed all of the data that is already available.

Because data is downloaded only as it is requested, clients that choose the data-pull model must make sure to read this data in a timely manner. In the case of Internet downloads with [URL monikers](url-monikers.md), the bind operation may fail if a client waits too long before requesting more data.

In the data-push model, the moniker drives the asynchronous bind operation and continuously notifies the client whenever new data is available. The client may choose whether to read the data at any point during the bind operation, but the moniker will drive the bind operation to completion regardless.

Also, you need to remember to follow the COM rules for memory allocation when using asynchronous monikers, specifically the following:

-   Whenever a COM interface or function call returns a buffer (string or other) to its client, the client is responsible for freeing the memory by calling [**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree).
-   Whenever a COM interface or function requires a buffer from its client, the client must allocate that buffer using [**CoTaskMemAlloc**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemalloc) and the callee must free it.

Be sure to follow these rules when allocating strings or buffers that are passed to asynchronous monikers, and remember to free memory returned by asynchronous monikers. See [Managing Memory Allocation](the-com-library.md) and related topics for complete details.

## Related topics

<dl> <dt>

[Asynchronous Monikers](asynchronous-monikers.md)
</dt> </dl>

 

 