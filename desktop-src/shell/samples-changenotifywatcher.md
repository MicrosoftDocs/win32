---
description: Demonstrates how to listen to Shell change notifications on a folder or item in the Windows Explorer namespace.
title: Change Notify Watcher Sample
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 02A7C5B4-94F2-4c35-9290-4C816E5CF63A
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Change Notify Watcher Sample

Demonstrates how to listen to Shell change notifications on a folder or item in the Windows Explorer namespace.

This topic contains the following sections.

- [Requirements](#requirements)
- [Downloading the Sample](#downloading-the-sample)
- [Building the Sample](#building-the-sample)
- [Running the Sample](#running-the-sample)

## Requirements



| Product                                | Minimum Product Version |
|----------------------------------------|-------------------------|
| Windows                                | Windows Vista           |
| Windows Software Development Kit (SDK) | 7.0                     |



 

## Downloading the Sample

| Location      | Path URL                                                                                             |
|---------------|------------------------------------------------------------------------------------------------------|
| GitHub  | [ChangeNotifyWatcher sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/shell/appplatform/ChangeNotifyWatcher) |

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

 

 



