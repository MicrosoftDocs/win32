---
description: As files, directories, and other NTFS file system objects are added, deleted, and modified, the NTFS file system enters change journal records in streams, one for each volume on the computer.
ms.assetid: c41aa3a8-c8d8-4bf2-9bbb-d6a6a556c5e4
title: Change Journal Records
ms.topic: article
ms.date: 05/31/2018
---

# Change Journal Records

As files, directories, and other NTFS file system objects are added, deleted, and modified, the NTFS file system enters change journal records in streams, one for each volume on the computer. Each record indicates the type of change and the object changed. The offset from the beginning of the stream for a particular record is called the update sequence number (USN) for the particular record. New records are appended to the end of the stream.

The NTFS file system may delete old records to conserve space. If needed records have been deleted, the indexing service recovers by re-indexing the volume, as it does when no change journal exists.

The change journal logs only the fact of a change to a file and the reason for the change (for example, write operations, truncation, lengthening, deletion, and so on). It does not record enough information to allow reversing the change.

In addition, multiple changes to the same file may result in only one reason flag being added to the current record. If the same kind of change occurs more than once, the NTFS file system does not write a new record for the changes after the first. For example, several write operations with no intervening close and reopen operations result in only one change record with the reason flag USN\_REASON\_DATA\_OVERWRITE set.

To illustrate how the change journal works, suppose a user accesses a file in the following order:

1.  Writes to the file.
2.  Sets the time stamp for the file.
3.  Writes to the file.
4.  Truncates the file.
5.  Writes to the file.
6.  Closes the file.

In this case, the NTFS file system takes the following actions in the change journal (where \| indicates a bitwise OR operation).



| Event                                 | NTFS file system action                                                                                                                                                                                                                                                    |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Initial write operation<br/>    | The NTFS file system writes a new USN record with the USN\_REASON\_DATA\_OVERWRITE reason flag set. For more information on possible reason flags, see the [**USN\_RECORD**](/windows/desktop/api/WinIoCtl/ns-winioctl-usn_record_v2) structure.<br/>                                                     |
| Setting of file time stamp<br/> | The NTFS file system writes a new USN record with the flag setting USN\_REASON\_DATA\_OVERWRITE \| USN\_REASON\_BASIC\_INFO\_CHANGE.<br/>                                                                                                                            |
| Second write operation<br/>     | The NTFS file system does not write a new USN record. Because USN\_REASON\_DATA\_OVERWRITE is already set for the existing record, no changes are made to the record.<br/>                                                                                           |
| File truncation<br/>            | The NTFS file system writes a new USN record with the flag setting USN\_REASON\_DATA\_OVERWRITE \| USN\_REASON\_BASIC\_INFO\_CHANGE \| USN\_REASON\_DATA\_TRUNCATION.<br/>                                                                                           |
| Third write operation<br/>      | The NTFS file system does not write a new USN record. Because USN\_REASON\_DATA\_OVERWRITE is already set for the existing record, no changes are made to the record.<br/>                                                                                           |
| Close operation<br/>            | If the user making changes is the only user of the file, the NTFS file system writes a new USN record with the following flag setting: USN\_REASON\_DATA\_OVERWRITE \| USN\_REASON\_BASIC\_INFO\_CHANGE \| USN\_REASON\_DATA\_TRUNCATION \| USN\_REASON\_CLOSE.<br/> |



 

The change journal accumulates a series of records between the first opening and last closing of a file. Each record has a new reason flag set, indicating that a new kind of change has occurred. The sequence of records gives a partial history of the file. The final record, created when the file is closed, adds the USN\_REASON\_CLOSE flag. This record represents a summary of changes to the file, but unlike the prior records, gives no indication of the order of the changes.

The next user to access and change the file generates a new USN record with a single reason flag.

 

 




