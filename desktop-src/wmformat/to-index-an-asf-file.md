---
title: To Index an ASF File
description: To Index an ASF File
ms.assetid: 33175444-365c-4b94-8b91-07198431062f
keywords:
- Windows Media Format SDK,indexing ASF files
- Advanced Systems Format (ASF),indexing files
- ASF (Advanced Systems Format),indexing files
- indexes,indexing ASF files
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Index an ASF File

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The process of indexing an ASF file is very simple. Make a call to [**IWMIndexer::StartIndexing**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmindexer-startindexing) and pass the file name. The indexer does the rest. The call to **StartIndexing** is asynchronous, so status must be monitored using the **OnStatus** callback.

The following code shows how to index an ASF file. If you want to configure the indexer prior to indexing the file, you will need to include code from the example included in [To Configure the Indexer](to-configure-the-indexer.md).

For this example, the handle that points to the event must be created as a global variable so it will be accessible by the callback. The following declaration should appear in a global scope.


```C++
HANDLE g_hEvent = NULL;

```



In a more realistic scenario, the event handle should be a data member of the class that contains both the callback and the logic for starting the indexer.

The indexer sends several events to the **OnStatus** callback after the call to **IWMIndexer::StartIndexing**. You can trap them as needed for your application. At a minimum, you need to trap WMT\_CLOSED, which is sent when indexing is complete. Use the following logic within the message switch in your implementation of the **OnStatus** callback.


```C++
// Inside the status switch statement.
case WMT_CLOSED:
   // You may want to deal with the HRESULT value passed with the status.
   // If you do, you should do it here.

   // Signal the event.
   SetEvent(g_hEvent);
   break;

```



For this example it is assumed that your implementation of the **OnStatus** callback is accessed through an object called MyCallback. For more information about using events and callbacks with this SDK, see [Using the Callback Methods](using-the-callback-methods.md).


```C++
IWMIndexer* pMyIndexer     = NULL;
HRESULT     hr             = S_OK;
WCHAR       pwszFileName[] = L"C:\SomeFile.wmv";

// Initialize COM.
hr = CoInitialize(NULL);

// Create an event for asynchronous calls.
g_hEvent = CreateEvent(NULL, TRUE, FALSE, NULL);

// Create an indexer.
hr = WMCreateIndexer(&pMyIndexer);

// TODO: Configure the indexer if needed. See To Configure the Indexer.

// Start the indexer.
hr = pMyIndexer->StartIndexing(pwszFileName, &MyCallback, NULL);

// Wait for the indexer to finish.
WaitForSingleObject(g_hEvent, INFINITE);

// Clean up.
pMyIndexer->Release();
pMyIndexer = NULL

CloseHandle(g_hEvent);
g_hEvent = NULL;

```



## Related topics

<dl> <dt>

[**IWMIndexer Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmindexer)
</dt> <dt>

[**To Configure the Indexer**](to-configure-the-indexer.md)
</dt> <dt>

[**WMCreateIndexer**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreateindexer)
</dt> <dt>

[**Working with Indexes**](working-with-indexes.md)
</dt> </dl>

 

 




