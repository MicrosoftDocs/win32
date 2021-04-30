---
description: Your globalized application must define a variety of user interface elements, such as menus, dialog boxes, help strings, and other items, represented as localized resources.
ms.assetid: 4d8b769d-0830-4e4e-b284-ce0b21dfe5d4
title: MUI Resource Management
ms.topic: article
ms.date: 05/31/2018
---

# MUI Resource Management

Your globalized application must define a variety of user interface elements, such as menus, dialog boxes, help strings, and other items, represented as localized resources. The user interface language becomes one of the settings for the application. This section describes the MUI resource technology, which we recommend that you use for creating your application resources.

## Features of the MUI Resource Technology

The MUI resource technology, exposed in Windows Vista and later, has the following characteristics:

-   Language-specific resource files are stored separately from the application code binary, so that a code change does not affect the resources.
-   The resources for multiple languages can be deployed in a single installation or separate installations for each language.
-   A resource is loaded and displayed according to the language of the application as set by the user.

This technology associates the resources defined in language-specific files with a particular version of a language-neutral (LN) file. The LN file is a Win32 PE file representing the application code binary and language-neutral resources. Association of files uses a checksum reflected in resource configuration data contained in all associated files. The resource loader uses the checksum to verify that the files hold the same version of the required resources. It also validates the language in the language-specific file with its folder name. The loader does not load a resource file if the appropriate association is not established.

Specifically the main checksum is calculated from the major and minor version numbers of a file and the file name (case sensitive), which are obtained from the version resource. This checksum should not change between RTM and service pack versions of the same component. Additionally, a service checksum is used to determine the appropriate version of the language-specific resource file to load. This checksum is calculated based on the localizable resources in the file.

MUI furnishes two resource utilities that you can use to prepare resource files for your application. A MUI-specific utility, called MUIRCT, allows you to build an LN file and associated language-specific resource files. On Windows Vista and later, the Windows RC Compiler has also been modified to build these files according to the MUI resource technology. For syntax and details of these tools, see [Resource Utilities](resource-utilities.md).

## LN File

The LN file for a MUI application contains executable code and language-neutral resources that are shared and installed by all language versions of the application.

## Language-Specific Resource File

A language-specific resource file normally contains user interface strings and other elements that require localization for a particular language. Your MUI application uses one language-specific resource file per supported language. The LN file for the application is the same for each language-specific resource file.

When built using the MUI resource technology, language-specific files have a ".mui" extension and are handled as follows:

-   The language-specific files associated with a given LN file all share the same file name, which is formed by adding the extension ".mui" to the full file name (with extension) of the corresponding LN file. For example, an LN file named "Myfile.dll" has language-specific files named "Myfile.dll.mui".
-   The language-specific files reside in subfolders of the folder containing the LN file. Each folder name reflects the language.

## Resource Configuration Data

To associate an LN file with its language-specific files, the MUI resource technology uses resource configuration data, including the checksum. The resource build procedure places this information in an RC Config section of each LN and language-specific file. A human-readable form of this information is available via the MUIRCT utility. For more information, see [Resource Utilities](resource-utilities.md).

## Related topics

<dl> <dt>

[About Multilingual User Interface](about-multilingual-user-interface.md)
</dt> <dt>

[Resource Utilities](resource-utilities.md)
</dt> </dl>

 

 



