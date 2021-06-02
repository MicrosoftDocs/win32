---
description: The HKEY\_CLASSES\_ROOT (HKCR) key contains file name extension associations and COM class registration information such as ProgIDs, CLSIDs, and IIDs. It is primarily intended for compatibility with the registry in 16-bit Windows.
ms.assetid: b404875f-11e1-48f2-98d2-0378a0646ed3
title: HKEY_CLASSES_ROOT Key
ms.topic: article
ms.date: 05/31/2018
---

# HKEY\_CLASSES\_ROOT Key

The **HKEY\_CLASSES\_ROOT** (**HKCR**) key contains file name extension associations and COM class registration information such as [ProgIDs](../com/-progid--key.md), [CLSIDs](../com/clsid-key-hklm.md), and [IIDs](../com/interface-key.md). It is primarily intended for compatibility with the registry in 16-bit Windows.

Class registration and file name extension information is stored under both the **HKEY\_LOCAL\_MACHINE** and **HKEY\_CURRENT\_USER** keys. The **HKEY\_LOCAL\_MACHINE\\Software\\Classes** key contains default settings that can apply to all users on the local computer. The **HKEY\_CURRENT\_USER\\Software\\Classes** key contains settings that apply only to the interactive user. The **HKEY\_CLASSES\_ROOT** key provides a view of the registry that merges the information from these two sources. **HKEY\_CLASSES\_ROOT** also provides this merged view for applications designed for previous versions of Windows.

The user-specific settings have priority over the default settings. For example, the default setting might specify a particular application to handle .doc files. But a user can override this setting by specifying a different application in the registry.

Registry functions such as [**RegOpenKeyEx**](/windows/desktop/api/Winreg/nf-winreg-regopenkeyexa) or [**RegQueryValueEx**](/windows/desktop/api/Winreg/nf-winreg-regqueryvalueexa) allow you to specify the **HKEY\_CLASSES\_ROOT** key. When you call these functions from a process running in the interactive user account, the system merges the default settings in **HKEY\_LOCAL\_MACHINE\\Software\\Classes** with the interactive user's settings at **HKEY\_CURRENT\_USER\\Software\\Classes**. For more information on how these settings are merged, see [Merged View of HKEY\_CLASSES\_ROOT](merged-view-of-hkey-classes-root.md).

To change the settings for the interactive user, store the changes under **HKEY\_CURRENT\_USER\\Software\\Classes** rather than **HKEY\_CLASSES\_ROOT**.

To change the default settings, store the changes under **HKEY\_LOCAL\_MACHINE\\Software\\Classes**. If you write keys to a key under **HKEY\_CLASSES\_ROOT**, the system stores the information under **HKEY\_LOCAL\_MACHINE\\Software\\Classes**. If you write values to a key under **HKEY\_CLASSES\_ROOT**, and the key already exists under **HKEY\_CURRENT\_USER\\Software\\Classes**, the system will store the information there instead of under **HKEY\_LOCAL\_MACHINE\\Software\\Classes**.

Processes running in a security context other than that of the interactive user should not use the **HKEY\_CLASSES\_ROOT** key with the registry functions. Instead, such processes can explicitly open the **HKEY\_LOCAL\_MACHINE\\Software\\Classes** key to access the default settings. To open a registry key that merges the contents of **HKEY\_LOCAL\_MACHINE\\Software\\Classes** with the settings for a specified user, these processes can call the [**RegOpenUserClassesRoot**](/windows/desktop/api/Winreg/nf-winreg-regopenuserclassesroot) function. For example, a thread that is [impersonating](/windows/desktop/SecAuthZ/client-impersonation) a client can call **RegOpenUserClassesRoot** if it needs to retrieve a merged view for the client being impersonated. Note that **RegOpenUserClassesRoot** fails if the user profile for the specified user has not been loaded. The system automatically loads the profile for the interactive user when logging on. For other users, you need to call the [**LoadUserProfile**](/windows/win32/api/userenv/nf-userenv-loaduserprofilea) function to explicitly load the user's profile.

If an application is run with administrator rights and User Account Control is disabled, the COM runtime ignores the per-user COM configuration and accesses only the per-machine COM configuration. Applications that require administrator rights should register dependent COM objects during installation to the per-machine COM configuration store (**HKEY\_LOCAL\_MACHINE\\Software\\Classes**). For more information, see [AC: UAC: COM Per-User Configuration](/previous-versions/bb756926(v=msdn.10)).

**Windows Server 2003 and Windows XP/2000:** Applications can register dependent COM objects to either the per-machine or per-user COM configuration store (**HKEY\_LOCAL\_MACHINE\\Software\\Classes** or **HKEY\_CURRENT\_USER\\Software\\Classes**).

## Related topics

<dl> <dt>

[HKEY\_CLASSES\_ROOT (Resource Kit Registry Reference)](/previous-versions/windows/it-pro/windows-server-2003/cc739822(v=ws.10))
</dt> </dl>

 

 
