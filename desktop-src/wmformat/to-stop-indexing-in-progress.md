---
title: To Stop Indexing in Progress
description: To Stop Indexing in Progress
ms.assetid: '76c641fa-ea00-4035-bc30-a92059da584a'
keywords: ["Windows Media Format SDK,stopping indexing in progress", "Advanced Systems Format (ASF),stopping indexing in progress", "ASF (Advanced Systems Format),stopping indexing in progress", "indexes,stopping indexing in progress"]
---

# To Stop Indexing in Progress

After you begin indexing with a call to [**IWMIndexer::StartIndexing**](iwmindexer-startindexing.md), the indexer will normally continue until the file is indexed. You can stop indexing operations by calling the [**IWMIndexer::Cancel**](iwmindexer-cancel.md) method. After you have canceled indexing, you can call **StartIndexing** again, but the indexer will start from the beginning of the file rather than resuming from the point of cancellation.

Because **StartIndexing** is an asynchronous call, you will normally need to call **Cancel** from some other thread or event handler in your application. Typically **Cancel** will be called from an event procedure associated with a button control of a Windows application.

When indexing is canceled, the indexer will pass a status message of WMT\_CLOSED, just as if the file had been indexed properly.

## Related topics

<dl> <dt>

[**IWMIndexer Interface**](iwmindexer.md)
</dt> <dt>

[**Working with Indexes**](working-with-indexes.md)
</dt> </dl>

 

 




