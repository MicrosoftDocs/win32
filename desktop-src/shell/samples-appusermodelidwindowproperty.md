---
Description: Demonstrates how to control the taskbar grouping behavior of an application's windows through the System.AppUserModel.ID property.
title: Application User Model ID (AppID) Window Property Sample
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Application User Model ID (AppID) Window Property Sample

Demonstrates how to control the taskbar grouping behavior of an application's windows through the [System.AppUserModel.ID](https://msdn.microsoft.com/windows/desktop/07858b3c-e601-40ec-a87a-d66612d5473a) property.

This topic contains the following sections.

-   [Description](#description)
-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [Running the Sample](#running-the-sample)
-   [Related topics](#related-topics)

## Description

This sample shows how to set the [System.AppUserModel.ID](https://msdn.microsoft.com/windows/desktop/07858b3c-e601-40ec-a87a-d66612d5473a) property through the use of the window's [**IPropertyStore**](https://msdn.microsoft.com/windows/desktop/e995aaa1-d4c9-475f-b1fa-b9123cd5b653) implementation, which is obtained through [**SHGetPropertyStoreForWindow**](https://msdn.microsoft.com/windows/desktop/772aa2c8-6dd1-480c-a008-58f30902cb80).

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



 

In the case of the Windows SDK, once you have downloaded and installed it, you will find the samples in the installed directory. For example, use of the default installation path for the Windows 7 SDK results in the samples being placed under `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\`.

## Building the Sample

To build the sample from the command prompt:

1.  Open the command prompt window and navigate to the **AppUserModelIDWindowProperty** project directory.
2.  Enter `msbuild AppUserModelIDWindowProperty.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **AppUserModelIDWindowProperty** project directory.
2.  Double-click the icon for the AppUserModelIDWindowProperty.sln file to open the project in Visual Studio.
3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

1.  Navigate to the directory that contains the new executable, using the command prompt or Windows Explorer.
2.  At the command line, enter `AppUserModelIDWindowProperty.exe`. Alternatively, from Windows Explorer double-click the icon for AppUserModelIDWindowProperty.exe.
3.  To demonstrate the effect Application User Model IDs (AppUserModelIDs) have on taskbar grouping, launch at least three instances of the application at the same time.
4.  Use the menu to set a different AppUserModelID on each of the three windows. Notice that each separate AppUserModelID results in a separate taskbar button and that windows can change their identity at runtime.
5.  Set at least two windows to the second AppUserModelID. Notice that they both move into the same taskbar group.
6.  Open the **Taskbar and Start Menu Properties** window by right-clicking the taskbar and selecting **Properties** in the context menu. Change the **Taskbar buttons:** drop-down between the **Combine when taskbar is full** and **Never combine** values. Notice that each window can get a separate button, but that the buttons are grouped by AppUserModelID.

## Related topics

<dl> <dt>

[Application User Model IDs (AppUserModelIDs)](appids.md)
</dt> </dl>

 

 



