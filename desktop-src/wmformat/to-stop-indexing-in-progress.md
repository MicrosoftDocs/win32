---
title: To Stop Indexing in Progress
description: To Stop Indexing in Progress
ms.assetid: 76c641fa-ea00-4035-bc30-a92059da584a
keywords:
- Windows Media Format SDK,stopping indexing in progress
- Advanced Systems Format (ASF),stopping indexing in progress
- ASF (Advanced Systems Format),stopping indexing in progress
- indexes,stopping indexing in progress
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Stop Indexing in Progress

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

After you begin indexing with a call to [**IWMIndexer::StartIndexing**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmindexer-startindexing), the indexer will normally continue until the file is indexed. You can stop indexing operations by calling the [**IWMIndexer::Cancel**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmindexer-cancel) method. After you have canceled indexing, you can call **StartIndexing** again, but the indexer will start from the beginning of the file rather than resuming from the point of cancellation.

Because **StartIndexing** is an asynchronous call, you will normally need to call **Cancel** from some other thread or event handler in your application. Typically **Cancel** will be called from an event procedure associated with a button control of a Windows application.

When indexing is canceled, the indexer will pass a status message of WMT\_CLOSED, just as if the file had been indexed properly.

## Related topics

<dl> <dt>

[**IWMIndexer Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmindexer)
</dt> <dt>

[**Working with Indexes**](working-with-indexes.md)
</dt> </dl>

 

 




