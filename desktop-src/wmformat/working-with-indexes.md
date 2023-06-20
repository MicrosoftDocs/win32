---
title: Working with Indexes
description: Working with Indexes
ms.assetid: 7daa4b29-0597-462d-ad65-135d0ef7362d
keywords:
- Windows Media Format SDK,indexes
- Advanced Systems Format (ASF),indexes
- ASF (Advanced Systems Format),indexes
- indexes,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Working with Indexes

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media Format SDK supports seeking and striding through content. Seeking enables you to specify a place on the file's timeline to begin playback. Striding enables you to fast-forward and rewind the output of a file. Files must be indexed to take advantage of these features. An index is a series of values representing positions in the file (either presentation times, frame numbers, or SMTPE time codes) with corresponding offsets into the data section of the file for each. Indexing is most important for video streams, as audio stream presentation time can be easily estimated. However, some audio streams may require indexes as well. By default, the writer will index every new ASF file. If changes are made to the content of a file, you must refresh the index yourself using the indexer object.

The indexer supports both temporal and frame-based indexing as well as indexing based on SMPTE time codes (if present). The writer will create a temporal index by default for every new video stream encoded to a file. You must explicitly configure and call the indexer to create a frame-based or SMPTE time code index.

When changes are made to the content of an ASF file, it must be indexed again.

The following sections present example code for performing common indexing tasks.

-   [To Disable Automatic Indexing](to-disable-automatic-indexing.md)
-   [To Configure the Indexer](to-configure-the-indexer.md)
-   [To Index an ASF File](to-index-an-asf-file.md)
-   [To Stop Indexing in Progress](to-stop-indexing-in-progress.md)

In addition, the DSCopy sample application illustrates the use of the indexer. For more information, see [Sample Applications](sample-applications.md).

 

 




