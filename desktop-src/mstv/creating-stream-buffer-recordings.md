---
title: Creating Stream Buffer Recordings
description: Creating Stream Buffer Recordings
ms.assetid: 1aee15a3-5bc8-401b-9b37-b9351fd7c91f
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating Stream Buffer Recordings

This topic applies to Windows XP Service Pack 1 or later.

The Stream Buffer Sink filter writes data to temporary backing files. To create a permanent recording, call the [**IStreamBufferSink::CreateRecorder**](/previous-versions/windows/desktop/api/Sbe/nf-sbe-istreambuffersink-createrecorder) method on the Stream Buffer Sink filter. This method creates a new [Recording](recording-object.md) object, which the application uses to start and stop the recording.

The **CreateRecorder** method specifies the type of recording to make:

-   A *content* recording writes the data to a new permanent file.
-   A *reference* recording creates a stub file that refers to the existing backing files, which are made permanent. Create a reference recording if you want to save data that has already been captured.

To start the recording, call [**IStreamBufferRecordControl::Start**](/previous-versions/windows/desktop/api/Sbe/nf-sbe-istreambufferrecordcontrol-start). In a reference recording, you can set a start time in the past, as long as the backing files still contain that portion of the stream. To stop the recording and close the file, call [**IStreamBufferRecordControl::Stop**](/previous-versions/windows/desktop/api/Sbe/nf-sbe-istreambufferrecordcontrol-stop).

The following code shows how to create a reference recording:


```C++
CComPtr<IUnknown> pRecUnk;
hr = pSink->CreateRecorder(
    L"C:\\MyRecording.sbe", 
    RECORDING_TYPE_REFERENCE, 
    &amp;pRecUnk);
if (SUCCEEDED(hr))
{
        // Start the recording.
        CComQIPtr<IStreamBufferRecordControl> pRecControl(pRecUnk);
        REFERENCE_TIME rtStart = -50000000; // Start 5 seconds ago.
        pRecControl->Start(&amp;rtStart);
        
        // Later:
        pRecControl->Stop(0); // Stop the recording and close the file.
 }
```



To play the recording, create a source graph containing the Stream Buffer Source filter and call [**IFileSourceFilter::Load**](https://msdn.microsoft.com/library/windows/desktop/dd389983) to set the file name. (See [Creating Stream Buffer Graphs](creating-stream-buffer-graphs.md).)

**Content Recordings**

When a content recording begins, the Stream Buffer Sink filter stops writing to the backing files and starts writing to the recording file. The recording file is not destroyed when the application exits. The file length is limited only by disk storage space. When the recording ends, the Stream Buffer Sink filter starts writing data to the backing files again.

The sink filter can only make one content recording at a time.

**Reference Recordings**

A reference recording creates a stub file, which contains information about the recording but does not contain the captured data. The capture data remains in the backing files, and the stub file does not grow as more content is recorded.

A reference recording also creates data files that are hard links to the backing files. The data files are stored as hidden system files in the same directory as the stub file. The naming convention for these files is `stubfilename_#.SBE`. For example, if the stub file is named `MyFile.SBE`, the data files are named `MyFile_1.SBE`, `MyFile_2.SBE`, and so forth.

Each data file references an entire backing file, even if the backing file starts earlier than the start time for the recording, or stops later than the stop time. The stub file contains the start and stop times for the recording, so any additional data is skipped on playback.

> [!Note]  
> Because the data files are actually hard links to the backing files, any limitations associated with hard links apply to these files. For example, hard links must be on the same volume as the original file. Also, the backing files are not deleted when the main stub file is deleted; the application should delete them when they are no longer wanted.

 

Reference recordings should not be used for long-term storage of content. If you want to save content beyond the current session, you should use the [**IStreamBufferRecComp**](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambufferreccomp) interface to copy the reference recording into a content recording.

 

 




