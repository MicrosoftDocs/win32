---
description: The ACTION property can be set to the following values.
ms.assetid: 'f2c436b6-ebd9-4ac4-8609-f54129023ca7'
title: ACTION property
ms.topic: article
ms.date: 05/31/2018
---

# ACTION property

The **ACTION** property can be set to the following values.

## Value



| Value                                                                                                                                            | Meaning                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <span id="INSTALL"></span><span id="install"></span><dl> <dt>**INSTALL**</dt> </dl>       | [INSTALL Action](install-action.md)<br/>     |
| <span id="ADVERTISE"></span><span id="advertise"></span><dl> <dt>**ADVERTISE**</dt> </dl> | [ADVERTISE Action](advertise-action.md)<br/> |
| <span id="ADMIN"></span><span id="admin"></span><dl> <dt>**ADMIN**</dt> </dl>             | [ADMIN Action](admin-action.md)<br/>         |



 

The **ACTION** property determines which action to perform if a Null action name is supplied to [**MsiDoAction**](/windows/desktop/api/Msiquery/nf-msiquery-msidoactiona) or the [**DoAction Method**](session-doaction.md). If no value is defined for the **ACTION** property, the installer calls the [INSTALL Action](install-action.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




