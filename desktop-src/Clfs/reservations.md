---
Description: 'An application reserves space in the log when it has data that will be written to the log in the future, but cannot write it immediately.'
ms.assetid: 'cc52812e-4e1a-426c-8580-b32d354a4b9a'
title: Reservations
---

# Reservations

An application reserves space in the log when it has data that will be written to the log in the future, but cannot write it immediately. Reservations provide a guarantee that the data can be written to the log when the data is available to be written. When using logs, applications often reserve one or more log records in a marshaling area. You may reserve records to guarantee that future append operations will occur.

## Compensation Records

CLFS is an ARIES-compliant (Algorithm for Recovery and Isolation Exploiting Semantics) logging system that is meant for write-ahead logging. In write-ahead logging, an application writes an undo record before it performs the operation, reserving the amount of space that it would take in the log to write a compensating record, which may be used during roll-back. Later, the reserved space is used when the compensation record is actually written.

## Reservations

Reservations are typically used by transactional applications. Transactional applications use reservations in roll-back operations to guarantee that an operation can be completed before the data is committed; otherwise, the changes are rolled back.

During a roll-back operation, a transactional resource manager (RM) must be able to recover its state if the RM is interrupted during the roll-back operation. CLFS allows an RM to reserve space in a log before it is used. The [**ReserveAndAppendLog**](reserveandappendlog.md) function can either reserve space or append data, or both, depending on the parameters that are specified when the call is made. As work progresses in a transaction, an application can append the undo information and reserve space for compensation records. During a roll-back operation, compensation records that are created indicate what has been undone on the disk. The records are appended using space that has been previously reserved. This guarantees that an RM does not run out of log space while performing a roll-back operation—which is a fatal condition. If a log fills up during a transaction, an application can safely roll back a transaction without corrupting durable data.

## Reserving Log Records

Calling the [**AllocReservedLog**](allocreservedlog.md), [**ReserveAndAppendLog**](reserveandappendlog.md), or [**ReserveAndAppendLogAligned**](reserveandappendlogaligned.md) function reserves space in the marshaling area for a log stream.

Each record in the log is rounded up to the nearest block size.

## Freeing Reserved Log Records

Applications can reserve or consume log space, or both at any given time. After a commit record is written to the log, an application can free up the reservations for the compensation records. This action can be done by calling either the [**FreeReservedLog**](freereservedlog.md), [**ReserveAndAppendLog**](reserveandappendlog.md), or [**ReserveAndAppendLogAligned**](reserveandappendlogaligned.md) function. Calling the **ReserveAndAppendLog** function allows reservations, the appending of records, and the freeing of reservations to be done with one atomic action.

When you free records, you must free the same records that you reserved in a previous call to the [**ReserveAndAppendLog**](reserveandappendlog.md) or [**ReserveAndAppendLogAligned**](reserveandappendlogaligned.md) function.

You can use the [**ReserveAndAppendLog**](reserveandappendlog.md) or [**ReserveAndAppendLogAligned**](reserveandappendlogaligned.md) function to perform multiple actions atomically, by specifying either positive or negative reservations and data to be appended, or both.

The following functions can be used to perform reservations.



| Function                                                         | Description                                                                                                                                                                                                                                                                                      |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AlignReservedLog**](alignreservedlog.md)                     | Calculates the sector-aligned reservation size for a set of records.                                                                                                                                                                                                                             |
| [**AllocReservedLog**](allocreservedlog.md)                     | Allocates sector-aligned space for a set of reserved records.                                                                                                                                                                                                                                    |
| [**FreeReservedLog**](freereservedlog.md)                       | Reduces the number of reserved log records in a marshaling area made by calling [**ReserveAndAppendLog**](reserveandappendlog.md), [**ReserveAndAppendLogAligned**](reserveandappendlogaligned.md), or [**AllocReservedLog**](allocreservedlog.md).                                           |
| [**ReserveAndAppendLog**](reserveandappendlog.md)               | Reserves space for log buffers, appends a log record to the log, or does both.                                                                                                                                                                                                                   |
| [**ReserveAndAppendLogAligned**](reserveandappendlogaligned.md) | Reserves space for log buffers, appends a log record to the log, or both. This function is like [**ReserveAndAppendLog**](reserveandappendlog.md), but [**ReserveAndAppendLogAligned**](reserveandappendlogaligned.md) aligns the write entries of the record to the specified byte alignment. |



 

 

 



