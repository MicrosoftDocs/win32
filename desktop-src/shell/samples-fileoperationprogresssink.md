---
description: Demonstrates how to use the IFileOperationProgressSink interface methods for monitoring the details of IFileOperation interface actions.
title: File Operation Progress Sink
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 196ABB75-1FE0-44f5-9060-59AAB4231567
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# File Operation Progress Sink

Demonstrates how to use the [**IFileOperationProgressSink**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifileoperationprogresssink) interface methods for monitoring the details of [**IFileOperation**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifileoperation) interface actions.

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



 

## Downloading the Sample

| Location      | Path URL                                                                                             |
|---------------|------------------------------------------------------------------------------------------------------|
| GitHub  | [FileOperationProgressSink sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/shell/appplatform/FileOperationProgressSink) |

## Building the Sample

To build the sample from the command prompt window:

1.  Open the command prompt window and navigate to the **FileOperationProgressSink** project directory.
2.  Enter `msbuild FileOperationProgressSinkSample.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **FilesInUse** project directory. For example, the full default installation path is `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\WinUI\Shell\AppPlatform\FileOperationProgressSinkSample`.
2.  Double-click the icon for the FileOperationProgressSinkSample.sln file to open the project in Visual Studio.
    > [!Note]  
    > The .sln file name extension is not shown under default folder settings. In that situation, it can be identified by its unique icon or by its type description, "Microsoft Visual Studio Solution".

     

3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

1.  Navigate to the directory that contains the new executable, using the command prompt window or Windows Explorer.
2.  At the command prompt, enter `FileOperationProgressSinkSample.exe`, or from Windows Explorer, double-click the icon for FileOperationProgressSinkSample.exe.

 

 



