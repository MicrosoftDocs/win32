---
Description: The ASF indexer is a WMContainer layer component that is used to read or write Index Objects in an Advanced Systems Format (ASF) file. This topic provides information about using the ASF indexer to seek within an ASF file.
ms.assetid: 9c501d33-847e-448e-a19c-39dfbc7757ca
title: Using the Indexer to Seek Within an ASF File
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using the Indexer to Seek Within an ASF File

The ASF *indexer* is a WMContainer layer component that is used to read or write Index Objects in an Advanced Systems Format (ASF) file. This topic provides information about using the ASF indexer to seek within an ASF file.

-   [Initializing the Indexer for Seeking](#initializing-the-indexer-for-seeking)
-   [Getting the Seek Position.](#getting-the-seek-position)
-   [Related topics](#related-topics)

For information about the structure of an ASF file, see [ASF File Structure](asf-file-structure.md).

## Initializing the Indexer for Seeking

To initialize the ASF indexer for seeking:

1.  Call [**MFCreateASFIndexer**](/windows/win32/wmcontainer/nf-wmcontainer-mfcreateasfindexer?branch=master) to create a new instance of the ASF indexer.
2.  Call [**IMFASFIndexer::Initialize**](/windows/win32/wmcontainer/nf-wmcontainer-imfasfindexer-initialize?branch=master) to initialize the indexer. This method gets information from the ASF header to determine which ASF streams are indexed. By default, the indexer object is configured for seeking.
3.  Call [**IMFASFIndexer::GetIndexPosition**](/windows/win32/wmcontainer/nf-wmcontainer-imfasfindexer-getindexposition?branch=master) to find the offset of the index within the ASF file.
4.  Call the [**MFCreateASFIndexerByteStream**](/windows/win32/wmcontainer/nf-wmcontainer-mfcreateasfindexerbytestream?branch=master) function to create a byte stream for reading the index. The input to this function is a pointer to a byte stream that contains the ASF file, and the offset of the index (from the previous step).
5.  Call [**IMFASFIndexer::SetIndexByteStreams**](/windows/win32/wmcontainer/nf-wmcontainer-imfasfindexer-setindexbytestreams?branch=master) to set the index byte stream on the indexer.

The following code shows these steps:


```C++
HRESULT CreateASFIndexer(
    IMFByteStream *pContentByteStream,  // Pointer to the content byte stream
    IMFASFContentInfo *pContentInfo,
    IMFASFIndexer **ppIndexer
    )
{
    IMFASFIndexer *pIndexer = NULL;
    IMFByteStream *pIndexerByteStream = NULL;

    QWORD qwLength = 0, qwIndexOffset = 0, qwBytestreamLength = 0;

    // Create the indexer.
    HRESULT hr = MFCreateASFIndexer(&amp;pIndexer);
    if (FAILED(hr))
    {
        goto done;
    }

    //Initialize the indexer to work with this ASF library
    hr =  pIndexer->Initialize(pContentInfo);
    if (FAILED(hr))
    {
        goto done;
    }

    //Check if the index exists. You can only do this after creating the indexer

    //Get byte stream length
    hr = pContentByteStream->GetLength(&amp;qwLength);
    if (FAILED(hr))
    {
        goto done;
    }

    //Get index offset
    hr = pIndexer->GetIndexPosition(pContentInfo, &amp;qwIndexOffset);
    if (FAILED(hr))
    {
        goto done;
    }

    if ( qwIndexOffset >= qwLength)
    {
        //index object does not exist, release the indexer
        goto done;
    }
    else
    {
        // initialize the indexer
        // Create a byte stream that the Indexer will use to read in
        // and parse the indexers.
         hr = MFCreateASFIndexerByteStream(
             pContentByteStream,
             qwIndexOffset,
             &amp;pIndexerByteStream
             );

        if (FAILED(hr))
        {
            goto done;
        }
   }

    hr = pIndexer->SetIndexByteStreams(&amp;pIndexerByteStream, 1);
    if (FAILED(hr))
    {
        goto done;
    }

    // Return the pointer to the caller.
    *ppIndexer = pIndexer;
    (*ppIndexer)->AddRef();

done:
    SafeRelease(&amp;pIndexer);
    SafeRelease(&amp;pIndexerByteStream);
    return hr;
}
```



## Getting the Seek Position.

1.  To find out if a particular stream is indexed, call [**IMFASFIndexer::GetIndexStatus**](/windows/win32/wmcontainer/nf-wmcontainer-imfasfindexer-getindexstatus?branch=master). If the stream is indexed, the *pfIsIndexed* parameter receives the value **TRUE**; otherwise it receives the value **FALSE**.
2.  By default, the indexer uses forward seeking. For reverse seeking (that is, seeking from the end of the file), call [**IMFASFIndexer::SetFlags**](/windows/win32/wmcontainer/nf-wmcontainer-imfasfindexer-setflags?branch=master) and set the **MFASF\_INDEXER\_READ\_FOR\_REVERSEPLAYBACK** flag. Otherwise, skip this step.
3.  If the stream is indexed, get the seek position for a specified presentation time by calling [**IMFASFIndexer::GetSeekPositionForValue**](/windows/win32/wmcontainer/nf-wmcontainer-imfasfindexer-getseekpositionforvalue?branch=master). This method reads the ASF index and finds the index entry that is closest to the requested time. The method returns the byte offset of the data packet specified by the index entry. The byte offset is relative to the start of the ASF Data Object.

The [**GetSeekPositionForValue**](/windows/win32/wmcontainer/nf-wmcontainer-imfasfindexer-getseekpositionforvalue?branch=master) method takes a pointer to the [**ASF\_INDEX\_IDENTIFIER**](/windows/win32/wmcontainer/ns-wmcontainer-_asf_index_identifier?branch=master) structure. This structure specifies an index type and a stream identifier. Currently, the index type must be GUID\_NULL, which specifies time-based indexing.

The following code gets a seek position, given a stream identifier and target presentation time. If the call succeeds, it returns the data offset in the *pcbDataOffset* parameter and the approximate actual seek time in *phnsApproxSeekTime*.


```C++
HRESULT GetSeekPositionWithIndexer(
    IMFASFIndexer *pIndexer,
    WORD          wStreamNumber,
    MFTIME        hnsSeekTime,          // Desired seek time, in 100-nsec.
    BOOL          bReverse,
    QWORD         *pcbDataOffset,       // Receives the offset in bytes.
    MFTIME        *phnsApproxSeekTime   // Receives the approximate seek time.
    )
{
    // Query whether the stream is indexed.

    ASF_INDEX_IDENTIFIER IndexIdentifier = { GUID_NULL, wStreamNumber };

    BOOL fIsIndexed = FALSE;

    ASF_INDEX_DESCRIPTOR descriptor;

    DWORD cbIndexDescriptor = sizeof(descriptor);

    HRESULT hr = pIndexer->GetIndexStatus(
        &amp;IndexIdentifier,
        &amp;fIsIndexed,
        (BYTE*)&amp;descriptor,
        &amp;cbIndexDescriptor
        );

    if (hr == MF_E_BUFFERTOOSMALL)
    {
        hr = S_OK;
    }
    else if (FAILED(hr))
    {
        goto done;
    }

    if (!fIsIndexed)
    {
        hr = MF_E_ASF_NOINDEX;
        goto done;
    }

    if (bReverse)
    {
        hr = pIndexer->SetFlags(MFASF_INDEXER_READ_FOR_REVERSEPLAYBACK);
        if (FAILED(hr))
        {
            goto done;
        }
    }

    // Get the offset from the indexer.

    PROPVARIANT var;

    var.vt = VT_I8;
    var.hVal.QuadPart = hnsSeekTime;

    hr = pIndexer->GetSeekPositionForValue(
        &amp;var,
        &amp;IndexIdentifier,
        pcbDataOffset,
        phnsApproxSeekTime,
        0
        );

done:
    return hr;
}
```



## Related topics

<dl> <dt>

[ASF Indexer](asf-index-object.md)
</dt> </dl>

 

 



