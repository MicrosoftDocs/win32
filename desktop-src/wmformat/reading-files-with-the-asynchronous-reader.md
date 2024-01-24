---
title: Reading Files with the Asynchronous Reader
description: Reading Files with the Asynchronous Reader
ms.assetid: 3cc72f8d-bf1f-416d-bc90-21dfb92a55aa
keywords:
- Windows Media Format SDK,reading files
- Windows Media Format SDK,asynchronous readers
- Advanced Systems Format (ASF),asynchronous readers
- ASF (Advanced Systems Format),asynchronous readers
- Advanced Systems Format (ASF),reading files
- ASF (Advanced Systems Format),reading files
- asynchronous readers,IWMReaderCallback interface
- IWMReaderCallback,asynchronous readers
- asynchronous readers,reading files
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Reading Files with the Asynchronous Reader

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The asynchronous reader reads the content from ASF files using multiple threads and asynchronous calls. The features supported by the asynchronous reader make it well suited for applications that render content to end users.

The most basic functionality of the reader object can be broken down into the following steps. In these steps "the application" refers to the program you write using the Windows Media Format SDK.

1.  The application implements the [**IWMReaderCallback**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreadercallback) interface to handle messages from the reader. This includes two callback methods: **OnStatus**, which receives messages relating to the status of various aspects of the reader and **OnSample**, which receives uncompressed samples from the reader.
2.  The application passes to the reader the name of a file to read. When the reader opens the file, it assigns an output number to each stream. If the file uses mutual exclusion, the reader assigns a single output for all of the mutually exclusive streams.
3.  The application gets information about the configuration of the various outputs from the reader. The information gathered will enable the application to properly render media samples.
4.  The application instructs the reader to begin reading data from the file. The reader begins delivering uncompressed samples to the **OnSample** callback one at a time in buffers wrapped in buffer objects. The samples delivered by the reader are in presentation-time order. The reader will continue delivering samples until stopped by the application or until the end of the file is reached.
5.  The application is responsible for rendering data after it is delivered by the reader. The Windows Media Format SDK does not provide any rendering routines. Typically, applications will use other SDKs to render data, such as the Microsoft DirectX® SDK, or the multimedia functions of the Microsoft Windows Platform SDK.
6.  When reading is complete, the application instructs the reader to close the file.

These steps are illustrated in the AudioPlayer sample application, among others. For more information, see [Sample Applications](sample-applications.md).

The reader also supports more advanced functionality. The reader enables you to do the following:

-   Pause playback of a file.
-   Retrieve reader performance statistics.
-   Control stream selection for mutually exclusive streams.
-   Manually allocate buffers for output.
-   Provide your own clock.
-   Retrieve the status of file operations (buffering, download, or save).
-   Open a file using the standard COM interface, **IStream**.
-   Seek to specific points in an ASF file.
-   Read profile data from the header of the file.

The following sections describe the use of the reader object in detail.

-   [To Implement Reader Messages in the OnStatus Callback](to-implement-reader-messages-in-the-onstatus-callback.md)
-   [To Implement the OnSample Callback](to-implement-the-onsample-callback.md)
-   [To Create a Reader and Open a File](to-create-a-reader-and-open-a-file.md)
-   [To Retrieve Media Samples with the Asynchronous Reader](to-retrieve-media-samples-with-the-asynchronous-reader.md)
-   [To Seek By Time Using the Asynchronous Reader](to-seek-by-time-using-the-asynchronous-reader.md)
-   [To Seek By Frame Number Using the Asynchronous Reader](to-seek-by-frame-number-using-the-asynchronous-reader.md)
-   [To Seek By SMPTE Time Code Using the Asynchronous Reader](to-seek-by-smpte-time-code-using-the-asynchronous-reader.md)
-   [To Seek to Markers](to-seek-to-markers.md)
-   [To Pause or Stop Playback](to-pause-or-stop-playback.md)
-   [To Get Reader Performance Statistics](to-get-reader-performance-statistics.md)
-   [To Use Manual Stream Selection](to-use-manual-stream-selection.md)
-   [To Deliver Compressed Samples with the Asynchronous Reader](to-deliver-compressed-samples-with-the-asynchronous-reader.md)

## Related topics

<dl> <dt>

[**Reading ASF Files**](reading-asf-files.md)
</dt> <dt>

[**Reader Object**](reader-object.md)
</dt> </dl>

 

 




