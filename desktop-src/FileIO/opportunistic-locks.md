---
description: An opportunistic lock (also called an oplock) is a lock placed by a client on a file residing on a server.
ms.assetid: 'b4c2f5f0-a29b-4598-a49b-da99e93d2991'
title: Opportunistic Locks
ms.topic: article
ms.date: 07/21/2023
---

# Opportunistic Locks

An opportunistic lock (also called an oplock) is a lock placed by a client on a file residing on a server. In most cases, a client requests an opportunistic lock so it can cache data locally, thus reducing network traffic and improving apparent response time. Opportunistic locks are used by network redirectors on clients with remote servers, as well as by client applications on local servers.

> [!NOTE]
> The articles about opportunistic locks found in this section pertain primarily to client applications, although some information is provided for network redirectors. You can find more oplock information for network redirectors in the Windows WDK's [Oplocks](/windows-hardware/drivers/ifs/oplock-overview) articles.

Opportunistic locks coordinate data caching and coherency between clients and servers and among multiple clients. Data that is coherent is data that is the same across the network. In other words, if data is coherent, data on the server and all the clients is synchronized.

Opportunistic locks are not commands by the client to the server. They are requests from the client to the server. From the point of view of the client, they are opportunistic. In other words, the server grants such locks whenever other factors make the locks possible.

When a local application requests access to a remote file, the implementation of opportunistic locks is transparent to the application. The network redirector and the server involved open and close the opportunistic locks automatically. However, opportunistic locks can also be used when a local application requests access to a local file, and access by other applications and processes must be delegated to prevent corruption of the file. In this case, the local application directly requests an opportunistic lock from the local file system and caches the file locally. When used in this way, the opportunistic lock is effectively a semaphore managed by the local server, and is mainly used for the purposes of data coherency in the file and file access notification.

Before using opportunistic locks in your application, you should be familiar with the file access and sharing modes described in [Creating and Opening Files](creating-and-opening-files.md).

The maximum number of concurrent opportunistic locks that you can create is limited only by the amount of available memory.

Local applications should not attempt to request opportunistic locks from remote servers. An error will be returned by [**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) if an attempt is made to do this.

Opportunistic locks are of very limited use for applications. The only practical use is to test a network redirector or a server opportunistic lock handler. Typically, file systems implement support for opportunistic locks. Applications generally leave opportunistic lock management to the file system drivers. Anyone implementing a file system should use the [Installable File System (IFS) Kit](/previous-versions/gg463062(v=msdn.10)). Anyone developing a device driver other than an installable file system should use the [Windows Driver Kit (WDK)](https://www.microsoft.com/?ref=go).

Opportunistic locks and the associated operations are a superset of the opportunistic lock portion of the Common Internet File System (CIFS) protocol, an Internet Draft. The CIFS protocol is an enhanced version of the Server Message Block (SMB) protocol. For more information, see [Microsoft SMB Protocol and CIFS Protocol Overview](microsoft-smb-protocol-and-cifs-protocol-overview.md). The CIFS Internet Draft explicitly identifies that a CIFS implementation may implement opportunistic locks by refusing to grant them.

The following topics identify opportunistic locks.

## In this section

| Topic | Description |
|--------|--------|
| [Local Caching](local-caching.md) | *Local caching* of data is a technique used to speed network access to data files. It involves caching data on clients rather than on servers when possible. |
| [Data Coherency](data-coherency.md) | If data is coherent, data on the server and all the clients is synchronized. One type of software system that provides data coherency is a revision control system (RCS). |
| [How to Request an Opportunistic Lock](how-to-request-an-opportunistic-lock.md) | Opportunistic locks are requested by first opening a file with permissions and flags appropriate to the application opening the file. All files for which opportunistic locks will be requested must be opened for overlapped (asynchronous) operation. |
| [Server Response to Open Requests on Locked Files](server-response-to-open-requests-on-locked-files.md) | You can minimize the impact your application has on other clients and the impact they have on your application by granting as much sharing as possible, requesting the minimum access level necessary, and using the least intrusive opportunistic lock suitable for your application. |
| [Types of Opportunistic Locks](types-of-opportunistic-locks.md) | Describes level 1, level 2, batch, and filter opportunistic locks. |
| [Breaking Opportunistic Locks](breaking-opportunistic-locks.md) | Breaking an opportunistic lock is the process of degrading the lock that one client has on a file so that another client can open the file, with or without an opportunistic lock. |
| [Opportunistic Lock Examples](opportunistic-lock-examples.md) | Diagrams of network-traffic views for a level 1 opportunistic lock, a batch opportunistic lock, and a filter opportunistic lock. |
| [Opportunistic Lock Operations](opportunistic-lock-operations.md) | If an application requests opportunistic locks, all files for which it requests locks must be opened for overlapped (asynchronous) input and output by using the [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function with the **FILE\_FLAG\_OVERLAPPED** flag. |

For additional information about opportunistic locks, see the CIFS Internet Draft document. Any discrepancies between this topic and the current CIFS Internet Draft should be resolved in favor of the CIFS Internet Draft.

## See also

[NetApp File Access and Protocols Management Guide](https://library.netapp.com/ecmdocs/ECMP1401220/html/frameset.html)

[Oplocks (WDK)](/windows-hardware/drivers/ifs/oplock-overview)
