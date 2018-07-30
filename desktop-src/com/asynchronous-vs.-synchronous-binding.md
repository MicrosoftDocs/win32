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

The client may check to see whether the moniker is asynchronous by calling the [**IsAsyncMoniker**](https://msdn.microsoft.com/library/ms775110(v=VS.85).aspx) function. If the client returns the BINDF\_ASYNCHRONOUS flag, rather than returning an object pointer or a storage pointer from subsequent calls to [**IMoniker::BindToStorage**](/windows/desktop/api/ObjIdl/nf-objidl-imoniker-bindtostorage) or [**IMoniker::BindToObject**](/windows/desktop/api/ObjIdl/nf-objidl-imoniker-bindtoobject), the moniker returns MK\_S\_ASYNCHRONOUS in place of the object pointer and **NULL** in place of the storage pointer. In response, the client should wait to receive the requested object or storage during implementation of [**IBindStatusCallback::OnDataAvailable**](https://msdn.microsoft.com/library/ms775061(v=VS.85).aspx) and [**IBindStatusCallBack::OnObjectAvailable**](https://msdn.microsoft.com/library/ms775063(v=VS.85).aspx).

The callback object also receives progress notification through [**IBindStatusCallback::OnProgress**](https://msdn.microsoft.com/library/ms775064(v=VS.85).aspx), data availability notification through [**OnDataAvailable**](https://msdn.microsoft.com/library/ms775061(v=VS.85).aspx), and various other notifications from the moniker about the status of the binding operation.

If the client does not return the BINDF\_ASYNCHRONOUS flag from the moniker's call to [**IBindStatusCallback::GetBindInfo**](https://msdn.microsoft.com/library/ms775058(v=VS.85).aspx), the bind operation will proceed synchronously and the desired object or storage will be returned from subsequent calls to [**BindToObject**](/windows/desktop/api/ObjIdl/nf-objidl-imoniker-bindtoobject) or [**BindToStorage**](/windows/desktop/api/ObjIdl/nf-objidl-imoniker-bindtostorage). Similarly, if the client desires synchronous operation and does not wish to receive any progress notifications or callbacks, it can request an asynchronous moniker to behave synchronously by not implementing [**IBindStatusCallback**](https://msdn.microsoft.com/library/ms775060(v=VS.85).aspx). In such cases, the asynchronous moniker will behave like a standard synchronous moniker.

## Related topics

<dl> <dt>

[Asynchronous Monikers](asynchronous-monikers.md)
</dt> </dl>

 

 




