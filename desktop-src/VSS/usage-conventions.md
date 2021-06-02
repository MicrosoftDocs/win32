---
description: When developing your own VSS application, you should observe the following guidelines and restrictions.
ms.assetid: d4edc16c-f768-4095-9b2a-b706f19f9e61
title: VSS Application Compatibility
ms.topic: article
ms.date: 05/31/2018
---

# VSS Application Compatibility

When developing your own VSS application, you should observe the following guidelines and restrictions. You may find it helpful to refer to the sample code for VSS requesters, providers, and writers that is provided in the Microsoft Windows Software Development Kit (SDK).

> [!Note]  
> The Windows SDK can be used to develop VSS applications only for Windows Vista and later Windows operating system versions. It cannot be used to develop VSS requesters, providers, or writers for Windows Server 2003 R2, Windows Server 2003, or Windows XP.

 

**Windows Server 2003 R2, Windows Server 2003 and Windows XP:** VSS is available in the Volume Shadow Copy Service 7.2 SDK, which you can download from [https://www.microsoft.com/download/details.aspx?id=23490](https://www.microsoft.com/download/details.aspx?id=23490). Note that the 64-bit vssapi.lib files in the directories under the Win2003\\Obj directory can be used for the 64-bit versions of Windows Server 2003 R2, Windows Server 2003, and Windows XP. This SDK also provides sample code for VSS requesters, providers, and writers.

## Compiling VSS Applications

When developing a requester, such as a backup application:

-   Include the following headers: <dl> Vss.h  
    VsWriter.h  
    VsBackup.h  
    </dl>
-   Link the following library: <dl> VssApi.Lib  
    </dl>

When developing a writer:

-   Include the following headers: <dl> Vss.h  
    VsWriter.h  
    </dl>
-   Link the following library: <dl> VssApi.lib  
    </dl>

## Supported Configurations and Restrictions

The following list describes supported configurations and restrictions:

-   VSS is provided and supported on versions of the Windows operating system beginning with Windows XP.
-   The following table summarizes compatibility information across Windows versions. Note that if a VSS application is "compiled for" a specified Windows version, this means that the application was compiled using the header files and libraries that are specific to that version.

    > [!Note]  
    > Hardware providers will run only on Windows server operating system versions. They will not run on Windows client operating system versions.

     

    > [!Note]  
    > In the following tables, Windows Server 2008 with Service Pack 2 (SP2) should be considered the same as Windows Server 2008. For more information about Windows Server 2008 with SP2, see <https://go.microsoft.com/fwlink/p/?linkid=178730>. Windows Server 2003 R2 should be considered the same as Windows Server 2003.

     

    > [!Note]  
    > If a VSS application is compiled for Windows Server 2003 or later, it will also run on later versions of Windows.

     

    

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>VSS requesters, writers, and providers compiled for</th>
    <th>Will run on</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td>Windows Server 2008 R2 (64-bit), Windows 7 (64-bit), Windows Server 2008 (64-bit) and Windows Vista (64-bit)</td>
    <td>Windows Server 2008 R2 (64-bit), Windows 7 (64-bit), Windows Server 2008 (64-bit) and Windows Vista (64-bit)</td>
    </tr>
    <tr class="even">
    <td>Windows Server 2008 R2 (32-bit), Windows 7 (32-bit), Windows Server 2008 (32-bit) and Windows Vista (32-bit)</td>
    <td>Windows Server 2008 R2 (32-bit), Windows 7 (32-bit), Windows Server 2008 (32-bit) and Windows Vista (32-bit)</td>
    </tr>
    <tr class="odd">
    <td>Windows Server 2003 (64-bit)</td>
    <td>Windows Server 2008 R2 (64-bit), Windows 7 (64-bit), Windows Server 2008 (64-bit), Windows Vista (64-bit), and Windows Server 2003 (64-bit)</td>
    </tr>
    <tr class="even">
    <td>Windows Server 2003 (32-bit)</td>
    <td>Windows Server 2008 R2 (32-bit), Windows 7 (32-bit), Windows Server 2008 (32-bit), Windows Vista (32-bit), and Windows Server 2003 (32-bit)
    <blockquote>
    [!Note]<br />
    Requesters will also run on Windows Server 2003 (64-bit).
    </blockquote>
    <br/></td>
    </tr>
    <tr class="odd">
    <td>Windows XP 64-Bit Edition</td>
    <td>Windows Server 2003 (64-bit) and Windows XP 64-Bit Edition</td>
    </tr>
    <tr class="even">
    <td>Windows XP (32-bit)</td>
    <td>Windows XP (32-bit)</td>
    </tr>
    </tbody>
    </table>

    

     

    

    | To compile a VSS requester, writer, or provider for        | Use                                                                                                                                       |
    |------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
    | Windows Server 2008 R2 or Windows 7                        | Windows SDK for Windows 7 (Available from the [Windows Download Center](https://www.microsoft.com/download/details.aspx?id=8279).)                |
    | Windows Server 2008 or Windows Vista                       | Windows SDK for Windows Server 2008 (Available from the [Windows SDK Developer Center](https://msdn.microsoft.com/windows/bb980924.aspx).) |
    | Windows Server 2003 R2, Windows Server 2003, or Windows XP | [Volume Shadow Copy Service 7.2 SDK](https://www.microsoft.com/download/details.aspx?id=23490)                                                      |

    

     

-   All 32-bit VSS applications (requesters, providers, and writers) must run as native 32-bit or 64-bit applications. Running them under WOW64 is not supported.

    **Windows Server 2003 and Windows XP:** Running 32-bit VSS requesters under WOW64 is supported, but not for system-state backups. Running 32-bit VSS providers and writers under WOW64 is not supported. Support for running 32- bit requesters under WOW64 was removed in Windows Vista and subsequent versions.

-   A shadow copy that was created on Windows Server 2003 R2 or Windows Server 2003 cannot be used on a computer that is running Windows Server 2008 R2 or Windows Server 2008. A shadow copy that was created on Windows Server 2008 R2 or Windows Server 2008 cannot be used on a computer that is running Windows Server 2003. However, a shadow copy that was created on Windows Server 2008 can be used on a computer that is running Windows Server 2008 R2, and vice versa.
-   To support shadow copies, a system running VSS must have at least one NTFS file system. This file system will host the shadow copy's "diff area." For more information, see [System Provider](providers.md).
-   Given the presence of one NTFS file system, and given the appropriate choice of context (see [Shadow Copy Context Configurations](shadow-copy-context-configurations.md)), any supported local file system can be shadow copied.
-   You can make shadow copies only for locally mounted file systems. Remote shares and other cross-mounted file systems cannot be shadow copied by the system that mounts them. These file systems can be shadow copied only by the systems that serve out the file systems.
-   Writers and requesters should specify only local resources. Local resources are sets of files whose absolute path starts with a drive letter, and the drive letter cannot be associated with a mounted folder on a remote share.
-   The maximum number is of software shadow copies for each volume is 512. However, by default you can only maintain 64 shadow copies that are used by the Shadow Copies of Shared Folders feature. To change the limit for the Shadow Copies of Shared Folders feature, use the [MaxShadowCopies](../backup/registry-keys-for-backup-and-restore.md) registry key.
-   The Backup Components infrastructure does not support backing up cluster resources as writer components. To back up cluster resources, applications should assume that the path is local to a specified particular cluster node.
-   [!Note]  
    > Microsoft does not provide developer or IT professional technical support for implementing online system state restores on Windows (all releases).

     

    When backing up and recovering system state, the recommended strategy is to back up and recover the system and boot volumes in addition to the files enumerated by the system state writers.

    > [!Note]  
    > System state writers are writers that have the [**VSS\_USAGE\_TYPE**](/windows/win32/api/VsWriter/ne-vswriter-vss_usage_type) attribute set to either VSS\_UT\_BOOTABLESYSTEMSTATE or VSS\_UT\_SYSTEMSERVICE.

     

 

 
