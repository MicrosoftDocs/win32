---
description: The installer sets the RollbackDisabled property when rollback has been disabled.
ms.assetid: 72215b0f-2fc4-49aa-abf8-3206bdfc765f
title: RollbackDisabled property
ms.topic: reference
ms.date: 05/31/2018
---

# RollbackDisabled property

The installer sets the **RollbackDisabled** property when rollback has been disabled. **RollbackDisabled** is used by package authors who need to ensure that the installer has not disabled rollback. The **RollbackDisabled** property can be used in a conditional expression that effectively refuses to continue with the installation if **RollbackDisabled** property is set.

## Default Value

By default, rollback is enabled.

## Remarks

Because [rollback](rollback-custom-actions.md) and [commit](commit-custom-actions.md) do not run while rollback is disabled, the installer cannot properly install a package that uses these types of custom actions in a transaction during the installation. In this case, the author of the package should include a condition using DisableRollback that prevents the installation from continuing if rollback is disabled.

The DisableRollback policy value can be set by an administrator as a part of assigning system policy. Administrators are advised to not disable rollback unless necessary. For more information about DisableRollback policy value, see [System Policy](system-policy.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[Rollback Installation](rollback-installation.md)
</dt> <dt>

[System Policy](system-policy.md)
</dt> <dt>

[rollback custom actions](rollback-custom-actions.md)
</dt> <dt>

[commit custom actions](commit-custom-actions.md)
</dt> </dl>

 

 




