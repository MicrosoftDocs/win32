---
title: Asynchronous and Synchronous Binding
description: Asynchronous and Synchronous Binding
ms.assetid: 9852df19-5ae4-4425-9ce0-cac160d68456
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous and Synchronous Binding

The client may check to see whether the moniker is asynchronous by calling the [**IsAsyncMoniker**](https://www.bing.com/search?q=**IsAsyncMoniker**) function. If the client returns the BINDF\_ASYNCHRONOUS flag, rather than returning an object pointer or a storage pointer from subsequent calls to [**IMoniker::BindToStorage**](/windows/desktop/api/ObjIdl/nf-objidl-imoniker-bindtostorage) or [**IMoniker::BindToObject**](/windows/desktop/api/ObjIdl/nf-objidl-imoniker-bindtoobject), the moniker returns MK\_S\_ASYNCHRONOUS in place of the object pointer and **NULL** in place of the storage pointer. In response, the client should wait to receive the requested object or storage during implementation of [**IBindStatusCallback::OnDataAvailable**](9755eda0-4d33-49e1-9bdd-f50a906e826f) and [**IBindStatusCallBack::OnObjectAvailable**](d225d7f0-69eb-4359-88a4-17c9ea9e7be4).

The callback object also receives progress notification through [**IBindStatusCallback::OnProgress**](c6541dd3-8095-481a-a2d5-08acaba91aad), data availability notification through [**OnDataAvailable**](9755eda0-4d33-49e1-9bdd-f50a906e826f), and various other notifications from the moniker about the status of the binding operation.

If the client does not return the BINDF\_ASYNCHRONOUS flag from the moniker's call to [**IBindStatusCallback::GetBindInfo**](a402c6a2-bae3-4874-8fc9-67d04b67687e), the bind operation will proceed synchronously and the desired object or storage will be returned from subsequent calls to [**BindToObject**](/windows/desktop/api/ObjIdl/nf-objidl-imoniker-bindtoobject) or [**BindToStorage**](/windows/desktop/api/ObjIdl/nf-objidl-imoniker-bindtostorage). Similarly, if the client desires synchronous operation and does not wish to receive any progress notifications or callbacks, it can request an asynchronous moniker to behave synchronously by not implementing [**IBindStatusCallback**](https://www.bing.com/search?q=**IBindStatusCallback**). In such cases, the asynchronous moniker will behave like a standard synchronous moniker.

## Related topics

<dl> <dt>

[Asynchronous Monikers](asynchronous-monikers.md)
</dt> </dl>

 

 




