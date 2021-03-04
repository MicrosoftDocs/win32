---
description: This section describes sample applications that demonstrate how to use Media Foundation.Encoding SamplesPlayback SamplesPlug-InsSource Reader SamplesVideo CaptureMiscellaneous SamplesDeprecated or Obsolete SamplesRelated topics
ms.assetid: 9d460107-ec12-4df5-a7a9-d19943685599
title: Media Foundation SDK Samples
ms.topic: article
ms.date: 05/31/2018
---

# Media Foundation SDK Samples

This section describes sample applications that demonstrate how to use Media Foundation.

-   [Encoding Samples](#encoding-samples)
-   [Playback Samples](#playback-samples)
-   [Plug-Ins](#plug-ins)
-   [Source Reader Samples](#source-reader-samples)
-   [Video Capture](#video-capture)
-   [Miscellaneous Samples](#miscellaneous-samples)
-   [Deprecated or Obsolete Samples](#deprecated-or-obsolete-samples)
-   [Related topics](#related-topics)

## Encoding Samples



| Sample                            | Description                                                 |
|-----------------------------------|-------------------------------------------------------------|
| [Transcode](transcode-sample.md) | Shows how to reencode a media file to Windows Media format. |



 

## Playback Samples



| Sample                                            | Description                                                                                                                                                                                                     |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [BasicPlayback](/previous-versions//bb970475(v=vs.85))          | Plays audio and video files by using the [Media Session](media-session.md). This sample demonstrates how to create playback topologies, control the Media Session, and receive session events during playback. |
| [MFPlayer](/previous-versions//bb970516(v=vs.85))                    | Demonstrates some playback functions that are not included in the [BasicPlayback](/previous-versions//bb970475(v=vs.85)) sample.                                                                                              |
| [ProtectedPlayback](protectedplayback-sample.md) | Plays protected audio and video files. This sample shows how to use the protected media path (PMP) session and how to use content enabler objects.                                                              |



 

## Plug-Ins



| Sample                                       | Sub-Area                         | Description                                                                                            |
|----------------------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------|
| [Decoder](decoder-sample.md)                | Media Foundation transform (MFT) | Video decoder.                                                                                         |
| [EVRPresenter](evrpresenter-sample.md)      | Miscellaneous                    | Custom presenter for the [Enhanced Video Renderer](enhanced-video-renderer.md) (EVR).                 |
| [MFT\_AudioDelay](mft-audiodelay-sample.md) | MFT                              | Audio effect transform. Shows how to write a basic MFT for audio processing.                           |
| [MFT\_Grayscale](mft-grayscale-sample.md)   | MFT                              | Grayscale video effect. Shows how to write a basic MFT for video processing.                           |
| [MPEG1Source](mpeg1source-sample.md)        | Media source                     | Parses MPEG-1 systems-layer streams. Shows how to write a custom media source and byte-stream handler. |
| [WavSink](wavsink-sample.md)                | Media sink                       | An archive sink that writes .wav files. Shows how to write a custom media sink.                        |
| [WavSource](wavsource-sample.md)            | Media source                     | Parses .wav files. Shows how to write a custom media source and byte-stream handler.                   |



 

## Source Reader Samples



| Sample                                      | Description                                                                         |
|---------------------------------------------|-------------------------------------------------------------------------------------|
| [Audio Clip](audio-clip-sample.md)         | Uses the [Source Reader](source-reader.md) to decode audio from a media file.      |
| [VideoThumbnail](videothumbnail-sample.md) | Uses the [Source Reader](source-reader.md) to get single frames from a video file. |



 

## Video Capture



| Sample                                        | Description                                                                                 |
|-----------------------------------------------|---------------------------------------------------------------------------------------------|
| [MFCaptureD3D](mfcaptured3d-sample.md)       | Shows how to preview video from a video capture device, using Direct3D to render the video. |
| [MFCaptureToFile](mfcapturetofile-sample.md) | Shows how to capture video from a video camera to a file.                                   |



 

## Miscellaneous Samples



| Sample                                         | Description                                                                                                                                           |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ASFParser](asfparser-sample.md)              | Shows how to parse data from an Advanced Systems Format (ASF) file.                                                                                   |
| [DXVA-HD](dxva-hd-sample.md)                  | Shows how to use Microsoft DirectX Video Acceleration High Definition (DXVA-HD).                                                                      |
| [DXVA2\_VideoProc](dxva2-videoproc-sample.md) | Uses DirectX Video Acceleration (DXVA) 2.0 to create a stream of 4:2:2 YUV video. This sample shows how to use the video processing features of DXVA. |



 

## Deprecated or Obsolete Samples



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Sample</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="mfplayer2-sample.md">MFPlayer2</a></td>
<td>Demonstrates some advanced playback features of the <a href="using-mfplay-for-audio-video-playback.md">MFPlay</a> API.</td>
</tr>
<tr class="even">
<td><a href="/previous-versions//bb970336(v=vs.85)">PlaybackFX</a></td>
<td>Applies a grayscale effect to video. Shows how to insert MFTs into a playback topology.<br/>
<blockquote>
[!Note]<br />
This sample is no longer included in the SDK.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><a href="playlist-sample.md">Playlist</a></td>
<td>Plays a sequence of audio files using the sequencer source.<br/>
<blockquote>
[!Note]<br />
This sample is no longer included in the SDK.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><a href="simplecapture-sample.md">SimpleCapture</a></td>
<td>Shows how to preview video from a video capture device, using the MFPlay API.</td>
</tr>
<tr class="odd">
<td><a href="simpleplay-sample.md">SimplePlay</a></td>
<td>Shows how to play a media file using the MFPlay API.</td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Microsoft Media Foundation](microsoft-media-foundation-sdk.md)
</dt> <dt>

[About Media Foundation](about-the-media-foundation-sdk.md)
</dt> </dl>

 

 
