---
title: Localizing the Troubleshooting Pack
description: To specify that the package is localized, set the Localized attribute of GlobalDiagnosticPackage or LocalDiagnosticPackage to \ 0034;true \ 0034;.
ms.assetid: 085e99b1-13d8-4b77-846d-dfda4c576a35
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Localizing the Troubleshooting Pack

To specify that the package is localized, set the **Localized** attribute of [**GlobalDiagnosticPackage**](package-globaldiagnosticpackage-complextype.md) or [**LocalDiagnosticPackage**](package-localdiagnosticpackage-complextype.md) to "true". If true, all UI string elements must be of the form "@*resource.dll*,-*resourceID*" (they cannot be literal strings). WTP will load the strings from the language-specific resource DLL. If the package is not localized, WTP reads the string directly from the manifest.

The troubleshooting pack's root folder must contain a language-neutral resource DLL and a language-specific subfolder for each locale that the pack supports. The name of the subfolder must be the language name string (for example, en-US for English (United States)). Each subfolder must contain the language-specific resource file (\*.dll.mui). If the scripts in the pack use localized strings, the subfolders must also include the Windows PowerShell data file (\*.psd1).

Each language-specific subfolder must contain a catalog file that includes all files in the folder. The language packs must be signed by the same publisher that signed the troubleshooting pack. WTP validates that all localized resources are trusted.

The name of the catalog file must use the same name as the subfolder that contains it (for example, if the subfolder is en-US, the catalog file must be named en-US.cat). The catalog header must contain a PackageId attribute that is set to the value of the manifest's ID node (see [**DiagnosticIdentification**](package-diagnosticidentification-complextype.md)). The following is an example of a .cdf file for a language pack. If your scripts use localized string, the .cdf file must also include an entry for the .psd1 file.

``` syntax
[CatalogHeader]
Name=en-US.cat
PublicVersion=0x0000001
EncodingType=0x00010001
CATATTR1=0x10010001:OSAttr:2:6.1
CATATTR2=0x10010001:PackageId:PopupBlocker

[CatalogFiles]
<hash>resource.dll.mui=resource.dll.mui
<hash>resource.dll.muiATTR1=0x10010001:Filename:resource.dll.mui
<hash>en-US.cdf=en-US.cdf
<hash>en-US.cdfATTR1=0x10010001:Filename:en-US.cdf
```

Language packs can be distributed and installed separately from the troubleshooting pack.

### Localized support for scripts

Windows PowerShell version 2 uses .psd1 files to support localization. For each locale that you support, create a .psd1 file that contains language-specific strings and place each file in its language-specific subfolder of the troubleshooting pack. To load localized strings from a .psd1 file to be used in your script, use the Import-LocalizedData cmdlet as shown in the following example.


```PowerShell
Import-LocalizedData -bindingvariable localizationString -filename CL_LocalizationData
```



You would then use the *localizationString* variable to access the strings as shown in the following example. Set *stringid* to the name of a string identifier found in the CL\_LocalizationData.psd1 file.


```PowerShell
$obj | select-object -Property @{Name=$localizationString.stringid;Expression={$_.OldPropertyName}} | convertto-xml | update-diagreport
```



 

 




