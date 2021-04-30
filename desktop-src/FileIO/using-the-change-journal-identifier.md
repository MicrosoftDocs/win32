---
description: The NTFS file system associates an unsigned 64-bit identifier with each change journal.
ms.assetid: 5ae79460-b69a-4901-a417-1d5358dcba29
title: Using the Change Journal Identifier
ms.topic: article
ms.date: 05/31/2018
---

# Using the Change Journal Identifier

The NTFS file system associates an unsigned 64-bit identifier with each change journal. The journal is stamped with this identifier when it is created. The file system stamps the journal with a new identifier where the existing update sequence number (USN) records either are or may be unusable.

For example, the NTFS file system restamps a change journal with a new identifier when a volume is moved from one version of NTFS to another and then back. Such a move can happen in a dual-boot environment or when working with removable media.

To obtain the identifier of the current change journal on a specified volume, use the [**FSCTL\_QUERY\_USN\_JOURNAL**](/windows/win32/api/winioctl/ni-winioctl-fsctl_query_usn_journal) control code. To perform this and all other change journal operations, you must have system administrator privileges. That is, you must be a member of the Administrators group.

When an administrator deletes and re-creates the change journal, for example when the current USN value approaches the maximum possible USN value, the USN values begin again from zero. When the NTFS file system stamps a journal with a new identifier rather than re-creating the journal, it does not reset the USN to zero but continues from the current USN. In either case, all existing USNs are less than any future USNs.

When you need information on a specific set of records, use the [**FSCTL\_QUERY\_USN\_JOURNAL**](/windows/win32/api/winioctl/ni-winioctl-fsctl_query_usn_journal) control code to obtain the change journal identifier. Then use the [**FSCTL\_READ\_USN\_JOURNAL**](/windows/win32/api/winioctl/ni-winioctl-fsctl_read_usn_journal) control code to read the journal records of interest. The NTFS file system only returns records that are valid for the journal specified by the identifier.

Your application needs both the records' USNs and the identifier to read the journal. This requirement provides an integrity check for cases where your application should ignore the existing records in the file and where records were written in previous instances of the journal for the same volume.

To obtain the records in which you are interested, you must start at the oldest record (that is, with the lowest USN) and scan forward until you locate the first record of interest.

 

 
