---
title: Reading ASF Files
description: Reading ASF Files
ms.assetid: e0aabe05-b317-42ac-85fc-5a75165722d4
keywords:
- Windows Media Format SDK,reading ASF files
- Windows Media Format SDK,Advanced Systems Format (ASF)
- Advanced Systems Format (ASF),reading files
- ASF (Advanced Systems Format),reading files
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Reading ASF Files

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media Format SDK can be used to deliver media samples from an ASF file. Two objects are used to retrieve samples, the reader object and the synchronous reader object.

The reader object is the original reading object in the Windows Media Format SDK. The reader object uses an asynchronous architecture to push samples to an application. Applications built using the reader object must implement callback functions that respond to the various messages and events that result from this multi-threaded model. For clarity, this section will refer to the reader object as the asynchronous reader.

The synchronous reader object is new for this version of the Windows Media Format SDK. The synchronous reader does not use multiple threads in processing samples from ASF files. An application built using the synchronous reader retrieves samples on demand, rather than waiting for the reader to send them.

When creating an application to read ASF files, you must choose which reader object to use. In general, applications designed to deliver Windows Media-based content should be created using the asynchronous reader, while applications designed to edit ASF files should be created with the synchronous reader.

The following table lists the major features of both reader objects. Use this table to help determine which object to use for your application.



| Feature                                                                    | Async reader | Sync reader |
|----------------------------------------------------------------------------|--------------|-------------|
| Read uncompressed samples by output number                                 | Yes          | Yes         |
| Read compressed samples by stream number                                   | Yes          | Yes         |
| Read uncompressed samples by stream number                                 | No           | Yes         |
| Read from Internet site                                                    | Yes          | No          |
| Read metadata                                                              | Yes          | Yes         |
| Seek to presentation time                                                  | Yes          | Yes         |
| Seek to frame                                                              | Yes          | Yes         |
| Seek to marker                                                             | Yes          | No          |
| Switch between compressed and uncompressed sample delivery during playback | No           | Yes         |
| Open files using **IStream** interface                                     | Yes          | Yes         |



 

The following sections provide more information about working with the two reader objects.



| Section                                                                                      | Description                                                                                                                             |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [Working with Outputs](working-with-outputs.md)                                             | Describes how to use and manipulate outputs. Applies to both reader objects.                                                            |
| [Allocating Buffers for File Reading](allocating-buffers-for-file-reading.md)               | Describes how to use your own pool of buffers to hold samples delivered by the reader or synchronous reader.                            |
| [Reading Metadata at Playback](reading-metadata-at-playback.md)                             | Describes how to take advantage of metadata support at playback. Applies to both reader objects.                                        |
| [Getting Profile Information at Playback](getting-profile-information-at-playback.md)       | Describes how to access profile information for opened files. Applies to both reader objects.                                           |
| [Reading Multichannel Audio](reading-multichannel-audio.md)                                 | Describes how to configure the writer to properly decode multichannel audio.                                                            |
| [Rendering Content](rendering-content.md)                                                   | Discusses the issues related to rendering uncompressed samples. Applies to both reader objects.                                         |
| [Getting the Best Video Seeking Performance](getting-the-best-video-seeking-performance.md) | Describes ways to improve video seeking performance.                                                                                    |
| [Reading Files with the Asynchronous Reader](reading-files-with-the-asynchronous-reader.md) | Describes how to read ASF files using the asynchronous reader object.                                                                   |
| [Reading Files with the Synchronous Reader](reading-files-with-the-synchronous-reader.md)   | Describes how to read ASF files using the synchronous reader object.                                                                    |
| [Enabling DirectX Video Acceleration](enabling-directx-video-acceleration.md)               | Describes how to implement DirectX Video Acceleration to use the hardware acceleration features of some video cards for decoding video. |



 

## Related topics

<dl> <dt>

[**Programming Guide**](programming-guide.md)
</dt> <dt>

[**Reader Object**](reader-object.md)
</dt> <dt>

[**Synchronous Reader Object**](synchronous-reader-object.md)
</dt> </dl>

 

 




