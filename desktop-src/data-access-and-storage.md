---
Description: 'Windows has APIs, components, and services that support your desktop apps in data access and storage.'
ms.assetid: '8097ee91-f9f9-4e49-a501-5c54153eced8'
title: Data Access and Storage
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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



| Topic                                                                                                            | Description                                                                                                                                                                                                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Background Intelligent Transfer Service](https://msdn.microsoft.com/library/windows/desktop/bb968799)<br/>        | Background Intelligent Transfer Service (BITS) transfers files (downloads or uploads) between a client and server and provides progress information related to the transfers. You can also download files from a peer. <br/>                                                                          |
| [Backup](backup.md)<br/>                                                                                  | Describes registry keys and specialized APIs for backup and restore, the Volume Shadow Copy Service (VSS), and the Windows Server Backup feature.<br/>                                                                                                                                                |
| [Cloud Filter API](https://msdn.microsoft.com/library/windows/desktop/mt827575)<br/>                                                   | The Cloud Filter API provides functionality at the boundary between the user mode and the file system. This API handles creation and management of placeholder files and directories. Users of this API are typically sync providers and to some extent, Windows applications.<br/>                   |
| [Common Log File System](https://msdn.microsoft.com/library/windows/desktop/bb986747)<br/>                                            | The Common Log File System (CLFS) API provides a high-performance, general-purpose log file subsystem that dedicated client applications can use and multiple clients can share to optimize log access.<br/>                                                                                          |
| [Distributed File System](https://msdn.microsoft.com/library/bb524800)<br/>                                                | The Distributed File System (DFS) functions provide the ability to logically group shares on multiple servers and to transparently link shares into a single hierarchical namespace.<br/>                                                                                                             |
| [Distributed File System Replication](https://msdn.microsoft.com/library/bb540031)<br/>                | The Distributed File System Replication (DFSR) service is a state-based, multimaster replication engine that supports replication scheduling and bandwidth throttling.<br/>                                                                                                                           |
| [Extensible Storage Engine](https://msdn.microsoft.com/library/windows/desktop/gg269259.aspx)<br/>         | The Extensible Storage Engine (ESE) is an advanced indexed and sequential access method (ISAM) storage technology. ESE enables applications to store and retrieve data from tables using indexed or sequential cursor navigation.<br/>                                                                |
| [File Management API (FMAPI)](https://msdn.microsoft.com/library/windows/desktop/dd239113)<br/>                                      | The File Management APIs provide a way for developers to discover and restore deleted files from unencrypted volumes. The File Management APIs also provide the ability to use a password or recovery key file for the discovery and recovery of deleted files from BitLocker-encrypted volumes.<br/> |
| [Image Mastering API](https://msdn.microsoft.com/library/windows/desktop/aa366450)<br/>                                                                   | The image mastering API enables applications to stage and burn images to CD and DVD optical storage media. Other disc-like media that lay images in the same manner can also use this API. <br/>                                                                                                      |
| [Imaging API](https://msdn.microsoft.com/en-us/library/windows/desktop/dd851933.aspx)<br/>                 | The Windows Imaging Interface Reference describes the programmatic method for managing Windows image (.wim) files.<br/>                                                                                                                                                                               |
| [iSCSI Discovery Library API](https://msdn.microsoft.com/library/windows/desktop/bb870774)<br/>                           | The iSCSI Discovery Library API allows initiators to locate any accessible target devices as well as the associated addresses with a minimal amount of required configurations.<br/>                                                                                                                  |
| [iSCSI Software Target API](https://msdn.microsoft.com/library/hh830439)<br/>                               | The iSCSI Software Target API provides a WMI interface for managing Microsoft iSCSI Software Target, such as creating virtual disks and presenting it to the client.<br/>                                                                                                                             |
| [Local File Systems](https://msdn.microsoft.com/library/windows/desktop/aa364407)<br/>                                                                 | Describes directory, disk, file, and volume management. Also describes Transactional NTFS (TxF).<br/>                                                                                                                                                                                                 |
| [MSXML](b24aafc2-bf1b-4702-bf1c-b7ae3597eb0c)<br/>                                                         | Microsoft XML Core Services (MSXML) allows customers who use JScript, Visual Basic Scripting Edition (VBScript), and Microsoft Visual Studio to build high-performance XML-based applications.<br/>                                                                                                   |
| [Non-Volatile Memory Library (NVML)](persistent-memory-programming-in-windows---nvml-integration.md)<br/> | Allows developers to utilize NVML APIs in order to code for persistent memory in Windows environments.<br/>                                                                                                                                                                                           |
| [Offline Files](https://msdn.microsoft.com/library/cc296092)<br/>                                                              | The Offline Files API allows applications to control and monitor the behavior of Offline Files programmatically.<br/>                                                                                                                                                                                 |
| [Packaging](https://msdn.microsoft.com/library/windows/desktop/dd371623)<br/>                                                                            | The packaging APIs provide support for applications that produce or consume files, called packages, that are compliant with the Open Packaging Conventions.<br/>                                                                                                                                      |
| [Remote Differential Compression](https://msdn.microsoft.com/library/aa373254)<br/>                                | Remote Differential Compression (RDC) allows applications to synchronize data between two computers in an efficient manner.<br/>                                                                                                                                                                      |
| [User State Management API](https://msdn.microsoft.com/library/windows/desktop/hh830616)<br/>                                     | The User State Management API provides an alternative way to configure and retrieve current status for the Windows components related to user state. The Windows components that expose configuration and status through these APIs are Folder Redirection, Offline Files, and Roaming Profiles.<br/> |
| [Virtual Disk Service](https://msdn.microsoft.com/library/windows/desktop/bb986750)<br/>                                              | The Virtual Disk Service (VDS) manages a wide range of storage configurations, from single-disk desktops to external storage arrays.<br/>                                                                                                                                                             |
| [Virtual Storage](https://msdn.microsoft.com/library/windows/desktop/dd323653)<br/>                                                              | The Virtual Hard Disk (VHD) format is a publicly-available image format specification that specifies a virtual hard disk encapsulated in a single file, capable of hosting native file systems while supporting standard disk and file operations.<br/>                                               |
| [Windows Data Access Components](dedd0762-f224-4736-9894-32bd8313ea61)<br/>                                | Windows Data Access Components (Windows DAC) 6.0 is a set of technologies that provide access to information across the enterprise. These technologies include Microsoft ActiveX Data Objects (ADO), OLE DB, and Microsoft Open Database Connectivity (ODBC).<br/>                                    |
| [Windows Storage Management API](https://msdn.microsoft.com/library/windows/desktop/hh830613)<br/>                      | The Windows Storage Management API is used to manage a wide range of storage configurations, from single-disk desktops to external storage arrays.<br/>                                                                                                                                               |
| [Windows Sync](https://msdn.microsoft.com/library/windows/desktop/dd317274)<br/>                                                                  | The Microsoft Windows Sync API provides a way for developers to write custom synchronization providers that enable devices to synchronize data with data stores on a computer or on a network.<br/>                                                                                                   |
| [WMI Provider for NFS](https://msdn.microsoft.com/library/ff706658)<br/>                                            | Microsoft Services for Network File System (NFS) provides a file sharing solution that enables you to transfer files using the NFS protocol between computers running Windows and third-party operating systems.<br/>                                                                                 |
| [XmlLite](5b1fe27d-a9ec-4c60-9022-253a41b523f9)<br/>                                                       | XmlLite is a lightweight XML parser designed for ease of use, performance, and standards compliance.<br/>                                                                                                                                                                                             |



 

 

 




