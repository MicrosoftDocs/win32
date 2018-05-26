---
Description: This topic describes how to use the Source Reader in asynchronous mode.
ms.assetid: 9D3C2780-D7DB-4151-8474-9A19EC94F6BE
title: Using the Source Reader in Asynchronous Mode
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using the Source Reader in Asynchronous Mode

This topic describes how to use the [Source Reader](source-reader.md) in asynchronous mode. In asynchronous mode, the application provides a callback interface, which is used to notify the application that data is available.

This topic assumes that you have already read the topic [Using the Source Reader to Process Media Data](processing-media-data-with-the-source-reader.md).

## Using Asynchronous Mode

The Source Reader operates either in synchronous mode or asynchronous mode. The code example shown in the previous section assumes that the Source Reader is using synchronous mode, which is the default. In synchronous mode, the [**IMFSourceReader::ReadSample**](/windows/win32/mfreadwrite/nf-mfreadwrite-imfsourcereader-readsample?branch=master) method blocks while the media source produces the next sample. A media source typically acquires data from some external source (such as a local file or a network connection), so the method can block the calling thread for a noticeable amount of time.

In asynchronous mode, the [**ReadSample**](/windows/win32/mfreadwrite/nf-mfreadwrite-imfsourcereader-readsample?branch=master) returns immediately and the work is performed on another thread. After the operation is complete, the Source Reader calls the application through the [**IMFSourceReaderCallback**](/windows/win32/mfreadwrite/nn-mfreadwrite-imfsourcereadercallback?branch=master) callback interface. To use asynchronous mode, you must provide a callback pointer when you first create the Source Reader, as follows:

1.  Create an attribute store by calling the [**MFCreateAttributes**](/windows/win32/mfapi/nf-mfapi-mfcreateattributes?branch=master) function.
2.  Set the [MF\_SOURCE\_READER\_ASYNC\_CALLBACK](mf-source-reader-async-callback.md) attribute on the attribute store. The attribute value is a pointer to your callback object.
3.  When you create the Source Reader, pass the attribute store to the creation function in the *pAttributes* parameter. All of the functions to create the Source Reader have this parameter.

The following example shows these steps.


```C++
HRESULT CreateSourceReaderAsync(
    PCWSTR pszURL, 
    IMFSourceReaderCallback *pCallback, 
    IMFSourceReader **ppReader)
{
    HRESULT hr = S_OK;
    IMFAttributes *pAttributes = NULL;

    hr = MFCreateAttributes(&amp;pAttributes, 1);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pAttributes->SetUnknown(MF_SOURCE_READER_ASYNC_CALLBACK, pCallback);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = MFCreateSourceReaderFromURL(pszURL, pAttributes, ppReader);

done:
    SafeRelease(&amp;pAttributes);
    return hr;
}
```



After you create the Source Reader, you cannot switch modes between synchronous and asynchronous.

To get data in asynchronous mode, call the [**ReadSample**](/windows/win32/mfreadwrite/nf-mfreadwrite-imfsourcereader-readsample?branch=master) method but set the last four parameters to **NULL**, as shown in the following example.


```C++
    // Request the first sample.
    hr = pReader->ReadSample(MF_SOURCE_READER_FIRST_VIDEO_STREAM, 
        0, NULL, NULL, NULL, NULL);
```



When the [**ReadSample**](/windows/win32/mfreadwrite/nf-mfreadwrite-imfsourcereader-readsample?branch=master) method completes asynchronously, the Source Reader calls your [**IMFSourceReaderCallback::OnReadSample**](/windows/win32/mfreadwrite/nf-mfreadwrite-imfsourcereadercallback-onreadsample?branch=master) method. This method has five parameters:

-   *hrStatus*: Contains an **HRESULT** value. This is the same value that [**ReadSample**](/windows/win32/mfreadwrite/nf-mfreadwrite-imfsourcereader-readsample?branch=master) would return in synchronous mode. If *hrStatus* contains an error code, you can ignore the remaining parameters.
-   *dwStreamIndex*, *dwStreamFlags*, llTimestamp, and *pSample*: These three parameters are equivalent to the last three parameters in [**ReadSample**](/windows/win32/mfreadwrite/nf-mfreadwrite-imfsourcereader-readsample?branch=master). They contain the stream number, status flags, and [**IMFSample**](/windows/win32/mfobjects/nn-mfobjects-imfsample?branch=master) pointer, respectively.


```C++
    STDMETHODIMP OnReadSample(HRESULT hrStatus, DWORD dwStreamIndex,
        DWORD dwStreamFlags, LONGLONG llTimestamp, IMFSample *pSample);
```



In addition, the callback interface defines two other methods:

-   [**OnEvent**](/windows/win32/mfreadwrite/nf-mfreadwrite-imfsourcereadercallback-onevent?branch=master). Notifies the application when certain events occur in media source, such as buffering or network connection events.
-   [**OnFlush**](/windows/win32/mfreadwrite/nf-mfreadwrite-imfsourcereadercallback-onflush?branch=master). Called when the [**Flush**](/windows/win32/mfreadwrite/nf-mfreadwrite-imfsourcereader-flush?branch=master) method completes.

## Implementing the Callback Interface

The callback interface must be thread-safe, because [**OnReadSample**](/windows/win32/mfreadwrite/nf-mfreadwrite-imfsourcereadercallback-onreadsample?branch=master) and the other callback methods are called from worker threads.

There are several different approaches you can take when you implement the callback. For example, you can do all of the work inside the callback, or you can use the callback to notify the application (for example, by signaling an event handle) and then do work from the application thread.

The [**OnReadSample**](/windows/win32/mfreadwrite/nf-mfreadwrite-imfsourcereadercallback-onreadsample?branch=master) method will be called once for every call that you make to the [**IMFSourceReader::ReadSample**](/windows/win32/mfreadwrite/nf-mfreadwrite-imfsourcereader-readsample?branch=master) method. To get the next sample, call **ReadSample** again. If an error occurs, **OnReadSample** is called with an error code for the *hrStatus* parameter.

The following example shows a minimal implementation of the callback interface. First, here is the declaration of a class that implements the interface.


```C++
#include <shlwapi.h>

class SourceReaderCB : public IMFSourceReaderCallback
{
public:
    SourceReaderCB(HANDLE hEvent) : 
      m_nRefCount(1), m_hEvent(hEvent), m_bEOS(FALSE), m_hrStatus(S_OK)
    {
        InitializeCriticalSection(&amp;m_critsec);
    }

    // IUnknown methods
    STDMETHODIMP QueryInterface(REFIID iid, void** ppv)
    {
        static const QITAB qit[] =
        {
            QITABENT(SourceReaderCB, IMFSourceReaderCallback),
            { 0 },
        };
        return QISearch(this, qit, iid, ppv);
    }
    STDMETHODIMP_(ULONG) AddRef()
    {
        return InterlockedIncrement(&amp;m_nRefCount);
    }
    STDMETHODIMP_(ULONG) Release()
    {
        ULONG uCount = InterlockedDecrement(&amp;m_nRefCount);
        if (uCount == 0)
        {
            delete this;
        }
        return uCount;
    }

    // IMFSourceReaderCallback methods
    STDMETHODIMP OnReadSample(HRESULT hrStatus, DWORD dwStreamIndex,
        DWORD dwStreamFlags, LONGLONG llTimestamp, IMFSample *pSample);

    STDMETHODIMP OnEvent(DWORD, IMFMediaEvent *)
    {
        return S_OK;
    }

    STDMETHODIMP OnFlush(DWORD)
    {
        return S_OK;
    }

public:
    HRESULT Wait(DWORD dwMilliseconds, BOOL *pbEOS)
    {
        *pbEOS = FALSE;

        DWORD dwResult = WaitForSingleObject(m_hEvent, dwMilliseconds);
        if (dwResult == WAIT_TIMEOUT)
        {
            return E_PENDING;
        }
        else if (dwResult != WAIT_OBJECT_0)
        {
            return HRESULT_FROM_WIN32(GetLastError());
        }

        *pbEOS = m_bEOS;
        return m_hrStatus;
    }
    
private:
    
    // Destructor is private. Caller should call Release.
    virtual ~SourceReaderCB() 
    {
    }

    void NotifyError(HRESULT hr)
    {
        wprintf(L"Source Reader error: 0x%X\n", hr);
    }

private:
    long                m_nRefCount;        // Reference count.
    CRITICAL_SECTION    m_critsec;
    HANDLE              m_hEvent;
    BOOL                m_bEOS;
    HRESULT             m_hrStatus;

};
```



In this example, we are not interested in the [**OnEvent**](/windows/win32/mfreadwrite/nf-mfreadwrite-imfsourcereadercallback-onevent?branch=master) and [**OnFlush**](/windows/win32/mfreadwrite/nf-mfreadwrite-imfsourcereadercallback-onflush?branch=master) methods, so they simply return **S\_OK**. The class uses an event handle to signal the application; this handle is provided through the constructor.

In this minimal example, the [**OnReadSample**](/windows/win32/mfreadwrite/nf-mfreadwrite-imfsourcereadercallback-onreadsample?branch=master) method just prints the time stamp to the console window. Then it stores the status code and the end-of-stream flag, and signals the event handle:


```C++
HRESULT SourceReaderCB::OnReadSample(
    HRESULT hrStatus,
    DWORD /* dwStreamIndex */,
    DWORD dwStreamFlags,
    LONGLONG llTimestamp,
    IMFSample *pSample      // Can be NULL
    )
{
    EnterCriticalSection(&amp;m_critsec);

    if (SUCCEEDED(hrStatus))
    {
        if (pSample)
        {
            // Do something with the sample.
            wprintf(L"Frame @ %I64d\n", llTimestamp);
        }
    }
    else
    {
        // Streaming error.
        NotifyError(hrStatus);
    }

    if (MF_SOURCE_READERF_ENDOFSTREAM & dwStreamFlags)
    {
        // Reached the end of the stream.
        m_bEOS = TRUE;
    }
    m_hrStatus = hrStatus;

    LeaveCriticalSection(&amp;m_critsec);
    SetEvent(m_hEvent);
    return S_OK;
}
```



The following code shows the application would use this callback class to read all of the video frames from a media file:


```C++
HRESULT ReadMediaFile(PCWSTR pszURL)
{
    HRESULT hr = S_OK;

    IMFSourceReader *pReader = NULL;
    SourceReaderCB *pCallback = NULL;

    HANDLE hEvent = CreateEvent(NULL, FALSE, FALSE, NULL);
    if (hEvent == NULL)
    {
        hr = HRESULT_FROM_WIN32(GetLastError());
        goto done;
    }

    // Create an instance of the callback object.
    pCallback = new (std::nothrow) SourceReaderCB(hEvent);
    if (pCallback == NULL)
    {
        hr = E_OUTOFMEMORY;
        goto done;
    }

    // Create the Source Reader.
    hr = CreateSourceReaderAsync(pszURL, pCallback, &amp;pReader);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = ConfigureDecoder(pReader, MF_SOURCE_READER_FIRST_VIDEO_STREAM);
    if (FAILED(hr))
    {
        goto done;
    }

    // Request the first sample.
    hr = pReader->ReadSample(MF_SOURCE_READER_FIRST_VIDEO_STREAM, 
        0, NULL, NULL, NULL, NULL);
    if (FAILED(hr))
    {
        goto done;
    }

    while (SUCCEEDED(hr))
    {
        BOOL bEOS;
        hr = pCallback->Wait(INFINITE, &amp;bEOS);
        if (FAILED(hr) || bEOS)
        {
            break;
        }
        hr = pReader->ReadSample(MF_SOURCE_READER_FIRST_VIDEO_STREAM,
            0, NULL, NULL, NULL, NULL);
    }

done:
    SafeRelease(&amp;pReader);
    SafeRelease(&amp;pCallback);
    return hr;
}
```



## Related topics

<dl> <dt>

[Source Reader](source-reader.md)
</dt> </dl>

 

 



