---
description: This section describes considerations for deploying your MUI application for optimal use by the application loading logic and the resource loader.
ms.assetid: 6c10b355-9bdd-4dba-8446-91034d4fe9b8
title: Application Deployment
ms.topic: article
ms.date: 05/31/2018
---

# Application Deployment

This section describes considerations for deploying your MUI application for optimal use by the application loading logic and the resource loader.

## Packaging

Packaging for the application depends on the type of language support provided, as Windows installs language packs based on user preferences. For example, if you have decided on supporting system language settings, you might want to provide all language support in a single package, regardless of the intended user.

If the application and resources are large, you should use one package per supported language. For instance, you might use this packaging type if your application is presenting user-selectable languages and the user needs dynamic addition and removal of language resources.

## File Placement on Windows Vista and Later

This section describes file placement for a MUI application targeted only at Windows Vista and later.

### Place the LN File

A typical LN file for a MUI application is an .exe file or a .dll file, for example, BakerDelta.dll. You should place this file in the root folder where your application is installed, for example, X:\\\\&lt;somepath&gt;\\BakerDelta.dll.

### Place Language-Specific Resource Files

Your language-specific resource files must have predictable names formed by appending ".mui" to the full name of the LN file, for example, BakerDelta.dll.mui. These files must be placed in subfolders named after the appropriate [language names](language-names.md). The following example shows placement of resources for the BakerDelta.dll LN file, with language-specific resource files for English (United Kingdom), English (United States), neutral English, Spanish (Spain), Spanish (Mexico), and neutral Spanish:

-   X:\\\\&lt;somepath&gt;\\BakerDelta.dll
-   X:\\\\&lt;somepath&gt;\\en-GB\\BakerDelta.dll.mui
-   X:\\\\&lt;somepath&gt;\\en-US\\BakerDelta.dll.mui
-   X:\\\\&lt;somepath&gt;\\en\\BakerDelta.dll.mui
-   X:\\\\&lt;somepath&gt;\\es-ES\\BakerDelta.dll.mui
-   X:\\\\&lt;somepath&gt;\\es-MX\\BakerDelta.dll.mui
-   X:\\\\&lt;somepath&gt;\\es\\BakerDelta.dll.mui

The resource files must be placed in their correct locations during installation of the MUI application or a language package. It is important to place each file in the correct folder, as the resource loader cannot operate properly otherwise. Using the example above, the resource loader examines X:\\&lt;somepath&gt;\\en-US\\BakerDelta.dll.mui for English (United States) resources. If the loader looks in that file and encounters only Spanish-language resources, it fails.

## File Placement on a Pre-Windows Vista Operating System

An application to run on a pre-Windows Vista operating system can use the Windows Vista convention of placing language-specific resource files in folders based on language names. Alternatively, the application can conform to an older convention that forms paths from [language identifiers](language-identifiers.md). For applications that only support a single language, you can just place the language-specific resource file in the root directory with the binary file.

For example, consider an LN file called BakerDelta.dll, with language-specific resource files for English (United Kingdom), English (United States), neutral English, Spanish (Spain), Spanish (Mexico), and neutral Spanish. An installation on a pre-Windows Vista operating system might place these files as follows:

-   X:\\\\&lt;somepath&gt;\\BakerDelta.dll
-   X:\\\\&lt;somepath&gt;\\BakerDelta.dll.mui (optional .mui file containing resources in the language of the operating system as the ultimate fallback)
-   X:\\\\&lt;somepath&gt;\\MUI\\0809\\BakerDelta.dll.mui
-   X:\\\\&lt;somepath&gt;\\MUI\\0409\\BakerDelta.dll.mui
-   X:\\\\&lt;somepath&gt;\\MUI\\0209\\BakerDelta.dll.mui
-   X:\\\\&lt;somepath&gt;\\MUI\\040a\\BakerDelta.dll.mui
-   X:\\\\&lt;somepath&gt;\\MUI\\080a\\BakerDelta.dll.mui
-   X:\\\\&lt;somepath&gt;\\MUI\\0209\\BakerDelta.dll.mui

In addition to these files, the application can set up an ultimate fallback language-specific resource file, to reside in the same folder as the application itself. For the above example, this file is X:\\&lt;somepath&gt;\\BakerDelta.dll.mui.

## Installation

Installation logic for copying and setting up application files relies on the supported languages and the location of language resource files in the correct install locations. An installer must install and set up the application so that the user can easily add and remove languages.

If your application simply installs the language of the target operating system, the installer must detect the operating system user interface to determine the application resources to install. To support the best user experience, the installer should also detect the user interface language to present a localized user interface for the installation itself.

It is recommended to use Windows Installer (MSI) to create your installation software. Associated resources should be included in the base language resource file, as described in [Creating the Base Language Resource File](creating-the-base-language-resource-file.md). For instructions on using MSI to prepare the application installer, see [Windows Installer](../msi/windows-installer-portal.md).

## Uninstall Program

You might also want to furnish an uninstall program with your MUI application. MSI is also recommended for creation of this program. For instructions on using MSI to prepare the uninstall software, see [Windows Installer](../msi/windows-installer-portal.md).

## Related topics

<dl> <dt>

[Using Multilingual User Interface](using-multilingual-user-interface.md)
</dt> </dl>

 

 
