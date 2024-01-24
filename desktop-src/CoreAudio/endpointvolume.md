---
description: This sample application uses the Core Audio APIs to change the volume of the device, as specified by the user.
ms.assetid: 2597f3b1-5339-4fd4-9938-39ff917626b4
title: EndpointVolume
ms.topic: article
ms.date: 05/31/2018
---

# EndpointVolume

This sample application uses the Core Audio APIs to change the volume of the device, as specified by the user.

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
-   [EndpointVolume API](endpointvolume-api.md) to control volume levels of the device endpoint.

## Requirements



| Product                                                        | Version   |
|----------------------------------------------------------------|-----------|
| [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx) | Windows 7 |
| Visual Studio                                                  | 2008      |



 

## Downloading the Sample

This sample is available in the following locations.



| Location    | Path/URL                                                                                        |
|-------------|-------------------------------------------------------------------------------------------------|
| Windows SDK | \\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Multimedia\\Audio\\EndpointVolume\\... |



 

## Building the Sample

To build the x sample, use the following steps:

To build the EndpointVolumeChanger sample, use the following steps:

1.  Open the CMD shell for the Windows SDK and change to the EndpointVolume sample directory.
2.  Run the command `start EndpointVolumeChanger.sln` in the EndpointVolume directory to open the EndpointVolumeChanger project in the Visual Studio window.
3.  From within the window, select the **Debug** or **Release** solution configuration, select the **Build** menu from the menu bar, and select the **Build** option. If you do not open Visual Studio from the CMD shell for the SDK, Visual Studio will not have access to the SDK build environment. In that case, the sample will not build unless you explicitly set environment variable MSSdk, which is used in the project file, WASAPIEndpointVolume.vcproj.

## Running the Sample

If you build the demo application successfully, an executable file, EndpointVolumeChanger.exe, is generated. To run it, type `EndpointVolumeChanger` in a command window followed by required or optional arguments. The following example shows how to toggle the mute setting on the default console device.

`EndpointVolumeChanger.exe -console -m`

The following table shows the arguments.

| Argument        | Description                                                         |
|-----------------|---------------------------------------------------------------------|
| -?              | Shows help.                                                         |
| -h              | Shows help.                                                         |
| -+              | Increments the volume level on audio endpoint device by one step. . |
| -up             | Increments the volume level on audio endpoint device by one step.   |
| --              | Decrements the volume level on audio endpoint device by one step.   |
| -down           | Decrements the volume level on audio endpoint device by one step.   |
| -v              | Sets the master volume level on the audio endpoint device.          |
| -console        | Use the default console device.                                     |
| -communications | Use the default communication device.                               |
| -multimedia     | Use the default multimedia device.                                  |
| -endpoint       | Use the endpoint identifier specified in the switch value.          |



 

If the application is run without arguments, it enumerates the available devices and prompts the user to select a device. After the user specifies the device, the application displays the current volume settings for the endpoint. The volume can be controlled by using the switches described in the preceding table.

For more information about controlling the volume levels of audio endpoint devices, see [EndpointVolume API](endpointvolume-api.md).

## Related topics

<dl> <dt>

[SDK Samples That Use the Core Audio APIs](sdk-samples-that-use-the-core-audio-apis.md)
</dt> </dl>

 

 



