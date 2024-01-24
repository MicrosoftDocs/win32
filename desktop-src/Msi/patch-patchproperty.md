---
description: The PatchProperty property gets information about a specific patch applied to a specific instance of the product. This property calls MsiGetPatchInfoEx.
ms.assetid: c58897de-c30b-4269-9926-040613052616
title: Patch.PatchProperty method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Patch.PatchProperty
api_type: 
- COM
api_location: 
- Msi.dll
---

# Patch.PatchProperty method

The **PatchProperty** property gets information about a specific patch applied to a specific instance of the product. This property calls [**MsiGetPatchInfoEx**](/windows/desktop/api/Msi/nf-msi-msigetpatchinfoexa).

## Syntax


```JScript
Patch.PatchProperty(
  szProperty
)
```



## Parameters

<dl> <dt>

*szProperty* 
</dt> <dd>

The *szProperty* parameter can be one of the following values.



| Name          | Meaning                                                                                                                                                                                                                                                                                                                      |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LocalPackage  | Get the cached patch file used by the product.                                                                                                                                                                                                                                                                               |
| Transforms    | Get the set of patch transforms applied to the product by the last patch installation. This value may not be available for per-user-unmanaged applications if the user is not logged in to the computer.                                                                                                                     |
| InstallDate   | Get the date when the patch was applied to the product.                                                                                                                                                                                                                                                                      |
| Uninstallable | Returns "1" if the patch is marked as possible to uninstall from the product. In this case, the installer can still block the uninstallation if this patch is required by another patch that cannot be uninstalled.                                                                                                          |
| State         | Returns "1" if this patch is currently applied to the product. Returns "2" if this patch has been superseded by another patch. Returns "4" if this patch has been made obsolete by another patch. These values correspond to the constants used by the *dwFilter* parameter of [**MsiEnumPatchesEx**](/windows/desktop/api/Msi/nf-msi-msienumpatchesexa). |
| DisplayName   | Get the registered display name for the patch. For patches that do not include the DisplayName property in the [MsiPatchMetadata](msipatchmetadata-table.md) table, the returned display name is an empty string ("").                                                                                                      |
| MoreInfoURL   | Get the registered support information URL for the patch. For patches that do not include the MoreInfoURL property in the [MsiPatchMetadata](msipatchmetadata-table.md) table, the returned support information URL is an empty string ("").                                                                                |



 

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method can return ERROR\_UNKNOWN\_PATCH, if the [**Patch**](patch-object.md) object is initialized with an empty string for *ProductCode*.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer 3.0 or later on Windows Server 2003, Windows XP, and Windows 2000<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                                                   |
| IID<br/>     | IID\_IPatch is defined as 000C10A1-0000-0000-C000-000000000046<br/>                                                                                                                                                                                                            |



## See also

<dl> <dt>

[**Patch**](patch-object.md)
</dt> <dt>

[**MsiEnumPatchesEx**](/windows/desktop/api/Msi/nf-msi-msienumpatchesexa)
</dt> <dt>

[**MsiGetPatchInfoEx**](/windows/desktop/api/Msi/nf-msi-msigetpatchinfoexa)
</dt> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 




