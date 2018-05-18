---
title: Positioning in Streams
description: Positioning in Streams
ms.assetid: '97ab491d-1a58-4b4b-a13a-215be24dac1c'
keywords: ["AVIStreamStart function", "AVIStreamFindSample function", "AVIStreamSampleToTime function"]
---

# Positioning in Streams

AVIFile provides several ways to locate and move to a position in a data stream. The functions and macros in this section let your application find the starting position, length, and key frames (containing a complete image in the sample) within a stream. The functions and macros also associate time with positions in a stream by calculating the elapsed time needed to play a stream from its beginning to any point in a stream.

## Finding the Starting Position

You can retrieve the sample number of the first frame in a video stream by using the [**AVIStreamStart**](avistreamstart.md) function. (The frames of a movie might start at sample 0 or 1, depending on the preference of the author.) You can also obtain this information by using the [**AVIStreamInfo**](avistreaminfo.md) function. This function stores the sample number in the **dwStart** member of the [**AVISTREAMINFO**](avistreaminfo-struct.md) structure. You can retrieve the starting time of a stream's first sample by using the [**AVIStreamStartTime**](avistreamstarttime.md) macro.

You can retrieve the stream length by using the [**AVIStreamLength**](avistreamlength.md) function. This function returns the number of samples in the stream. You can also obtain this information by using the **AVIStreamInfo** function. This function stores the stream length in the **dwLength** member of the **AVISTREAMINFO** structure. To retrieve the length of a stream in milliseconds, use the [**AVIStreamLengthTime**](avistreamlengthtime.md) macro.

In a video stream, each sample generally corresponds to a frame of video. There might, however, be samples for which no video data is present. If you call the [**AVIStreamRead**](avistreamread.md) function specifying one of those positions, it returns a data length of 0 bytes. You can find samples that contain data by using the [**AVIStreamFindSample**](avistreamfindsample.md) function and specifying the FIND\_ANY flag.

In an audio stream, each sample corresponds to one data block of audio data. For example, if the audio data has a 22 kHz ADPCM (Adaptive Differential Pulse Code Modulation) format, each sample for **AVIStreamLength** corresponds to a block of 256 bytes of compressed audio data. This block of audio data contains approximately 500 audio samples when uncompressed. The functions and macros of AVIFile, however, treat each 256-byte block as a single sample.

> [!Note]  
> Valid positions within a stream range from the beginning to the end of the stream, which is the sum of the stream starting point and its length. The position represented by the sum of the starting position and the length corresponds to a time after the last data has been rendered; it does not contain any data. You can retrieve the sample number that represents the end of the stream by using the [**AVIStreamEnd**](avistreamend.md) macro. You can retrieve the time value in milliseconds that represents the end of the stream by using the [**AVIStreamEndTime**](avistreamendtime.md) macro.

 

## Finding Sample and Key Frames

You can search for different types of samples in a stream by using the [**AVIStreamFindSample**](avistreamfindsample.md) function. This function searches backward or forward through a stream for a sample of the appropriate type, beginning with the sample number you specify. You can search for different types of samples in a stream by specifying a flag in the **AVIStreamFindSample** calling sequence. Specify the FIND\_ANY flag to locate nonempty samples or to skip samples that lack data. Specify the FIND\_KEY flag to search for key frames that contain the data to render a complete image without needing to reference previous frames. Specify the FIND\_FORMAT flag to search for changes to the format. **AVIStreamFindSample** is used mainly with video streams.

Several macros that use AVIFile functions supplement the stream search features. The following list provides a brief description of each macro. The macros that search for a specific position or type of data require a starting location to be specified in the stream.



| Macro                                                                | Description                                                                                                                 |
|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| [**AVIStreamIsKeyFrame**](avistreamiskeyframe.md)                   | Indicates whether a sample in a specified stream is a key frame.                                                            |
| [**AVIStreamNearestKeyFrame**](avistreamnearestkeyframe.md)         | Locates the key frame at or preceding a specified position in a stream.                                                     |
| [**AVIStreamNearestKeyFrameTime**](avistreamnearestkeyframetime.md) | Determines the time corresponding to the beginning of the key frame nearest (at or preceding) a specified time in a stream. |
| [**AVIStreamNearestSample**](avistreamnearestsample.md)             | Locates the nearest nonempty sample at or preceding a specified position in a stream.                                       |
| [**AVIStreamNearestSampleTime**](avistreamnearestsampletime.md)     | Determines the time corresponding to the beginning of a sample that is nearest to a specified time in a stream.             |
| [**AVIStreamNextKeyFrame**](avistreamnextkeyframe.md)               | Locates the next key frame following a specified position in a stream.                                                      |
| [**AVIStreamNextKeyFrameTime**](avistreamnextkeyframetime.md)       | Returns the time of the next key frame in a stream, starting at a given time.                                               |
| [**AVIStreamNextSample**](avistreamnextsample.md)                   | Locates the next nonempty sample from a specified position in a stream.                                                     |
| [**AVIStreamNextSampleTime**](avistreamnextsampletime.md)           | Returns the time that a sample changes to the next sample in the stream.                                                    |
| [**AVIStreamPrevKeyFrame**](avistreamprevkeyframe.md)               | Locates the key frame that precedes a specified position in a stream.                                                       |
| [**AVIStreamPrevKeyFrameTime**](avistreamprevkeyframetime.md)       | Returns the time of the previous key frame in the stream, starting at a given time.                                         |
| [**AVIStreamPrevSample**](avistreamprevsample.md)                   | Locates the nonempty sample that precedes a specified position in a stream.                                                 |
| [**AVIStreamPrevSampleTime**](avistreamprevsampletime.md)           | Determines the time at which the previous sample replaces its predecessor in the stream.                                    |
| [**AVIStreamSampleToSample**](avistreamsampletosample.md)           | Returns the sample in a stream that occurs at the same time as a sample that occurs in a second stream.                     |



 

## Switching Between Samples and Time

You can determine the elapsed time from the beginning of a stream to a sample using the [**AVIStreamSampleToTime**](avistreamsampletotime.md) function. This function converts the sample number to a time value expressed in milliseconds. For a video frame (which spans several milliseconds), this value represents the time the sample begins to play since playback began and assumes the video clip plays at normal speed. For an audio sample (which has several samples in a millisecond), the time value corresponds to the time at which the sample begins to play and assumes the audio stream plays at normal speed.

Conversely, you can find the sample number associated with a time value by using the [**AVIStreamTimeToSample**](avistreamtimetosample.md) function. This function converts the millisecond value to a sample number and assumes the video clip plays at normal speed.

Because **AVIStreamSampleToTime** returns the time at which a frame begins to play, the relationship between **AVIStreamSampleToTime** and **AVIStreamTimeToSample** is not truly inverse. They determine the position in a file more acurately than they determine time. For example, two consecutive audio samples might both play in the same millisecond. Using **AVIStreamSampleToTime** to convert the sample numbers would result in identical time values. If you convert the time value back to a sample number by using **AVIStreamTimeToSample**, a single sample would be referenced.

 

 




