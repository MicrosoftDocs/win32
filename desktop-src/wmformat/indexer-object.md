---
title: Indexer Object
description: Indexer Object
ms.assetid: 652e04a5-ed6e-4e92-acf4-55ed82f77ef1
keywords:
- Windows Media Format SDK,indexer objects
- Advanced Systems Format (ASF),indexer objects
- ASF (Advanced Systems Format),indexer objects
- objects,indexer objects
- indexer objects
- indexes,indexer objects
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Indexer Object

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The indexer object creates an index in an ASF file. An index is a standard part of an ASF file that equates video samples with times, frame numbers, or (if applicable) Society of Motion Picture and Television Engineers (SMPTE) standard time stamps. Without an index, neither the reader object nor the synchronous reader object can seek to a point in the middle of a file.

Indexes created by this object are only necessary if the file contains one or more video streams. This is because audio data is not temporally compressed, making it easy to find a given time in an audio stream.

The indexer object is created by the [**WMCreateIndexer**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreateindexer) function, which sets a pointer to an **IWMIndexer** interface. The other interfaces of the indexer object can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by the indexer object.



| Interface                          | Description                                                                         |
|------------------------------------|-------------------------------------------------------------------------------------|
| [**IWMIndexer**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmindexer)   | Starts and stops the indexing process.                                              |
| [**IWMIndexer2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmindexer2) | Configures the indexer, enabling indexing by frame, by time, or by SMPTE time code. |



 

The following callback interface must be implemented by the application in order to use the indexer object.



| Interface                                      | Description                                                                |
|------------------------------------------------|----------------------------------------------------------------------------|
| [**IWMStatusCallback**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstatuscallback) | Receives status messages from processes that execute in a separate thread. |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Working with Indexes**](working-with-indexes.md)
</dt> </dl>

 

 




