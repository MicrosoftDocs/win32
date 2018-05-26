---
title: Music Bundle Signature Sample
description: A sample application that uses the Packaging APIs to sign a custom-format package, called a music bundle, and then validate the generated signature.
ms.assetid: f4f337dc-85ba-4dd9-aba8-f81c0e29088e
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Music Bundle Signature Sample

A sample application that uses the Packaging APIs to sign a custom-format package, called a music bundle, and then validate the generated signature.

This topic contains the following sections.

-   [Description](#description)
-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [Running the Sample](#running-the-sample)
-   [Additional Information](#additional-information)
-   [Sample Files](#sample-files)

## Description

This sample demonstrates how to use Packaging Digital Signature APIs to sign a custom package format and to validate the resultant signature.

The sample demonstrates the following features:

-   Signing the music bundle.
-   Validating the music bundle.

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
    2.  Navigate to the directory that contains the MusicBundleSignature.sln file.
    3.  Double-click the MusicBundleSignature.sln file to open it with Visual Studio 2008.
    4.  Go to the **Build** menu in Visual Studio 2008 and select **Build Solution**.
        > [!Note]  
        > If the sample does not build successfully, close Visual Studio 2008 and run the [.NET Framework Configuration Tool](a7106c52-68da-490e-b129-971b2c743764) (Mscorcfg.msc) before attempting to build the sample.

         

    Using the command prompt:

    1.  Open the command prompt.
    2.  Navigate to the directory that contains the MusicBundleSignature.vcproj file.
    3.  Enter the following command: **msbuild MusicBundleSignature.vcproj**.

Either the Debug or Release build mode may be used.

## Running the Sample

Before running the sample application, ensure that the sample project has been built in the Debug or Release mode that corresponds to the build mode that will be used to run the sample.

> [!Note]  
> To run the sample successfully, at least one X.509 certificate must be present. If an X.509 certificate is not present, the [Certificate Creation Tool](b0343f8e-9c41-4852-a85c-f8a0c408cf0d) (Makecert.exe) can be used to generate a certificate for testing purposes.

 

The following procedures describe how to run the sample using Visual Studio or the command prompt.

<dl> Using Visual Studio 2008:

1.  Open the **Properties** of the sample project.
2.  Under **Configuration Properties**, click the **Debugging** item.
3.  Type following argument into the **Command Arguments** text box and then click **OK**: MusicBundleSignature.exe.
4.  Run the sample.

  
Using the command prompt:

1.  Open the command prompt.
2.  Navigate to the directory that contains either the \\Debug or the \\Release project directory, as determined by the mode used to build and run the sample.
3.  Run the sample by entering the command: **MusicBundleSignature.exe**.

  
</dl>

## Additional Information

When run, the sample creates two files.

-   "SampleMusicBundle\_signed.zip": the signed version of the original "SampleMusicBundle.zip" package.
-   "signer1.cer": a certificate file that can be used to identify the signer of the package.

## Sample Files



| File                                          | Description                                                                                                                             |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| MusicBundleSignature.sln                      | Visual Studio 2008 solution file.<br/>                                                                                            |
| MusicBundleSignature.vcproj                   | Visual Studio 2008 project file.<br/>                                                                                             |
| [sign.h](sign-h.md)                          | Declaration of a function to sign the sample package. Also contains a description of the signing policy used for the sample.<br/> |
| [sign.cpp](sign-cpp.md)                      | Definitions of the sign function and helper functions used to sign the sample package.<br/>                                       |
| [validate.h](validate-h.md)                  | Declaration of a function to validate the signature of the signed sample package.<br/>                                            |
| [validate.cpp](validate-cpp.md)              | Definitions of the validate function and helper functions used to validate the signature of the signed sample package.<br/>       |
| [util.h](musicbundlesignature-util-h.md)     | Declarations for helper utility functions for using OPC, COM, and managing resources.<br/>                                        |
| [util.cpp](musicbundlesignature-util-cpp.md) | Definitions for helper utility functions for using OPC, COM, and managing resources.<br/>                                         |
| SampleMusicBundle.zip                         | An unsigned music bundle package containing music files and information.<br/>                                                     |



 

 

 





