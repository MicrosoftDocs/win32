---
title: Set Author Sample
description: A sample application that uses the Packaging APIs to read and modify an existing package.
ms.assetid: 26785d8c-7f18-412b-a5bd-61bcff72c7da
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set Author Sample

A sample application that uses the Packaging APIs to read and modify an existing package.

This topic contains the following sections.

-   [Description](#description)
-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [Running the Sample](#running-the-sample)
-   [Additional Information](#additional-information)
-   [Sample Files](#sample-files)

## Description

A sample console application that demonstrates how to use the Packaging API in conjunction with MSXML to read and modify an Office Open XML word processing file, such as a Microsoft Word 2007 or a Windows WordPad document.

The sample demonstrates the following features:

-   Using the Packaging APIs in conjunction with MSXML.
-   Loading a package that is an Office Open XML word processing document.
-   Displaying some of the text in the document package.
-   Modifying core properties of the document package.
-   Saving the modified package as a new word processing document.

## Requirements



| Product                                                                                             | Version        |
|-----------------------------------------------------------------------------------------------------|----------------|
| [Microsoft Windows Software Development Kit (SDK)](http://go.microsoft.com/fwlink/p/?linkid=129787) | Windows 7      |
| [ATL](http://go.microsoft.com/fwlink/p/?linkid=142947)                                              | .NET Framework |



 

## Downloading the Sample

This sample is available in the following locations:



| Location     | Path/URL                                                                           |
|--------------|------------------------------------------------------------------------------------|
| Windows SDK  | \\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\dataaccess\\OPC           |
| Code Gallery | [Download from MSDN Code Gallery](http://go.microsoft.com/fwlink/p/?linkid=178659) |



 

## Building the Sample

The following procedure describes how to build the sample.

1.  Install the Microsoft Windows Software Development Kit (SDK).
2.  Register the Windows SDK.
3.  Follow steps for building, using Visual Studio or the command prompt.

    Using Visual Studio 2008:

    1.  Open Windows Explorer.
    2.  Navigate to the directory that contains the setauthor.sln file.
    3.  Double-click the setauthor.sln file to open it with Visual Studio 2008.
    4.  Go to the **Build** menu in Visual Studio and select **Build Solution**.
        > [!Note]  
        > If the sample does not build successfully, close Visual Studio 2008 and run the [.NET Framework Configuration Tool](https://msdn.microsoft.com/windows/desktop/a7106c52-68da-490e-b129-971b2c743764) (Mscorcfg.msc) before attempting to build the sample.

         

    Using the command prompt:

    1.  Open the command prompt.
    2.  Navigate to the directory that contains the "setauthor.vcproj" file.
    3.  Enter the following command: **msbuild setauthor.vcproj**.

Either the Debug or Release build mode may be used.

## Running the Sample

Before running the sample application, ensure that the sample project has been built in the Debug or Release mode that corresponds to the build mode that will be used to run the sample.

The following procedures describe how to run the sample using Visual Studio or the command prompt.

<dl> Using Visual Studio 2008:

1.  Open the **Properties** of the sample project.
2.  Under **Configuration Properties**, click the **Debugging** item.
3.  Type either of the following two sets of arguments into the **Command Arguments** text box and then click **OK**.
    -   To view text and authorship information when the sample program runs, type: setauthor.exe sample.docx.
    -   To view text and modify authorship information when the sample program runs, type: setauthor.exe sample.docx *&lt;NewAuthorName&gt;&lt;NewDocumentName&gt;*.docx.
4.  Run the sample.

  
Using the command prompt:

1.  Open the command prompt.
2.  Navigate to the directory that contains either the \\Debug or the \\Release project directory, as determined by the mode used to build and run the sample.
3.  Run the sample by entering either of the following commands.
    -   To view text and authorship information, enter: **setauthor.exe sample.docx**.
    -   To view text and modify authorship information, enter: **setauthor.exe sample.docx &lt;NewAuthorName&gt; &lt;NewDocumentName&gt;.docx**.

  
</dl>

## Additional Information

The modifications made to the package can also been seen in the package file itself after the package has been saved. Rename the output file by adding a .zip extension, and browse the package. Navigate to the Core Properties part and open it with Notepad or Internet Explorer to view properties XML markup.

## Sample Files



| File                               | Description                                                                             |
|------------------------------------|-----------------------------------------------------------------------------------------|
| setauthor.sln                      | Visual Studio 2008 solution file.<br/>                                            |
| setauthor.vcproj                   | Visual Studio 2008 project file.<br/>                                             |
| [setauthor.cpp](setauthor-cpp.md) | Entry point for the sample.<br/>                                                  |
| [wordlib.h](wordlib-h.md)         | Declarations of utility functions for Open Office XML word processing files.<br/> |
| [wordlib.cpp](wordlib-cpp.md)     | Definitions of utility functions for Open Office XML word processing files.<br/>  |
| [opclib.h](opclib-h.md)           | Declarations of utility functions for packages in general.<br/>                   |
| [opclib.cpp](opclib-cpp.md)       | Definitions of utility functions for packages in general.<br/>                    |
| [util.h](setauthor-util-h.md)     | Helper definitions for using COM and ATL.<br/>                                    |
| sample.docx                        | An Office Open XML word processing document for use with the sample.<br/>         |



 

 

 





