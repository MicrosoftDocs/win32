---
description: A Windows Installer Patch (MSP) can be applied when installing an application for the first time by using the PATCH property.
ms.assetid: 2c4b9d5a-34fb-4a0b-b530-30bf238468fd
title: Patching Initial Installations
ms.topic: article
ms.date: 05/31/2018
---

# Patching Initial Installations

A Windows Installer Patch (MSP) can be applied when installing an application for the first time by using the [**PATCH**](patch.md) property.

To apply a patch the first time the application is installed, the [**PATCH**](patch.md) property must be set on the command line. Specify the full path to the patch on the command line as the "PATCH={*path to patch*}" property-value pair.

Note that specifying the [**PATCH**](patch.md) property on the command line overrides the patch applicability checks performed when using [**MsiApplyPatch**](/windows/desktop/api/Msi/nf-msi-msiapplypatcha) or the /p [Command Line Option](command-line-options.md).

If a patch is applied using [**MsiApplyPatch**](/windows/desktop/api/Msi/nf-msi-msiapplypatcha) or the /p [Command Line Option](command-line-options.md), the installer compares the applications currently installed on the computer to the list of product codes eligible to receive the patch in the [**Template Summary**](template-summary.md) property.

When you set the [**PATCH**](patch.md) property on the command line to install on first installation, the applications eligible to receive the patch is determined by validation conditions on the transforms embedded in the patch package. The recommended method for generating a patch package is to use a patch creation tool such as [Msimsp.exe](msimsp-exe.md) and [PATCHWIZ.DLL](patchwiz-dll.md). The validation conditions on transforms in the patch originate from the ProductValidateFlags column in the [TargetImages](targetimages-table-patchwiz-dll-.md) table of the Patch Creation Properties (.pcp) file.

The patch can be applied the first time the application is installed by a command line, another application, or script.

The following shows first-time patching from the command line.

**msiexec /I** *package.msi* **PATCH=***"c:\\directory\\patch.msp"*

The following shows first-time patching from another application.

``` syntax
UINT uiStat = MsiInstallProduct(_T("package.msi"), _T("PATCH=c:\directory\patch.msp"));
```

The following shows first-time patching from script.


```VB
Dim Installer as Object
Set Installer = CreateObject("WindowsInstaller.Installer")
Installer.InstallProduct "package.msi", "PATCH=c:\directory\patch.msp"
```



**Windows Installer 3.0 and later:  **

Beginning with Windows Installer version 3.0, multiple patches can be applied when installing an application for the first time. Set the [**PATCH**](patch.md) property to a semicolon delimited list of the patches' full paths. The following shows first-time patching of multiple patches from the command line.

**msiexec /I** *package.msi* **PATCH=***"c:\\directory\\patch.msp;c:\\directory\\patch2.msp;c:\\directory\\patch3.msp"*

 

 



