---
title: Package-Flags attribute
description: A bitfield that contains the deployment state flags for an application.
ms.assetid: 5b6cfed5-db04-438e-912b-60dce7a16409
ms.tgt_platform: multiple
keywords:
- Package-Flags attribute AD Schema
- packageFlags attribute AD Schema
topic_type:
- apiref
api_name:
- Package-Flags
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# Package-Flags attribute

A bitfield that contains the deployment state flags for an application.

This attribute can be zero or a combination of one or more of the following values.

| Value                 | Description                                                                                                                                                                                                                                                                                                    |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x00000004<br/> | The unmanaged version of this application must be uninstalled before assigning. **Windows XP with SP1 and later:** This flag is not supported.<br/> <br/>                                                                                                                                          |
| 0x00000008<br/> | This is a published application.<br/>                                                                                                                                                                                                                                                                    |
| 0x00000010<br/> | This package was deployed after Beta 3 of Windows 2000.<br/>                                                                                                                                                                                                                                             |
| 0x00000020<br/> | This application can be installed with the **Add or Remove Programs** feature of the Control Panel.<br/>                                                                                                                                                                                                 |
| 0x00000040<br/> | This application can be auto-installed on demand.<br/>                                                                                                                                                                                                                                                   |
| 0x00000080<br/> | This application is orphaned. A published application can become orphaned if the administrator removes the application from the list of deployable applications.<br/>                                                                                                                                    |
| 0x00000100<br/> | This application should be treated as uninstalled.<br/>                                                                                                                                                                                                                                                  |
| 0x00000200<br/> | This application is available as a pilot only.<br/>                                                                                                                                                                                                                                                      |
| 0x00000400<br/> | This is an assigned application. An assigned application cannot be fully removed by the user. If the user attempts to uninstall the application with the **Add or Remove Programs** feature of the Control Panel, the application will be re-advertised to the computer when the removal completes.<br/> |
| 0x00000800<br/> | This application is orphaned when the policy is removed. If the administrator removes the policy that is related to this application, the administrator will no longer control the deployment of the application, but the installed application will continue to function.<br/>                          |
| 0x00001000<br/> | This application is uninstalled when the deployment policy is removed.<br/>                                                                                                                                                                                                                              |
| 0x00002000<br/> | A full installation of user-assigned applications will be performed.<br/>                                                                                                                                                                                                                                |
| 0x00004000<br/> | Older versions of this application must be upgraded to this version.<br/>                                                                                                                                                                                                                                |
| 0x00008000<br/> | This package supports only a minimal user interface with a progress bar for the installation process.<br/>                                                                                                                                                                                               |
| 0x00010000<br/> | This is a package for 32-bit versions of Windows that should not be executed on Windows XP Professional x64 Edition or 64-bit versions of Windows Server 2003.<br/>                                                                                                                                      |
| 0x00020000<br/> | This package is suitable for any language.<br/>                                                                                                                                                                                                                                                          |
| 0x00040000<br/> | This package has upgrades.<br/>                                                                                                                                                                                                                                                                          |
| 0x00080000<br/> | This package has a full user interface for the installation process.<br/>                                                                                                                                                                                                                                |
| 0x00100000<br/> | Classes for this application are preserved during a redeploy operation if the application is redeployed in a domain renaming.<br/>                                                                                                                                                                       |



 



| Entry | Value |
|-------------------|--------------------------------------|
| CN                | Package-Flags                        |
| Ldap-Display-Name | packageFlags                         |
| Size              | \-                                   |
| Update Privilege  | \-                                   |
| Update Frequency  | \-                                   |
| Attribute-Id      | 1.2.840.113556.1.4.327               |
| System-Id-Guid    | 7d6c0e99-7e20-11d0-afd6-00c04fd930c9 |
| Syntax            | [**Enumeration**](s-enumeration.md) |



## Implementations

-   [**Windows 2000 Server**](#windows-2000-server)
-   [**Windows Server 2003**](#windows-server-2003)
-   [**Windows Server 2003 R2**](#windows-server-2003-r2)
-   [**Windows Server 2008**](#windows-server-2008)
-   [**Windows Server 2008 R2**](#windows-server-2008-r2)
-   [**Windows Server 2012**](#windows-server-2012)

## Windows 2000 Server



| Entry | Value |
|------------------------|------------------------------------------------------------------|
| Link-Id                | \-                                                               |
| MAPI-Id                | \-                                                               |
| System-Only            | False                                                            |
| Is-Single-Valued       | True                                                             |
| Is Indexed             | True                                                             |
| In Global Catalog      | False                                                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                     |
| Range-Lower            | \-                                                               |
| Range-Upper            | \-                                                               |
| Search-Flags           | 0x00000001                                                       |
| System-Flags           | 0x00000010                                                       |
| Classes used in        | [**Package-Registration**](c-packageregistration.md)<br/> |



## Windows Server 2003



| Entry | Value |
|------------------------|------------------------------------------------------------------|
| Link-Id                | \-                                                               |
| MAPI-Id                | \-                                                               |
| System-Only            | False                                                            |
| Is-Single-Valued       | True                                                             |
| Is Indexed             | True                                                             |
| In Global Catalog      | False                                                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                     |
| Range-Lower            | \-                                                               |
| Range-Upper            | \-                                                               |
| Search-Flags           | 0x00000001                                                       |
| System-Flags           | 0x00000010                                                       |
| Classes used in        | [**Package-Registration**](c-packageregistration.md)<br/> |



## Windows Server 2003 R2



| Entry | Value |
|------------------------|------------------------------------------------------------------|
| Link-Id                | \-                                                               |
| MAPI-Id                | \-                                                               |
| System-Only            | False                                                            |
| Is-Single-Valued       | True                                                             |
| Is Indexed             | True                                                             |
| In Global Catalog      | False                                                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                     |
| Range-Lower            | \-                                                               |
| Range-Upper            | \-                                                               |
| Search-Flags           | 0x00000001                                                       |
| System-Flags           | 0x00000010                                                       |
| Classes used in        | [**Package-Registration**](c-packageregistration.md)<br/> |



## Windows Server 2008



| Entry | Value |
|------------------------|------------------------------------------------------------------|
| Link-Id                | \-                                                               |
| MAPI-Id                | \-                                                               |
| System-Only            | False                                                            |
| Is-Single-Valued       | True                                                             |
| Is Indexed             | True                                                             |
| In Global Catalog      | False                                                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                     |
| Range-Lower            | \-                                                               |
| Range-Upper            | \-                                                               |
| Search-Flags           | 0x00000001                                                       |
| System-Flags           | 0x00000010                                                       |
| Classes used in        | [**Package-Registration**](c-packageregistration.md)<br/> |



## Windows Server 2008 R2



| Entry | Value |
|------------------------|------------------------------------------------------------------|
| Link-Id                | \-                                                               |
| MAPI-Id                | \-                                                               |
| System-Only            | False                                                            |
| Is-Single-Valued       | True                                                             |
| Is Indexed             | True                                                             |
| In Global Catalog      | False                                                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                     |
| Range-Lower            | \-                                                               |
| Range-Upper            | \-                                                               |
| Search-Flags           | 0x00000001                                                       |
| System-Flags           | 0x00000010                                                       |
| Classes used in        | [**Package-Registration**](c-packageregistration.md)<br/> |



## Windows Server 2012



| Entry | Value |
|------------------------|------------------------------------------------------------------|
| Link-Id                | \-                                                               |
| MAPI-Id                | \-                                                               |
| System-Only            | False                                                            |
| Is-Single-Valued       | True                                                             |
| Is Indexed             | True                                                             |
| In Global Catalog      | False                                                            |
| NT-Security-Descriptor | O:BAG:BAD:S:                                                     |
| Range-Lower            | \-                                                               |
| Range-Upper            | \-                                                               |
| Search-Flags           | 0x00000001                                                       |
| System-Flags           | 0x00000010                                                       |
| Classes used in        | [**Package-Registration**](c-packageregistration.md)<br/> |



 

 





