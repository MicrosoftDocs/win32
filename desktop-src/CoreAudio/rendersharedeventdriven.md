---
description: This sample application uses the Core Audio APIs to render audio data to an output device, specified by the user.
ms.assetid: 92e644be-df8b-415d-ac8e-c0c30c85f844
title: RenderSharedEventDriven
ms.topic: article
ms.date: 05/31/2018
---

# RenderSharedEventDriven

This sample application uses the Core Audio APIs to render audio data to an output device, specified by the user. This sample demonstrates event-driven buffering for a rendering client in shared mode. For a shared-mode stream, the client shares the endpoint buffer with the audio engine.

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
-   WASAPI for stream management operations.

## Requirements



| Product                                                        | Version   |
|----------------------------------------------------------------|-----------|
| [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx) | Windows 7 |
| Visual Studio                                                  | 2008      |



 

## Downloading the Sample

This sample is available in the following locations.



| Location    | Path/URL                                                                                                 |
|-------------|----------------------------------------------------------------------------------------------------------|
| Windows SDK | \\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Multimedia\\Audio\\RenderSharedEventDriven\\... |



 

## Building the Sample

To build the RenderSharedEventDriven sample, use the following steps:

1.  Open the CMD shell for the Windows SDK and change to the RenderSharedEventDriven sample directory.
2.  Run the command `start WASAPIRenderSharedEventDriven.sln` in the RenderSharedEventDriven directory to open the WASAPIRenderSharedEventDriven project in the Visual Studio window.
3.  From within the window, select the **Debug** or **Release** solution configuration, select the **Build** menu from the menu bar, and select the **Build** option. If you do not open Visual Studio from the CMD shell for the SDK, Visual Studio will not have access to the SDK build environment. In that case, the sample will not build unless you explicitly set environment variable MSSdk, which is used in the project file, WASAPIRenderSharedEventDriven.vcproj.

## Running the Sample

If you build the demo application successfully, an executable file, WASAPIRenderSharedEventDriven.exe, is generated. To run it, type `WASAPIRenderSharedEventDriven` in a command window followed by required or optional arguments. The following example shows how to run the sample by specifying playback duration on the default multimedia device.

`WASAPIRenderSharedEventDriven.exe -d 20 -multimedia`

The following table shows the arguments.

| Argument        | Description                                                |
|-----------------|------------------------------------------------------------|
| -?              | Shows help.                                                |
| -h              | Shows help.                                                |
| -f              | Sine wave frequency in Hz.                                 |
| -l              | Audio render latency in milliseconds.                      |
| -d              | Sine wave duration in seconds.                             |
| -m              | Disables the use of MMCSS.                                 |
| -console        | Use the default console device.                            |
| -communications | Use the default communication device.                      |
| -multimedia     | Use the default multimedia device.                         |
| -endpoint       | Use the endpoint identifier specified in the switch value. |



 

If the application is run without arguments, it enumerates the available devices and prompts the user to select a device for the rendering session. After the user specifies a device, the application renders a sine wave at 440 Hz for 10 seconds. These values can be modified by specifying -f and -d switch values.

RenderSharedEventDriven demonstrates event-driven buffering. The sample shows how to:

-   Instantiate an audio client, configure it to run in exclusive mode, and enable event-driven buffering by setting the **AUDCLNT\_STREAMFLAGS\_EVENTCALLBACK** flag in the call to [**IAudioClient::Initialize**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-initialize).
-   Associate the client with the samples that are ready to be rendered by providing an event handle to the system by calling the [**IAudioClient::SetEventHandle**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-seteventhandle) method.
-   Create a render thread to proces samples from the audio engine.
-   Check the mix format of the device endpoint to determine whether the samples can be rendered. If the device does not support the mix format, the data is converted to PCM.
-   Handle stream switching.

After the rendering session begins and the stream starts, the audio engine signals the supplied event handle to notify the client each time a buffer becomes ready for the client to process. The audio data can also be processed in a timer-driven loop. This mode is demonstrated in the [RenderSharedTimerDriven](rendersharedtimerdriven.md) sample.

For more information about rendering a stream, see [Rendering a Stream](rendering-a-stream.md).

## Related topics

<dl> <dt>

[SDK Samples That Use the Core Audio APIs](sdk-samples-that-use-the-core-audio-apis.md)
</dt> </dl>

 

 



