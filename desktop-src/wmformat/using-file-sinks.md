---
title: Using File Sinks
description: Using File Sinks
ms.assetid: 0cc4320a-c975-452d-bd1c-394d43bd4585
keywords:
- Advanced Systems Format (ASF),file sinks
- ASF (Advanced Systems Format),file sinks
- Advanced Systems Format (ASF),sinks
- ASF (Advanced Systems Format),sinks
- sinks,file sinks
- file sinks,about
- file sinks,creating
- file sinks,stopping
- file sinks,starting
- file sinks,closing
- sinks,statistics
ms.topic: article
ms.date: 05/31/2018
---

# Using File Sinks

Under normal circumstances, you can simply pass the writer an output file name using the [**IWMWriter::SetOutputFilename**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-setoutputfilename) method, and the writer object will write the file to disk automatically. In this case, the writer is actually creating and controlling a writer file sink object that handles writing the file to disk. A writer file sink object controls the flow of data from the writer object to a single file.

You can create your own file sinks to get more control over how the sink writes the file. You can also access the default writer file sink created by the writer in response to a call to **SetOutputFilename**.

## Creating File Sinks

To create a file sink and add it to the writer, perform the following steps.

1.  Create a new sink by calling the [**WMCreateWriterFileSink**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatewriterfilesink) function.
2.  Supply a file name for the sink by calling [**IWMWriterFileSink::Open**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriterfilesink-open).
3.  Add the file sink to the writer by calling [**IWMWriterAdvanced::AddSink**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced-addsink).
4.  Perform writing in the usual way.
5.  After writing is completed, the sink will close the file automatically.

## Stopping and Starting File Sinks

After writing operations begin, you can stop writing to a file sink by calling [**IWMWriterFileSink2::Stop**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriterfilesink2-stop).

There are many potential reasons why you would want to stop writing to a sink. For example, if you are recording from a live source, you may only be interested in some of the content.

You can resume writing to a file sink by calling [**IWMWriterFileSink2::Start**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriterfilesink2-start). Both **Stop** and **Start** use presentation times to control approximately when the command is executed. You can use the [**IWMWriterFileSink3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriterfilesink3) methods to gain more control over start and stop times.

## Closing File Sinks

Normally, a file sink is closed automatically. If you are finished writing to a sink, but writing operations to other sinks are continuing, you should explicitly close the sink to conserve resources. To close a file sink, call [**IWMWriterFileSink2::Close**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriterfilesink2-close).

## Getting Sink Statistics

You can get the file size and duration for an open sink by calling [**IWMWriterFileSink2::GetFileSize**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriterfilesink2-getfilesize) and [**IWMWriterFileSink2::GetFileDuration**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriterfilesink2-getfileduration) respectively.

## Related topics

<dl> <dt>

[**IWMWriterFileSink Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriterfilesink)
</dt> <dt>

[**IWMWriterFileSink2 Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriterfilesink2)
</dt> <dt>

[**IWMWriterFileSink3 Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriterfilesink3)
</dt> <dt>

[**Writer File Sink Object**](writer-file-sink-object.md)
</dt> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




