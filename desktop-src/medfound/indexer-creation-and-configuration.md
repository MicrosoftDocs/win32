---
Description: 'This topic provides information about creating the default indexer object provided by Media Foundation.'
ms.assetid: '3a2caf11-808b-4910-b83c-a272a026f0d3'
title: Indexer Creation and Configuration
---

# Indexer Creation and Configuration

The ASF *indexer* is a WMContainer layer component that is used to read or write Index Objects in an Advanced Systems Format (ASF) file. This topic provides information about creating the default indexer object provided by Media Foundation.

For information about the structure of an ASF file, see [ASF File Structure](asf-file-structure.md).

**To create and initialize the ASF indexer**

1.  Call the [**MFCreateASFIndexer**](mfcreateasfindexer.md) function to receive an [**IMFASFIndexer**](imfasfindexer.md) pointer to the indexer object.
2.  Call [**IMFASFIndexer::SetFlags**](imfasfindexer-setflags.md) to specify the read or write mode for indexer object. By default, the indexer is configured for forward seeking.

    

    | Use                       | Flag                                           |
    |---------------------------|------------------------------------------------|
    | Reading (forward seeking) | Zero (default)                                 |
    | Reading (reverse seeking) | **MFASF\_INDEXER\_READ\_FOR\_REVERSEPLAYBACK** |
    | Writing                   | MFASF\_INDEXER\_WRITE\_NEW\_INDEX              |

    

     

    > [!Note]  
    > The same instance of the indexer cannot be used for both reading and writing. You must configure the indexer for one or the other.

     

3.  Call [**IMFASFIndexer::Initialize**](imfasfindexer-initialize.md) to initialize the indexer by specifying the [**IMFASFContentInfo**](imfasfcontentinfo.md) pointer of the ContentInfo object that describes the file to be written or read. The ContentInfo object contains information that constitutes the [ASF Header Object](asf-file-structure.md#header-object). The indexer object requires a valid ContentInfo object before generating or reading index entries of an ASF file.

The following code example shows how an application can create and initialize the indexer object to work with specific ASF content. The ContentInfo object represents the ASF Header Object; the content is passed as a byte stream.


```C++
HRESULT CreateASFIndexer(
    IMFASFContentInfo* pContentInfo, 
    DWORD dwFlags,
    IMFASFIndexer** ppIndexer
    )
{
    *ppIndexer = NULL;

    IMFASFIndexer *pIndexer = NULL;

    HRESULT hr = MFCreateASFIndexer(&amp;pIndexer);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pIndexer->SetFlags(dwFlags);
    if (FAILED(hr))
    {
        goto done;
    }

    hr =  pIndexer->Initialize(pContentInfo);
    if (FAILED(hr))
    {
        goto done;
    }

    // Return the object to the caller.
    *ppIndexer = pIndexer;
    (*ppIndexer)->AddRef();

done:
    // Clean up.
    SafeRelease(&amp;pIndexer);
    return hr;
}
```



## Related topics

<dl> <dt>

[ASF Indexer](asf-index-object.md)
</dt> <dt>

[Using the Indexer to Seek Within an ASF File](using-the-indexer-to-seek.md)
</dt> <dt>

[Using the Indexer to Write a New Index](using-the-indexer-to-write-a-new-index.md)
</dt> </dl>

 

 



