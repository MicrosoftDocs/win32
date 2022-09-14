---
description: User system policies used with the Windows Installer.
ms.assetid: 74e940a1-dc7c-4ea3-ab62-d118204dac3e
title: User Policies
ms.topic: article
ms.date: 05/31/2018
---

# User Policies

The following user policies can be configured under

**HKEY\_CURRENT\_USER**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**



| Value name                                                            | Value data types          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------------------------------------------------------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AlwaysInstallElevated](alwaysinstallelevated.md)<br/>         | **REG\_DWORD**<br/> | If this value is set to "1" and the corresponding computer value is also set, the installer always installs with elevated privileges.<br/> Otherwise, the installer uses elevated privileges to install managed applications and uses the current user's privilege level for nonmanaged applications.<br/>                                                                                                                                                                                                      |
| [DisableMedia](disablemedia.md)<br/>                           | **REG\_DWORD**<br/> | If the [DisableMedia](disablemedia.md) policy is set to "1", users and administrators running a maintenance installation of one product are prevented from using the Browse Dialog to browse media sources, such as CD-ROM, for the sources of other installable products. Browsing for other products is prevented regardless of whether the installation is with elevated privileges. It is still possible for the user to reinstall the product from media if the user has a correctly labeled media source.<br/> |
| [DisableRollback](disablerollback.md)<br/>                     | **REG\_DWORD**<br/> | If this value is set to "1", the installer will not store rollback files during installation, disabling installation rollback. By default, rollback is enabled. Administrators are advised to not use this policy unless it is absolutely essential.<br/>                                                                                                                                                                                                                                                             |
| [SearchOrder](searchorder.md)<br/>                             | **REG\_SZ**<br/>    | Order in which the installer searches the three different types of sources:<br/> "n"– network<br/> "m"– media (CD-ROM or DVD)<br/> "u"– URL (Uniform Resource Locator)<br/> For example, a value of "nmu" instructs the installer to search network sources first, media sources second, and URL sources last. Leaving out a letter removes the corresponding volume type from the search. Default order in absence of this value is network first, then media followed by URL.<br/>          |
| [TransformsAtSource policy](transformsatsource-policy.md)<br/> | **REG\_DWORD**<br/> | If this value exists and is set to "1"; the installer searches for transform files in the root of any network sources in the [**sourcelist**](sourcelist.md) for the product. By default, transforms are stored in the Application Data folder of a user's profile.<br/>                                                                                                                                                                                                                                             |



 

 

 




