---
description: Recommendations for optimal file system transactions.
ms.assetid: 847939ff-5322-4023-8ef7-9d845e80d65c
title: Performance Considerations for Transactional NTFS
ms.topic: article
ms.date: 05/31/2018
---

# Performance Considerations for Transactional NTFS

Transactional NTFS (TxF) has been carefully designed for performance and will typically perform better than general-purpose transactional alternatives under similar scenarios. However, file system transactions have more overhead than non-transacted operations, and some reduction in I/O performance compared to non-transacted I/O is to be expected. Performance-critical applications should perform a technology adoption qualification cycle, evaluating the performance impact of transacted file system operations.

## Overview of TxF Operations

TxF uses *undo* logging to record the changes necessary to put the file system back into a consistent state, also referred to as a rollback, should a transaction abort occur. This undo logging generates additional I/O and is the source of TxF performance overhead compared to non-transactional file system operations.

A high-level summary of how TxF operates is as follows:

-   As a transaction progresses, TxF writes *undo* records into its log file for each modification it makes to the file system. If an abort occurs, these undo records are parsed to put the file system back in the state it was before the transaction began.
-   A *metadata change* undo record describes a change only to the file system's metadata. Some examples of this are moves, renames, appends, and attribute changes. For metadata change undo records, all of the information necessary to undo the change is in the record and stored in the log file.
-   An *overwrite* undo record describes an overwrite of a portion of a file. When a file overwrite occurs, the file's original contents are stored in a special undo file in a hidden directory and the overwrite undo record points to this file. When file updates are eventually flushed from cache to disk, the contents of the undo file must also be flushed, so a transacted file overwrite could generate up to two extra random I/O operations: one to read the old data and one to write it to the undo file. These extra I/O operations are a performance cost of TxF.
-   When a commit occurs, TxF first flushes all undo information, then flushes the actual file changes, and then writes and flushes a commit record. If there are no undo files to flush, the only additional TxF overhead relative to non-transacted I/O is the log flushes themselves. However, log flushes result in efficient large sequential writes so the performance cost is minimal.
-   TxF is optimized for commit. It is expected that most transactions will succeed and not need to rollback, therefore all undo records for a transaction are expected to go unused. From a performance perspective, TxF commit operations are fast and rollbacks are resource-intensive.
-   Rollback is more resource-intensive than commit. During rollback, all the changes that were made in the transaction have to be un-done. In general, rollback duration can be approximately the same it took to originally make the changes. For example, if it took 1 second to make all the changes then it could take about 1 second to undo them. For very long transactions, rollback can create additional performance impacts. For example, system boot time can be delayed if the system must automatically rollback a transaction in the event that the system stops responding and must perform an unscheduled restart.

The summary conclusions about performance that can be drawn from the previous list are as follows:

-   The performance cost of TxF for transactions involving file overwrites can be significant.
-   The performance cost of TxF for transactions involving only metadata operations can be relatively low, provided large transactions be used. A large transaction is when there are many undo records for every commit record.

## Recommendations For Best Performance

Amortize TxF overhead over larger transactions. For example, if you have *N* sets of changes to make where each change has *M* steps and you have the option to either do this as *N* transactions of *M* steps each or do it all as a single transaction with *M*\**N* steps, the latter option would be more efficient.

Consider the possible impact on boot of very large transactions. As previously stated, rollback can be slow and will delay boot time if the system needs to perform automatic rollbacks as boot time. The larger the transaction, the longer the delay.

Keep transactions to mostly metadata operations. This is what TxF is optimized for and, in general, the performance is about the same as non-transacted file I/O for large metadata transactions. Examples of efficient metadata TxF functions are [**MoveFileTransacted**](/windows/desktop/api/WinBase/nf-winbase-movefiletransacteda), [**SetFileAttributesTransacted**](/windows/desktop/api/WinBase/nf-winbase-setfileattributestransacteda), [**CopyFileTransacted**](/windows/desktop/api/WinBase/nf-winbase-copyfiletransacteda), [**DeleteFileTransacted**](/windows/desktop/api/WinBase/nf-winbase-deletefiletransacteda), [**CreateHardLinkTransacted**](/windows/desktop/api/WinBase/nf-winbase-createhardlinktransacteda), and appended writes (calls to the [**WriteFile**](/windows/desktop/api/FileAPI/nf-fileapi-writefile) function when the file pointer as at the end the file, or *EOF*). An example of resource-intensive non-metadata operations are calls to the **WriteFile** function when the file pointer is not at the EOF.

## Summary of TxF Performance Expectations

For in-place updates, overwrites to a section of a file will be much slower than non-transacted file I/O, while TxF performance for file system metadata operations (for example, create, move, and append) is comparable to non-transacted file I/O for large transactions.

 

 



