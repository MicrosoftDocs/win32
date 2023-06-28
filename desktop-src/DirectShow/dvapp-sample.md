---
description: DVApp Sample
ms.assetid: 80375170-d0d6-4371-abe3-078703e158b1
title: DVApp Sample
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DVApp Sample

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

## Description

Digital Video (DV) capture application.

This sample demonstrates how to build various types of filter graphs for controlling DV camcorders. It also shows how to perform capture, preview, transmit, and device control with a DV camcorder.

### Usage

The DVApp application supports the following modes:

-   Preview: Renders DV from the camcorder to a video window.
-   DV to type-1 file: Captures DV data from the camcorder to a type-1 DV file.
-   Type-1 file to DV: Transmits data from a type-1 DV file to the camcorder.
-   DV to type-2 file: Captures DV data from the camcorder to a type-2 DV file.
-   Type-2 file to DV: Transmits data from a type-2 DV file to the camcorder.

The capture and transmit modes also perform preview. Each of those modes has a **No Preview** option as well, which disables preview. Capturing without preview is more efficient and can reduce the number of dropped frames.

The application starts in preview mode. To select another mode, choose a mode from the **Graph Mode** menu. For each mode, DVApp builds a filter graph that supports the functionality of that mode. To save the graph as a GraphEdit (.grf) file, select **Save Graph to File** from the **File** menu. Quit DVApp before opening the file in GraphEdit.

To capture to a file:

1.  From the **File** menu, choose **Set Output File** and enter a file name.
2.  From the **Graph Mode** menu, select a *DV to File* mode (type 1 or type 2, with or without preview).
3.  Click **Record**.
4.  If the camcorder is in VTR mode, click **Play**.
5.  To stop capturing, click **Stop**.

To transmit from a file to the camcorder:

1.  From the **File** menu, click **Set Input File** and select a DV file. The file must match the selected mode (type 1 or type 2).
2.  From the **Graph Mode** menu, select a *File to DV* mode (type 1 or type 2, with or without preview).
3.  Click **Play**.
4.  To record the data to tape, click **Record**.
5.  To stop transmitting, click **Stop**.

If the camcorder is in VTR mode, the user can control the transport mechanism through the application's VCR-style buttons. To seek the tape, enter the target timecode and click the seek button.

To limit how much data the application captures, choose **Capture Size** from the **File** menu.

To check the tape format (NTSC or PAL), choose **Check Tape** from the **Options** menu.

To change the size of the preview window, choose **Change Decode Size** from the **Options** menu.

### Programming Notes

The main purpose of this application is to show how to build various DV capture and transmit graphs.

### Device Arrival and Removal

The application handles device arrival and removal, using two different techniques. For device arrival, the application's message loop responds to WM\_DEVICECHANGE messages. For device removal, the application responds to [**EC\_DEVICE\_LOST**](ec-device-lost.md) events from the filter graph manager. Either approach works, although the EC\_DEVICE\_LOST event depends on the existence of the device in the filter graph.

The application only handles one device at a time. If the current device is removed, the application looks for another DV device on the system.

On some DV camcorders, the user must shut off the device when switching it between camera mode and VTR mode, which triggers a device-lost message. The application responds by enabling or disabling the appropriate menu commands. However, if the user toggles rapidly between modes, the camcorder might not generate a device-lost message. You can force the menus to update by choosing **Refresh Mode** from the **Options** menu. Some DV camcorders can toggle modes without shutting off, but send a device-lost message only when they switch to VTR mode.

### Device Control

The functionality of the **Play** and **Record** button depends on the current mode:

-   Preview: The filter graph runs automatically. The **Play** button starts the transport.
-   Capture to file: The **Record** button runs the graph, and the **Play** button starts the transport.
-   Transmit to device: The **Play** button runs the graph, and the **Record** button starts the transport.

The sample application does not perform frame-accurate capture. At various points, the application calls the **Sleep** function to wait for the device to respond. Newer DV camcorders send a notification when the state of the device changes. Older devices might not support notification; for the purposes of a sample, calling **Sleep** is a simpler solution.

## Downloading the Sample

To download the DirectShow SDK samples, install the latest version of the [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx).

This sample is installed under the following path: *\[SDK Root\]*\\Samples\\Multimedia\\DirectShow\\Capture\\DVApp.

## Related topics

<dl> <dt>

[Controlling a DV Camcorder](controlling-a-dv-camcorder.md)
</dt> <dt>

[Digital Video in DirectShow](digital-video-in-directshow.md)
</dt> <dt>

[DirectShow Samples](directshow-samples.md)
</dt> </dl>

 

 



