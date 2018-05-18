---
title: Music Bundle Sample
description: A sample application that uses the Packaging APIs to produce and consume a custom-format package, called a music bundle.
ms.assetid: '8063fcb5-4629-4b6b-857b-bb22f0572f0d'
---

# Music Bundle Sample

A sample application that uses the Packaging APIs to produce and consume a custom-format package, called a music bundle.

This topic contains the following sections.

-   [Description](#description)
-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [Running the Sample](#running-the-sample)
-   [Sample Files](#sample-files)

## Description

This sample demonstrates how to use the Packaging APIs to produce and consume a custom-format package, called a music bundle.

The sample demonstrates the following features of the Packaging APIs:

-   Creating a new, empty package that will be a music bundle.
-   Adding parts and relationships to the music bundle.
-   Saving the music bundle.
-   Loading the music bundle.
-   Accessing music bundle parts and relationships.

## Requirements



| Product                                                                                             | Version        |
|-----------------------------------------------------------------------------------------------------|----------------|
| [Microsoft Windows Software Development Kit (SDK)](http://go.microsoft.com/fwlink/p/?linkid=129787) | Windows 7      |
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
3.  Follow steps for building, using Visual Studio 2008 or the command prompt.

    Using Visual Studio 2008:

    1.  Open Windows Explorer.
    2.  Navigate to the directory that contains the MusicBundle.sln file.
    3.  Double-click the MusicBundle.sln file to open it with Visual Studio 2008.
    4.  Go to the **Build** menu in Visual Studio 2008 and select **Build Solution**.
        > [!Note]  
        > If the sample does not build successfully, close Visual Studio 2008 and run the [.NET Framework Configuration Tool](a7106c52-68da-490e-b129-971b2c743764) (Mscorcfg.msc) before attempting to build the sample.

         

    Using the command prompt:

    1.  Open the command prompt.
    2.  Navigate to the directory that contains the MusicBundle.vcproj file.
    3.  Enter the following command: **msbuild MusicBundle.vcproj**.

Either the Debug or Release build mode may be used.

## Running the Sample

Before running the sample application, ensure that the sample project has been built in the Debug or Release mode that corresponds to the build mode that will be used to run the sample.

The following procedures describe how to run the sample using Visual Studio or the command prompt.

<dl> Using Visual Studio 2008:

1.  Open the **Properties** of the sample project.
2.  Under **Configuration Properties**, click the **Debugging** item.
3.  Type either of the following two sets of arguments into the **Command Arguments** text box and then click **OK**.
    -   To create and save the music bundle when the sample program runs, type: MusicBundle.exe -p *&lt;Input Directory&gt;&lt;Output Package Path&gt;*.<dl> The *&lt;Input Directory&gt;* is the full path of the ProductionData directory provided with the sample.  
        The *&lt;Output Package Path&gt;* is the full path and name of the package to be created.  
        </dl>
    -   To load and unpack the music bundle when the sample program runs, type: **MusicBundle.exe -c** *&lt;Input Package Path&gt;&lt;Output Directory&gt;*.<dl> *&lt;Input Package Path&gt;* is the full path to the \\ConsumptionData\\SampleMusicBundle.zip music bundle that is provided with the sample.  
        *&lt;Output Directory&gt;* is the full path to the directory where the music bundle will be unpacked.  
        </dl>
4.  Run the sample.

</dd> Using the command prompt:

1.  Open the command prompt.
2.  Navigate to the directory that contains either the \\Debug or the \\Release project directory, as determined by the mode used to build and run the sample.
3.  Run the sample by entering either of the following commands.
    -   To create and save the music bundle when the sample program runs, enter: **MusicBundle.exe -p** *&lt;Input Directory&gt;&lt;Output Package Path&gt;*.<dl> The *&lt;Input Directory&gt;* is the full path of the ProductionData directory provided with the sample.  
        The *&lt;Output Package Path&gt;* is the full path and name of the package to be created.  
        </dl>
    -   To load and unpack the music bundle when the sample program runs, enter: **MusicBundle.exe -c** *&lt;Input Package Path&gt;&lt;Output Directory&gt;*.<dl> *&lt;Input Package Path&gt;* is the full path to the \\ConsumptionData\\SampleMusicBundle.zip music bundle that is provided with the sample.  
        *&lt;Output Directory&gt;* is the full path to the directory where the music bundle will be unpacked.  
        </dl>

</dd> </dl>

## Sample Files



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>File</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>musicbundle.sln</td>
<td>Visual Studio 2008 solution file.<br/></td>
</tr>
<tr class="even">
<td>musicbundle.vcproj</td>
<td>Visual Studio 2008 project file.<br/></td>
</tr>
<tr class="odd">
<td>[musicbundle.h](musicbundle-h.md)</td>
<td>Main header file declaring two production and consumption functions. Also contains a description of the custom OPC file format used in the sample.<br/></td>
</tr>
<tr class="even">
<td>[musicbundle.cpp](musicbundle-cpp.md)</td>
<td>Entry point for the sample.<br/></td>
</tr>
<tr class="odd">
<td>[MusicBundleProduction.cpp](https://msdn.microsoft.com/library/windows/desktop/dd742758)</td>
<td>Definition of the production function declared in musicbundle.h and production helper functions.<br/></td>
</tr>
<tr class="even">
<td>[MusicBundleConsumption.cpp](https://msdn.microsoft.com/library/windows/desktop/dd742757)</td>
<td>Definition of the consumption function declared in musicbundle.h and consumption helper functions.<br/></td>
</tr>
<tr class="odd">
<td>[util.h](musicbundle-util-h.md)</td>
<td>Declarations for helper utility functions for using OPC, COM, and managing resources.<br/></td>
</tr>
<tr class="even">
<td>[util.cpp](musicbundle-util-cpp.md)</td>
<td>Definitions for helper utility functions for using OPC, COM, and managing resources.<br/></td>
</tr>
<tr class="odd">
<td>ConsumptionData\SampleMusicBundle.zip</td>
<td>A package containing sample music files that can be consumed using the sample application.
<blockquote>
[!Note]<br />
The ZIP extension is used in this example to clearer indicate that the music bundle is a ZIP-based package. The package format designer can use an extension specific to the scenario.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>ProductionData\*</td>
<td>Files used to produce the sample's music bundle OPC package, in the directory structure needed by the sample. <br/></td>
</tr>
</tbody>
</table>



 

 

 





