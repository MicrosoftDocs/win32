---
description: The Windows Registry Service supports a VSS writer, called the registry writer, which allows requesters to back up a system registry using data stored on a shadow copied volume.
ms.assetid: 94a45b04-0bdc-4211-bed0-caeabba774af
title: Registry Backup and Restore Operations Under VSS
ms.topic: article
ms.date: 03/03/2023
---

# Registry Backup and Restore Operations Under VSS

The Windows Registry Service supports a VSS writer, called the registry writer, which allows requesters to back up a system registry using data stored on a shadow copied volume. For more information about the registry writer, see [In-Box VSS Writers](in-box-vss-writers.md).

The registry writer performs in-place backups and restores of the registry. In addition, the registry writer reports only system hives; it does not report user hives.

**Windows Server 2003:** The registry writer uses an intermediate repository file (also known as a spit file) to store registry data. In addition, the registry writer reports system hives and user hives.

The writer ID for the registry writer is AFBAB4A2-367D-4D15-A586-71DBB18F8485.

**Windows XP:** There is no registry writer. The registry data is reported by the Bootable State writer, whose writer ID is F2436E37-09F5-41AF-9B2A-4CA2435DBFD5.

> [!Note]  
> Microsoft does not provide developer or IT professional technical support for implementing online system state restores on Windows (all releases). For information about using Microsoft-provided APIs and procedures to implement online system state restores, see the community resources available at the [MSDN Community Center](https://msdn.microsoft.com/community/default.aspx).

 

> [!Note]  
> The following information only applies to Windows Server 2003 and Windows XP.

 

## Registry Backup Using VSS

The registry writer will export and save active registry files in the locations defined by the key **HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Control**\\**hivelist**.

The names of the values under this registry entry identify the registry hive to be saved, and the value's data provides the file containing the file (the hive file). The hive files are specified with the following format: \\Device\\*HarddiskVolumeX*\\*path*\\*filename*.

For example, under **HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Control**\\**hivelist**, you might see **\\REGISTRY\\MACHINE\\SOFTWARE** = \\Device\\HarddiskVolume1\\Windows\\System32\\config\\SOFTWARE.

The registry writer ensures that hive files are saved to disk prior to its shadow copy.

When backing up the registry hives, a requester would replace \\Device\\*HarddiskVolumeX* with the [*device object*](vssgloss-d.md) string of the volume's shadow copy.

> [!Note]  
> You can convert the \\Device\\*HarddiskVolumeX* path to an equivalent Win32 path by using the [**QueryDosDevice**](/windows/win32/api/fileapi/nf-fileapi-querydosdevicew) function. For more information, see [Obtaining a File Name From a File Handle](../memory/obtaining-a-file-name-from-a-file-handle.md) or [Displaying Volume Path Names](../fileio/displaying-volume-paths.md).

 

## Registry Restore Using Non-VSS Win32 APIs

> [!Note]  
> Registry Restore is not supported on Windows Server 2016 and later.

For an online (safe mode or full operating system) restore, the subkeys in the **HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Control**\\**Session Manager**\\**PendingFileRenameOperations** registry key must be preserved.

The [**MoveFileEx**](/windows/win32/api/winbase/nf-winbase-movefileexa) and [**MoveFileTransacted**](/windows/win32/api/winbase/nf-winbase-movefiletransacteda) functions use this registry key to store information about files that were renamed by using the MOVEFILE\_DELAY\_UNTIL\_REBOOT value in the *dwFlags* parameter.

To preserve the contents of the **PendingFileRenameOperations** registry key, your backup application should call the [**RegLoadKey**](/windows/win32/api/winreg/nf-winreg-regloadkeya) function to connect the registry file to be restored to the active registry. Your backup application can then use the various registry functions to copy the desired keys and values into the loaded hive. After the copy is complete, the [**RegFlushKey**](/windows/win32/api/winreg/nf-winreg-regflushkey) and [**RegUnloadKey**](/windows/win32/api/winreg/nf-winreg-regunloadkeya) functions should be called.

For an offline (Windows Recovery Environment or Windows PE) restore, it is not necessary to honor the **PendingFileRenameOperations** registry key.

## Registry Restore Using Non-VSS Win32 APIs in Windows Server 2003

> [!Note]  
> The following information applies only to restore operations related to disaster recovery (also known as bare-metal recovery) that are performed in Windows Server 2003.

 

When restoring the registry, a backup application needs to move some of the subkeys from the current registry into the registry that is to be restored.

To do this, a backup application can call **RegLoadKey** to connect the registry file to be restored to the currently active registry. It can then use the various registry functions to copy the desired keys and values into the loaded hive. After the copy is complete, **RegFlushKey** and **RegUnloadKey** are called.

There is a registry key that indicates to a restore application (requester) the registry keys under **HKEY\_LOCAL\_MACHINE\\SYSTEM** that should not be overwritten at restore time:

**HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\BackupRestore\\KeysNotToRestore**

Part of the system state restore process involves restoring a previously backed-up registry.

Backup applications need to take special care when restoring the **HKEY\_LOCAL\_MACHINE\\SYSTEM** hive because the process of installing a temporary version of the Windows operating system will have established keys in the newly installed system hive whose values must survive the restore operation.

For example, when the replacement system has a network interface card different from the original system, restoration of the original keys for the previous card will lead to unpredictable results. This is because the Plug and Play service has detected and placed proper service and driver registry entries into the registry. These values must be preserved to properly boot after system restore.

This section describes how backup applications can discover which keys and files are to be preserved when executing a restore of the **HKEY\_LOCAL\_MACHINE\\SYSTEM** hive. In some cases, this will involve programmatically copying the keys from the newly installed installation hive into the hive to be restored. In other cases, ensuring that a product's registry keys are not replaced is as simple as specifying such keys in the product's INF configuration file.

Keys (and key data) that are to be preserved are enumerated in the **HKEY\_LOCAL\_MACHINE\\SYSTEM** hive under the

**HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\BackupRestore\\KeysNotToRestore**

key as sets of REG\_MULTI\_SZ strings (called *key strings* in this document).

A backup application (requester) must examine the values of these keys in the active registry and the newly restored registry because any application or service can add values at any time.

How key strings are to be interpreted by backup applications is determined by their terminal character:

1.  Key strings terminated with a backslash ('\\') are interpreted as subkeys. When such a substring is encountered, the backup application must preserve all data and all subordinate keys.

    For example, the following specifies that all subordinate keys and data are to be preserved across a restore operation:

    **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\dmio\\boot info\\**

    To this end, this key and all subordinate keys and data must be copied from the existing registry (that is, the one created by the installation of Windows) into the newly restored registry. This is called a *key replace* operation. This operation replaces the corresponding key in the restored registry.

2.  Key strings whose termination character is an asterisk ('\*') specifies that all subkeys should be merged. For example, the key string:

    **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\\***

    specifies that the services key in the existing registry (for example those created by the installation of Windows) must be merged into the restored registry. This is called a *key merge* operation, and if a subkey exists in both the existing hive and the restored hive, the key in the restored directory is preserved with the following exceptions:

    -   If the subkey in the existing hive contains a value named "start", and the subkey in the restored does not.
    -   If the subkey in both the existing and restored hive contain a value named "start", and its numeric value in the existing hive is less.

    The "start" value in the registry specifies when a service or driver will start and can have a numeric value from 0-4. The lower the value, the sooner in the boot process the service will start.

    If this key exists in both the existing and the restored directory, you must examine the value of the start key in each hive. If the value in the existing hive is lower than the value in the restored directory, the lower value must be preserved.

    Once again, this key is used to determine whether a service or driver is to be started at boot time, at system time, manually, automatically, or be disabled. The lower value represents an earlier start time. The earlier start time must be applied to the new registry to ensure that the service or drivers are started properly at the next boot.

3.  Key strings whose termination character is neither a backslash nor an asterisk are interpreted as registry values to be preserved.

    For example, the key string:

    **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\PendingFileRenameOperations**

    The mechanism by which keys can be preserved programmatically involves the Win32 registry API. For example, one algorithm is enumerated below:

    1.  Restore the backed-up system hive file to a file. For this example, let the name be System.reg.
    2.  Use **RegLoadKey** to load System.reg into **HKEY\_LOCAL\_MACHINE** under a temporary name. For example, one such name might be

        **HKEY\_LOCAL\_MACHINE\\TMP\_SYSTEM**

    3.  Enumerate the values in the **KeysNotToRestore** subkey from both of the registry copies and create a superset of the lists. Copy each such key from the existing

        **HKEY\_LOCAL\_MACHINE\\SYSTEM**

        key into the

        **HKEY\_LOCAL\_MACHINE\\TMP\_SYSTEM**

        key according to the semantics described above.

    4.  When complete use the **RegFlushKey** & **RegUnloadKey** entry points to save the

        **HKEY\_LOCAL\_MACHINE\\TMP\_SYSTEM**

        key back to System.reg.

    5.  Finally, use **RegReplaceKey** to specify that System.reg is to replace the

        **HKEY\_LOCAL\_MACHINE\\SYSTEM**

        hive file, SYSTEM.

 

 
