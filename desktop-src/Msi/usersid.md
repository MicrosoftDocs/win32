---
Description: The installer sets the value of the UserSID property to the string representation of the security identifier (SID) of the user running the installation. For more information, see Authorization Structures.
ms.assetid: ac06a696-53c6-45b1-9ad1-1aa35564ce77
title: UserSID property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UserSID property

The installer sets the value of the **UserSID** property to the string representation of the security identifier (SID) of the user running the installation. For more information, see [Authorization Structures](security.authorization_structures).

## Default Value

None.

## Remarks

The Windows Installer set this property on Windows 2000, Windows XP and Windows Vista. This property is not defined on all other operating systems.

Note that this property has the special attribute that it can be retrieved from a deferred custom action. A custom action running with elevated privileges can still return the user's SID in **UserSID** property. For information, see [Obtaining Context Information for Deferred Execution Custom Actions](obtaining-context-information-for-deferred-execution-custom-actions.md).

## Requirements



|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




