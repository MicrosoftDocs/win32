---
description: Removal of Windows Registry Reflection
ms.assetid: 4b42d44d-cde8-4d96-96c5-24b7ab7e4cec
title: Removal of Windows Registry Reflection
ms.topic: article
ms.date: 05/31/2018
---

# Removal of Windows Registry Reflection

## Platform

**Clients** - Windows 7  
**Servers** - Windows Server 2008 R2  









## Feature Impact

 **Severity** - Low  
**Frequency** - Low  





## Description

The registry reflection process copies registry keys and values between two registry views to keep them in synch. In previous 64-bit installations of Windows, the process reflected a subset of the redirected registry keys between the 32-bit and 64-bit views. However, the implementation of this caused some inconsistencies in the state of the registry. (For details on Registry Reflection, please refer to the corresponding MSDN article in the *Links to Other Resources* section below.)

Starting with Windows 7, we have removed registry reflection completely and merged the keys that used to be reflected:

-   HKEY\_LOCAL\_MACHINE\\Software\\Classes
-   HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\COM3
-   HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\EventSystem
-   HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Ole
-   HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Rpc
-   HKEY\_USERS\\\*\\Software\\Classes
-   HKEY\_USERS\\\*\_Classes

Effectively, this provides the same reflection behavior, since changes to these keys immediately are available for both 32-bit and 64-bit applications.

The keys that were reflected conditionally remain split:

-   HKEY\_LOCAL\_MACHINE\\Software\\Classes\\CLSID
-   HKEY\_LOCAL\_MACHINE\\Software\\Classes\\Interface
-   HKEY\_USERS\\\*\\Software\\Classes\\CLSID
-   HKEY\_USERS\\\*\\Software\\Classes\\Interface
-   HKEY\_USERS\\\*\_Classes\\CLSID
-   HKEY\_USERS\\\*\_Classes\\Interface

They are used to keep the data that should not be shared between 32-bit and 64-bit applications.

## Manifestation

CLSID and Interface keys from the list above are not reflected anymore while they are still redirected. While this is the desired behavior in most of cases, it is possible that applications could take a dependency on their reflected behavior in Vista.

The functions allowing applications to control reflection (RegDisableReflectionKey and RegEnableReflectionKey) are no-ops in Windows 7.

## Mitigation of Impact

COM is the major consumer of registry reflection. COM and other consumers were updated to accommodate this change. This change does not affect applications that use standard COM APIs..

## Solution

Apply one of the following options if you are relying on registry reflection to synchronize 32bit and 64bit views:

-   Create keys in both views explicitly during installation
-   Move the keys out of the scope of reflected keys
-   Check both views of the registry when querying for a reflected key

    **Note:** KEY\_WOW64\_32KEY and KEY\_WOW64\_64KEY flags cannot be combined

Apply one of the following options if you are relying on RegDisableReflectionKey functions to disable registry reflection:

-   Create keys in both views explicitly during installation
-   Move the keys out of the scope of reflected keys
-   Use platform-specific subkeys (like x86, amd64 and ia64) to separate bitness-specific data

## Links to Other Resources

-   [Registry Reflection article](../winprog64/registry-reflection.md)
-   [Redirected keys list within Registry Redirector article](../winprog64/registry-redirector.md)
-   [Best Practices for Wow64](/windows-hardware/drivers/display/microsoft-windows-vista-display-driver-64-bit-issues)

> [!Note]  
> These resources may not be available in some languages and countries/regions.

 

 

 
