---
title: Writing Streams to a File
description: Writing Streams to a File
ms.assetid: 'a3766f8c-aaa6-4fc5-a306-54aee71018f1'
keywords: ["AVIFileCreateStream function"]
---

# Writing Streams to a File

You can also create a file containing data streams by writing a new data stream to a file.

You can create a new stream in a new or existing file by using the [**AVIFileCreateStream**](avifilecreatestream.md) function. This function defines a new stream according to the characteristics described in an [**AVISTREAMINFO**](avistreaminfo-struct.md) structure, creates a stream interface for the new stream, increments the reference count of the stream, and returns the address of the stream-interface pointer.

Before you write the content of the stream, you must specify the stream format. You can set the stream format by using the [**AVIStreamSetFormat**](avistreamsetformat.md) function. When setting the format of a video stream, you must supply this function with a [**BITMAPINFO**](https://msdn.microsoft.com/library/windows/desktop/dd183375) structure containing the appropriate information. When setting the format of an audio stream, you must supply a [**WAVEFORMAT**](waveformat.md) or [**WAVEFORMATEX**](waveformatex.md) structure containing the appropriate information. The information you need to supply to the function for other stream types depends on the stream type and the stream handler.

You can write the multimedia content in a stream by using the [**AVIStreamWrite**](avistreamwrite.md) function. This function copies raw data from an application-supplied buffer into the specified stream. The default AVI file handler appends information to the end of a stream. The default WAVE handler can write waveform-audio data within a stream as well as at the end of a stream.

You can write supplementary information about the file or stream that is not included in the [**AVIFileCreateStream**](avifilecreatestream.md) or [**AVIStreamSetFormat**](avistreamsetformat.md) function by using the [**AVIFileWriteData**](avifilewritedata.md) and [**AVIStreamWriteData**](avistreamwritedata.md) functions. You can record data that is applicable to the entire file, such as copyright information and modification history, by using **AVIFileWriteData**. You can record stream-specific information, such as compression and decompression settings, by using **AVIStreamWriteData**. The supplementary information is stored in separate chunks within the file.

You can close the stream after you finish writing to the new stream by using the [**AVIStreamRelease**](avistreamrelease.md) function. This function clears buffers used in recording the stream data, and it completes and closes any incomplete data chunks in the file.

## Related topics

<dl> <dt>

[Stream Operations](stream-operations.md)
</dt> </dl>

 

 




