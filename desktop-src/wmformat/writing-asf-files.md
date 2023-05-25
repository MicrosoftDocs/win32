---
title: Writing ASF Files
description: Writing ASF Files
ms.assetid: d722b676-bf65-4f91-8118-bb12d3bbb6cb
keywords:
- Windows Media Format SDK,writing ASF files
- Windows Media Format SDK,creating ASF files
- Windows Media Format SDK,Advanced Systems Format (ASF)
- Advanced Systems Format (ASF),writing files
- ASF (Advanced Systems Format),writing files
- Advanced Systems Format (ASF),creating files
- ASF (Advanced Systems Format),creating files
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Writing ASF Files

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can use the writer object of the Windows Media Format SDK to create ASF files from digital media data. To create an instance of the writer object, call the [**WMCreateWriter**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatewriter) function. The writer object coordinates the functionality of a number of components, including codecs, which are external to the Windows Media Format SDK.

The basic functionality of the writer object can be broken down into the following steps. In these steps, "the application" refers to the program you write using the Windows Media Format SDK.

1.  The application supplies the writer with a profile to use in creating the ASF file. When the writer loads the profile data, it assigns an input number to each connection of the profile.
2.  The application supplies the writer with an output file name for the file to be written. The writer creates a writer file sink object to manage the file creation and input. For more information, see [Writer File Sink Object](writer-file-sink-object.md).
3.  The writer creates a header for the new file based on information in the profile.
4.  The application passes uncompressed samples to the writer. Samples are passed one at a time in buffers wrapped in buffer objects. The application should pass samples for each stream concurrently so that the writer receives all samples in presentation-time order.
5.  The writer passes the samples to the appropriate codec for compression. When the writer receives the compressed samples, it interleaves them with samples from the other streams so that samples go into the file in presentation time order irrespective of stream. The sample data is then made into packets and written to the data section of the file.
6.  When all samples are processed, the writer can add an index to the file to enhance seeking performance.

These steps are illustrated in the WMStats sample application, among others. For more information, see [Sample Applications](sample-applications.md).

The writer also supports more advanced functionality, enabling you to do the following:

-   Edit metadata in the header of the file.
-   Write precompressed samples.
-   Write to network sinks for streaming live data.
-   Write to file sinks for advanced file control options.
-   Write to push sinks for distribution to servers that will deliver content to end users.
-   Deliver postview samples for verification of output.
-   Deliver writer-performance statistics.

The following sections describe the use of the writer object in detail.



| Section                                                                    | Description                                                                                            |
|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [To Use Profiles with the Writer](to-use-profiles-with-the-writer.md)     | Describes how to specify a profile to use with the writer.                                             |
| [Working with Inputs](working-with-inputs.md)                             | Describes how to identify and configure the input settings in the writer.                              |
| [To Edit Metadata with the Writer](to-edit-metadata-with-the-writer.md)   | Describes how to use the writer to edit metadata for a new file.                                       |
| [To Write Samples](to-write-samples.md)                                   | Describes how to pass samples to the writer.                                                           |
| [Setting Data Unit Extensions](setting-data-unit-extensions.md)           | Describes how to add extended data to samples.                                                         |
| [Writing Compressed Samples](writing-compressed-samples.md)               | Describes how to pass pre-compressed samples to the writer.                                            |
| [Writing Image Streams](writing-image-streams.md)                         | Describes how to configure an input for an image stream.                                               |
| [Writing Video Image Samples](writing-video-image-samples.md)             | Describes how to configure Video Image samples.                                                        |
| [Writing Variable Bit Rate Streams](writing-variable-bit-rate-streams.md) | Describes how to write variable bit rate (VBR) streams.                                                |
| [Using Two-Pass Encoding](using-two-pass-encoding.md)                     | Describes how to have the codec perform a preliminary pass before writing the file.                    |
| [To Force Key-Frame Insertion](to-force-key-frame-insertion.md)           | Describes how to manually force the codec to encode a sample as a key frame.                           |
| [To Manage Writer Latency](to-manage-writer-latency.md)                   | Describes how to minimize the time it takes the writer to process samples into an output file or sink. |
| [Working with Writer Sinks](working-with-writer-sinks.md)                 | Describes how to use writer sinks to deliver your content to files or network locations.               |
| [To Get Writer Statistics](to-get-writer-statistics.md)                   | Describes how to get statistics for the writer.                                                        |
| [To Use Writer Postview](to-use-writer-postview.md)                       | Describes how to get uncompressed samples as you write a file for verification.                        |



 

## Related topics

<dl> <dt>

[**Programming Guide**](programming-guide.md)
</dt> <dt>

[**Writer File Sink Object**](writer-file-sink-object.md)
</dt> <dt>

[**Writer Network Sink Object**](writer-network-sink-object.md)
</dt> <dt>

[**Writer Object**](writer-object.md)
</dt> </dl>

 

 




