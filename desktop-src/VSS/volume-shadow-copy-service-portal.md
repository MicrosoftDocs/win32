---
description: Back up volumes while applications on a system continue to write to the volumes. Minimize application downtime by quickly creating a snapshot (shadow copy) of a volume that duplicates all data. Perform multivolume backup.
ms.assetid: 1eca1e3e-fc86-44b5-b3c4-bcee41bc5a43
title: Volume Shadow Copy Service
ms.topic: article
ms.date: 05/31/2018
---

# Volume Shadow Copy Service

## Purpose

The Volume Shadow Copy Service (VSS) is a set of COM interfaces that implements a framework to allow volume backups to be performed while applications on a system continue to write to the volumes.

For an introduction to VSS for system administrators, see [Volume Shadow Copy Service](/windows-server/storage/file-server/volume-shadow-copy-service) in the TechNet Library.

## Run-time requirements

VSS is supported on Microsoft Windows XP and later. For information about run-time requirements for a particular programming element, see the Requirements section of the documentation for that element.

All 32-bit VSS applications (requesters, providers, and writers) must run as native 32-bit or 64-bit applications. Running them under WOW64 is not supported. For more information, see [Supported Configurations and Restrictions](usage-conventions.md).

**Windows Server 2003 and Windows XP:** Running 32-bit VSS requesters under WOW64 is supported, but not for system-state backups. Running 32-bit VSS providers and writers under WOW64 is not supported. Support for running 32-bit requesters under WOW64 was removed in Windows Vista and subsequent versions.

> [!Note]  
> A shadow copy that was created on Windows Server 2003 R2 or Windows Server 2003 cannot be used on a computer that is running Windows Server 2008 R2 or Windows Server 2008. A shadow copy that was created on Windows Server 2008 R2 or Windows Server 2008 cannot be used on a computer that is running Windows Server 2003. However, a shadow copy that was created on Windows Server 2008 can be used on a computer that is running Windows Server 2008 R2, and vice versa.

 

## In this section



| Topic                                                          | Description                                                                                                                         |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [Overview](volume-shadow-copy-service-overview.md)<br/> | Describes the VSS object model, backup and restore strategies, and how to create VSS providers, requesters, and writers.<br/> |
| [Reference](volume-shadow-copy-reference.md)<br/>       | Describes VSS classes, data types, enumerations, functions, interfaces, and structures.<br/>                                  |



 

## Additional resources



|   Resource                                 |   Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows Vista and later            | VSS is available in the Microsoft Windows Software Development Kit (SDK). You can install the SDK for Windows 7 and Windows Server 2008 R2 from the [Windows Download Center](https://www.microsoft.com/download/details.aspx?id=8279). You can also download the [ISO version](https://www.microsoft.com/download/details.aspx?id=8442) of the SDK from the Windows Download Center. Previous versions of the SDK can be downloaded from the [Windows SDK Download Page](https://msdn.microsoft.com/windows/bb980924.aspx). |
| Windows Server 2003 and Windows XP | VSS is available in the Volume Shadow Copy Service 7.2 SDK, which you can download from the [Windows Download Center](https://www.microsoft.com/download/details.aspx?id=23490). Note that the 64-bit vssapi.lib files in the directories under the Win2003\\Obj directory can be used for the 64-bit versions of Windows Server 2003 and Windows XP.                                                                                                                                                                 |



 

 

 
