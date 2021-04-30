---
description: Applications can save part of the registry in a file and then load the contents of the file back into the registry.
ms.assetid: a71a564d-934a-46e8-b555-989a6fa82337
title: Registry Files
ms.topic: article
ms.date: 05/31/2018
---

# Registry Files

Applications can save part of the registry in a file and then load the contents of the file back into the registry. A registry file is useful when a large amount of data is being manipulated, when many entries are being made in the registry, or when the data is transitory and must be loaded and then unloaded again. Applications that back up and restore parts of the registry are likely to use registry files.

To save a key and its subkeys and values to a registry file, an application can call the [**RegSaveKey**](/windows/desktop/api/Winreg/nf-winreg-regsavekeya) or [**RegSaveKeyEx**](/windows/desktop/api/Winreg/nf-winreg-regsavekeyexa) function.

[**RegSaveKey**](/windows/desktop/api/Winreg/nf-winreg-regsavekeya) and [**RegSaveKeyEx**](/windows/desktop/api/Winreg/nf-winreg-regsavekeyexa) create the file with the archive attribute. The file is created in the current directory of the process for a local key, and in the %systemroot%\\system32 directory for a remote key.

Registry files have the following two formats: standard and latest. The standard format is the only format supported by Windows 2000. It is also supported by later versions of Windows for backward compatibility. [**RegSaveKey**](/windows/desktop/api/Winreg/nf-winreg-regsavekeya) creates files in the standard format.

The latest format is supported starting with Windows XP. Registry files that are created in this format cannot be loaded on Windows 2000. [**RegSaveKeyEx**](/windows/desktop/api/Winreg/nf-winreg-regsavekeyexa) can save registry files in either format by specifying either REG\_STANDARD\_FORMAT or REG\_LATEST\_FORMAT. Therefore, it can be used to convert registry files that use the standard format to the latest format.

To write the registry file back to the registry, an application can use the [**RegLoadKey**](/windows/desktop/api/Winreg/nf-winreg-regloadkeya), [**RegReplaceKey**](/windows/desktop/api/Winreg/nf-winreg-regreplacekeya), or [**RegRestoreKey**](/windows/desktop/api/Winreg/nf-winreg-regrestorekeya) functions as follows.

-   **RegLoadKey** loads registry data from a specified file into a specified subkey under **HKEY\_USERS** or **HKEY\_LOCAL\_MACHINE** on the calling application's computer or on a remote computer. The function creates the specified subkey if it does not already exist. After calling this function, an application can use the [**RegUnLoadKey**](/windows/desktop/api/Winreg/nf-winreg-regunloadkeya) function to restore the registry to its previous state.
-   [**RegReplaceKey**](/windows/desktop/api/Winreg/nf-winreg-regreplacekeya) replaces a key and all its subkeys and values in the registry with the data contained in a specified file. The new data takes effect the next time the system is started.
-   [**RegRestoreKey**](/windows/desktop/api/Winreg/nf-winreg-regrestorekeya) loads registry data from a specified file into a specified key on the calling application's computer or on a remote computer. This function replaces the subkeys and values below the specified key with the subkeys and values that follow the top-level key in the file.

The [**RegConnectRegistry**](/windows/desktop/api/Winreg/nf-winreg-regconnectregistrya) function establishes a connection to a predefined registry handle on another computer. An application uses this function primarily to access information from a remote registry on other machines in a network environment, which you can also do by using the Registry Editor. You might want to access a remote registry to back up a registry or regulate network access to it. Note that you must have appropriate permissions to access a remote registry using this function.

 

 



