---
description: Writers can fine-tune the performance of various types of backup at the file set level by indicating through a file specification backup type, indicated by a bit mask or bitwise OR of the members of the VSS\_FILE\_SPEC\_BACKUP\_TYPE enumeration.
ms.assetid: a3ac69b4-894a-4536-8fab-f45ad7e5118a
title: File Level Schema Support
ms.topic: article
ms.date: 05/31/2018
---

# File Level Schema Support

Writers can fine-tune the performance of various types of backup at the [*file set*](vssgloss-f.md) level by indicating through a file specification backup type, indicated by a bit mask or bitwise OR of the members of the [**VSS\_FILE\_SPEC\_BACKUP\_TYPE**](/windows/desktop/api/Vss/ne-vss-vss_file_spec_backup_type) enumeration.

For specified types of backup, the writer indicates the following:

-   Whether it will be necessary to shadow copy the volume to properly back up a file set. For instance, if the files in a file set are not exclusively opened by the writer and it can ensure that it is stable, a shadow copy is not needed.
-   Whether the requester has to perform the backup in such a way that, regardless of last modification time or other issues, the version of the file set's files current at backup will be restored. Typically, this means that the file set is copied as part of the backup.

The values of [**VSS\_FILE\_SPEC\_BACKUP\_TYPE**](/windows/desktop/api/Vss/ne-vss-vss_file_spec_backup_type) that indicate shadow copy requirement are:

-   VSS\_FSBT\_ALL\_SNAPSHOT\_REQUIRED
-   VSS\_FSBT\_FULL\_SNAPSHOT\_REQUIRED
-   VSS\_FSBT\_DIFFERENTIAL\_SNAPSHOT\_REQUIRED
-   VSS\_FSBT\_INCREMENTAL\_SNAPSHOT\_REQUIRED
-   VSS\_FSBT\_LOG\_SNAPSHOT\_REQUIRED

The values of [**VSS\_FILE\_SPEC\_BACKUP\_TYPE**](/windows/desktop/api/Vss/ne-vss-vss_file_spec_backup_type) that indicate the requirement to back up a file are:

-   VSS\_FSBT\_ALL\_BACKUP\_REQUIRED
-   VSS\_FSBT\_FULL\_BACKUP\_REQUIRED
-   VSS\_FSBT\_DIFFERENTIAL\_BACKUP\_REQUIRED
-   VSS\_FSBT\_INCREMENTAL\_BACKUP\_REQUIRED
-   VSS\_FSBT\_LOG\_BACKUP\_REQUIRED

By default, file sets are tagged with a file specification backup type of VSS\_FSBT\_ALL\_BACKUP\_REQUIRED \| VSS\_FSBT\_ALL\_SNAPSHOT\_REQUIRED, meaning that a shadow copy is always required in handling the file set's files, and that the files should be copied in all types of backup.

 

 



