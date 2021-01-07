---
description: Implementing IWICMetadataBlockWriter
ms.assetid: 31824f21-04b1-45ca-adfa-15fd348e14a1
title: Implementing IWICMetadataBlockWriter
ms.topic: article
ms.date: 05/31/2018
---

# Implementing IWICMetadataBlockWriter

## IWICMetadataBlockWriter

-   [InitializeFromBlockReader](#initializefromblockreader)
-   [GetWriterByIndex](#getwriterbyindex)
-   [AddWriter](#addwriter)
-   [SetWriterByIndex](#setwriterbyindex)
-   [RemoveWriterByIndex](#removewriterbyindex)

The frame-level encoding class implements this interface to expose all the metadata blocks and request the appropriate metadata writer for each block. If your image format supports global metadata, outside of any individual frame, you should also implement this interface on the container-level encoder class. For a more detailed discussion of metadata handlers, refer to the section on the [**IWICMetadataBlockReader**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatablockreader) in the section on Implementing a WIC-Enabled Decoder.

``` syntax
interface IWICMetadataBlockWriter : IWICMetadataBlockReader
{
   // All methods required
   HRESULT InitializeFromBlockReader ( IWICMetadataBlockReader *pIMDBlockReader );
   HRESULT GetWriterByIndex ( UINT nIndex, IWICMetadataWriter **ppIMetadataWriter );
   HRESULT AddWriter (IWICMetadataWriter *pIMetadataWriter );
   HRESULT SetWriterByIndex ( UINT nIndex, IWICMetadataWriter *pIMetadataWriter );
   HRESULT RemoveWriterByIndex ( UINT nIndex );
}
```

### InitializeFromBlockReader

[**InitializeFromBlockReader**](/windows/desktop/api/Wincodecsdk/nf-wincodecsdk-iwicmetadatablockwriter-initializefromblockreader) uses an [**IWICMetadataBlockReader**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatablockreader) to initialize the block writer. You can get the **IWICMetadataBlockReader** from the decoder that decoded the image.


```C++
UINT blockCount = 0;
IWICMetadataReader* pMetadataReader = NULL;
IWICMetadataWriter** ppMetadataWriter = NULL;
HRESULT hr;

hr = m_pBlockReader->GetCount(&blockCount);
ppMetadataWriter = IWICMetadataWriter*[blockCount];

for (UINT x=0; x < blockCount; x++)
{
   hr = m_pBlockReader->GetReaderByIndex(&pMetadataReader);
   hr = m_pComponentFactory->CreateMetadataWriterFromReader(
         pMetadataReader, NULL, &ppMetadataWriter[x]);
}
```



Because initializing the [**IWICMetadataBlockWriter**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatablockwriter) with an [**IWICMetadataBlockReader**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatablockreader) instantiates a metadata writer for each metadata reader exposed by the **IWICMetadataBlockReader** object, the application doesn’t have to explicitly request a writer for each block of metadata.

### GetWriterByIndex

[**GetWriterByIndex**](/windows/desktop/api/Wincodecsdk/nf-wincodecsdk-iwicmetadatablockwriter-getwriterbyindex) returns the [**IWICMetadataWriter**](/windows/desktop/api/Wincodecsdk/nn-wincodecsdk-iwicmetadatawriter) object for the nth metadata block, where n is the value passed in the *nIndex* parameter. If there is no metadata writer registered that can handle the type of metadata in the nth block, the component factory will return the Unknown Metadata Handler, which will treat the block of metadata as a binary large object (BLOB). It will serialize it out as a bit stream without attempting to parse it.

### AddWriter

[**AddWriter**](/windows/desktop/api/Wincodecsdk/nf-wincodecsdk-iwicmetadatablockwriter-addwriter) allows a caller to add a new metadata writer. This is required if an application wants to add metadata of a different format than any of the existing metadata blocks. For example, an application may want to add some XMP metadata. If there is no existing XMP metadata block, the application must instantiate an XMP metadata writer and use the **AddWriter** method to include it in the collection of metadata writers.

### SetWriterByIndex

[**SetWriterByIndex**](/windows/desktop/api/Wincodecsdk/nf-wincodecsdk-iwicmetadatablockwriter-setwriterbyindex) is used to add a metadata writer at a specific index in the collection. If a metadata writer is currently exists at that index, the new one should replace it.

### RemoveWriterByIndex

[**RemoveWriterByIndex**](/windows/desktop/api/Wincodecsdk/nf-wincodecsdk-iwicmetadatablockwriter-removewriterbyindex) is used to remove a metadata writer from the collection.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Implementing IWICBitmapFrameEncode](-wic-imp-iwicbitmapframeencode.md)
</dt> <dt>

[CODEC Installation and Registration](-wic-codecinstallandreg.md)
</dt> <dt>

[How to Write a WIC-Enabled CODEC](-wic-howtowriteacodec.md)
</dt> <dt>

[Windows Imaging Component Overview](-wic-about-windows-imaging-codec.md)
</dt> </dl>

 

 



