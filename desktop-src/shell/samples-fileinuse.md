---
description: Demonstrates how to customize the File In Use dialog to display additional information and options for files that are currently opened in the application.
title: File Is In Use Sample
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 22EFE7CC-D223-46b3-BD6B-293E3FA0BA01
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# File Is In Use Sample

Demonstrates how to customize the **File In Use** dialog to display additional information and options for files that are currently opened in the application.

This topic contains the following sections.

-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [Running the Sample](#running-the-sample)

## Requirements



| Product                                | Minimum Product Version |
|----------------------------------------|-------------------------|
| Windows                                | Windows Vista           |
| Windows Software Development Kit (SDK) | 6.1                     |



 

For additional requirements, see the IFileIsInUse\_sample.docx file included with the sample.

## Downloading the Sample

| Location      | Path URL                                                                                             |
|---------------|------------------------------------------------------------------------------------------------------|
| GitHub  | [FileIsInUse sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/shell/appplatform/fileisinuse) |

## Building the Sample

To build the sample from the Command Prompt window:

1.  Open the Command Prompt window and navigate to the **FileIsInUse** project directory.
2.  Enter `msbuild FileIsInUse.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **FilesInUse** project directory. For example, the full default installation path is `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\WinUI\Shell\AppPlatform\FileIsInUse`.
2.  Double-click the icon for the FileIsInUseSample.sln file to open the project in Visual Studio.
    > [!Note]  
    > The .sln file name extension is not shown under default folder settings. In that situation, it can be identified by its unique icon or by its type description, "Microsoft Visual Studio Solution".

     

3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

1.  Navigate to the directory that contains the new executable, using the command prompt window or Windows Explorer.
2.  At the command prompt, enter `FileIsInUseSample.exe`, or from Windows Explorer, double-click the icon for FileIsInUseSample.exe.

For detailed information about this code sample, see the IFileIsInUse\_sample.docx file included with the sample.

 

 



