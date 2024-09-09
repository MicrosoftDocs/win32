---
title: Working with Metadata
description: Working with Metadata
ms.assetid: 15d835c2-e227-4e69-a8b2-9b1c6d671022
keywords:
- Windows Media Format SDK,metadata overview
- Advanced Systems Format (ASF),metadata overview
- ASF (Advanced Systems Format),metadata overview
- metadata,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Working with Metadata

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Metadata support is provided by the writer object, the reader and synchronous reader objects, and the metadata editor object. For general information about metadata, see [Metadata](metadata.md). For information about the features supporting metadata in the Windows Media Format SDK, see [Metadata Features](metadata-features.md).

The interface for metadata editing is [**IWMHeaderInfo3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo3), which you can obtain by calling the **QueryInterface** method of any interface in one of the objects listed above. **IWMHeaderInfo3** inherits the methods of [**IWMHeaderInfo**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo) and [**IWMHeaderInfo2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo2). The methods of **IWMHeaderInfo3** that deal with metadata attributes represent a different approach to accessing metadata than that used by the methods of **IWMHeaderInfo**. You should always use the newer methods.

Metadata in an ASF file is identified by an index and a stream number. File-level attributes are assigned a stream number of 0. In previous versions of the Windows Media Format SDK, attributes could be identified by name. However, because you can now duplicate attribute names within a stream, this is no longer possible. Instead, you can retrieve all the indexes matching a name. For more information, see [Retrieving Metadata Attributes](retrieving-metadata-attributes.md).

To aid in finding attributes quickly, you can use a special stream number, 0xFFFF. Use this stream number to identify the file as a whole, rather than a specific stream or the file-level attributes. The objects of the Windows Media Format SDK maintain separate indexes for each stream and for the file-level attributes. When using stream 0xFFFF, the indexes are different from those you use when specifying a specific stream. For example, the attribute that is index 0 for stream 0 will not be the same as the attribute that is index 0 for stream 0xFFFF.

The following sections describe the use of metadata in greater detail.



| Section                                                                    | Description                                                                       |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [Retrieving Metadata Attributes](retrieving-metadata-attributes.md)       | Describes how to read metadata attributes from a file header.                     |
| [Setting Metadata Attributes](setting-metadata-attributes.md)             | Describes how to add new metadata attributes to a file header.                    |
| [Editing Metadata Attributes](editing-metadata-attributes.md)             | Describes how to edit existing metadata attributes.                               |
| [Removing Metadata Attributes](removing-metadata-attributes.md)           | Describes how to remove existing metadata attributes.                             |
| [Using Complex Metadata Attributes](using-complex-metadata-attributes.md) | Describes how to work with attributes whose values are represented by structures. |



 

Several of the sample applications show how to retrieve and edit metadata. In particular, see the MetadataEdit sample, which comes in both C++ and C# versions.

## Related topics

<dl> <dt>

[**Attributes**](attributes.md)
</dt> <dt>

[**Programming Guide**](programming-guide.md)
</dt> <dt>

[**Sample Applications**](sample-applications.md)
</dt> </dl>

 

 




