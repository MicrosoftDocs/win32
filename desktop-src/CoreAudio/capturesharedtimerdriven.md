---
description: This sample application uses the Core Audio APIs to capture audio data from an input device specified by the user and writes it to a uniquely named .wav file in the current directory. This sample demonstrates timer-driven buffering.
ms.assetid: 06124b99-89b3-4dfa-b989-a54746ecd697
title: CaptureSharedTimerDriven
ms.topic: article
ms.date: 05/31/2018
---

# CaptureSharedTimerDriven

This sample application uses the Core Audio APIs to capture audio data from an input device specified by the user and writes it to a uniquely named .wav file in the current directory. This sample demonstrates timer-driven buffering.

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
-   [WASAPI](wasapi.md) for stream management operations.

## Requirements



| Product                                                        | Version   |
|----------------------------------------------------------------|-----------|
| [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx) | Windows 7 |
| Visual Studio                                                  | 2008      |



 

## Downloading the Sample

This sample is available in the following locations.



| Location    | Path/URL                                                                                                  |
|-------------|-----------------------------------------------------------------------------------------------------------|
| Windows SDK | \\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Multimedia\\Audio\\CaptureSharedTimerDriven\\... |



 

## Building the Sample

To build the CaptureSharedTimerDriven sample, use the following steps:

1.  Open the CMD shell for the Windows SDK and change to the CaptureSharedTimerDriven sample directory.
2.  Run the command `start WASAPICaptureSharedTimerDriven.sln` in the CaptureSharedTimerDriven directory to open the WASAPICaptureSharedTimerDriven project in the Visual Studio window.
3.  From within the window, select the **Debug** or **Release** solution configuration, select the **Build** menu from the menu bar, and select the **Build** option. If you do not open Visual Studio from the CMD shell for the SDK, Visual Studio will not have access to the SDK build environment. In that case, the sample will not build unless you explicitly set environment variable MSSdk, which is used in the project file, WASAPICaptureSharedTimerDriven.vcproj.

## Running the Sample

If you build the demo application successfully, an executable file, WASAPICaptureSharedTimerDriven.exe, is generated. To run it, type `WASAPICaptureSharedTimerDriven` in a command window followed by required or optional arguments. The following example shows how to run the sample by specifying capture duration on the default multimedia device.

`WASAPICaptureSharedTimerDriven.exe -d 20 -multimedia`

The following table shows the arguments.

| Argument        | Description                                                |
|-----------------|------------------------------------------------------------|
| -?              | Shows help.                                                |
| -h              | Shows help.                                                |
| -l              | Audio capture latency in milliseconds.                     |
| -d              | Audio capture duration in seconds.                         |
| -m              | Disables the use of MMCSS.                                 |
| -console        | Use the default console device.                            |
| -communications | Use the default communication device.                      |
| -multimedia     | Use the default multimedia device.                         |
| -endpoint       | Use the endpoint identifier specified in the switch value. |



 

If the application is run without arguments, it enumerates the available devices and prompts the user to select a device for the capture session. The default console, communication, and multimedia devices are listed followed by devices and the endpoint identifiers. If no duration is specified, the audio stream from the specified device is captured for 10 seconds. The application writes the captured data to a uniquely named .wav file.

CaptureSharedTimerDriven demonstrates timer-driven buffering. In this mode, the client must wait for a period of time (half the latency, specified by the -d switch value, in milliseconds). When the client wakes up, half way through the processing period, it pulls the next set of samples from the engine. Before each processing pass in the buffering loop, the client must find out the amount of capture data available so that the data does not overrun the capture buffer. The audio data that is captured from the specified device can be processed by enabling event-driven buffering. This mode is demonstrated in the [CaptureSharedEventDriven](capturesharedeventdriven.md) sample.

## Related topics

<dl> <dt>

[SDK Samples That Use the Core Audio APIs](sdk-samples-that-use-the-core-audio-apis.md)
</dt> </dl>

 

 



