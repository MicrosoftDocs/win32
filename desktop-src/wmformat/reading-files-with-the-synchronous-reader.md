---
title: Reading Files with the Synchronous Reader
description: Reading Files with the Synchronous Reader
ms.assetid: 18c6c0cd-478f-4325-b23e-571c33779a96
keywords:
- Windows Media Format SDK,reading files
- Windows Media Format SDK,synchronous readers
- Advanced Systems Format (ASF),synchronous readers
- ASF (Advanced Systems Format),synchronous readers
- Advanced Systems Format (ASF),reading files
- ASF (Advanced Systems Format),reading files
- synchronous readers,IWMReaderCallback interface
- IWMReaderCallback,synchronous readers
- synchronous readers,reading files
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Reading Files with the Synchronous Reader

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can use the synchronous reader to read an ASF file using synchronous calls instead of the asynchronous methods in the reader object. Using synchronous calls reduces the number of threads required to read a file. The asynchronous reader uses multiple threads for processing streams. For files with multiple streams, the number of threads used can become very large. The synchronous reader uses only one thread.

The synchronous reader was designed to meet the needs of content creation and file editing applications. You can use the synchronous reader for other applications, but its functionality is limited.

The synchronous reader can open files that are local, or files on a network using the UNC path name (such as "\\\\someshare\\somedirectory\\somefile.wmv"). You cannot stream files to the synchronous reader, or open files from an Internet location. The synchronous reader also provides support for using the **IStream** COM interface as a source.

The synchronous reader provides more versatility for retrieving samples from an ASF file than the asynchronous reader. The synchronous reader can deliver samples by stream number as well as by output. Samples delivered by stream number can be compressed or uncompressed. The synchronous reader can also switch between compressed and uncompressed delivery during playback; this feature is known as "fast editing." This feature enables an editing application to read Windows Media-based content and pass it directly through to the writer until a desired frame is reached. At that point the application can tell the reader to start delivering uncompressed content, which the application can then modify and pass to the writer for recompression. When the application has finished modifying the specified frames, it can tell the reader to start delivering compressed frames again.

The most basic functionality of the synchronous reader object can be broken down into the following steps. In these steps "the application" refers to the program you write using the Windows Media Format SDK.

1.  The application passes to the synchronous reader the name of a file to read. When the synchronous reader opens the file, it assigns an output number to each stream. If the file uses mutual exclusion, the reader assigns a single output for all of the mutually exclusive streams.
2.  The application gets information about the configuration of the various outputs from the reader. The information gathered will enable the application to properly render media samples.
3.  The application begins requesting samples, one at a time, from the synchronous reader. The synchronous reader delivers each sample in a buffer object for which it delivers the [**INSSBuffer**](/previous-versions/windows/desktop/api/wmsbuffer/nn-wmsbuffer-inssbuffer) interface.
4.  The application is responsible for rendering data after it is delivered by the reader. The Windows Media Format SDK does not provide any rendering routines. Typically, applications will use other SDKs to render data, such as the Microsoft Direct X SDK, or the multimedia functions of the Microsoft Windows Platform SDK.

These steps are illustrated in the WMSyncReader sample application. For more information, see [Sample Applications](sample-applications.md).

The synchronous reader also supports more advanced functionality. The synchronous reader enables you to do the following:

-   Specify a range of samples to retrieve by time or by frame number.
-   Control stream selection for mutually exclusive streams.
-   Open a file using the standard COM interface, **IStream**.
-   Read profile data from the file header.
-   Read metadata from the file header.
-   Switch between stream and output samples during playback.
-   Switch between compressed and uncompressed stream samples during playback.

The following sections describe the use of the synchronous reader object in detail.

-   [To Create a Synchronous Reader and Open a File](to-create-a-synchronous-reader-and-open-a-file.md)
-   [To Find Stream Numbers and Output Numbers](to-find-stream-numbers-and-output-numbers.md)
-   [To Retrieve Media Samples with the Synchronous Reader](to-retrieve-media-samples-with-the-synchronous-reader.md)
-   [To Seek By Time Using the Synchronous Reader](to-seek-by-time-using-the-synchronous-reader.md)
-   [To Seek By Frame Number Using the Synchronous Reader](to-seek-by-frame-number-using-the-synchronous-reader.md)
-   [To Seek By SMPTE Time Code Using the Synchronous Reader](to-seek-by-smpte-time-code-using-the-synchronous-reader.md)
-   [To Retrieve Stream Samples with the Synchronous Reader](to-retrieve-stream-samples-with-the-synchronous-reader.md)
-   [To Retrieve Compressed Samples with the Synchronous Reader](to-retrieve-compressed-samples-with-the-synchronous-reader.md)

**Example Code**

The following example code shows how to read samples from an ASF file using the synchronous reader. It specifies by frame number a range of samples to deliver.


```C++
IWMSyncReader* pSyncReader = NULL;
INSSBuffer*    pMyBuffer   = NULL;

QWORD cnsSampleTime = 0;
QWORD cnsSampleDuration = 0;
DWORD dwFlags = 0;
DWORD dwOutputNumber;
HRESULT hr = S_OK;

// Initialize COM.
hr = CoInitialize(NULL);

// Create a synchronous reader.
hr = WMCreateSyncReader(NULL, WMT_RIGHT_PLAYBACK, &pSyncReader);

// Open an ASF file.
hr = pSyncReader->Open(L"c:\\somefile.wmv");

// TODO: Identify the properties for each output. This works 
// exactly as it does with the asynchronous reader.

// Specify a playback range from frame number 100 of the video 
// stream to the end of the file. Assume that the video stream 
// is stream number 2.
hr = pSyncReader->SetRangeByFrame(2, 100, 0);

// Loop through all the samples in the specified range.
do
{
   // Get the next sample, regardless of its stream number.
   hr = pSyncReader->GetNextSample(0,
                                   &pMyBuffer,
                                   &cnsSampleTime,
                                   &cnsSampleDuration,
                                   &dwFlags,
                                   &dwOutputNumber,
                                   NULL);

   if(SUCCEEDED(hr))
   {
      // TODO: Process the sample in whatever way is appropriate 
      // to your application. When finished, clean up.
      pMyBuffer->Release();
      pMyBuffer = NULL;
      cnsSampleTime     = 0;
      cnsSampleDuration = 0;
      dwFlags           = 0;
      dwOutputNumber    = 0;
   }
} 
while (SUCCEEDED(hr));

pSyncReader->Release();
pSyncReader = NULL;

```



## Related topics

<dl> <dt>

[**IWMSyncReader Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmsyncreader)
</dt> <dt>

[**Reading ASF Files**](reading-asf-files.md)
</dt> <dt>

[**Synchronous Reader Object**](synchronous-reader-object.md)
</dt> </dl>

 

 




