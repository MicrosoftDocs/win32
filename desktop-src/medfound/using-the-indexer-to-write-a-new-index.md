---
description: This topic shows how to write an index for an Advanced Systems Format (ASF) file.
ms.assetid: a14e3bef-0232-4259-930a-d860ed9230fd
title: Using the Indexer to Write a New Index
ms.topic: article
ms.date: 05/31/2018
---

# Using the Indexer to Write a New Index

This topic shows how to write an index for an Advanced Systems Format (ASF) file.

Here is the general procedure for creating an ASF index:

1.  Initialize a new instance of the ASF indexer object, as described in [Indexer Creation and Configuration](indexer-creation-and-configuration.md).
2.  Optionally, configure the indexer.
3.  Send ASF data packets to the indexer.
4.  Commit the index.
5.  Get the completed index from the indexer, and write it to a stream.

## Configure the Indexer

To use the indexer to write a new index object, the indexer object must have the flag MFASF\_INDEXER\_WRITE\_NEW\_INDEX set with a call to [**IMFASFIndexer::SetFlags**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfindexer-setflags) before it is initialized with [**IMFASFIndexer::Initialize**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfindexer-initialize).

When the indexer is configured for writing an index, the caller chooses the streams to be indexed. By default, the indexer attempts to create an Index Object for all streams. The default time interval is one second.

[**IMFASFIndexer::SetIndexStatus**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfindexer-setindexstatus) can be used to override the indexer object's default choice of streams and index types.

The following example code shows the initialization of an ASF\_INDEX\_DESCRIPTOR and an ASF\_INDEX\_IDENTIFIER before a call to [**SetIndexStatus**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfindexer-setindexstatus).


```
ASF_INDEX_DESCRIPTOR IndexerType;
ZeroMemory(&IndexerType, sizeof(ASF_INDEX_DESCRIPTOR));

ASF_INDEX_IDENTIFIER IndexIdentifier;
ZeroMemory(&IndexIdentifier, sizeof(ASF_INDEX_IDENTIFIER));

IndexIdentifier.guidIndexType = GUID_NULL;
IndexIdentifier.wStreamNumber = 1;

IndexerType.Identifier = IndexIdentifier;
IndexerType.cPerEntryBytes  = MFASFINDEXER_PER_ENTRY_BYTES_DYNAMIC;
IndexerType.dwInterval  = MFASFINDEXER_NO_FIXED_INTERVAL;

hr = pIndexer->SetIndexStatus((BYTE*)&IndexerType, sizeof(ASF_INDEX_DESCRIPTOR), TRUE);
```



The index identifier must have its GUID index type set to GUID\_NULL to indicate that the index type will be presentation time-based. The index identifier must also be initialized with the stream number of the ASF stream to be indexed. After the index identifier is set, use it to initialize the index descriptor.

The index descriptor structure has members which must be set before the call to [**SetIndexStatus**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfindexer-setindexstatus). **Identifier** is an [**ASF\_INDEX\_IDENTIFIER**](/windows/desktop/api/wmcontainer/ns-wmcontainer-asf_index_identifier) structure that identifies the stream number and the type of index. **cPerEntryBytes** is the number of bytes used for each index entry. If the value is MFASFINDEXER\_PER\_ENTRY\_BYTES\_DYNAMIC, the index entries have variable size. **dwInterval** is the indexing interval. A value of MFASFINDEXER\_NO\_FIXED\_INTERVAL indicates that there is no fixed indexing interval.

## Send ASF Data Packets to the Indexer

Because the indexer is a WMContainer level object, it must be used in conjunction with the multiplexer during packet generation.

Packets returned from [**GetNextPacket**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmultiplexer-getnextpacket) can be sent to the indexer object through calls to [**GenerateIndexEntries**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfindexer-generateindexentries) where it creates index entries for each packet sent.

The following code demonstrates how this may be done:


```C++
HRESULT SendSampleToMux(
    IMFASFMultiplexer *pMux,
    IMFASFIndexer *pIndex,
    IMFSample *pSample,
    WORD wStream,
    IMFByteStream *pDestStream
    )
{
    IMFSample *pOutputSample = NULL;
    IMFMediaBuffer *pDataPacket = NULL;

    DWORD dwMuxStatus = ASF_STATUSFLAGS_INCOMPLETE;

    HRESULT hr = pMux->ProcessSample(wStream, pSample, 0);
    if (FAILED(hr))
    {
        goto done;
    }

    while (dwMuxStatus & ASF_STATUSFLAGS_INCOMPLETE)
    {
        hr = pMux->GetNextPacket(&dwMuxStatus, &pOutputSample);
        if (FAILED(hr))
        {
            goto done;
        }

        if (pOutputSample)
        {
            // Send the data packet to the indexer
            hr = pIndex->GenerateIndexEntries(pOutputSample);
            if (FAILED(hr))
            {
                goto done;
            }

            // Convert the sample to a contiguous buffer.
            hr = pOutputSample->ConvertToContiguousBuffer(&pDataPacket);
            if (FAILED(hr))
            {
                goto done;
            }

            // Write the buffer to the byte stream.
            hr = WriteBufferToByteStream(pDestStream, pDataPacket, NULL);
            if (FAILED(hr))
            {
                goto done;
            }
        }

        SafeRelease(&pOutputSample);
        SafeRelease(&pDataPacket);
    }

done:
    SafeRelease(&pOutputSample);
    SafeRelease(&pDataPacket);
    return hr;
}
```



For more information, see [Generating New ASF Data Packets](generating-new-asf-data-packets.md).

## Commit the Index

After the last packet has had an index entry created for it, the index must be committed. This is done with a call to [**IMFASFIndexer::CommitIndex**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfindexer-commitindex). **CommitIndex** takes a pointer to the ContentInfo object which describes the content of the ASF file. Committing the index finishes the indexing and updates the header with new information about file size and seekability.

## Get the Completed Index

To get the completed index from the indexer, perform the following steps:

1.  Call [**IMFASFIndexer::GetIndexWriteSpace**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfindexer-getindexwritespace) to get the size of the index.
2.  Call [**MFCreateMemoryBuffer**](/windows/desktop/api/mfapi/nf-mfapi-mfcreatememorybuffer) to create a media buffer. You can either allocate an buffer that is large enough to hold the entire index, of allocate a smaller buffer and get the index in chunks.
3.  Call [**IMFASFIndexer::GetCompletedIndex**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfindexer-getcompletedindex) to get the index data. On the first call, set the *cbOffsetWithinIndex* parameter to zero. If you get the index in chunks, increment *cbOffsetWithinIndex* each time by the size of the data from the previous call.
4.  Call [**IMFMediaBuffer::Lock**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediabuffer-lock) to get a pointer to the index data and the size of the data.
5.  Write the index data to the ASF file.
6.  Call [**IMFMediaBuffer::Unlock**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediabuffer-unlock) to unlock the media buffer.
7.  Repeat steps 3–6 until you have written the entire index.

The following code shows these steps:


```C++
HRESULT WriteASFIndex(IMFASFIndexer *pIndex,IMFByteStream *pStream)
{
    const DWORD cbChunkSize = 4096;

    IMFMediaBuffer *pBuffer = NULL;

    QWORD cbIndex = 0;
    DWORD cbIndexWritten = 0;

    HRESULT hr = pIndex->GetIndexWriteSpace(&cbIndex);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = MFCreateMemoryBuffer(cbChunkSize, &pBuffer);
    if (FAILED(hr))
    {
        goto done;
    }

    while (cbIndexWritten < cbIndex)
    {
        BYTE *pData = NULL;
        DWORD cbData = 0;
        DWORD cbWritten = 0;

        hr = pIndex->GetCompletedIndex(pBuffer, cbIndexWritten);
        if (FAILED(hr))
        {
            goto done;
        }

        hr = pBuffer->Lock(&pData, NULL, &cbData);
        if (FAILED(hr))
        {
            goto done;
        }

        hr = pStream->Write(pData, cbData, &cbWritten);

        (void)pBuffer->Unlock();

        if (FAILED(hr))
        {
            goto done;
        }

        cbIndexWritten += cbData;
    }

done:
    SafeRelease(&pBuffer);
    return hr;
};
```



## Related topics

<dl> <dt>

[ASF Indexer](asf-index-object.md)
</dt> </dl>

 

 



