---
title: How to Configure the MI Development Environment
description: This topic includes step-by-step instructions to configure a development environment for coding, registering, and testing MI providers and clients.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 48F32EEF-7CF3-4443-95B4-97E208164ACE
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# How to: Configure the MI Development Environment

This topic includes step-by-step instructions to configure a development environment for coding, registering, and testing MI providers and clients.

## Instructions

### Step 1: Install the Windows SDK

The Windows Software Development Kit (SDK) for Windows 8 contains headers, libraries, and a selection of tools that you can use when you create applications that run on Windows operating systems. For MI development the SDK includes the **Convert-MofToProvider** tool that takes a MOF file as input and generates the skeleton code for an MI provider, .NET reference assemblies for MI client development in managed languages such as Microsoft Visual C#, and header files for MI provider and client development in native languages such as Microsoft Visual C++.

1.  For Windows 8, download the [Windows Software Development Kit (SDK) for Windows 8](Http://Go.Microsoft.Com/FWLink/p/?LinkID=306595) (Http://Go.Microsoft.Com/FWLink/p/?LinkID=306595).
2.  Run the Windows SDK setup application.
3.  On the **Specify Location** dialog, enter the desired **Download Path** where the Windows SDK will be installed.
4.  Click **Next**.
5.  On the **Select the features you want to download** dialog, check the **Windows Software Development Kit** option for native development (for coding native MI providers and clients) and the **.NET Framework 4.5 Software Development Kit** for managed development (for coding managed MI clients).
6.  When done, click **Download**.

### Step 2: Install Visual Studio

While not strictly required, Visual Studio (including the different editions of Visual Studio Express) creates a rich development environment for coding and debugging MI providers and clients.

-   Download the appropriate Microsoft Visual Studio SKU from the [Visual Studio download page](Http://Go.Microsoft.Com/FWLink/p/?LinkID=306593) (Http://Go.Microsoft.Com/FWLink/p/?LinkID=306593).

### Step 3: Download the CIM Schema Files

The current version of MI supports CIM schema 2.26. You'll need to download that schema's MOF files from the DMTF (Distributed Management Task Force) web site.

1.  Browse to the [CIM schema 2.26](Http://Go.Microsoft.Com/FWLink/p/?LinkID=306560) page (Http://Go.Microsoft.Com/FWLink/p/?LinkID=306560) on the DMTF website.
2.  Click the link titled **Zip archive of all Final MOF files (1.4MB)**.
3.  The download is a .ZIP file that you can extract to the desired local or network drive.

### Step 4: Create the MSFT\_Qualifiers File

If you have downloaded the [MI API Samples](Http://Go.Microsoft.Com/FWLink/p/?LinkID=306594), you will already have this file. If not, you can create the only needed file from that sample by performing the following steps - as opposed to downloading all of the samples.

1.  In your editor, create a new text file.
2.  Copy the following contents into the new file:

    ```mof
    Qualifier Stream : boolean = false, 
        Scope( method, parameter), 
        Flavor(DisableOverride, ToSubclass);

    Qualifier ClassVersion : string = null, 
        Scope(class, association, indication), 
        Flavor(EnableOverride, Restricted);
    ```

    

3.  Save the file as **MSFT\_Qualifiers.mof** into an appropriate directory. Take note of the directory you use as it will be needed for the **Create the Environment Variables** section of this topic.

### Step 5: Create the Environment Variables

The following environment variables are used throughout the topics in this section.

> [!Note]  
> The environment variable values in this section will work for an installation of the Windows SDK where the default installation location was used. If the default installation location was changed during the installation of the Windows SDK, you'll need to use that location in setting the following environment variables.

 

1.  Create an environment variable called **SDKDIR** and point it to the Windows SDK installation directory. For example:

    ``` syntax
    32-bit (x86): SET SDKDIR=C:\Program Files\Windows Kits\8.0
    64-bit (amd64): SET SDKDIR=C:\Program Files (x86)\Windows Kits\8.0
    ```

2.  Create an environment variable called **SDKMIDOTNETDIR** and point it to the location of the MI reference assembly needed for using the MI managed API. For example:

    ``` syntax
    32-bit (x86): SET SDKMIDOTNETDIR=C:\Program Files\Reference Assemblies\Microsoft\WMI\v1.0
    64-bit (amd64): SET SDKMIDOTNETDIR=C:\Program Files (x86)\Reference Assemblies\Microsoft\WMI\v1.0
    ```

3.  Create an environment variable called **SDKBINDER** and point it to the Windows SDK bin directory. This will enable you to easily access the **Convert-MofToProvider** tool. For example:

    ``` syntax
    32-bit (x86): SET SDKBINDIR=%SDKDIR%\bin\x64
    64-bit (amd64): SET SDKBINDIR=%SDKDIR%\bin\x32
    ```

4.  Create an environment variable called **CIM2260DIR** and point it to the location where you installed the CIM 2.26 schema files.

    ``` syntax
    SET CIM2260DIR=<Directory containing the CIM 2.26 schema files>
    ```

5.  Create an environment variable called **MIINCLUDEDIR** and point it to the location where you placed the **MSFT\_Qualifiers.mof** file.

    ``` syntax
    SET MIINCLUDEDIR=<Directory containing the MSFT_Qualifiers.mof file>
    ```

 

 




