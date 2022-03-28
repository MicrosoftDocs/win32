---
description: Demonstrates taskbar icon overlays and progress bars.
title: Taskbar Peripheral Status Sample
ms.topic: article
ms.date: 05/31/2018
ms.assetid: E4B693FB-EE7D-47d0-A5D8-91205AD4A3DC
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Taskbar Peripheral Status Sample

Demonstrates taskbar icon overlays and progress bars.

This topic contains the following sections.

- [Description](#description)
- [Requirements](#requirements)
- [Downloading the Sample](#downloading-the-sample)
- [Building the Sample](#building-the-sample)
- [Running the Sample](#running-the-sample)
- [Related topics](#related-topics)

## Description

This sample creates an example taskbar button on which it demonstrates the use of [**ITaskbarList3::SetOverlayIcon**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-itaskbarlist3-setoverlayicon) by allowing you to apply various overlays chosen from a menu.

The sample also provides the option of simulating a progress indicator on the button, demonstrating the use of [**ITaskbarList3::SetProgressState**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-itaskbarlist3-setprogressstate) and [**ITaskbarList3::SetProgressValue**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-itaskbarlist3-setprogressvalue) by showing at first an indeterminate progress indicator (TBPF\_INDETERMINATE), and then a normal proportional indicator (TBPF\_NORMAL).

## Requirements



| Product                                | Minimum Product Version |
|----------------------------------------|-------------------------|
| Windows                                | Windows 7               |
| Windows Software Development Kit (SDK) | 7.0                     |



 

## Downloading the Sample

| Location      | Path URL                                                                                             |
|---------------|------------------------------------------------------------------------------------------------------|
| GitHub  | [TaskBarPeripheralStatus sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/shell/appshellintegration/TaskbarPeripheralStatus) |

## Building the Sample

To build the sample from the command prompt:

1.  Open the command prompt window and navigate to the **TaskbarPeripheralStatus** project directory.
2.  Enter `msbuild PeripheralStatus.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **TaskbarPeripheralStatus** project directory.
2.  Double-click the icon for the PeripheralStatus.sln file to open the project in Visual Studio.
3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

1.  Navigate to the directory that contains the new executable file (for instance, `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\WinUI\Shell\AppShellIntegration\TaskbarPeripheralStatus\Win32\Debug`), using the command prompt or Windows Explorer.

    -   If using the command line, enter `PeripheralStatus.exe`.
    -   If using Windows Explorer, double-click the icon for PeripheralStatus.exe.

    A new window will open, with an associated taskbar button.

2.  To demonstrate overlays, choose **Overlay 1** or **Overlay 2** from the window's **Peripheral Status** menu. The chosen overlay appears on the taskbar button. To remove the overlay, choose **Clear Overlay**.
3.  To demonstrate the progress bar, choose **Simulate Progress** from the window's **Peripheral Status** menu. The taskbar button will show an indeterminate progress indicator then switch to a normal indicator.
4.  Choose **Exit** from the window's **File** menu to end the program.

## Related topics

<dl> <dt>

[Taskbar Extensions](taskbar-extensions.md)
</dt> </dl>

 

 



