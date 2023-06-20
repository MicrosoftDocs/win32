---
title: Positioning in Streams
description: Positioning in Streams
ms.assetid: 97ab491d-1a58-4b4b-a13a-215be24dac1c
keywords:
- AVIStreamStart function
- AVIStreamFindSample function
- AVIStreamSampleToTime function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Positioning in Streams

\[The feature associated with this page, [AVIFile Functions and Macros](/windows/win32/multimedia/avifile-functions-and-macros), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader). **Source Reader** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** instead of **AVIFile Functions and Macros**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

AVIFile provides several ways to locate and move to a position in a data stream. The functions and macros in this section let your application find the starting position, length, and key frames (containing a complete image in the sample) within a stream. The functions and macros also associate time with positions in a stream by calculating the elapsed time needed to play a stream from its beginning to any point in a stream.

## Finding the Starting Position

You can retrieve the sample number of the first frame in a video stream by using the [**AVIStreamStart**](/windows/desktop/api/Vfw/nf-vfw-avistreamstart) function. (The frames of a movie might start at sample 0 or 1, depending on the preference of the author.) You can also obtain this information by using the [**AVIStreamInfo**](/windows/desktop/api/Vfw/nf-vfw-avistreaminfoa) function. This function stores the sample number in the **dwStart** member of the [**AVISTREAMINFO**](/windows/desktop/api/Vfw/ns-vfw-avistreaminfoa) structure. You can retrieve the starting time of a stream's first sample by using the [**AVIStreamStartTime**](/windows/desktop/api/Vfw/nf-vfw-avistreamstarttime) macro.

You can retrieve the stream length by using the [**AVIStreamLength**](/windows/desktop/api/Vfw/nf-vfw-avistreamlength) function. This function returns the number of samples in the stream. You can also obtain this information by using the **AVIStreamInfo** function. This function stores the stream length in the **dwLength** member of the **AVISTREAMINFO** structure. To retrieve the length of a stream in milliseconds, use the [**AVIStreamLengthTime**](/windows/desktop/api/Vfw/nf-vfw-avistreamlengthtime) macro.

In a video stream, each sample generally corresponds to a frame of video. There might, however, be samples for which no video data is present. If you call the [**AVIStreamRead**](/windows/desktop/api/Vfw/nf-vfw-avistreamread) function specifying one of those positions, it returns a data length of 0 bytes. You can find samples that contain data by using the [**AVIStreamFindSample**](/windows/desktop/api/Vfw/nf-vfw-avistreamfindsample) function and specifying the FIND\_ANY flag.

In an audio stream, each sample corresponds to one data block of audio data. For example, if the audio data has a 22 kHz ADPCM (Adaptive Differential Pulse Code Modulation) format, each sample for **AVIStreamLength** corresponds to a block of 256 bytes of compressed audio data. This block of audio data contains approximately 500 audio samples when uncompressed. The functions and macros of AVIFile, however, treat each 256-byte block as a single sample.

> [!Note]  
> Valid positions within a stream range from the beginning to the end of the stream, which is the sum of the stream starting point and its length. The position represented by the sum of the starting position and the length corresponds to a time after the last data has been rendered; it does not contain any data. You can retrieve the sample number that represents the end of the stream by using the [**AVIStreamEnd**](/windows/desktop/api/Vfw/nf-vfw-avistreamend) macro. You can retrieve the time value in milliseconds that represents the end of the stream by using the [**AVIStreamEndTime**](/windows/desktop/api/Vfw/nf-vfw-avistreamendtime) macro.

 

## Finding Sample and Key Frames

You can search for different types of samples in a stream by using the [**AVIStreamFindSample**](/windows/desktop/api/Vfw/nf-vfw-avistreamfindsample) function. This function searches backward or forward through a stream for a sample of the appropriate type, beginning with the sample number you specify. You can search for different types of samples in a stream by specifying a flag in the **AVIStreamFindSample** calling sequence. Specify the FIND\_ANY flag to locate nonempty samples or to skip samples that lack data. Specify the FIND\_KEY flag to search for key frames that contain the data to render a complete image without needing to reference previous frames. Specify the FIND\_FORMAT flag to search for changes to the format. **AVIStreamFindSample** is used mainly with video streams.

Several macros that use AVIFile functions supplement the stream search features. The following list provides a brief description of each macro. The macros that search for a specific position or type of data require a starting location to be specified in the stream.



| Macro                                                                | Description                                                                                                                 |
|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| [**AVIStreamIsKeyFrame**](/windows/desktop/api/Vfw/nf-vfw-avistreamiskeyframe)                   | Indicates whether a sample in a specified stream is a key frame.                                                            |
| [**AVIStreamNearestKeyFrame**](/windows/desktop/api/Vfw/nf-vfw-avistreamnearestkeyframe)         | Locates the key frame at or preceding a specified position in a stream.                                                     |
| [**AVIStreamNearestKeyFrameTime**](/windows/desktop/api/Vfw/nf-vfw-avistreamnearestkeyframetime) | Determines the time corresponding to the beginning of the key frame nearest (at or preceding) a specified time in a stream. |
| [**AVIStreamNearestSample**](/windows/desktop/api/Vfw/nf-vfw-avistreamnearestsample)             | Locates the nearest nonempty sample at or preceding a specified position in a stream.                                       |
| [**AVIStreamNearestSampleTime**](/windows/desktop/api/Vfw/nf-vfw-avistreamnearestsampletime)     | Determines the time corresponding to the beginning of a sample that is nearest to a specified time in a stream.             |
| [**AVIStreamNextKeyFrame**](/windows/desktop/api/Vfw/nf-vfw-avistreamnextkeyframe)               | Locates the next key frame following a specified position in a stream.                                                      |
| [**AVIStreamNextKeyFrameTime**](/windows/desktop/api/Vfw/nf-vfw-avistreamnextkeyframetime)       | Returns the time of the next key frame in a stream, starting at a given time.                                               |
| [**AVIStreamNextSample**](/windows/desktop/api/Vfw/nf-vfw-avistreamnextsample)                   | Locates the next nonempty sample from a specified position in a stream.                                                     |
| [**AVIStreamNextSampleTime**](/windows/desktop/api/Vfw/nf-vfw-avistreamnextsampletime)           | Returns the time that a sample changes to the next sample in the stream.                                                    |
| [**AVIStreamPrevKeyFrame**](/windows/desktop/api/Vfw/nf-vfw-avistreamprevkeyframe)               | Locates the key frame that precedes a specified position in a stream.                                                       |
| [**AVIStreamPrevKeyFrameTime**](/windows/desktop/api/Vfw/nf-vfw-avistreamprevkeyframetime)       | Returns the time of the previous key frame in the stream, starting at a given time.                                         |
| [**AVIStreamPrevSample**](/windows/desktop/api/Vfw/nf-vfw-avistreamprevsample)                   | Locates the nonempty sample that precedes a specified position in a stream.                                                 |
| [**AVIStreamPrevSampleTime**](/windows/desktop/api/Vfw/nf-vfw-avistreamprevsampletime)           | Determines the time at which the previous sample replaces its predecessor in the stream.                                    |
| [**AVIStreamSampleToSample**](/windows/desktop/api/Vfw/nf-vfw-avistreamsampletosample)           | Returns the sample in a stream that occurs at the same time as a sample that occurs in a second stream.                     |



 

## Switching Between Samples and Time

You can determine the elapsed time from the beginning of a stream to a sample using the [**AVIStreamSampleToTime**](/windows/desktop/api/Vfw/nf-vfw-avistreamsampletotime) function. This function converts the sample number to a time value expressed in milliseconds. For a video frame (which spans several milliseconds), this value represents the time the sample begins to play since playback began and assumes the video clip plays at normal speed. For an audio sample (which has several samples in a millisecond), the time value corresponds to the time at which the sample begins to play and assumes the audio stream plays at normal speed.

Conversely, you can find the sample number associated with a time value by using the [**AVIStreamTimeToSample**](/windows/desktop/api/Vfw/nf-vfw-avistreamtimetosample) function. This function converts the millisecond value to a sample number and assumes the video clip plays at normal speed.

Because **AVIStreamSampleToTime** returns the time at which a frame begins to play, the relationship between **AVIStreamSampleToTime** and **AVIStreamTimeToSample** is not truly inverse. They determine the position in a file more acurately than they determine time. For example, two consecutive audio samples might both play in the same millisecond. Using **AVIStreamSampleToTime** to convert the sample numbers would result in identical time values. If you convert the time value back to a sample number by using **AVIStreamTimeToSample**, a single sample would be referenced.

 

 




