---
title: To Configure the Indexer
description: To Configure the Indexer
ms.assetid: 0e28e8dd-1586-45e6-8a08-5245d465d068
keywords:
- Windows Media Format SDK,configuring indexers
- Advanced Systems Format (ASF),configuring indexers
- ASF (Advanced Systems Format),configuring indexers
- indexes,configuring indexers
ms.topic: article
ms.date: 05/31/2018
---

# To Configure the Indexer

You can configure the indexer before using it to index an ASF file. Each stream in the file can be configured separately, or you can set the same configuration for all streams.

If you are configuring multiple steams for indexing in a file, you must configure them all and then begin indexing. If you configure and index a stream and then configure another stream in the same file, starting the indexer again will delete the first index. This is to comply with the ASF file format.

The following code shows how to configure the indexer. The code assumes that the file to be indexed has two streams: the first is an audio stream which does not need to be indexed, and the second is a video stream. This code shows only how to configure the indexer. To index a file, you must follow the steps presented in [To Index an ASF File](to-index-an-asf-file.md).


```C++
IWMIndexer*  pBaseIndexer = NULL;
IWMIndexer2* pMyIndexer   = NULL;

DWORD          dwInterval;
HRESULT hr = S_OK;

// Initialize COM.
hr = CoInitialize(NULL);

// Create an indexer.
hr = WMCreateIndexer(&pBaseIndexer);

// Retrieve an IWMIndexer2 interface pointer for the indexer just created.
hr = pBaseIndexer->QueryInterface(IID_IWMIndexer2, (void**)&pMyIndexer);

// Release the base indexer.
pBaseIndexer->Release();
pBaseIndexer = NULL;

// Set the index interval to 5 frames.
dwInterval = 5;

// Configure the indexer to create a frame-based index.
hr = pMyIndexer->Configure(2,                    // Stream Number.
                           WMT_IT_FRAME_NUMBERS, // Indexer type.
                           (void *)&dwInterval,  // Index interval.
                           NULL;        // Index type, use default.

// TODO: Index the file. See To Index an ASF File.

// Release the remaining interface.
pMyIndexer->Release();
pMyIndexer = NULL;

```



> [!Note]  
> The default index type is WMT\_IT\_NEAREST\_CLEAN\_POINT. Although you can set the index type to other values, doing so will degrade seeking performance.

 

## Related topics

<dl> <dt>

[**IWMIndexer2::Configure**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmindexer2-configure)
</dt> <dt>

[**To Index an ASF File**](to-index-an-asf-file.md)
</dt> <dt>

[**WMCreateIndexer**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreateindexer)
</dt> <dt>

[**Working with Indexes**](working-with-indexes.md)
</dt> </dl>

 

 




