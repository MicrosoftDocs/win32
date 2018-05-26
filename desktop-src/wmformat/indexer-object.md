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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Indexer Object

The indexer object creates an index in an ASF file. An index is a standard part of an ASF file that equates video samples with times, frame numbers, or (if applicable) Society of Motion Picture and Television Engineers (SMPTE) standard time stamps. Without an index, neither the reader object nor the synchronous reader object can seek to a point in the middle of a file.

Indexes created by this object are only necessary if the file contains one or more video streams. This is because audio data is not temporally compressed, making it easy to find a given time in an audio stream.

The indexer object is created by the [**WMCreateIndexer**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreateindexer?branch=master) function, which sets a pointer to an **IWMIndexer** interface. The other interfaces of the indexer object can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by the indexer object.



| Interface                          | Description                                                                         |
|------------------------------------|-------------------------------------------------------------------------------------|
| [**IWMIndexer**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmindexer?branch=master)   | Starts and stops the indexing process.                                              |
| [**IWMIndexer2**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmindexer2?branch=master) | Configures the indexer, enabling indexing by frame, by time, or by SMPTE time code. |



 

The following callback interface must be implemented by the application in order to use the indexer object.



| Interface                                      | Description                                                                |
|------------------------------------------------|----------------------------------------------------------------------------|
| [**IWMStatusCallback**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmstatuscallback?branch=master) | Receives status messages from processes that execute in a separate thread. |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Working with Indexes**](working-with-indexes.md)
</dt> </dl>

 

 




