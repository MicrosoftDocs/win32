---
description: The installer sets the Last Saved by Summary Property to a value that depends on whether this is an installation package, transform, or patch package.In an installation package, the installer sets this property to the value of the LogonUser property during an administrative installation. Developers of database editing tools may use this property during the development process to track the last person to modify the installation database. This property should be set to Null in a final shipping database. The installer never uses this property and a user never needs to modify it.In a transform, this summary property contains the platform and language ID(s) that a database should have after it has been transformed. The property specifies to what the Template Summary should be set in the new database.In a patch package, this summary property contains a semicolon-delimited list of transform substorage names in the order they are applied by this patch.
ms.assetid: 6da171d9-29db-4524-abc6-77db8fbfca38
title: Last Saved By Summary property
ms.topic: reference
ms.date: 05/31/2018
---

# Last Saved By Summary property

The installer sets the **Last Saved by Summary** Property to a value that depends on whether this is an installation package, transform, or patch package.

In an installation package, the installer sets this property to the value of the [**LogonUser**](logonuser.md) property during an [administrative installation](administrative-installation.md). Developers of database editing tools may use this property during the development process to track the last person to modify the installation database. This property should be set to Null in a final shipping database. The installer never uses this property and a user never needs to modify it.

In a transform, this summary property contains the platform and language ID(s) that a database should have after it has been transformed. The property specifies to what the [**Template Summary**](template-summary.md) should be set in the new database.

In a patch package, this summary property contains a semicolon-delimited list of transform substorage names in the order they are applied by this patch.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |



## See also

<dl> <dt>

[Summary Property Descriptions](summary-property-descriptions.md)
</dt> </dl>

 

 




