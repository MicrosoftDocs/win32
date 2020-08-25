---
title: Registry Reflection
description: The registry redirector isolates 32-bit and 64-bit applications by providing separate logical views of certain portions of the registry on WOW64. However, the values of some registry keys must be the same in both the 32-bit and 64-bit views.
ms.assetid: eac9038b-9f59-4ac7-8974-f94a4a62a257
keywords:
- registry reflection 64-bit Windows Programming
- reflection 64-bit Windows Programming
ms.topic: article
ms.date: 05/31/2018
---

# Registry Reflection

\[The information in this topic applies to Windows Server 2008, Windows Vista, Windows Server 2003, and Windows XP. Starting with Windows 7 and Windows Server 2008 R2, WOW64 no longer uses registry reflection and formerly reflected keys are shared instead. For more information, see [Registry Keys Affected by WOW64](shared-registry-keys.md).\]

The [registry redirector](registry-redirector.md) isolates 32-bit and 64-bit applications by providing separate logical views of certain portions of the registry on WOW64. However, the values of some registry keys must be the same in both the 32-bit and 64-bit views.

The process of *registry reflection* copies registry keys and values between two registry views to keep them synchronized. Each view has a separate physical copy of each reflected registry key, one for the 32-bit registry view and the other for the 64-bit registry view.

A reflected key is copied when a key is closed by calling [**RegCloseKey**](/windows/desktop/api/winreg/nf-winreg-regclosekey). Note that this gives rise to a possible race condition: if more than one process changes the reflected key, the last **RegCloseKey** call determines the key's final value.

The reflector copies COM activation data for Local servers between the views, but it does not copy in-process data because 32/64 in-process data mixing is not permitted on 64-bit Windows.

Reflection is not enabled for shared registry keys or for registry keys that are not redirected. For example, reflection is not enabled for the **HKEY\_LOCAL\_MACHINE\\System** key. For a list of registry keys that are redirected, shared, or reflected, see [Registry Keys Affected by WOW64](shared-registry-keys.md).

Registry reflection uses a "last writer wins" policy as illustrated in the following example:

-   After a clean installation of 64-bit Windows, 64-bit Wordpad.exe is registered to handle .doc files. The reflector copies the .doc registration from the 64-bit registry view into the 32-bit registry view.
-   An administrator installs 32-bit Office, which registers 32-bit Winword.exe to handle .doc files in the 32-bit registry view. The registry reflector copies this information into the 64-bit registry view, so both 32-bit and 64-bit applications launch the 32-bit version of Winword.exe for .doc files.
-   An administrator installs 64-bit Office, which registers 64-bit Winword.exe to handle .doc files in the 64-bit registry view. The registry reflector copies this information into the 32-bit registry, so both 32-bit and 64-bit applications launch the 64-bit version of Winword.exe for .doc files.

Therefore, the file association information is preserved for the most recently installed application.

It can be useful for 32-bit and 64-bit applications to share specific registry key values that are normally written to separate registry views. For example, a 32-bit OLE server that can serve requests from both 32-bit and 64-bit clients could make its 32-bit registry data available to the 64-bit view of the system registry.

When a component writes data in the system registry, WOW64 analyzes the information and makes a copy of the data in the alternate view of the registry when appropriate. Typically, this process keeps two separate physical copies of the same registry keys in both views in the registry, and is called registry reflection or registry mirroring.

Most of the keys under the classes root are in this category. Updates to the keys are reflected when the update completes and the handle to the key closes. In specific cases, writes to a key are not reflected if the key has some bitness dependency. For example, the 32-bit InprocServer32 key is not relevant for 64-bit applications, so the InprocServer32 key is not reflected to the 64-bit registry view. However, 64-bit applications can use the 32-bit LocalServer32 key and the LocalServer32 key gets reflected.

For **HKEY\_LOCAL\_MACHINE\\Software\\Classes\\CLSID** and **HKEY\_CURRENT\_USER\\Software\\Classes\\CLSID**, only CLSIDs that do not specify InprocServer32 or InprocHandler32 are reflected. Only LocalServer32 CLSIDs are reflected because they run out-of-process and can be activated by either 32- or 64-bit applications. InProcServer32 CLSIDs are not reflected because it is not possible to load a 32-bit DLL for execution in a 64-bit process, or a 64-bit DLL for execution in a 32-bit process.

For **HKEY\_LOCAL\_MACHINE\\Software\\Classes\\Appid** and **HKEY\_CURRENT\_USER\\Software\\Classes\\Appid**, the [DllSurrogate](../com/dllsurrogate.md) and [DllSurrogateExecutable]( ../com/dllsurrogateexecutable.md) registry values are not reflected if their value is an empty string.

To disable and enable registry reflection for a particular reflected key, use the [**RegDisableReflectionKey**](/windows/desktop/api/winreg/nf-winreg-regdisablereflectionkey) and [**RegEnableReflectionKey**](/windows/desktop/api/winreg/nf-winreg-regenablereflectionkey) functions. These functions do not affect keys that are not on the list of reflected keys earlier in this topic. Applications should disable reflection only for the registry keys that they create and not attempt to disable reflection for the predefined keys such as **HKEY\_LOCAL\_MACHINE** or **HKEY\_CURRENT\_USER**. To determine whether the keys on the reflection list have been disabled, use the [**RegQueryReflectionKey**](/windows/desktop/api/winreg/nf-winreg-regqueryreflectionkey) function.

Reflected keys should not be used in transacted registry operations. Writing to reflected keys during a transaction can cause the transaction to fail. For more information about transactions, see [Kernel Transaction Manager](/windows/desktop/Ktm/kernel-transaction-manager-portal).

## Related topics

<dl> <dt>

[Registry Redirector](registry-redirector.md)
</dt> <dt>

[Registry Reflection in Windows](/windows-hardware/drivers/display/microsoft-windows-vista-display-driver-64-bit-issues)
</dt> <dt>

[Registry Keys Affected by WOW64](shared-registry-keys.md)
</dt> </dl>

 

 