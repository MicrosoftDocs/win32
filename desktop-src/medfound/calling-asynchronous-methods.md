---
description: Calling Asynchronous Methods
ms.assetid: 1d8688a5-d476-457d-a0ad-e4f106ac3484
title: Calling Asynchronous Methods
ms.topic: reference
ms.date: 05/31/2018
---

# Calling Asynchronous Methods

In Media Foundation, many operations are performed asynchronously. Asynchronous operations can improve performance, because they do not block the calling thread. An asynchronous operation in Media Foundation is defined by a pair of methods with the naming convention **Begin...** and **End....**. Together, these two methods define an asynchronous read operation on the stream.

To start an asynchronous operation, call the **Begin** method. The **Begin** method always contains at least two parameters:

-   A pointer to the [**IMFAsyncCallback**](/windows/desktop/api/mfobjects/nn-mfobjects-imfasynccallback) interface. The application must implement this interface.
-   A pointer to an optional state object.

The [**IMFAsyncCallback**](/windows/desktop/api/mfobjects/nn-mfobjects-imfasynccallback) interface notifies the application when the operation is completed. For an example of how to implement this interface, see [Implementing the Asynchronous Callback](implementing-the-asynchronous-callback.md). The state object is optional. If specified, it must implement the **IUnknown** interface. You can use the state object to store any state information that is needed by your callback. If you do not need state information, you can set this parameter to **NULL**. The **Begin** method might contain additional parameters that are specific to that method.

If the **Begin** method returns a failure code, it means the operation has failed immediately, and the callback will not be invoked. If the **Begin** method succeeds, it means the operation is pending, and the callback will be invoked when the operation completes.

For example, the [**IMFByteStream::BeginRead**](/windows/desktop/api/mfobjects/nf-mfobjects-imfbytestream-beginread) method starts an asynchronous read operation on a byte stream:


```C++
    BYTE data[DATA_SIZE];
    ULONG cbRead = 0;

    CMyCallback *pCB = new (std::nothrow) CMyCallback(pStream, &hr);

    if (pCB == NULL)
    {
        hr = E_OUTOFMEMORY;
    }

    // Start an asynchronous request to read data.
    if (SUCCEEDED(hr))
    {
        hr = pStream->BeginRead(data, DATA_SIZE, pCB, NULL);
    }
```



The callback method is [**IMFAsyncCallback::Invoke**](/windows/desktop/api/mfobjects/nf-mfobjects-imfasynccallback-invoke). It has a single parameter, *pAsyncResult*, which is a pointer to the [**IMFAsyncResult**](/windows/desktop/api/mfobjects/nn-mfobjects-imfasyncresult) interface. To complete the asynchronous operation, call the **End** method that matches the asynchronous **Begin** method. The **End** method always takes an **IMFAsyncResult** pointer. Always pass in the same pointer that you received in the **Invoke** method. The asynchronous operation is not complete until you call the **End** method. You may call the **End** method from inside the **Invoke** method, or you can call it from another thread.

For example, to complete the [**IMFByteStream::BeginRead**](/windows/desktop/api/mfobjects/nf-mfobjects-imfbytestream-beginread) on a byte stream, call [**IMFByteStream::EndRead**](/windows/desktop/api/mfobjects/nf-mfobjects-imfbytestream-endread):


```C++
    STDMETHODIMP Invoke(IMFAsyncResult* pResult)
    {
        m_hrStatus = m_pStream->EndRead(pResult, &m_cbRead);

        SetEvent(m_hEvent);

        return S_OK;
    }
```



The return value of the **End** method indicates the status of the asynchronous operation. In most cases, your application will perform some work after the asynchronous operation completes, whether it completes successfully or not. You have several options:

-   Do the work inside the [**Invoke**](/windows/desktop/api/mfobjects/nf-mfobjects-imfasynccallback-invoke) method. This approach is acceptable as long as your application never blocks the calling thread or waits for anything inside the **Invoke** method. If you block the calling thread, you might block the streaming pipeline. For example, you might update some state variables, but do not perform a synchronous read operation or wait on a mutex object.
-   In the [**Invoke**](/windows/desktop/api/mfobjects/nf-mfobjects-imfasynccallback-invoke) method, set an event and return immediately. The application's calling thread waits for the event and does the work when the event is signaled.
-   In the [**Invoke**](/windows/desktop/api/mfobjects/nf-mfobjects-imfasynccallback-invoke) method, post a private window message to your application window and return immediately. The application does the work on its message loop. (Make sure to post the message by calling **PostMessage**, not **SendMessage**, because **SendMessage** can block the callback thread.)

It is important to remember that [**Invoke**](/windows/desktop/api/mfobjects/nf-mfobjects-imfasynccallback-invoke) is called from another thread. Your application is responsible for ensuring that any work performed inside **Invoke** is thread-safe.

By default, the thread that calls [**Invoke**](/windows/desktop/api/mfobjects/nf-mfobjects-imfasynccallback-invoke) makes no assumptions about the behavior of your callback object. Optionally, you can implement the [**IMFAsyncCallback::GetParameters**](/windows/desktop/api/mfobjects/nf-mfobjects-imfasynccallback-getparameters) method to return information about your callback implementation. Otherwise, this method can return **E\_NOTIMPL**:


```C++
    STDMETHODIMP GetParameters(DWORD* pdwFlags, DWORD* pdwQueue)
    {
        // Implementation of this method is optional.
        return E_NOTIMPL;
    }
```



If you specified a state object in the **Begin** method, you can retrieve it from inside your callback method by calling [**IMFAsyncResult::GetState**](/windows/desktop/api/mfobjects/nf-mfobjects-imfasyncresult-getstate).

## Related topics

<dl> <dt>

[Asynchronous Callback Methods](asynchronous-callback-methods.md)
</dt> </dl>

 

 



