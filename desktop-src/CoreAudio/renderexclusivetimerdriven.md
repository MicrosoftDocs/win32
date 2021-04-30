---
description: This sample application uses the Core Audio APIs to render audio data to an output device specified by the user. This sample demonstrates timer-driven buffering for a rendering client in exclusive mode.
ms.assetid: 9dcfccd2-a709-4b4e-bbb3-4c68a15cce03
title: RenderExclusiveTimerDriven
ms.topic: article
ms.date: 05/31/2018
---

# RenderExclusiveTimerDriven

This sample application uses the Core Audio APIs to render audio data to an output device specified by the user. This sample demonstrates timer-driven buffering for a rendering client in exclusive mode. For an exclusive-mode stream, the client shares the endpoint buffer with the audio device.

This topic contains the following sections.

-   [Description](#description)
-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [View the Sample Files](#view-the-sample-files)
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



| Location    | Path/URL                                                                                                    |
|-------------|-------------------------------------------------------------------------------------------------------------|
| Windows SDK | \\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Multimedia\\Audio\\RenderExclusiveTimerDriven\\... |



 

## Building the Sample

To build the RenderExclusiveTimerDriven sample, use the following steps:

1.  Open the CMD shell for the Windows SDK and change to the RenderExclusiveTimerDriven sample directory.
2.  Run the command `start WASAPIRenderExclusiveTimerDriven.sln` in the RenderExclusiveTimerDriven directory to open the WASAPIRenderExclusiveTimerDriven project in the Visual Studio window.
3.  From within the window, select the **Debug** or **Release** solution configuration, select the **Build** menu from the menu bar, and select the **Build** option. If you do not open Visual Studio from the CMD shell for the SDK, Visual Studio will not have access to the SDK build environment. In that case, the sample will not build unless you explicitly set environment variable MSSdk, which is used in the project file, WASAPIRenderExclusiveTimerDriven.vcproj.

## View the Sample Files

If you build the demo application successfully, an executable file, WASAPIRenderExclusiveTimerDriven.exe, is generated. To run it, type `WASAPIRenderExclusiveTimerDriven` in a command window followed by required or optional arguments. The following example shows how to run the sample by a specifying playback duration on the default console device.

`WASAPIRenderExclusiveTimerDriven.exe -d 20 -console`

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

RenderExclusiveTimerDriven demonstrates timer-driven buffering. In this mode, the client must wait for a period of time (half the latency, specified by the -d switch value, in milliseconds). When the client wakes up, half way through the processing period, it pulls the next set of samples from the engine. Before each processing pass in the buffering loop, the client must find out the amount of data to render so that the data does not overrun the buffer.

Audio data to be played on the specified device can be processed by enabling event-driven buffering. This mode is demonstrated in the RenderExclusiveTimerDriven sample.

For more information about rendering a stream, see [Rendering a Stream](rendering-a-stream.md).

## Related topics

<dl> <dt>

[SDK Samples That Use the Core Audio APIs](sdk-samples-that-use-the-core-audio-apis.md)
</dt> </dl>

 

 



