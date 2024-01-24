---
description: The distributed link tracking service enables client applications to track link sources that have moved.
ms.assetid: 6f438c72-f23d-4ca4-83bd-fe3bc433ceeb
title: Distributed Link Tracking and Object Identifiers
ms.topic: article
ms.date: 05/31/2018
---

# Distributed Link Tracking and Object Identifiers

Storing a reference to a file or directory by using its path and file name is not reliable. If a user renames a file, it breaks the links to the file. If a user renames the directory, it breaks the links to the file, and all files and subdirectories in the directory tree.

The **distributed link tracking service** enables client applications to track link sources that have moved. Clients that subscribe to the link tracking service can maintain the integrity of their references, and the objects can be tracked in a way that is transparent to the user.

## Object Identifiers

The link tracking service maintains its link to an object by using an **object identifier (ID)**. An object ID is an optional attribute that uniquely identifies a file or directory on a volume.

An index of all object IDs is stored on the volume. Rename, backup, and restore operations preserve object IDs. However, copy operations do not preserve object IDs, because that would violate their uniqueness.

You can perform the following operations on object IDs:

-   Creation
-   Deletion
-   Query

When you create an object ID, you establish the identity of the file to the link tracking service. Conversely, when you delete an object ID, the link tracking service stops maintaining links to the file. For a list of the file system control codes that perform operations on object IDs, see [File Management Control Codes](file-management-control-codes.md).

The distributed link tracking service tracks link sources for shell shortcuts and OLE links within NTFS file system volumes. The link client can fix a broken link with updated information on the new location of the link source.

## Link Tracking Features

Shell shortcuts include heuristic link tracking that uses a tree search algorithm to find a match for a moved link source. The search algorithm is based on the last known path of the file and file information that includes the creation date, file size, and file name and extension.

OLE linking includes the same heuristic link tracking. Windows also includes the same heuristic link tracking with some added improvements for searching name spaces to yield results in some common scenarios. The improvements include the following procedure that depends on time limits imposed by an client application.

**To search for name spaces**

1.  Search four directory levels down from the last directory.
2.  Move up one directory and repeat steps 1 and 2 another three times, which can yield results if the object has moved nearby.
3.  Search four levels down from the desktop root, which can yield results if the object has moved to a location on the same desktop.
4.  Search four levels down from the root on each local fixed drive.
5.  Repeat steps 1-3 without the four directory limit.

> [!Note]  
> These link tracking schemes are transparent to the end-user. However, they do not always yield positive results, and can be time consuming.

 

For more information about shell shortcuts, see [**IShellLink**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishelllinka).

For more information about OLE links, see [**IOleLink**](/windows/win32/api/oleidl/nn-oleidl-iolelink).

If a link is made to a file on NTFS 3.0 or later, and the file is moved to any other volume with NTFS 3.0 or later within the same domain, the file can be found by the tracking service, subject to time considerations. Additionally, if the file is moved outside the domain or within a workgroup, it is found.

To obtain the NTFS version of a volume, open a command prompt with Administrator access rights and execute the following command:

**fsutil fsinfo ntfsinfo** *X*__:__

where *X* is the drive letter of the volume.

When a link is created to a file, the target file is considered the **link source**, and the creator of the link is the **link client**. For example, if a shell shortcut is created to link to a text document, the text document is the link source, and the shell shortcut is the link client.

The distributed link tracking service maintains file links for the following situations that occur within a domain:

-   The link source file is moved from one NTFS file system volume to another within the same domain.
-   The name of the computer that holds the link source is renamed.
-   The network shares on the link source computer are changed.
-   The volume that holds the link source file is moved to another computer within the same domain.

The distributed link tracking service also attempts to maintain links in the preceding situations even when they do not occur within a domain, that is, they are cross domain or within a workgroup. Links can always be maintained in these situations when the network share on the link source computer is changed. They can also be maintained when a link source is moved within a computer. Links can usually be maintained when the link source is moved to another computer, but this form of tracking is less reliable over time.

## Link Tracking Functionality

Link tracking functionality is primarily implemented in the form of the following two system services:

-   Distributed Link Tracking Client
-   Distributed Link Tracking Server

<dl> <dt>

<span id="Distributed_Link_Tracking_Client"></span><span id="distributed_link_tracking_client"></span><span id="DISTRIBUTED_LINK_TRACKING_CLIENT"></span>Distributed Link Tracking Client
</dt> <dd>

The distributed link tracking client runs on all computers, and manages the link tracking activities for that computer. These activities include searching for link sources and processing link source moves. When a link source is moved, the service passes information to the distributed link tracking server that runs on domain controllers.

</dd> <dt>

<span id="Distributed_Link_Tracking_Server"></span><span id="distributed_link_tracking_server"></span><span id="DISTRIBUTED_LINK_TRACKING_SERVER"></span>Distributed Link Tracking Server
</dt> <dd>

The distributed link tracking server runs on each domain controller in a domain. The service accepts notifications of file and volume moves from the tracking service on a computer, and allows the distributed link tracking client to query the current location of a link source.

This server service maintains information in the domain controllers about volumes and files that have been moved. The information about moves cannot increase beyond a specific size, and it is automatically removed if it becomes unnecessary.

</dd> </dl>

The link tracking services are exposed by the [**IShellLink**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishelllinka) and [**IOleLink**](/windows/win32/api/oleidl/nn-oleidl-iolelink) interfaces. Therefore, they are used by shell shortcuts. When the [**IShellLink::Resolve**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishelllinka-resolve) method is called and the referent file cannot be found, for example, when the user activates a shell shortcut, the tracking service is called automatically to find the file. Similarly, when the [**IOleLink**](/windows/win32/api/oleidl/nn-oleidl-iolelink) implementation cannot find a file, for example, in its [**BindToSource**](/windows/desktop/api/oleidl/nf-oleidl-iolelink-bindtosource) method, it automatically calls on the tracking service.

## Link Tracking Limitations

The distributed link tracking services are available only on the NTFS file system, and are only available for link sources on NTFS 3.0 or later. Therefore, if a link source is moved to a FAT file system volume the tracking information is lost. Additionally, if a link source is moved between the NTFS 3.0 or later, but the computer that is performing the move is running an earlier version of Windows, the link tracking information is lost. When the link tracking information is lost, no harm is done to the link source file itself, it is simply not trackable by the distributed link tracking services.

To obtain the NTFS version of a volume, open a command prompt with Administrator access rights and execute the following command:

**fsutil fsinfo ntfsinfo** *X*__:__

where *X* is the drive letter of the volume.

Links to files on removable media are not maintained. Also, the tracking service does not recognize a new NTFS file system volume until the system is re-booted. A new volume might become available because of re-partitioning, reformatting a FAT file system volume to the NTFS file system, or connecting a new external drive.

 

 
