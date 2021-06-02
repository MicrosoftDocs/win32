---
description: This sample application demonstrates opening and closing communication streams and causing ducking events that an application can get to implement stream attenuation.
ms.assetid: 9a2131b2-ec4a-492a-a277-bd26ec8d67e5
title: DuckingCaptureSample
ms.topic: article
ms.date: 05/31/2018
---

# DuckingCaptureSample

This sample application demonstrates opening and closing communication streams and causing ducking events that an application can get to implement stream attenuation. This application implements a chat client that uses Core Audio APIs to read audio data from a communication device and to play it on the output device.

This topic contains the following sections.

-   [Description](#description)
-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [Running the Sample](#running-the-sample)
-   [Related topics](#related-topics)

## Description

This sample demonstrates the following features.

-   [MMDevice API](mmdevice-api.md) for multimedia device enumeration and selection.
-   [WASAPI](wasapi.md) for accessing the communications capture and render device, stream management operations, and handling ducking events.
-   [WAVE APIs](/previous-versions//ms713499(v=vs.85)) for accessing the communications device and capturing audio input.

## Requirements



| Product                                                        | Version   |
|----------------------------------------------------------------|-----------|
| [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx) | Windows 7 |
| Visual Studio 2008                                             |           |



 

## Downloading the Sample

This sample is available in the following locations.



| Location    | Path/URL                                                                                              |
|-------------|-------------------------------------------------------------------------------------------------------|
| Windows SDK | \\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Multimedia\\Audio\\DuckingCaptureSample\\... |



 

## Building the Sample

To build the DuckingCaptureSample sample, use the following steps:

1.  Open the DuckingCaptureSample.sln in Visual Studio 2008.
2.  From within the window, select the **Debug** or **Release** solution configuration, select the **Build** menu from the menu bar, and select the **Build** option. If you do not open Visual Studio from the CMD shell for the SDK, Visual Studio will not have access to the SDK build environment. In that case, the sample will not build unless you explicitly set environment variable MSSdk, which is used in the project file, DuckingCaptureSample.vcproj.

## Running the Sample

If you build the application successfully, an executable file, DuckingCaptureSample.exe, is generated. To run it, select **Start Debugging** or **Start Without Debugging** from the **Debug** menu or type `DuckingCaptureSample` in a command window.

DuckingCaptureSample provides the user with two implementations to capture audio from the default console device: WASAPI and Wave APIs. To start a capture session, select a mode and click **Start** on the application's user interface. To end the session, click **Stop**. Depending on the device specified by the user (input or output), the application uses MMDevice API to get a reference to the default rendering or capture communication device. After the user starts a chat session, the application performs the following tasks:

-   Creates and initializes an audio client in event-driven mode.
-   Associates the client with the event handle that signals that samples are ready for capture or rendering.
-   Sets up a capture client and a rendering client for the transport.
-   Creates the chat thread and starts the audio engine.

For capturing audio data, with each processing pass, the sample uses the capture client to get the total amount of captured data that is available in the buffer, read data from the default input device, and release the packet and make the buffer available for reading the next set of captured data.

For rendering, the application determines the amount of data that is queued up to play in the capture endpoint buffer. It accordingly writes to the buffer and releases the buffer in preparation for the next processing pass until all of the data has been written. For rendering, silent frames are prerolled to prevent the audio engine from glitching on startup. DuckingCaptureSample also shows how to hide the render stream from the volume mixer.

For more information about the stream attenuation feature, see [Using a Communication Device](using-the-communication-device.md).

## Related topics

<dl> <dt>

[SDK Samples That Use the Core Audio APIs](sdk-samples-that-use-the-core-audio-apis.md)
</dt> </dl>

 

 
