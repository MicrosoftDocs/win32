---
description: The recommended method for generating a patch package is to use a patch creation tool such as Msimsp.exe to call UiCreatePatchPackage in Patchwiz.dll. Msimsp.exe and PatchWiz.dll are provided in the Windows Installer SDK.
ms.assetid: 7fa661aa-d52c-4b08-961f-90ec778f02ff
title: Generating a Patch Package
ms.topic: article
ms.date: 05/31/2018
---

# Generating a Patch Package

The recommended method for generating a patch package is to use a patch creation tool such as [Msimsp.exe](msimsp-exe.md) to call [UiCreatePatchPackage](uicreatepatchpackage-patchwiz-dll-.md) in [Patchwiz.dll](patchwiz-dll.md). Msimsp.exe and PatchWiz.dll are provided in the Windows Installer SDK.

The following example command line uses Msimsp.exe and the .pcp file created in [Creating a Patch Creation Properties File](creating-a-patch-creation-properties-file.md) to generate the sample patch package MNP2000.msp.

**Msimsp.exe -s C:\\Note\_Installer\\Patch\\MNP2000.pcp -p C:\\Note\_Installer\\Patch\\MNP2000.msp**

An authored patch creation tool may generate the patch package by calling [UiCreatePatchPackage](uicreatepatchpackage-patchwiz-dll-.md) as follows.

``` syntax
UiCreatePatchPackage ("C:\\Note_Installer\\Patch\\MNP2000.pcp", "C:\\Note_Installer\\Patch\\MNP2000.msp", NULL, NULL, "", TRUE)
```

[Continue](applying-a-patch-package-to-a-local-installation.md)

 

 



