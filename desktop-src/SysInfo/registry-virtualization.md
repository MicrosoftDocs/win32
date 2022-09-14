---
description: Registry virtualization is an application compatibility technology that enables registry write operations that have global impact to be redirected to per-user locations.
ms.assetid: dace2f65-df60-419a-8be8-ab60668e6396
title: Registry Virtualization
ms.topic: article
ms.date: 05/31/2018
---

# Registry Virtualization

*Registry virtualization* is an application compatibility technology that enables registry write operations that have global impact to be redirected to per-user locations. This redirection is transparent to applications reading from or writing to the registry. It is supported starting with Windows Vista.

This form of virtualization is an interim application compatibility technology; Microsoft intends to remove it from future versions of the Windows operating system as more applications are made compatible with Windows Vista and later versions of Windows. Therefore, it is important that your application does not become dependent on the behavior of registry virtualization in the system.

Virtualization is intended only to provide compatibility for existing applications. Applications designed for Windows Vista and later versions of Windows should not write to sensitive system areas, nor should they rely on virtualization to remedy any problems. When updating existing code to run on Windows Vista and later versions of Windows, developers should ensure that applications only store data in per-user locations or in computer locations within %alluserprofile% that properly use an access control list (ACL).

For more information about building UAC-compliant applications, see the [UAC Developer Guide](/previous-versions/dotnet/articles/aa480150(v=msdn.10)).

## Virtualization Overview

Prior to Windows Vista, applications were typically run by administrators. As a result, applications could freely access system files and registry keys. If these applications were run by a standard user, they would fail due to insufficient access rights. Windows Vista and later versions of Windows improve application compatibility for these applications by automatically redirecting these operations. For example, registry operations to the global store (**HKEY\_LOCAL\_MACHINE\\Software**) are redirected to a per-user location within the user's profile known as the *virtual store* (**HKEY\_USERS\\\<User SID\>\_Classes\\VirtualStore\\Machine\\Software**).

Registry virtualization can be broadly classified into the following types:

<dl> <dt>

<span id="Open_Registry_Virtualization"></span><span id="open_registry_virtualization"></span><span id="OPEN_REGISTRY_VIRTUALIZATION"></span>Open Registry Virtualization
</dt> <dd>

If the caller does not have write access to a key and attempts to open the key, the key is opened with the maximum allowed access for that caller.

If the REG\_KEY\_DONT\_SILENT\_FAIL flag is set for the key, the operation fails and the key is not opened. For more information, see "Controlling Registry Virtualization" later in this topic.

</dd> <dt>

<span id="Write_Registry_Virtualization"></span><span id="write_registry_virtualization"></span><span id="WRITE_REGISTRY_VIRTUALIZATION"></span>Write Registry Virtualization
</dt> <dd>

If the caller does not have write access to a key and attempts to write a value to it or create a subkey, the value is written to the virtual store.

For example, if a limited user attempts to write a value to the following key: **HKEY\_LOCAL\_MACHINE\\Software**\\*AppKey1*, virtualization redirects the write operation to **HKEY\_USERS\\\<User SID\>\_Classes\\VirtualStore\\Machine\\Software**\\*AppKey1*.

</dd> <dt>

<span id="Read_Registry_Virtualization"></span><span id="read_registry_virtualization"></span><span id="READ_REGISTRY_VIRTUALIZATION"></span>Read Registry Virtualization
</dt> <dd>

If the caller reads from a key that is virtualized, the registry presents a merged view of both the virtualized values (from the virtual store) and the non-virtual values (from the global store) to the caller.

For example, suppose **HKEY\_LOCAL\_MACHINE\\Software**\\*AppKey1* contains two values V1 and V2 and that a limited user writes a value V3 to the key. When the user attempts to read values from this key, the merged view includes values V1 and V2 from the global store and value V3 from the virtual store.

Note that virtual values take precedence over global values when present. In the example above, even if the global store had value V3 under this key, the value V3 would still be returned to the caller from the virtual store. If V3 were to be deleted from the virtual store, then V3 would be returned from the global store. In other words, if V3 were to be deleted from **HKEY\_USERS\\\<User SID\>\_Classes\\VirtualStore\\Machine\\Software**\\*AppKey1* but **HKEY\_LOCAL\_MACHINE\\Software**\\*AppKey1* had a value V3, then that value would be returned from the global store.

</dd> </dl>

## Registry Virtualization Scope

Registry virtualization is enabled only for the following:

-   32-bit interactive processes.
-   Keys in **HKEY\_LOCAL\_MACHINE\\Software**.
-   Keys that an administrator can write to. (If an administrator cannot write to a key, then the application would have failed on previous versions of Windows even if it was run by an administrator.)

Registry virtualization is disabled for the following:

-   64-bit processes.
-   Processes that are not interactive, such as services.

    Note that using the registry as an inter-process communication (IPC) mechanism between a service (or any other process that does not have virtualization enabled) and an application will not work correctly if the key is virtualized. For instance, if an antivirus service updates its signature files based on a value set by an application, the service will never update its signature files because the service reads from the global store but the application writes to the virtual store.

-   Processes that impersonate a user. If a process attempts an operation while impersonating a user, that operation will not be virtualized.
-   Kernel-mode processes such as drivers.
-   Processes that have **requestedExecutionLevel** specified in their manifests.
-   Keys and subkeys of **HKEY\_LOCAL\_MACHINE\\Software\\Classes**, **HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows**, and **HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows NT**.

## Controlling Registry Virtualization

In addition to controlling virtualization at an application level by using **requestedExecutionLevel** in the manifest, an administrator can enable or disable virtualization on a per-key basis for keys in **HKEY\_LOCAL\_MACHINE\\Software**. To do this, use the Reg.exe command-line utility FLAGS option with the flags listed in the following table.



| Flag                         | Meaning                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| REG\_KEY\_DONT\_SILENT\_FAIL | This flag disables open registry virtualization. If this flag is set and an open operation fails on a key that has virtualization enabled, the registry does not attempt to reopen the key. If this flag is clear, the registry attempts to reopen the key with MAXIMUM\_ALLOWED access instead of the requested access.                                                                   |
| REG\_KEY\_DONT\_VIRTUALIZE   | This flag disables write registry virtualization. If this flag is set and a create key or set value operation fails because the caller does not have sufficient access right to the parent key, the registry fails the operation. If this flag is clear, the registry attempts to write the key or value in the virtual store. The caller must have the KEY\_READ right on the parent key. |
| REG\_KEY\_RECURSE\_FLAG      | If this flag is set, registry virtualization flags are propagated from the parent key. If this flag is clear, registry virtualization flags are not propagated. Changing this flag affects only new descendent keys created after the flag is changed. It does not set or clear these flags for existing descendent keys.                                                                  |



 

The following example shows the use of the Reg.exe command-line utility with the FLAGS option to query the state of the virtualization flags for a key.

``` syntax
C:\>reg flags HKLM\Software\AppKey1 QUERY

HKEY_LOCAL_MACHINE\Software\AppKey1

        REG_KEY_DONT_VIRTUALIZE: CLEAR
        REG_KEY_DONT_SILENT_FAIL: CLEAR
        REG_KEY_RECURSE_FLAG: CLEAR

The operation completed successfully.
```

Whenever auditing is enabled on a key that is being virtualized, a new virtualization audit event is generated to indicate that the key is being virtualized (addition to the usual audit events). Administrators can use this information to monitor the status of virtualization on their systems.

## Related topics

<dl> <dt>

[Getting Started with User Account Control](/previous-versions/windows/it-pro/windows-vista/cc507861(v=technet.10))
</dt> <dt>

[Understanding and Configuring User Account Control](/previous-versions/windows/it-pro/windows-vista/cc709628(v=ws.10))
</dt> <dt>

[Developer Best Practices and Guidelines for Applications in a Least Privileged Environment](/previous-versions/dotnet/articles/aa480150(v=msdn.10))
</dt> </dl>

 

 
