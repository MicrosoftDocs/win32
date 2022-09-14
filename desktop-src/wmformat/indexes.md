---
title: Indexes
description: Indexes
ms.assetid: 54c694f6-3c10-4d7c-bcd1-f2b17d652e8e
keywords:
- Windows Media Format SDK,indexes
- Advanced Systems Format (ASF),indexes
- ASF (Advanced Systems Format),indexes
- Windows Media Format SDK,temporal indexes
- Advanced Systems Format (ASF),temporal indexes
- ASF (Advanced Systems Format),temporal indexes
- Windows Media Format SDK,frame-based indexes
- Advanced Systems Format (ASF),frame-based indexes
- ASF (Advanced Systems Format),frame-based indexes
- Windows Media Format SDK,SMPTE time codes
- Advanced Systems Format (ASF),SMPTE time codes
- ASF (Advanced Systems Format),SMPTE time codes
- indexes,about
- temporal indexes
- frame-based indexes
- SMPTE time codes,indexes
ms.topic: article
ms.date: 05/31/2018
---

# Indexes

A common requirement for applications that read digital media files is the ability to seek to a specific point in the content. Seeking can be difficult because there is no guarantee that the various streams in a file have samples with concurrent start times. This problem is addressed with the use of *indexes*. An index is an object in an ASF file that equates video samples with their presentation times. No index is required for audio streams because audio data is more closely connected with presentation time than video data is.

The indexer object of the Windows Media Format SDK can create three different types of indexes: temporal indexes, frame-based indexes, and SMPTE time code indexes.

Temporal indexes are the most common type. They simply equate video samples with the corresponding presentation times.

A frame-based index equates video samples with video frame numbers and presentation times. Frame numbers are particularly useful in applications that edit video.

A SMTPE time code index is the rarest type of index. It uses SMPTE time code as the basis of the index and can be used only on streams that have SMPTE time stamps included with their samples. For more information about SMPTE time code, see [SMPTE Time Code Support](smpte-time-code-support.md).

An ASF file can contain an index of each type for each video stream it contains. As a default, a temporal index is included for each video stream in files created by the writer object. You can change the automatic indexing settings for your files to suit your needs.

## Related topics

<dl> <dt>

[**ASF File Features**](asf-file-features.md)
</dt> <dt>

[**Working with Indexes**](working-with-indexes.md)
</dt> <dt>

[**Reading Files with the Asynchronous Reader**](reading-files-with-the-asynchronous-reader.md)
</dt> <dt>

[**Reading Files with the Synchronous Reader**](reading-files-with-the-synchronous-reader.md)
</dt> </dl>

 

 




