---
description: During a concurrent installation, the installer sets the ParentOriginalDatabase property in the concurrent installation's session to the same value as the OriginalDatabase property in the parent installation's session.
ms.assetid: 8af1c7e5-313c-47b7-be0f-0e31ef21f6a6
title: ParentOriginalDatabase property
ms.topic: reference
ms.date: 05/31/2018
---

# ParentOriginalDatabase property

During a concurrent installation, the installer sets the **ParentOriginalDatabase** property in the concurrent installation's session to the same value as the [**OriginalDatabase**](originaldatabase.md) property in the parent installation's session. Parent installations use the concurrent installation actions to perform a concurrent installation. An installation package can determine whether it is being installed by a concurrent installation action by checking the value of this property.

> [!Note]  
> Concurrent installations are not recommended for the installation of applications intended for release to the public. For information about concurrent installations please see [Concurrent Installations](concurrent-installations.md).

 

> [!Note]  
> This property is not set if the concurrent installation is being run by the [RemoveExistingProducts](removeexistingproducts-action.md) action.

 

## Remarks

To prevent a package from ever being installed as a concurrent installation, add either of the following conditional statements to the [LaunchCondition](launchcondition-table.md) table. This prevents the package from ever being installed by a concurrent installation action run by another installation. This does not prevent the package from being installed by the [RemoveExistingProducts](removeexistingproducts-action.md) action.

``` syntax
"Not ParentProductCode"
```

``` syntax
"Not ParentOriginalDatabase"
```

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[**ParentProductCode**](parentproductcode.md)
</dt> </dl>

 

 




