---
title: Building Filter Graphs to Write ASF Files (QASF)
description: Building Filter Graphs to Write ASF Files (QASF)
ms.assetid: 45583c97-4e59-4a6a-987b-5486e6f33990
keywords:
- Windows Media Format SDK,building filter graphs (QASF)
- Windows Media Format SDK,DirectShow
- Windows Media Format SDK,writing ASF files (QASF)
- Advanced Systems Format (ASF),building filter graphs (QASF)
- ASF (Advanced Systems Format),building filter graphs (QASF)
- Advanced Systems Format (ASF),writing (QASF)
- ASF (Advanced Systems Format),writing (QASF)
- Advanced Systems Format (ASF),DirectShow
- ASF (Advanced Systems Format),DirectShow
- DirectShow,building filter graphs (QASF)
- DirectShow,writing ASF files (QASF)
- Windows Media Format SDK,QASF
- Advanced Systems Format (ASF),QASF
- ASF (Advanced Systems Format),QASF
- DirectShow,QASF
ms.topic: article
ms.date: 05/31/2018
---

# Building Filter Graphs to Write ASF Files (QASF)

Applications based on DirectShow typically use one of three basic types of filter graphs when creating Windows Media–based content:

-   Filter graphs for converting or transcoding content from some other format into Windows Media Format.
-   Filter graphs for inserting content that is not Windows Media-based (native stream formats) into ASF files.
-   Filter graphs for capturing live data and encoding it immediately into Windows Media Format before saving it to disk.

Each type of filter graph is described in more detail in the following sections.



| Section                                                                                                             | Description                                                                                           |
|---------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [Transcoding Files (QASF)](transcoding-files--qasf.md)                                                             | Describes how to create file-transcoding filter graphs.                                               |
| [Inserting Native Stream Formats Into ASF Files (QASF)](inserting-native-stream-formats-into-asf-files--qasf.md)   | Describes how to place any type of compressed or non-compressed audio or video data into an ASF file. |
| [Capturing Directly from a Device to an ASF File (QASF)](capturing-directly-from-a-device-to-an-asf-file--qasf.md) | Describes how to create capture filter graphs that output to an ASF file.                             |



 

 

 




