---
description: This sample uses the Core Audio APIs to capture a high-quality voice stream. The sample supports acoustic echo cancellation (AEC) and microphone array processing by using the AEC DMO, also called the Voice capture DSP, provided by Microsoft .
ms.assetid: 932d3442-1beb-4938-9382-031c61cd9b05
title: AECMicArray
ms.topic: article
ms.date: 05/31/2018
---

# AECMicArray

This sample uses the Core Audio APIs to capture a high-quality voice stream. The sample supports acoustic echo cancellation (AEC) and microphone array processing by using the AEC DMO, also called the Voice capture DSP, provided by Microsoft .

This topic containes the following sections.

-   [Description](#description)
-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [Running the Sample](#running-the-sample)
-   [Related topics](#related-topics)

## Description

This sample demonstrates the following features.

-   [MMDevice](mmdevice-api.md) for multimedia device enumeration and selection.
-   [WASAPI](wasapi.md) for stream management operations such as starting and stopping the stream, stream switching.
-   [DeviceTopology](devicetopology-api.md) for enumerating audio adapters.
-   [EndpointVolume](endpointvolume-api.md) control the volume levels of [audio sessions](audio-sessions.md).

## Requirements



| Product                                                        | Version                     |
|----------------------------------------------------------------|-----------------------------|
| [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx) | Windows Vista or later      |
| Visual Studio                                                  | 2005 (non-express editions) |



 

## Downloading the Sample

This sample is available in the following locations.



| Location    | Path/URL                                                                                     |
|-------------|----------------------------------------------------------------------------------------------|
| Windows SDK | \\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Multimedia\\Audio\\AECMicArray\\... |



 

## Building the Sample

To build the AecSDKDemo sample, use the following steps:

1.  Open an SDK command window.
2.  Type **cd %MSSDK%\\Setup**.
3.  Run VCIntegrate.exe.

    From this point forward, command windows will have the proper environment settings to build an application that takes advantage of the SDK.

4.  Build the sample.

## Running the Sample

If you build the demo application successfully, an executable file, AecSDKDemo.exe is generated. To run it, type `AecSDKDemo` in a command window followed by required or optional arguments as described below.

`AecSDKDemo -out mic_out.pcm -mod system_mode [-option value] `

The following table shows the arguments.

| Argument  | Description                                                                                                                           |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------|
| -out      | Required. Specifies output file name.                                                                                                 |
| -mod      | Required. Specifies voice capture system mode. Refer to "Configuring the voice capture DMO" section in the sample readme for details. |
| -feat     | Optional. Turns feature mode on (1) or off (0).                                                                                       |
| -ns       | Optional. Turns noise suppression on (1) or off (0). Feature mode must be on for specifying this.                                     |
| -agc      | Optional. Turns digital AGC on (1) or off (0). Feature mode must be on for specifying this.                                           |
| -cntrclip | Optional. Turns center clipping on (1) or off (0). Feature mode must be on for specifying this.                                       |
| -spkdev   | Optional. Specifies speaker device index. If not specified, the user will be asked to select.                                         |
| -micdev   | Optional. Specifies microphone device index. If not specified, the user will be asked to select.                                      |
| -duration | Optional. Specifies how long the application runs.                                                                                    |



 

This sample application does not play any signals. To run the demo properly for AEC enabled modes (mode 0 and 4), users must play some audio signals through the same speaker device specified for the DMO (that is, the device specified by the "-spkdev" option), which simulates the far-end voice in a two-way chatting scenario. Users can use any player to play any audio signals. If there is no active render stream on the selected speaker device, the DMO will fail to process.

## Related topics

<dl> <dt>

[SDK Samples That Use the Core Audio APIs](sdk-samples-that-use-the-core-audio-apis.md)
</dt> </dl>

 

 



