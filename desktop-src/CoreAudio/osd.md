---
description: This sample uses the Core Audio APIs to implement an on-screen display that shows volume changes to the output stream that plays through the default audio-rendering endpoint device.
ms.assetid: 33a1e843-f7c7-4da9-a51e-83a3f0a6ac70
title: OSD
ms.topic: article
ms.date: 05/31/2018
---

# OSD

This sample uses the Core Audio APIs to implement an on-screen display that shows volume changes to the output stream that plays through the default audio-rendering endpoint device. The on-screen display appears when the user adjusts the volume level in the Windows volume-control program, Sndvol.exe, and it disappears after the volume level remains unchanged for a short period.

This topic containes the following sections.

-   [Description](#description)
-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [Running the Sample](#running-the-sample)
-   [Related topics](#related-topics)

## Description

This sample demonstrates the following features.

-   [MMDevice API](mmdevice-api.md) for multimedia device enumeration and selection.
-   Audio [EndpointVolume API](endpointvolume-api.md)

## Requirements



| Product                                                        | Version                |
|----------------------------------------------------------------|------------------------|
| [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx) | Windows Vista or later |
| Visual Studio                                                  | 2005 or later          |



 

## Downloading the Sample

This sample is available in the following locations.



| Location    | Path/URL                                                                             |
|-------------|--------------------------------------------------------------------------------------|
| Windows SDK | \\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Multimedia\\Audio\\OSD\\... |



 

## Building the Sample

1.  Open the CMD shell for the Windows SDK and change to the OSD sample directory.
2.  Run the command "start OSD.sln" in the OSD directory to open the OSD project in the Visual Studio window.
3.  From within the window, select the **Debug** or **Release** solution configuration, select the **Build** menu from the menu bar, and select the **Build** option. If you do not open Visual Studio from the CMD shell for the SDK, Visual Studio will not have access to the SDK build environment. In that case, the sample will not build unless you explicitly set environment variable MSSdk, which is used in the project file, OSD.vcproj.

## Running the Sample

1.  Run the OSD executable file, OSD.exe, in Windows Vista or later. Note that you will not see a system tray icon or a window for the application, but you can see the process running using TaskMgr.exe.
2.  Run sndvol.exe to change the volume or mute, or change the volume using keyboard controls or an HID control. The OSD user interface is displayed.
3.  To exit the application, run TaskMgr.exe, highlight the OSD.exe process and click **End Process**.

## Related topics

<dl> <dt>

[SDK Samples That Use the Core Audio APIs](sdk-samples-that-use-the-core-audio-apis.md)
</dt> </dl>

 

 



