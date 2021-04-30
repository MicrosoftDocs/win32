---
description: If neither file has a version number, the Windows Installer uses the logic illustrated by the following flow diagram to determine whether to replace all of the installed files belonging to the component.
ms.assetid: 82cb0d96-f49f-408e-a8c6-a0d1ee9af8c7
title: Neither File Has a Version
ms.topic: article
ms.date: 05/31/2018
---

# Neither File Has a Version

If the key file of a component being installed (copy-A) has the same name as a file already installed in the target location (copy-B), the installer compares the version number, date, and language of the two files.

If neither file has a version number, the installer uses the logic illustrated by the following flow diagram to determine whether to replace all of the installed files belonging to the component. Because the installer only installs entire components, if the installed key file is replaced, then all of the component's files are replaced.

Note that this diagram illustrates the default [File Versioning Rules](file-versioning-rules.md), which can be overridden by setting the [**REINSTALLMODE**](reinstallmode.md) property. The default value of the **REINSTALLMODE** property is "omus".

![default file versioning rules when neither file has a version number](images/waiflow2.png)

See the examples of default file versioning in [Replacing Existing Files](replacing-existing-files.md).

-   [Both Files Have a Version](both-files-have-a-version.md)
-   [Neither File Has a Version with File Hash Check](neither-file-has-a-version-with-file-hash-check.md)
-   [One File Has a Version](one-file-has-a-version.md)

 

 



