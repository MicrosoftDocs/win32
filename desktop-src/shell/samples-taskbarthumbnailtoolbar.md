---
Description: Demonstrates a thumbnail toolbar, an active toolbar control embedded in a window's thumbnail preview, used to provide access to a window's key commands without making the user restore or activate the application's window.
title: Taskbar Thumbnail Toolbar Sample
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Taskbar Thumbnail Toolbar Sample

Demonstrates a thumbnail toolbar, an active toolbar control embedded in a window's thumbnail preview, used to provide access to a window's key commands without making the user restore or activate the application's window.

This topic contains the following sections.

-   [Description](#description)
-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [Running the Sample](#running-the-sample)
-   [Related topics](#related-topics)

## Description

This sample shows how to provide a simple toolbar to a taskbar thumbnail preview. The toolbar consists of three buttons. Clicking a button displays a window to confirm that the button was activated. The following APIs are demonstrated:

-   [**ITaskbarList3::ThumbBarAddButtons**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-itaskbarlist3-thumbbaraddbuttons)
-   [**ITaskbarList3::ThumbBarSetImageList**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-itaskbarlist3-thumbbarsetimagelist)
-   [**THUMBBUTTON**](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-thumbbutton) structure

## Requirements



| Product                                | Minimum Product Version |
|----------------------------------------|-------------------------|
| Windows                                | Windows 7               |
| Windows Software Development Kit (SDK) | 7.0                     |



 

## Downloading the Sample

This sample is available in the following locations.



| Location      | Path URL                                                                                             |
|---------------|------------------------------------------------------------------------------------------------------|
| Code Gallery  | [Windows Shell Integration Samples on Code Gallery](http://go.microsoft.com/fwlink/p/?linkid=155659) |
| Windows 7 SDK | [Download Windows 7 SDK](http://go.microsoft.com/fwlink/p/?linkid=129787)                            |



 

In the case of the Windows SDK, once you have downloaded and installed it, you will find the samples in the installed directory. For example, use of the default installation path for the Windows 7 SDK results in this sample being placed under `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\WinUI\Shell\AppShellIntegration\TaskbarThumbnailToolbar`.

## Building the Sample

To build the sample from the command prompt:

1.  Open the command prompt window and navigate to the **TaskbarThumbnailToolbar** project directory.
2.  Enter `msbuild ThumbnailToolbar.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **TaskbarThumbnailToolbar** project directory.
2.  Double-click the icon for the ThumbnailToolbar.sln file to open the project in Visual Studio.
3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

1.  Navigate to the directory that contains the new executable file (for instance, `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\WinUI\Shell\AppShellIntegration\TaskbarThumbnailToolbar\Debug`), using the command prompt or Windows Explorer.

    -   If using the command line, enter `ThumbnailToolbar.exe`.
    -   If using Windows Explorer, double-click the icon for ThumbnailToolbar.exe.

    A new window will open, with an associated taskbar button.

2.  Hover the cursor over the **ThumbnailToolbar** taskbar button so that the preview displays. Click one of the three buttons (green, yellow, red) shown in the preview's toolbar.
3.  Choose **Exit** from the window's **File** menu to end the program.

## Related topics

<dl> <dt>

[Taskbar Extensions](taskbar-extensions.md)
</dt> </dl>

 

 



