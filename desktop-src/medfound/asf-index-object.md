---
description: ASF Indexer
ms.assetid: 3f95b0ac-d70f-4bc2-8524-c7de1df34afa
title: ASF Indexer
ms.topic: article
ms.date: 05/31/2018
---

# ASF Indexer

The ASF *indexer* is a WMContainer layer component that is used to read or write Index Objects in an Advanced Systems Format (ASF) file. For information about the structure of an ASF file, see [ASF File Structure](asf-file-structure.md).

An application can use the indexer to perform seeking based on presentation time or to generate new index entries for an ASF file. The ASF indexer implements the [**IMFASFIndexer**](/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfindexer) interface.




| Index type | Description | 
|------------|-------------|
| Presentation time-based Index | Provides presentation time-based indexing for audio and video streams in index blocks to make indexing more space efficient. Each index block references index entries that contain a byte offset. <br /> The offset is the position of the data packet being seeked, relative to the start of the ASF Data Object.<br /> GUID_NULL must be used as the GUID type for the index identifier. For more information; see <a href="using-the-indexer-to-write-a-new-index.md">Using the Indexer to Write a New Index</a>.<br /> | 
| Timecode Index | Facilitates seeking by timecode in streams which contain timecode metadata. The timecodes conform to a SMPTE format (<em>Hours:Minutes:Seconds:Frames</em>). Each index block references index entries that contain a byte offset. <br /> The offset is the position of the data packet being seeked, relative to the start of the ASF Data Object.<br /><blockquote>[!Note]<br />Timecode index objects are not currently supported.</blockquote><br /><br /> | 
| Frame-based Index | Provides frame-based indexing for video streams. Indexes into the frame-based index are in terms of frame numbers, with the first frame for a stream in the ASF file corresponding to entry 0 in the frame-based index object. Each index block references index entries that contain a byte offset.<br /><blockquote>[!Note]<br />Frame-based index objects are not currently supported.</blockquote><br /><br /> | 




 

This section contains the following topics.



| Topic                                                                                | Description                                                                                                                      |
|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [Indexer Creation and Configuration](indexer-creation-and-configuration.md)         | How to create an indexer object and configure it for reading an existing index or for writing a new ASF Index Object for a file. |
| [Using the Indexer to Seek in a File](using-the-indexer-to-seek.md)                 | How to use the indexer to seek within an ASF file.                                                                               |
| [Using the Indexer to Write a New Index](using-the-indexer-to-write-a-new-index.md) | How to use the indexer to generate index entries and write a new Index Object for an ASF file.                                   |



 

## Related topics

<dl> <dt>

[WMContainer ASF Components](wmcontainer-asf-components.md)
</dt> <dt>

[ASF Support in Media Foundation](asf-support-in-media-foundation.md)
</dt> </dl>

 

 




