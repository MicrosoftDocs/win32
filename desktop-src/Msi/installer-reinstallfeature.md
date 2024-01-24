---
description: The ReinstallFeature method of the Installer object reinstalls features or corrects problems with installed features.
ms.assetid: cfe2aef4-7742-49cd-b7a3-7d484e1f85e3
title: Installer.ReinstallFeature method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.ReinstallFeature
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.ReinstallFeature method

The **ReinstallFeature** method of the [**Installer**](installer-object.md) object reinstalls features or corrects problems with installed features.

## Syntax


```JScript
Installer.ReinstallFeature(
  Product,
  Feature,
  ReinstallMode
)
```



## Parameters

<dl> <dt>

*Product* 
</dt> <dd>

Specifies the product code of the product.

</dd> <dt>

*Feature* 
</dt> <dd>

Specifies the feature to be reinstalled. The parent feature or child feature of the specified feature is not reinstalled. To reinstall the parent or child feature, you must call the **ReinstallFeature** method for each separately or use the [**ReinstallProduct**](installer-reinstallproduct.md) method.

</dd> <dt>

*ReinstallMode* 
</dt> <dd>

Specifies the type of reinstallation. This parameter can be one or more of the following values.



| Value                                                                                                                                                                                                                                                                    | Meaning                                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <span id="msiReinstallModeFileMissing"></span><span id="msireinstallmodefilemissing"></span><span id="MSIREINSTALLMODEFILEMISSING"></span><dl> <dt>**msiReinstallModeFileMissing**</dt> </dl>                     | Reinstalls only if the file is missing.<br/>                                |
| <span id="msiReinstallModeFileOlderVersion"></span><span id="msireinstallmodefileolderversion"></span><span id="MSIREINSTALLMODEFILEOLDERVERSION"></span><dl> <dt>**msiReinstallModeFileOlderVersion**</dt> </dl> | Reinstalls if the file is missing or is an older version.<br/>              |
| <span id="msiReinstallModeFileEqualVersion"></span><span id="msireinstallmodefileequalversion"></span><span id="MSIREINSTALLMODEFILEEQUALVERSION"></span><dl> <dt>**msiReinstallModeFileEqualVersion**</dt> </dl> | Reinstalls if the file is missing or is an equal or older version.<br/>     |
| <span id="msiReinstallModeFileExact"></span><span id="msireinstallmodefileexact"></span><span id="MSIREINSTALLMODEFILEEXACT"></span><dl> <dt>**msiReinstallModeFileExact**</dt> </dl>                             | Reinstalls if the file is missing or is not an exact version.<br/>          |
| <span id="msiReinstallModeFileVerify"></span><span id="msireinstallmodefileverify"></span><span id="MSIREINSTALLMODEFILEVERIFY"></span><dl> <dt>**msiReinstallModeFileVerify**</dt> </dl>                         | Checks sum executables, and reinstalls if they are missing or corrupt.<br/> |
| <span id="msiReinstallModeFileReplace"></span><span id="msireinstallmodefilereplace"></span><span id="MSIREINSTALLMODEFILEREPLACE"></span><dl> <dt>**msiReinstallModeFileReplace**</dt> </dl>                     | Reinstalls all files regardless of version.<br/>                            |
| <span id="msiReinstallModeUserData"></span><span id="msireinstallmodeuserdata"></span><span id="MSIREINSTALLMODEUSERDATA"></span><dl> <dt>**msiReinstallModeUserData**</dt> </dl>                                 | Ensures required per=user registry entries.<br/>                            |
| <span id="msiReinstallModeMachineData"></span><span id="msireinstallmodemachinedata"></span><span id="MSIREINSTALLMODEMACHINEDATA"></span><dl> <dt>**msiReinstallModeMachineData**</dt> </dl>                     | Ensures required per=machine registry entries.<br/>                         |
| <span id="msiReinstallModeShortcut"></span><span id="msireinstallmodeshortcut"></span><span id="MSIREINSTALLMODESHORTCUT"></span><dl> <dt>**msiReinstallModeShortcut**</dt> </dl>                                 | Validates shortcuts.<br/>                                                   |
| <span id="msiReinstallModePackage"></span><span id="msireinstallmodepackage"></span><span id="MSIREINSTALLMODEPACKAGE"></span><dl> <dt>**msiReinstallModePackage**</dt> </dl>                                     | Uses the recache source to install the package.<br/>                        |



 

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



## See also

<dl> <dt>

[**MsiReinstallFeature**](/windows/desktop/api/Msi/nf-msi-msireinstallfeaturea)
</dt> <dt>

[Installation and Configuration Functions](installer-function-reference.md)
</dt> </dl>

 

 




