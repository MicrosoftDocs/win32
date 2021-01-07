---
description: If both files have a version number, the Windows Installer uses the logic illustrated by the following flow diagram to determine whether to replace all of the installed files belonging to the component.
ms.assetid: c4c8a23b-e1c2-4c96-b708-7cbcbcab4cd4
title: Both Files Have a Version
ms.topic: article
ms.date: 05/31/2018
---

# Both Files Have a Version

If the key file of a component being installed (copy-A) has the same name as a file already installed in the target location (copy-B), the installer compares the version number and language of the two files.

If both files have a version number, the installer uses the logic illustrated by the following flow diagram to determine whether to replace all of the installed files belonging to the component. Because the installer only installs entire components, if the installed key file is replaced then all of the component's files are replaced.

Note that this diagram illustrates the default [File Versioning Rules](file-versioning-rules.md), which can be overridden by setting the [**REINSTALLMODE**](reinstallmode.md) property. The default value of the **REINSTALLMODE** property is "omus".

![default file versioning rules when both files have the same name or version number](images/waiflow1.png)

The previous diagram can also be used with files with no language specified. If copy-A has a specified language and copy-B has no specified language, copy-B is replaced with copy-A. If copy-A and copy-B both have no language specified, then copy-B is not replaced.

See examples of default file versioning in [Replacing Existing Files](replacing-existing-files.md).

-   [Neither File Has a Version](neither-file-has-a-version.md)
-   [Neither File Has a Version with File Hash Check](neither-file-has-a-version-with-file-hash-check.md)
-   [One File Has a Version](one-file-has-a-version.md)

 

 



