---
title: Video Resizing
description: Video Resizing
ms.assetid: 38ecb729-68eb-4452-8389-cabe987fb8b6
keywords:
- Windows Media Format SDK,video resizing
- Windows Media Format SDK,resizing video
- Advanced Systems Format (ASF),video resizing
- ASF (Advanced Systems Format),video resizing
- Advanced Systems Format (ASF),resizing video
- ASF (Advanced Systems Format),resizing video
- video resizing
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Video Resizing

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When you define the settings for a video stream, you must specify a width and height for the video frames. This video size determines the size of the video frames encoded in the data section of the file. However, the video size in a profile does not determine, or limit, the size of the input media that you deliver to the writer, or the size of the output media you receive from the reader. The writer can resize the video frames to suit the needs of your application.

Video image size can be thought of as going through three stages: input video size, stream video size, and output video size.

Input video size is the size of the frames that you pass as samples to the writer object. You define this size as one of the required video input properties. For more information about input properties, see [To Enumerate Input Formats](to-enumerate-input-formats.md).

Stream video size is the size of the frames in the data section of the ASF file. You define this size as one of the required stream configuration settings in the profile. If you are writing a file and the input video size is different from the stream video size, the writer resizes the frames while encoding. For more information about video stream properties, see [Configuring Video Streams](configuring-video-streams.md).

Output video size is the size of the frames delivered by the reader or synchronous reader. You define this size as one of the required video output properties. If you are reading a file and the output video size is different from the stream video size, the reader resizes the frames while decoding.

You cannot set a stream video size to an odd number of pixels wide. If you set the width of a video stream to an odd value, either the profile will not be accepted by the writer, or the resulting video will be encoded with a black line down one side to make up the difference.

You should take care when resizing video. Images tend to look their best at their original resolution. Resizing images can often cause distortion and make text illegible. If you are compressing video to a low bit rate, you will also find that resizing distortions can lead to severe compression artifacts.

The Windows Media Video 9 Screen codec does not support resizing.

## Related topics

<dl> <dt>

[**File Writing Features**](file-writing-features.md)
</dt> <dt>

[**Working with Inputs**](working-with-inputs.md)
</dt> <dt>

[**Working with Outputs**](working-with-outputs.md)
</dt> </dl>

 

 




