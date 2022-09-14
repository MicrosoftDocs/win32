---
title: ADSI and User Account Control
description: Windows and Windows Server have User Account Control, which has ramifications for applications that use Active Directory Service Interfaces (ADSI).
ms.assetid: 0b286252-8c24-4a18-9dc6-063ca158a8ff
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# ADSI and User Account Control

Windows and Windows Server have [User Account Control](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc709691(v=ws.10)), which has ramifications for applications that use [Active Directory Service Interfaces](active-directory-service-interfaces-adsi.md) (ADSI). Specifically, these interfaces were designed to be run by a user account with administrator privileges on the local computer.

**Problem**

Every time an application connects to the directory and attempts to create an ADSI object, the [Active Directory Schema](/windows/desktop/ADSchema/active-directory-schema) is checked for changes. If it has changed since the last connection, the schema is downloaded and stored in a cache on the local computer. In versions of Windows prior to Windows Vista, the default location for this cache was

`%systemroot%\SchCache\`

However, applications run by standard (that is, non-administrator) accounts will not have access to this directory, and consequently, applications that use ADSI interfaces that are run in this mode will download the schema on every connection, which will impact throughput and performance.

**Solutions**

*Single user* - To resolve this issue, there are new ADSI Provider registry control keys that determine the registry locations and file locations for cached [Active Directory Schema](/windows/desktop/ADSchema/active-directory-schema) objects. If the registry key

`HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\adsi\Cache\PerMachine`

is set to 0 (zero), each user will have a different storage location for ADSI; registry keys will be stored in

`HKEY_CURRENT_USER\Software\Microsoft\ADs\Providers\LDAP\`

and cache files will be stored in

`%LOCALAPPDATA%\Microsoft\Windows\SchCache`

These settings are the default settings on computers running Windows Server 2008 or Windows Vista.

*Multi-user* - If you are running ADSI applications on a computer with many user accounts (for example, a web server), then it's preferable not to have many copies of the [Active Directory Schema](/windows/desktop/ADSchema/active-directory-schema) cache using up large amounts of disk space. Setting the registry key

`HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\adsi\Cache\PerMachine`

to 1 (one) will revert ADSI to the previous behavior; all [Active Directory Schema](/windows/desktop/ADSchema/active-directory-schema) objects will be stored in their previous locations; the registry key will be in

`HKEY_LOCAL_MACHINE\Software\Microsoft\ADs\Providers\LDAP`

and the cache file will be in

`%systemroot%\SchCache`

In this case, administrator accounts should run the application, which will cause the schema file to be cached in the global location for future use by the less privileged users.

 

 