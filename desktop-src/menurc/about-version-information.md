---
title: About Version Information
description: This topic discusses the version information functions.
ms.assetid: 63fb6c0f-11b3-4d70-b1ba-56086cb02847
keywords:
- resources,version information
- version information
- adding version information
- file conflicts
ms.topic: article
ms.date: 05/31/2018
---

# About Version Information

You can use the version information functions to determine where a file should be installed and identify conflicts with currently installed files. These functions enable you to avoid the following problems:

-   installing older versions of components over newer versions
-   changing the language in a mixed-language system without notification
-   installing multiple copies of a library in different directories
-   copying files to network directories shared by multiple users

The version information functions enable applications to query a version resource for file information and present the information in a clear format. This information includes the file's purpose, author, version number, and so on.

You can add version information to any files that can have Windows resources, such as DLLs, executable files, or .fon font files. To add the information, create a [VERSIONINFO Resource](/windows/desktop/menurc/versioninfo-resource) and use the resource compiler to compile the resource.

 

 