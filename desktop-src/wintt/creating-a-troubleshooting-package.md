---
title: Creating a Troubleshooting Pack
description: A troubleshooting pack contains the following components.
ms.assetid: 4d86e628-0d8a-409a-8920-68c5ed9d892b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating a Troubleshooting Pack

A troubleshooting pack contains the following components.



| Component                | Description                                                                                                                               |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Troubleshooting manifest | Specifies the root causes that the pack can detect and the scripts used to detect them, resolve them, and verify that they were resolved. |
| Troubleshooter scripts   | The scripts used to detect if a root cause exists.                                                                                        |
| Resolver scripts         | The scripts used to resolve a root cause that the troubleshooter script found.                                                            |
| Verifier scripts         | The scripts used to verify whether the resolver scripts were able to resolve the issue.                                                   |
| Localized resources      | The localized resource strings used by the troubleshooting manifest and scripts.                                                          |



 

For details on writing these components, see the following topics:

-   [Writing a Troubleshooting Manifest](writing-the-troubleshooting-manifest.md)
-   [Writing Scripts](writing-the-scripts.md)
-   [Interacting with the User](interacting-with-the-user.md)
-   [Reporting](reporting.md)
-   [Localizing the Troubleshooting Pack](localizing-the-troubleshooting-package.md)

The contents of a troubleshooting pack is contained in a single root folder. The root folder must contain the manifest, scripts, and package catalog. If you localize the package, the root folder must also contain the language neutral resource DLL and a subfolder for each locale (the name of the subfolder must be a language name string, for example, en-US). Each subfolder must contain a locale-specific resource file (\*.dll.mui) and a catalog file. If the scripts in the pack use localized strings, the subfolders must also include the Windows PowerShell data file (\*.psd1).

Although you can author, package, and test troubleshooting packs manually, you should consider using the Windows Troubleshooting Pack Designer tool included in the Windows SDK. In addition to helping you author your manifest, the tool also creates a catalog for the troubleshooting pack, signs the pack, and creates a cabinet file that you can use to distribute the pack. The Windows SDK includes the tool in the \\Bin\\TSPDesigner folder.

 

 




