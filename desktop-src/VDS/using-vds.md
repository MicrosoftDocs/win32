---
description: Using VDS
ms.assetid: aa4be499-625d-4dbd-828c-4a55ff2dba2c
title: Using VDS
ms.topic: article
ms.date: 05/31/2018
---

# Using VDS

\[Beginning with Windows 8 and Windows Server 2012, the [Virtual Disk Service](virtual-disk-service-portal.md) COM interface is superseded by the [Windows Storage Management API](/previous-versions/windows/desktop/stormgmt/windows-storage-management-api-portal).\]

VDS supplies an interface for scripting and GUI development that can simplify the activities that are performed by a Windows server administrator who manages a heterogeneous set of storage systems, migrating data across different hardware configurations over time. If you are unfamiliar with the objects that are used in VDS development, see the [VDS Object Model](vds-object-model.md).

A few points before you begin:

-   While VDS includes a software provider, you must purchase a hardware provider and the associated hardware separately to take advantage of the hardware provider operations. For installation instructions, see the documentation that is provided by the hardware manufacturer.
-   Some operations require NTFS-formatted volumes. For example, when you mount a volume on an existing directory, the volume that contains the directory must be formatted with NTFS. Other file systems do not support this operation. For information about operations that require NTFS, see each method page in [VDS Reference](vds-reference.md).

## Programming Languages

Use any programming language that is suitable for development with COM, such as the C language or C++.

## Security

Windows Firewall is enabled by default. This can cause authentication to fail for callback interfaces, such as [**IVdsAdviseSink**](/windows/desktop/api/Vds/nn-vds-ivdsadvisesink), that can be executed remotely. If Windows Firewall is enabled on either the client or the server, you must add Remote Volume Management to the **Exceptions** tab in Windows Firewall.

**Windows Server 2003:** In Windows Server 2003 with Service Pack 2 (SP2) and Windows Server 2003 with Service Pack 1 (SP1), if Windows Firewall is enabled on either the client or the server and if the server is configured to use NTLM authentication, you must add the following settings to the **Exceptions** tab in Windows Firewall for the appropriate computer.

| Computer                 | Exceptions settings                                                                 |
|--------------------------|-------------------------------------------------------------------------------------|
| Client computer (local)  | Dmremote.exe<br/> Mmc.exe<br/> Vdsldr.exe<br/> TCP 135<br/> |
| Server computer (remote) | Dmadmin.exe<br/> Vds.exe<br/> TCP 135<br/>                        |



 

Note that Windows Firewall is not enabled by default until Windows Server 2003 with SP1.

An application that is using VDS must run under the Backup Operator or Administrators group account. Without the appropriate privilege, an application can create a service loader object, but the object will not load VDS. Instead, it returns an error indicating that access to VDS is denied.

If the network uses NTLM authentication, the client computer should allow anonymous access. In this case, if the client computer is running a Windows Server operating system, anonymous access is enabled by default. If it is running a Windows Client operating system, anonymous access must be enabled using Dcomcnfg.exe.

## Configuration and Query Operations

Configuration and query operations are scoped by the most relevant computer, provider, subsystem, or pack. Queries traverse only one provider or one level of the binding hierarchy. To build a full view, the caller must query across and down each level. The following list includes examples:

-   To view all disks on a computer, callers must query across all software providers for the disks that are claimed by those providers.
-   To determine which disks contribute to a software-stacked volume, callers first determine the contributing plexes and then query for the disk extents for each plex.
-   To view all the drives that are attached to a given subsystem, callers must query the subsystem.
-   To view all the LUNs that are exposed by a given subsystem, callers must query the subsystem.
-   To view all storage on a SAN or a cluster, callers must query each computer for all hardware providers, query each provider for all subsystems, and then query each subsystem.

While each individual query will not return duplicates, repeated queries across computers or across providers can accumulate duplicates. Callers must implement any filtering. Note also that SAN management applications can use the Active Directory or a repository to persist configuration information; it might not be necessary to query each computer.

## Related topics

<dl> <dt>

[Virtual Disk Service](virtual-disk-service-portal.md)
</dt> <dt>

[VDS Object Model](vds-object-model.md)
</dt> <dt>

[VDS Reference](vds-reference.md)
</dt> </dl>

 

