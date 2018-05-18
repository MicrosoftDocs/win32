---
title: Asynchronous and Synchronous Binding
description: Asynchronous and Synchronous Binding
ms.assetid: '9852df19-5ae4-4425-9ce0-cac160d68456'
---

# Asynchronous and Synchronous Binding

The client may check to see whether the moniker is asynchronous by calling the [**IsAsyncMoniker**](_inet_IsAsyncMoniker_Function_cpp) function. If the client returns the BINDF\_ASYNCHRONOUS flag, rather than returning an object pointer or a storage pointer from subsequent calls to [**IMoniker::BindToStorage**](imoniker-bindtostorage.md) or [**IMoniker::BindToObject**](imoniker-bindtoobject.md), the moniker returns MK\_S\_ASYNCHRONOUS in place of the object pointer and **NULL** in place of the storage pointer. In response, the client should wait to receive the requested object or storage during implementation of [**IBindStatusCallback::OnDataAvailable**](_inet_IBindStatusCallback_OnDataAvailable_Method) and [**IBindStatusCallBack::OnObjectAvailable**](_inet_IBindStatusCallback_OnObjectAvailable_Method).

The callback object also receives progress notification through [**IBindStatusCallback::OnProgress**](_inet_IBindStatusCallback_OnProgress_Method), data availability notification through [**OnDataAvailable**](_inet_IBindStatusCallback_OnDataAvailable_Method), and various other notifications from the moniker about the status of the binding operation.

If the client does not return the BINDF\_ASYNCHRONOUS flag from the moniker's call to [**IBindStatusCallback::GetBindInfo**](_inet_IBindStatusCallback_GetBindInfo_Method), the bind operation will proceed synchronously and the desired object or storage will be returned from subsequent calls to [**BindToObject**](imoniker-bindtoobject.md) or [**BindToStorage**](imoniker-bindtostorage.md). Similarly, if the client desires synchronous operation and does not wish to receive any progress notifications or callbacks, it can request an asynchronous moniker to behave synchronously by not implementing [**IBindStatusCallback**](_inet_IBindStatusCallback_Interface_cpp). In such cases, the asynchronous moniker will behave like a standard synchronous moniker.

## Related topics

<dl> <dt>

[Asynchronous Monikers](asynchronous-monikers.md)
</dt> </dl>

 

 




