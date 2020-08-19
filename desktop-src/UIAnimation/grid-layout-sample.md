---
title: Grid Layout Sample
description: Shows how to use Windows Animation, using Direct2D to animate a grid of images.
ms.assetid: f2f24058-c532-45ad-bde8-d05cfffcd505
ms.topic: article
ms.date: 05/31/2018
---

# Grid Layout Sample

Shows how to use Windows Animation, using Direct2D to animate a grid of images.

## Downloading the Sample

This sample is available in the following locations.



| Location                               | Path/URL                                                                                          |
|----------------------------------------|---------------------------------------------------------------------------------------------------|
| Windows Software Development Kit (SDK) | [Microsoft Windows Software Development Kit 7.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx) |
| Code Gallery                           | [Windows Animation Manager Sample Code](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/DirectCompositionWindowsAnimationManager)         |



 

After you have downloaded and installed the Windows SDK, you will find the samples in the installation directory. For example, if you use the default installation path for the Windows SDK for Windows 7, the samples are installed in C:\\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples.

## Building the Sample

Use one of the following methods to build the sample.

**To build the sample at the Command Prompt**

1.  Open the Command Prompt window and navigate to the GridLayout project directory. For example, the default installation path for this sample is C:\\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Multimedia\\WindowsAnimation\\GridLayout

2.  Run the following command: **msbuild GridLayout.sln**

**To build the sample using Microsoft Visual Studio (preferred)**

1.  Open Windows Explorer and navigate to the GridLayout project directory.

    > [!Note]  
    > The .sln file name extension is not shown under default folder settings. In that situation, it can be identified by its unique icon or by its type description, "Microsoft Visual Studio Solution".

     

2.  Double-click the icon for the GridLayout.sln file to open the project in Visual Studio.

3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

To run the sample:

1.  Navigate to the directory that contains the new executable, using either the command prompt or Windows Explorer.

2.  Run **GridLayout.exe** at the command prompt, or double-click the icon for GridLayout.exe in Windows Explorer.

3.  Sample images are loaded from the Picture Library. Resize the window and the images will arrange themselves into a grid.

 

 




