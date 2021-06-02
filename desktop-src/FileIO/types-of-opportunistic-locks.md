---
description: Describes level 1, level 2, batch, and filter opportunistic locks.
ms.assetid: 06136348-0c08-4e9c-9c96-fd3af33cbdc0
title: Types of Opportunistic Locks
ms.topic: article
ms.date: 05/31/2018
---

# Types of Opportunistic Locks

The opportunistic lock operations work with four types of opportunistic locks: level 1, level 2, batch, and filter. *Exclusive opportunistic locks* are level 1, batch, and filter locks. If a thread has any type of exclusive lock on a file, it cannot also have a level 2 lock on the same file.

## Level 1 Opportunistic Locks

A level 1 opportunistic lock on a file allows a client to read ahead in the file and cache both read-ahead and write data from the file locally. As long as the client has sole access to a file, there is no danger to data coherency in providing a level 1 opportunistic lock.

The client can request a level 1 opportunistic lock after opening a file. If no other client (or no other thread on the same client) has the file open, the server may grant the opportunistic lock. The client can then cache read and write data from the file locally. If another client has opened the file, then the server refuses the opportunistic lock and the client does no local caching. (The server may refuse the opportunistic lock for other reasons as well, such as not supporting opportunistic locks.)

When the server opens a file that already has a level 1 opportunistic lock on it, the server examines the sharing state of the file before it breaks the level 1 opportunistic lock. If the server breaks the lock after this examination, the time the client with the former lock spends flushing its write cache is time the client requesting the file must wait. This time expenditure means that level 1 opportunistic locks should be avoided on files that many clients open.

However, because the server checks the sharing state before it breaks the lock, in the case where the server would deny an open request due to a sharing conflict the server does not break the lock. For example, if you have opened a file, denied sharing for write operations, and obtained a level 1 lock, the server denies another client's request to open the file for writing before it even examines your lock on the file. In this instance, your opportunistic lock is not broken.

For an example of how a level 1 opportunistic lock works, see Level 1 Opportunistic Lock Example. For more information on breaking opportunistic locks, see [Breaking Opportunistic Locks](breaking-opportunistic-locks.md).

## Level 2 Opportunistic Locks

A level 2 opportunistic lock informs a client that there are multiple concurrent clients of a file and that none has yet modified it. This lock allows the client to perform read operations and obtain file attributes using cached or read-ahead local information, but the client must send all other requests (such as for write operations) to the server. Your application should use the level 2 opportunistic lock when you expect other applications to write to the file at random or read the file at random or sequentially.

A level 2 opportunistic lock is very similar to a filter opportunistic lock. In most situations, your application should use the level 2 opportunistic lock. Only use the filter lock if you do not want open operations for reading to cause sharing-mode violations in the time span between your application's opening the file and receiving the lock. For more information, see Filter Opportunistic Locks and [Server Response to Open Requests on Locked Files](server-response-to-open-requests-on-locked-files.md).

For more information on breaking opportunistic locks, see [Breaking Opportunistic Locks](breaking-opportunistic-locks.md).

## Batch Opportunistic Locks

A batch opportunistic lock manipulates file openings and closings. For example, in the execution of a batch file, the batch file may be opened and closed once for each line of the file. A batch opportunistic lock opens the batch file on the server and keeps it open. As the command processor "opens" and "closes" the batch file, the network redirector intercepts the open and close commands. All the server receives are the seek and read commands. If the client is also reading ahead, the server receives a particular read request at most one time.

When opening a file that already has a batch opportunistic lock, the server checks the sharing state of the file after breaking the lock. This check gives the holder of the lock a chance to complete flushing its cache and to close the file handle. An open operation attempted during the sharing check does not cause the sharing check to fail if the lock holder releases the lock.

For an example of how a batch opportunistic lock works, see Batch Opportunistic Lock Example. For more information on breaking opportunistic locks, see [Breaking Opportunistic Locks](breaking-opportunistic-locks.md).

## Filter Opportunistic Locks

A filter opportunistic lock locks a file so that it cannot be opened for either write or delete access. All clients must be able to share the file. Filter locks allow applications to perform nonintrusive filtering operations on file data (for example, a compiler opening source code or a cataloging program).

A filter opportunistic lock differs from a level 2 opportunistic lock in that it allows open operations for reading to occur without sharing-mode violations in the time span between your application's opening the file and receiving the lock. The filter opportunistic lock is the best lock to use when it is important to allow other clients reading access. In other cases, your application should use a level 2 opportunistic lock. A filter opportunistic lock differs from a batch opportunistic lock in that it does not allow multiple openings and closings to be handled by the network redirector the way a batch opportunistic lock does.

Your application should request a filter opportunistic lock on a file in three steps:

1.  Use the [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function to open a handle to the file with the *DesiredAccess* parameter set to zero, indicating no access, and the *dwShareMode* parameter set to the **FILE\_SHARE\_READ** flag to allow sharing for reading. The handle obtained at this point is called the locking handle.
2.  Request a lock on this handle with the [**FSCTL\_REQUEST\_FILTER\_OPLOCK**](/windows/win32/api/winioctl/ni-winioctl-fsctl_request_filter_oplock) control code.
3.  When the lock is granted, use [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) to open the file again with *DesiredAccess* set to the **GENERIC\_READ** flag. Set *dwShareMode* to the **FILE\_SHARE\_READ** flag to allow others to read the file while you have it open, the **FILE\_SHARE\_DELETE** flag to allow others to mark the file for deletion while you have it open, or both. The handle obtained at this point is called the read handle.

Use the read handle to read from or write to the contents of the file.

When opening a file that already has a filter opportunistic lock, the server breaks the lock and then checks the sharing state of the file. This check gives the client that held the former opportunistic lock a chance to abandon any cached data and acknowledge the break. An open operation attempted during this sharing check does not cause the sharing check to fail if the former lock holder releases the lock. The file system holds in abeyance the open operation until the lock's owner closes both the read handle and then the locking handle. After this is done, the other client's open request can proceed.

For more information on breaking opportunistic locks, see [Breaking Opportunistic Locks](breaking-opportunistic-locks.md).

 

 
