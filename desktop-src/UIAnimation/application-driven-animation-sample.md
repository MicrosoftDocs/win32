---
title: Application-Driven Animation Sample
description: Shows Windows Animation in the application-driven configuration by using Direct2D to animate the background color of a window and syncing to the refresh rate.
ms.assetid: deefc473-6749-4e2b-ad34-33ccd206d231
ms.topic: article
ms.date: 05/31/2018
---

# Application-Driven Animation Sample

Shows Windows Animation in the application-driven configuration by using Direct2D to animate the background color of a window and syncing to the refresh rate.

## Downloading the Sample

This sample is available in the following locations.



| Location                               | Path/URL                                                                                          |
|----------------------------------------|---------------------------------------------------------------------------------------------------|
| Windows Software Development Kit (SDK) | [Microsoft Windows Software Development Kit 7.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx) |
| Code Gallery                           | [Windows Animation Manager Sample Code](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/DirectCompositionWindowsAnimationManager)          |



 

After you have downloaded and installed the Windows SDK, you will find the samples in the installation directory. For example, if you use the default installation path for the Windows SDK for Windows 7, the samples are installed in C:\\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples.

## Building the Sample

Use one of the following methods to build the sample.

**To build the sample at the Command Prompt**

1.  Open the Command Prompt window and navigate to the AppDriven project directory. For example, the default installation path for this sample is C:\\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Multimedia\\WindowsAnimation\\AppDriven.

2.  Run the following command: **msbuild AppDriven.sln**

**To build the sample using Microsoft Visual Studio (preferred)**

1.  Open Windows Explorer and navigate to the AppDriven project directory.

2.  Double-click the icon for the AppDriven.sln file to open the project in Visual Studio.

    > [!Note]  
    > The .sln file name extension is not shown under default folder settings. In that situation, it can be identified by its unique icon or by its type description, "Microsoft Visual Studio Solution".

     

3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

To run the sample:

1.  Navigate to the directory that contains the new executable, using either the command prompt or Windows Explorer.

2.  Run **AppDriven.exe** at the command prompt, or double-click the icon for AppDriven.exe in Windows Explorer.

3.  Click anywhere in the client area, and the background color of the window will change to a random color.

 

 




