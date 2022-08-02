---
description: Windows has APIs, components, and services that support your desktop apps in data access and storage.
ms.assetid: 8097ee91-f9f9-4e49-a501-5c54153eced8
title: Data Access and Storage
ms.topic: reference
ms.date: 02/06/2019
---

# Data Access and Storage

Windows has APIs, components, and services that support your desktop apps in data access and storage. They provide:

-   File and file system management.
-   Database access.
-   Support for the transfer, synchronization, and replication of data.
-   Access to XML, package, and log files.
-   Image mastering.
-   Backup support.

## In this section

| Topic | Description |
|-|-|
| [Background Intelligent Transfer Service](/windows/desktop/Bits/background-intelligent-transfer-service-portal) | Background Intelligent Transfer Service (BITS) transfers files (downloads or uploads) between a client and server and provides progress information related to the transfers. You can also download files from a peer.  |
| [Backup](/windows/desktop/Backup/backup) | Registry keys for backup and restore allow backup applications to communicate with other applications and services about backup and restore operations. The tape backup API enables backup applications to archive data to tape. The single-instance store (SIS) API enables backup applications to use the SIS architecture for maintaining duplicate files with a minimum of overhead. The raw encryption API enables backup and restore of encrypted files. |
| [Cloud Sync Engines](cfapi/cloud-files-api-portal.md) | Starting in Windows 10, version 1709, Windows provides the *cloud files API*. This API formalizes support for cloud sync engines, and handles tasks such as creating and managing placeholder files and directories. Users of this API are typically sync providers and to some extent, Windows applications. |
| [Common Log File System](/previous-versions/windows/desktop/clfs/common-log-file-system-portal) | The Common Log File System (CLFS) API provides a high-performance, general-purpose log file subsystem that dedicated client applications can use and multiple clients can share to optimize log access. |
| [Distributed File System](/previous-versions/windows/desktop/dfs/distributed-file-system) | The Distributed File System (DFS) functions provide the ability to logically group shares on multiple servers and to transparently link shares into a single hierarchical namespace. |
| [Distributed File System Replication](/previous-versions/windows/desktop/dfsr/distributed-file-system-replication-dfsr-) | The Distributed File System Replication (DFSR) service is a state-based, multimaster replication engine that supports replication scheduling and bandwidth throttling. |
| [Extensible Storage Engine](/previous-versions/windows/desktop/Gg269259(v=EXCHG.10)) | The Extensible Storage Engine (ESE) is an advanced indexed and sequential access method (ISAM) storage technology. ESE enables applications to store and retrieve data from tables using indexed or sequential cursor navigation. |
| [File Management API (FMAPI)](/previous-versions/windows/desktop/fmapi/file-management-api-fmapi-) | The File Management APIs provide a way for developers to discover and restore deleted files from unencrypted volumes. The File Management APIs also provide the ability to use a password or recovery key file for the discovery and recovery of deleted files from BitLocker-encrypted volumes. |
| [Host bus adapter (HBA)](hba/hba-portal.md) | Host bus adapter (HBA). |
| [Image Mastering API](/windows/desktop/imapi/portal) | The image mastering API enables applications to stage and burn images to CD and DVD optical storage media. Other disc-like media that lay images in the same manner can also use this API.  |
| [Imaging API](/previous-versions/msdn10/dd851933(v=msdn.10)) | The Windows Imaging Interface Reference describes the programmatic method for managing Windows image (.wim) files. |
| [iSCSI Discovery Library API](/previous-versions/windows/desktop/iscsidisc/iscsi-discovery-library-api-portal) | The iSCSI Discovery Library API allows initiators to locate any accessible target devices as well as the associated addresses with a minimal amount of required configurations. |
| [iSCSI Software Target API](/previous-versions/windows/desktop/iscsitarg/iscsi-software-target-api-portal) | The iSCSI Software Target API provides a WMI interface for managing Microsoft iSCSI Software Target, such as creating virtual disks and presenting it to the client. |
| [Local File Systems](/previous-versions/windows/desktop/legacy/aa364407(v=vs.85)) | Describes directory, disk, file, and volume management. Also describes Transactional NTFS (TxF). |
| [MSXML](/previous-versions/windows/desktop/ms763742(v=vs.85)) | Microsoft XML Core Services (MSXML) allows customers who use JScript, Visual Basic Scripting Edition (VBScript), and Microsoft Visual Studio to build high-performance XML-based applications. |
| [Non-Volatile Memory Library (NVML)](./persistent-memory-programming-in-windows-nvml-integration.md) | Allows developers to utilize NVML APIs in order to code for persistent memory in Windows environments. |
| [Offline Files](/previous-versions/windows/desktop/offlinefiles/offline-files-portal) | The Offline Files API allows applications to control and monitor the behavior of Offline Files programmatically. |
| [Packaging](/previous-versions/windows/desktop/opc/packaging) | The packaging APIs provide support for applications that produce or consume files, called packages, that are compliant with the Open Packaging Conventions. |
| [Projected File System](ProjFS/projected-file-system.md) | The Projected File System (ProjFS) allows a user-mode application to project a hierarchical data store into the file system, where it appears as files and directories. Content is cached to the local file system on demand, allowing very large data stores to appear local without overwhelming local storage. |
| [Remote Differential Compression](/previous-versions/windows/desktop/rdc/remote-differential-compression) | Remote Differential Compression (RDC) allows applications to synchronize data between two computers in an efficient manner. |
| [User State Management API](/previous-versions/windows/desktop/usm/user-state-management-api-portal) | The User State Management API provides an alternative way to configure and retrieve current status for the Windows components related to user state. The Windows components that expose configuration and status through these APIs are Folder Redirection, Offline Files, and Roaming Profiles. |
| [Virtual Disk Service](/windows/desktop/VDS/virtual-disk-service-portal) | The Virtual Disk Service (VDS) manages a wide range of storage configurations, from single-disk desktops to external storage arrays. |
| [Virtual Storage](/windows/desktop/VStor/virtual-storage) | The Virtual Hard Disk (VHD) format is a publicly-available image format specification that specifies a virtual hard disk encapsulated in a single file, capable of hosting native file systems while supporting standard disk and file operations. |
| [Volume Shadow Copy Service](/windows/desktop/VSS/volume-shadow-copy-service-portal) | The Volume Shadow Copy Service (VSS) is a set of COM interfaces that implements a framework to allow volume backups to be performed while applications on a system continue to write to the volumes. |
| [Windows Data Access Components](/previous-versions/windows/desktop/legacy/aa968814(v=vs.85)) | Windows Data Access Components (Windows DAC) 6.0 is a set of technologies that provide access to information across the enterprise. These technologies include Microsoft ActiveX Data Objects (ADO), OLE DB, and Microsoft Open Database Connectivity (ODBC). |
| [Windows Storage Management API](/previous-versions/windows/desktop/stormgmt/windows-storage-management-api-portal) | The Windows Storage Management API is used to manage a wide range of storage configurations, from single-disk desktops to external storage arrays. |
| [Windows Sync](/previous-versions/windows/desktop/winsync/windows-sync) | The Microsoft Windows Sync API provides a way for developers to write custom synchronization providers that enable devices to synchronize data with data stores on a computer or on a network. |
| [WMI Provider for NFS](/previous-versions/windows/desktop/nfswmi/wmi-provider-for-nfs-portal) | Microsoft Services for Network File System (NFS) provides a file sharing solution that enables you to transfer files using the NFS protocol between computers running Windows and third-party operating systems. |
| [XmlLite](/previous-versions/windows/desktop/ms752872(v=vs.85)) | XmlLite is a lightweight XML parser designed for ease of use, performance, and standards compliance. |
