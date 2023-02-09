---
title: Change journal operations
description: Control codes and structures to use with the NTFS file system update sequence number (USN) change journal.
ms.assetid: 2215f0d4-6ac8-42a5-87a5-9c76d1fae3ed
ms.topic: article
ms.date: 02/09/2023
---

# Change journal operations

The following list identifies the control codes that work with the NTFS file system update sequence number (USN) change journal.

- [**FSCTL\_CREATE\_USN\_JOURNAL**](/windows/win32/api/winioctl/ni-winioctl-fsctl_create_usn_journal)
- [**FSCTL\_DELETE\_USN\_JOURNAL**](/windows/win32/api/winioctl/ni-winioctl-fsctl_delete_usn_journal)
- [**FSCTL\_ENUM\_USN\_DATA**](/windows/win32/api/winioctl/ni-winioctl-fsctl_enum_usn_data)
- [**FSCTL\_MARK\_HANDLE**](/windows/win32/api/winioctl/ni-winioctl-fsctl_mark_handle)
- [**FSCTL\_QUERY\_USN\_JOURNAL**](/windows/win32/api/winioctl/ni-winioctl-fsctl_query_usn_journal)
- [**FSCTL\_READ\_USN\_JOURNAL**](/windows/win32/api/winioctl/ni-winioctl-fsctl_read_usn_journal)

The following list identifies the structures information that relates to the NTFS file system USN change journal.

- [**CREATE\_USN\_JOURNAL\_DATA**](/windows/win32/api/WinIoCtl/ns-winioctl-create_usn_journal_data)
- [**DELETE\_USN\_JOURNAL\_DATA**](/windows/win32/api/WinIoCtl/ns-winioctl-delete_usn_journal_data)
- [**MARK\_HANDLE\_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-mark_handle_info)
- [**MFT\_ENUM\_DATA**](/windows/win32/api/WinIoCtl/ns-winioctl-mft_enum_data_v0)
- [**READ\_USN\_JOURNAL\_DATA**](/windows/win32/api/WinIoCtl/ns-winioctl-read_usn_journal_data_v0)
- [**USN\_JOURNAL\_DATA**](/windows/win32/api/WinIoCtl/ns-winioctl-usn_journal_data_v0)
- [**USN\_RECORD**](/windows/win32/api/WinIoCtl/ns-winioctl-usn_record_v2)
