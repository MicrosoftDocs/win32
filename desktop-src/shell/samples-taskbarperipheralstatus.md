---
Description: Demonstrates taskbar icon overlays and progress bars.
title: Taskbar Peripheral Status Sample
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Taskbar Peripheral Status Sample

Demonstrates taskbar icon overlays and progress bars.

This topic contains the following sections.

-   [Description](#description)
-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [Running the Sample](#running-the-sample)
-   [Related topics](#related-topics)

## Description

This sample creates an example taskbar button on which it demonstrates the use of [**ITaskbarList3::SetOverlayIcon**](/windows/win32/shobjidl_core/nf-shobjidl_core-itaskbarlist3-setoverlayicon?branch=master) by allowing you to apply various overlays chosen from a menu.

The sample also provides the option of simulating a progress indicator on the button, demonstrating the use of [**ITaskbarList3::SetProgressState**](/windows/win32/shobjidl_core/nf-shobjidl_core-itaskbarlist3-setprogressstate?branch=master) and [**ITaskbarList3::SetProgressValue**](/windows/win32/shobjidl_core/nf-shobjidl_core-itaskbarlist3-setprogressvalue?branch=master) by showing at first an indeterminate progress indicator (TBPF\_INDETERMINATE), and then a normal proportional indicator (TBPF\_NORMAL).

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



 

In the case of the Windows SDK, once you have downloaded and installed it, you will find the samples in the installed directory. For example, use of the default installation path for the Windows 7 SDK results in this sample being placed under `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\WinUI\Shell\AppShellIntegration\TaskbarPeripheralStatus`.

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

 

 



