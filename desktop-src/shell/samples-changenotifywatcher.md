---
Description: Demonstrates how to listen to Shell change notifications on a folder or item in the Windows Explorer namespace.
title: Change Notify Watcher Sample
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Change Notify Watcher Sample

Demonstrates how to listen to Shell change notifications on a folder or item in the Windows Explorer namespace.

This topic contains the following sections.

-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [Running the Sample](#running-the-sample)

## Requirements



| Product                                | Minimum Product Version |
|----------------------------------------|-------------------------|
| Windows                                | Windows Vista           |
| Windows Software Development Kit (SDK) | 7.0                     |



 

## Downloading the Sample

This sample is available in the following locations.



| Location      | Path URL                                                                                             |
|---------------|------------------------------------------------------------------------------------------------------|
| Code Gallery  | [Windows Shell Application Samples on Code Gallery](http://go.microsoft.com/fwlink/p/?linkid=155655) |
| Windows 7 SDK | [Download Windows 7 SDK](http://go.microsoft.com/fwlink/p/?linkid=129787)                            |



 

In the case of the Windows SDK, once you have downloaded and installed it, you will find the samples in the installed directory. For example, use of the default installation path for the Windows 7 SDK results in the samples being placed under `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\`.

## Building the Sample

To build the sample from the command prompt:

1.  Open the command prompt window and navigate to the **ChangeNotifyWatcher** project directory.
2.  Enter `msbuild ChangeNotifyWatcher.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **ChangeNotifyWatcher** project directory.
2.  Double-click the icon for the ChangeNotifyWatcher.sln file to open the project in Visual Studio.
3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

1.  Navigate to the directory that contains the new executable, using the command prompt or Windows Explorer.
2.  At the command prompt, enter `ChangeNotifyWatcher.exe`. Alternatively, from Windows Explorer double-click the icon for ChangeNotifyWatcher.exe.
3.  To demonstrate the effect, Application User Model IDs (AppUserModelIDs) select a folder to watch by either clicking **"Pick..."** or by using drag-and-drop on a folder from a Windows Explorer window into the sample's list view.

 

 



