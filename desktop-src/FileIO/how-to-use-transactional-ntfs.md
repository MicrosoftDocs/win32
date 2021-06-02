---
description: Managing transacted file handles in Transactional NTFS.
ms.assetid: 29879a3f-14b4-462c-a001-46c3c3eb74d1
title: How to Use Transactional NTFS
ms.topic: article
ms.date: 05/31/2018
---

# How to Use Transactional NTFS

## Transacted File Handles

Transactional NTFS (TxF) binds a file handle to a transaction. For operations that work on a handle (for example, the [**ReadFile**](/windows/desktop/api/FileAPI/nf-fileapi-readfile) and [**WriteFile**](/windows/desktop/api/FileAPI/nf-fileapi-writefile) functions), the actual API function call does not change. For file operations that take a name, there are explicit transacted functions for these operations. For example, instead of calling [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea), call [**CreateFileTransacted**](/windows/desktop/api/WinBase/nf-winbase-createfiletransacteda). This creates a transacted file handle, which can then be used for all file operations requiring a handle. All subsequent operations using this handle are transacted operations.

## Basic TxF Usage

The following series of steps represents the most basic usage for TxF. More complex scenarios are also supported, at the discretion of the application designer.

1.  Create a transaction by calling the KTM function [**CreateTransaction**](/windows/desktop/api/ktmw32/nf-ktmw32-createtransaction) or by using the **IKernelTransaction** interface of the [Distributed Transaction Coordinator](/previous-versions/windows/desktop/mscs/distributed-transaction-coordinator) (DTC).
2.  Get transacted file handle(s) by calling [**CreateFileTransacted**](/windows/desktop/api/WinBase/nf-winbase-createfiletransacteda).
3.  Modify the file(s) as necessary using the transacted file handle(s).
4.  Close all transacted file handles associated with the transaction created in step 1.
5.  Commit or abort the transaction by calling the corresponding KTM or DTC function.

## Key Points of the TxF Programming Model

The TxF programming model has the following key points for you to consider when you develop a TxF application:

-   It is highly recommended that an application close all transacted file handles before committing or rolling back a transaction. The system invalidates all transacted handles when a transaction ends. Any operation, except close, performed on a transacted handle after the transaction ends returns the following error: **ERROR\_HANDLE\_NO\_LONGER\_VALID**.
-   A file is viewed as a unit of storage. Partial updates and complete file overwrites are supported. Multiple transactions cannot concurrently modify the same file.
-   Memory mapped I/O is transparent and consistent with the regular file I/O. An application must flush and close an opened section before committing a transaction. Failure to do this can result in partial changes to the mapped file within the transaction. A rollback fails if this is not done.

## Common Programming Errors

The following common errors can occur when developing transacted applications:

-   Using a file handle after a transaction is completed.
-   Failing to close handles to deleted files and directories before committing a transaction, which will prevent the delete operations from occurring. This event must occur before performing the commit for the delete operation to be considered part of the transaction. This is because the system does not actually delete a file until the last handle to it is closed, even when the operation is not transacted, as part of the Windows file I/O subsystem.
-   Failing to account for system-initiated transaction rollbacks, which may happen at any time; for example, a transaction is rolled back if the system resources are exhausted.

 

 
