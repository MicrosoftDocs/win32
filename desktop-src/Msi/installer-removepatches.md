---
description: The RemovePatches method removes one or more patches to products eligible to receive the patch. The RemovePatches method calls MsiRemovePatches.
ms.assetid: 09c6ad3a-9f5e-4f9a-82c8-be7e411efd60
title: Installer.RemovePatches method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.RemovePatches
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.RemovePatches method

The **RemovePatches** method removes one or more patches to products eligible to receive the patch. The **RemovePatches** method calls [**MsiRemovePatches**](/windows/desktop/api/Msi/nf-msi-msiremovepatchesa).

## Syntax


```JScript
Installer.RemovePatches(
  PatchList,
  ProductCode,
  UninstallType,
  PropertyList
)
```



## Parameters

<dl> <dt>

*PatchList* 
</dt> <dd>

A string that contains a semicolon delimited list of patches to remove. Each patch can be represented by either the full path to the patch package or by patch GUID. This parameter is required.

</dd> <dt>

*ProductCode* 
</dt> <dd>

A string with the GUID of the product from which the patches are to be removed. This parameter is required.

</dd> <dt>

*UninstallType* 
</dt> <dd>

An integer value that specifies the type of patch removal. This parameter must be **msiInstallTypeSingleInstance**.

</dd> <dt>

*PropertyList* 
</dt> <dd>

A string that specifies the Property=Value pairs to include. This parameter is optional.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

See [Uninstalling Patches](uninstalling-patches.md) for an example that demonstrates how an application can remove a patch from all products that are available to the user.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer 3.0 or later on Windows Server 2003 or Windows XP.<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                                    |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                                         |



## See also

<dl> <dt>

[**ProductCode**](productcode.md)
</dt> <dt>

[**MsiRemovePatches**](/windows/desktop/api/Msi/nf-msi-msiremovepatchesa)
</dt> <dt>

[Uninstalling Patches](uninstalling-patches.md)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




