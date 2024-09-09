---
title: Retrieving Metadata Attributes
description: Retrieving Metadata Attributes
ms.assetid: d1d2c8e0-7445-4ee1-94d9-4c1ed74f8fe2
keywords:
- Windows Media Format SDK,retrieving metadata attributes
- Advanced Systems Format (ASF),retrieving metadata attributes
- ASF (Advanced Systems Format),retrieving metadata attributes
- metadata,retrieving attributes
- streams,retrieving metadata attributes
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Retrieving Metadata Attributes

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To retrieve an attribute from a file header, you must know the stream number and index of the attribute. You can use the [**IWMHeaderInfo3::GetAttributeIndices**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo3-getattributeindices) method to get the indexes for all attributes with the same name or all indexes in the same language. Like the other methods of [**IWMHeaderInfo3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo3), **GetAttributeIndices** deals with a single stream, or with all file-level attributes using stream 0. You can use 0xFFFF for the stream number to get global indexes matching your criteria throughout the entire file, regardless of stream number.

When you know the index of the attribute you want to retrieve, call [**IWMHeaderInfo3::GetAttributeByIndexEx**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo3-getattributebyindexex) to get the attribute. You need to make two calls to **GetAttributeByIndexEx** for each attribute retrieved. On the first call, pass **NULL** for the name and data buffer pointers to get the size needed. Then allocate buffers of the size indicated and make the second call to retrieve the name and data.

For example code showing how to retrieve metadata attributes, see [To Retrieve All Metadata in a File](to-retrieve-all-metadata-in-a-file.md).

## Related topics

<dl> <dt>

[**Working with Metadata**](working-with-metadata.md)
</dt> </dl>

 

 




