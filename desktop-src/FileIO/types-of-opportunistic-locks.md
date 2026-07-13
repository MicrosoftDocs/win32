---
description: Describes Read-Write-Handle, Read-Write, Read-Handle, Read, and the legacy Level 1, Level 2, Batch, and Filter opportunistic locks.
ms.assetid: 06136348-0c08-4e9c-9c96-fd3af33cbdc0
title: Types of Opportunistic Locks
ms.topic: reference
ms.date: 05/31/2018
---

# Types of Opportunistic Locks

> [!NOTE]
>
> The terms "opportunistic lock" and "oplock" are equivalent. This document will usually use the term "oplock" for brevity.

The oplock operations work with eight types of oplocks. Four types are considered current, while the other four are legacy.
* The current oplock types are: Read-Write-Handle, Read-Write, Read-Handle, and Read.
  * These oplock types were introduced in Windows 7. They are therefore commonly referred to as "Windows 7 oplocks".
* The legacy oplock types are: Level 1, Level 2, Batch, and Filter.
  * Level 1, Level 2, and Batch oplocks were introduced in Windows NT 3.1. Filter oplocks were introduced in Windows 2000.

Read-write-handle, Read-Write, Level 1, Batch, and Filter locks are *exclusive oplocks*. If a client has any type of exclusive oplock on a file, no other oplock may exist on the file.

Read-handle, Read, and Level 2 locks are *shareable oplocks*. Multiple clients may hold shareable oplocks on the same file.
* A given file may have Read and Level 2 oplocks on it at the same time.
* A file may also have Read and Read-Handle oplocks on it at the same time.
* A file may not have Read-Handle and Level 2 oplocks on it at the same time.

## Current Opportunistic Lock Types

### Read-Write-Handle Opportunistic Locks

A Read-Write-Handle oplock on a file allows a client to read ahead in a file and cache both read-ahead and write data locally. It also allows a client network redirector to avoid sending open and close operations to the server if the client repeatedly opens and closes the file, in much the same way as the legacy Batch oplock type.

A Read-Write-Handle oplock may be granted only if the client has the only open handle to the file.

### Read-Write Opportunistic Locks

A Read-Write oplock on a file allows a client to read ahead in a file and cache both read-ahead and write data locally. This is similar to a legacy Level 1 oplock.

A Read-Write-Handle oplock may be granted only if the client has the only open handle to the file.

### Read-Handle Opportunistic Locks

A Read-Handle oplock on a file allows a client to read ahead in a file and cache read-ahead data. Like a Read-Write-Handle oplock, it also allows a client network redirector to avoid sending open and close operations to the server if the client repeatedly opens and closes the file.

If an application has an open handle to a file and has been granted a Read-Handle oplock, and another file handle is opened to that file, the file system checks whether the new handle's share and access modes are compatible with existing handles. If so, the new handle is opened successfully. If not, the open operation is blocked and the Read-Handle oplock breaks. The application that owns the oplock may acknowledge the break by closing the handle that owns the Read-Handle oplock. In that case, the new handle is opened successfully (assuming there are no other open handles that conflict) and the opening application remains unaware that a conflicting file handle existed.

> [!NOTE]
>
> If the oplock owner acknowledges the Read-Handle oplock break without closing its file handle and it conflicts with the new open operation, the new open will fail with **ERROR_SHARING_VIOLATION**, just as if there had been no oplock in the first place.

If an application has an open handle to a file and has been granted a Read-Handle oplock, and a write operation occurs on a different file handle, the Read-Handle oplock will break. In this case the oplock breaks without blocking the write operation, unlike in the case described above where the oplock is protecting against sharing violations. An oplock break that does not block the breaking operation is called an *advisory break*. It serves to notify the client that owned the oplock that any data it may have cached is now stale, and it may need to refresh its cache.

### Read Opportunistic Locks

A Read oplock on a file allows a client to read ahead in a file and cache read-ahead data. A Read oplock behaves very similarly to a legacy Level 2 oplock.

### Atomic Create-With-Oplock

This is not an oplock type, it is a procedure that allows open operations for reading to occur without sharing-mode violations in the time span between your application's opening the file and receiving the lock. With legacy oplocks this is only possible with Filter oplocks and requires opening two handles. With Windows 7 oplocks an application may request any type of oplock using this procedure and need open only one handle.

To perform the atomic create-with-oplock procedure your application should do the following:

1. Use the [**CreateFile2**](/windows/win32/api/fileapi/nf-fileapi-createfile2) function to open the file. In the *dwFileFlags* field of the [CREATEFILE2_EXTENDED_PARAMETERS](/windows/win32/api/fileapi/ns-fileapi-createfile2_extended_parameters) structure, set the flag **FILE_FLAG_OPEN_REQUIRING_OPLOCK**. You may set the *dwDesiredAccess* and *dwShareMode* parameters as desired. For example, in the *dwDesiredAccess* parameter set **GENERIC_READ** so you can read the file, and in the *dwShareMode* parameter set the **FILE_SHARE_READ | FILE_SHARE_DELETE** flags to allow others to read, rename, and/or mark the file for deletion while you have it open.
2. Request an oplock on this handle with the [**FSCTL\_REQUEST\_OPLOCK**](/windows/win32/api/winioctl/ni-winioctl-fsctl_request_oplock) control code.

> [!NOTE]
>
> Your application should not perform any file system operations on the file between steps 1 and 2. Doing so may cause deadlocks.

The most common oplock to request using this procedure is the Read-Handle type. This allows your application to allow others as much concurrent access as possible, while still allowing your application to be notified if it needs to close its handle to avoid causing a sharing violation to a conflicting open.

## Legacy Opportunistic Lock Types

### Level 1 Opportunistic Locks

A Level 1 oplock on a file allows a client to read ahead in the file and cache both read-ahead and write data from the file locally. As long as the client has sole access to a file, there is no danger to data coherency in providing a Level 1 oplock.

The client can request a Level 1 oplock after opening a file. If no other client (or no other thread on the same client) has the file open, the server may grant the oplock. The client can then cache read and write data from the file locally. If another client has opened the file, then the server refuses the oplock and the client does no local caching. (The server may refuse the oplock for other reasons as well, such as not supporting oplocks.)

When the server opens a file that already has a Level 1 oplock on it, the server examines the sharing state of the file before it breaks the Level 1 oplock. If the server breaks the lock after this examination, the time the client with the former lock spends flushing its write cache is time the client requesting the file must wait. This time expenditure means that Level 1 oplocks should be avoided on files that many clients open.

However, because the server checks the sharing state before it breaks the lock, in the case where the server would deny an open request due to a sharing conflict the server does not break the lock. For example, if you have opened a file, denied sharing for write operations, and obtained a Level 1 lock, the server denies another client's request to open the file for writing before it even examines your lock on the file. In this instance, your oplock is not broken.

For an example of how a Level 1 oplock works, see [Level 1 Opportunistic Lock Example](opportunistic-lock-examples.md#level-1-opportunistic-lock). For more information on breaking oplocks, see [Breaking Opportunistic Locks](breaking-opportunistic-locks.md).

### Level 2 Opportunistic Locks

A Level 2 oplock informs a client that there are multiple concurrent clients of a file and that none has yet modified it. This lock allows the client to perform read operations and obtain file attributes using cached or read-ahead local information, but the client must send all other requests (such as for write operations) to the server. Your application should use the Level 2 oplock when you expect other applications to write to the file at random or read the file at random or sequentially.

A Level 2 oplock is very similar to a Filter oplock. In most situations, your application should use the Level 2 oplock. Only use the Filter lock if you do not want open operations for reading to cause sharing-mode violations in the time span between your application's opening the file and receiving the lock. For more information, see [Filter Opportunistic Locks](opportunistic-lock-examples.md#filter-opportunistic-lock) and [Server Response to Open Requests on Locked Files](server-response-to-open-requests-on-locked-files.md).

For more information on breaking oplocks, see [Breaking Opportunistic Locks](breaking-opportunistic-locks.md).

### Batch Opportunistic Locks

A Batch oplock manipulates file openings and closings. For example, in the execution of a batch file, the batch file may be opened and closed once for each line of the file. A Batch oplock opens the batch file on the server and keeps it open. As the command processor "opens" and "closes" the batch file, the network redirector intercepts the open and close commands. All the server receives are the seek and read commands. If the client is also reading ahead, the server receives a particular read request at most one time.

When opening a file that already has a Batch oplock, the server checks the sharing state of the file after breaking the lock. This check gives the holder of the lock a chance to complete flushing its cache and to close the file handle. An open operation attempted during the sharing check does not cause the sharing check to fail if the lock holder releases the lock.

For an example of how a Batch oplock works, see [Batch Opportunistic Lock Example](opportunistic-lock-examples.md#batch-opportunistic-lock). For more information on breaking oplocks, see [Breaking Opportunistic Locks](breaking-opportunistic-locks.md).

### Filter Opportunistic Locks

A Filter oplock locks a file so that it cannot be opened for either write or delete access. All clients must be able to share the file. Filter locks allow applications to perform nonintrusive filtering operations on file data (for example, a compiler opening source code or a cataloging program).

A Filter oplock differs from a Level 2 oplock in that it allows open operations for reading to occur without sharing-mode violations in the time span between your application's opening the file and receiving the lock. The Filter oplock is the best lock to use when it is important to allow other clients reading access. In other cases, your application should use a Level 2 oplock. A Filter oplock differs from a Batch oplock in that it does not allow multiple openings and closings to be handled by the network redirector the way a Batch oplock does.

Your application should request a Filter oplock on a file in three steps:

1.  Use the [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function to open a handle to the file with the *DesiredAccess* parameter set to zero, indicating no access, and the *dwShareMode* parameter set to the **FILE\_SHARE\_READ** flag to allow sharing for reading. The handle obtained at this point is called the locking handle.
2.  Request a lock on this handle with the [**FSCTL\_REQUEST\_FILTER\_OPLOCK**](/windows/win32/api/winioctl/ni-winioctl-fsctl_request_filter_oplock) control code.
3.  When the lock is granted, use [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) to open the file again with *DesiredAccess* set to the **GENERIC\_READ** flag. Set *dwShareMode* to the **FILE\_SHARE\_READ** flag to allow others to read the file while you have it open, the **FILE\_SHARE\_DELETE** flag to allow others to mark the file for deletion while you have it open, or both. The handle obtained at this point is called the read handle.

Use the read handle to read from or write to the contents of the file.

When opening a file that already has a Filter oplock, the server breaks the lock and then checks the sharing state of the file. This check gives the client that held the former oplock a chance to abandon any cached data and acknowledge the break. An open operation attempted during this sharing check does not cause the sharing check to fail if the former lock holder releases the lock. The file system holds in abeyance the open operation until the lock's owner closes both the read handle and then the locking handle. After this is done, the other client's open request can proceed.

For more information on breaking oplocks, see [Breaking Opportunistic Locks](breaking-opportunistic-locks.md).

## Current Vs. Legacy Oplock Types

The different Windows 7 oplock types are considered to be different "levels" of oplock. From highest to lowest, the order is: Read-Write-Handle, Read-Write, Read-Handle, Read. The oplock level is considered in certain operations, such as when a client requests a new oplock as part of acknowledging an oplock break.

Some legacy oplocks appear similar to Windows 7 oplocks. In particular, Read seems similar to Level 2, Read-Write seems similar to Level 1, and Read-Write-Handle seems similar to Batch. However, there are differences in behavior that allow for more flexible operations that are not achievable with the legacy oplocks. Some advantages to the Windows 7 oplock types are:

* They allow an application greater flexibility and clarity in expressing caching intentions.
* They provide greater flexibility in handling oplock breaks.
  * When a Level 1 or Batch oplock breaks, as part of the break acknowledgment the client may request that it breaks to Level 2 or to no oplock. When a Filter oplock breaks, the client must accept that it breaks to no oplock.
  * When a Windows 7 oplock breaks, as part of the break acknowledgment the client may request that it break to any Windows 7 oplock. The client may even request an oplock of a higher level. Depending on circumstances, such as whether or not another opener is waiting on the oplock break to be acknowledged, such a request may succeed.
* A client may request an in-place upgrade of a currently held Windows 7 oplock. For example, if it holds a Read oplock it may request an upgrade to Read-Handle, simply by requesting a Read-Handle oplock on the same file handle. Legacy oplocks cannot be upgraded in place.


 
