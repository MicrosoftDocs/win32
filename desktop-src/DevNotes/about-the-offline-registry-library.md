---
description: The offline registry library is used to modify a registry hive outside of the active system registry.
ms.assetid: 61db2804-1b67-473f-8dd7-6be6c6a7184e
title: About the Offline Registry Library
ms.topic: article
ms.date: 05/31/2018
---

# About the Offline Registry Library

The offline registry library is used to modify a registry hive outside of the active system registry.

The offline registry library is intended for registry update scenarios such as servicing an operating system image. The offline registry functions provide the following capabilities that are not available with the standard registry functions:

-   The offline registry functions can be used to modify a registry hive in any supported registry format. The standard registry functions can make changes only to an active registry hive and the changes must be compatible with the version of Windows running on the system.
-   The offline registry library requires only read access to open a registry hive file and write access to save the file. No other access checks are performed on objects in the hive, making it possible to modify the hive with standard user privileges. With the standard registry functions, loading a hive into the active registry is a privileged operation that requires administrative access.

The offline registry functions should not be used as a substitute for the system registry functions for the following reasons:

-   It is impossible to share registry hives between processes using the offline registry functions.
-   The offline registry functions use simple locking that can lead to serious performance degradation for multithreaded applications.
-   Changes made with the offline registry functions are not saved until the [**ORSaveHive**](orsavehive.md) function is called.

Applications should not use the offline registry functions to bypass the security requirements of the system registry. To load a hive, an application running without the special privileges required by the [RegLoadKey](/windows/win32/api/winreg/nf-winreg-regloadkeya) function can use the [RegLoadAppKey](/windows/win32/api/winreg/nf-winreg-regloadappkeya) function.

**Windows Server 2003 and Windows XP:** The [RegLoadAppKey](/windows/win32/api/winreg/nf-winreg-regloadappkeya) function is not supported.

An *offline registry hive* is a registry hive that has been loaded into memory using the offline registry functions. To create an empty offline registry hive, use the [**ORCreateHive**](orcreatehive.md) function. To modify an existing registry hive, use the [RegSaveKey](/windows/win32/api/winreg/nf-winreg-regsavekeya) or [RegSaveKeyEx](/windows/win32/api/winreg/nf-winreg-regsavekeyexa) function to save a hive from the active system registry to a file, and then use the [**OROpenHive**](oropenhive.md) function to open the file.

The [**ORCreateHive**](orcreatehive.md) and [**OROpenHive**](oropenhive.md) functions return a handle to the root key of the offline registry hive. This handle can be used like a handle to any other key in the offline registry hive with the following exceptions: the [**ORCreateKey**](orcreatekey.md) and [**OROpenKey**](oropenkey.md) functions cannot be used to return a handle to the root key; the [**ORCloseKey**](orclosekey.md) function cannot be used to close the root key; and the [**ORDeleteKey**](ordeletekey.md) function cannot be used to delete the root key. In all of these cases, the function fails with **ERROR\_INVALID\_PARAMETER**.

Use the [**ORCreateKey**](orcreatekey.md) function to add keys to an open offline registry hive and the [**ORSetValue**](orsetvalue.md) function to set the keys' values. The offline registry library supports other basic registry operations such as enumerating, retrieving, and deleting keys and values, and setting key attributes such as security and virtualization behavior. For a list of functions, see [Offline Registry Library Functions](offline-registry-library-functions.md).

To save changes made to an open offline registry hive, use the [**ORSaveHive**](orsavehive.md) function to save the hive to a file. (The changes do not persist unless **ORSaveHive** is called.) After saving the hive, use the [**ORCloseHive**](orclosehive.md) function to close the hive and free resources associated with it.

An offline registry hive is validated only when it is opened using the [**OROpenHive**](oropenhive.md) function. If the hive is corrupt, the operation simply fails; no attempt is made to repair the hive. Access checks on objects in the hive are not performed until the hive is loaded into an active registry with the [RegLoadKey](/windows/win32/api/winreg/nf-winreg-regloadkeya) function.

The offline registry functions do not support the [predefined keys](../sysinfo/predefined-keys.md).

All key and value name strings passed to offline registry functions must be Unicode.

## Related topics

<dl> <dt>

[Offline Registry Library\_Functions](offline-registry-library-functions.md)
</dt> </dl>

 

 
