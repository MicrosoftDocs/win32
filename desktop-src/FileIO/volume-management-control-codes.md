---
Description: Control codes used in volume management.
ms.assetid: 87f39e1c-3ebf-4c6f-a842-699ec3c45e76
title: Volume Management Control Codes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Volume Management Control Codes

Control codes used in volume management.

## In this section



| Topic                                                                                                                                      | Description                                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FSCTL\_CREATE\_USN\_JOURNAL**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                                 | Creates an update sequence number (USN) change journal stream on a target volume, or modifies an existing change journal stream.<br/>                                                                                                                               |
| [**FSCTL\_CSV\_QUERY\_DOWN\_LEVEL\_FILE\_SYSTEM\_CHARACTERISTICS**](/windows/win32/WinIoCtl/?branch=master)<br/> | Retrieves information about a file system for which CSVFS is a proxy.<br/>                                                                                                                                                                                          |
| [**FSCTL\_DELETE\_USN\_JOURNAL**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                                 | Deletes the update sequence number (USN) change journal on a volume, or waits for notification of change journal deletion.<br/>                                                                                                                                     |
| [**FSCTL\_DISMOUNT\_VOLUME**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                                        | Dismounts a volume regardless of whether or not the volume is currently in use. For more information, see the Remarks section.<br/>                                                                                                                                 |
| [**FSCTL\_ENUM\_USN\_DATA**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                                           | Enumerates the update sequence number (USN) data between two specified boundaries to obtain master file table (MFT) records.<br/>                                                                                                                                   |
| [**FSCTL\_EXTEND\_VOLUME**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                                            | Increases the size of a mounted volume.<br/>                                                                                                                                                                                                                        |
| [**FSCTL\_GET\_BOOT\_AREA\_INFO**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                                | Retrieves the locations of boot sectors for a volume. <br/> To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with the following parameters.<br/>                                                                      |
| [**FSCTL\_GET\_INTEGRITY\_INFORMATION**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                   | Retrieves the integrity status of a file or directory on a ReFS volume.<br/>                                                                                                                                                                                        |
| [**FSCTL\_GET\_NTFS\_VOLUME\_DATA**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                            | Retrieves information about the specified NTFS file system volume.<br/>                                                                                                                                                                                             |
| [**FSCTL\_GET\_RETRIEVAL\_POINTER\_BASE**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                | Returns the sector offset to the first logical cluster number (LCN) of the file system relative to the start of the volume.<br/> To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with the following parameters.<br/> |
| [**FSCTL\_GET\_RETRIEVAL\_POINTERS**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                         | Given a file handle, retrieves a data structure that describes the allocation and location on disk of a specific file, or, given a volume handle, the locations of bad clusters on a volume.<br/>                                                                   |
| [**FSCTL\_GET\_VOLUME\_BITMAP**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                                   | Retrieves a bitmap of occupied and available clusters on a volume.<br/>                                                                                                                                                                                             |
| [**FSCTL\_IS\_CSV\_FILE**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                                               | Determines whether a file is stored on a CSVFS volume, or retrieves namespace information.<br/>                                                                                                                                                                     |
| [**FSCTL\_IS\_FILE\_ON\_CSV\_VOLUME**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                         | Determines whether a file is stored on a CSVFS volume, or retrieves namespace information.<br/>                                                                                                                                                                     |
| [**FSCTL\_IS\_VOLUME\_MOUNTED**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                                   | Determines whether the specified volume is mounted, or if the specified file or directory is on a mounted volume.<br/>                                                                                                                                              |
| [**FSCTL\_IS\_VOLUME\_OWNED\_BYCSVFS**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                      | Determines whether a volume is locked by CSVFS.<br/>                                                                                                                                                                                                                |
| [**FSCTL\_LOCK\_VOLUME**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                                                | Locks a volume if it is not in use.<br/>                                                                                                                                                                                                                            |
| [**FSCTL\_LOOKUP\_STREAM\_FROM\_CLUSTER**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                | Given a handle to a NTFS volume or a file on a NTFS volume, returns a chain of data structures that describes streams that occupy the specified clusters.<br/>                                                                                                      |
| [**FSCTL\_MARK\_HANDLE**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                                                | Marks a specified file or directory and its change journal record with information about changes to that file or directory.<br/>                                                                                                                                    |
| [**FSCTL\_MOVE\_FILE**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                                                    | Relocates one or more virtual clusters of a file from one logical cluster to another within the same volume. This operation is used during [defragmentation](defragmenting-files.md).<br/>                                                                         |
| [**FSCTL\_QUERY\_FILE\_SYSTEM\_RECOGNITION**](/windows/win32/WinIoCtl/?branch=master)<br/>                                          | Queries for file system recognition information on a volume.<br/> To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with the following parameters.<br/>                                                                |
| [**FSCTL\_QUERY\_REGION\_INFO**](/windows/win32/WinIoctl/?branch=master)<br/>                                                                   | Retrieves the storage tier regions defined for a volume that supports data tiering.<br/> To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with the following parameters.<br/>                                         |
| [**FSCTL\_QUERY\_STORAGE\_CLASSES**](/windows/win32/WinIoctl/?branch=master)<br/>                                                           | Retrieves the storage tiers defined for a volume that supports data tiering.<br/> To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with the following parameters.<br/>                                                |
| [**FSCTL\_QUERY\_USN\_JOURNAL**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                                   | Queries for information on the current update sequence number (USN) change journal, its records, and its capacity.<br/>                                                                                                                                             |
| [**FSCTL\_READ\_FILE\_USN\_DATA**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                                | Retrieves the update sequence number (USN) change-journal information for the specified file or directory.<br/>                                                                                                                                                     |
| [**FSCTL\_READ\_FROM\_PLEX**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                                         | Reads from the specified plex.<br/>                                                                                                                                                                                                                                 |
| [**FSCTL\_READ\_USN\_JOURNAL**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                                     | Retrieves the set of update sequence number (USN) change journal records between two specified USN values.<br/>                                                                                                                                                     |
| [**FSCTL\_REPAIR\_COPIES**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                                            | Repair data corruption by selecting the proper copy to use.<br/>                                                                                                                                                                                                    |
| [**FSCTL\_SET\_INTEGRITY\_INFORMATION**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                   | Retrieves the integrity status of a file or directory on a ReFS volume.<br/>                                                                                                                                                                                        |
| [**FSCTL\_SHRINK\_VOLUME**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                                            | Signals that the volume is to be prepared to perform the shrink operation, the shrink operation is to be committed, or the shrink operation is to be terminated.<br/>                                                                                               |
| [**FSCTL\_UNLOCK\_VOLUME**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                                            | Unlocks a volume.<br/>                                                                                                                                                                                                                                              |
| [**FSCTL\_USN\_TRACK\_MODIFIED\_RANGES**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                  | Enables range tracking feature for update sequence number (USN) change journal stream on a target volume, or modifies already enabled range tracking parameters.<br/>                                                                                               |
| [**FSCTL\_WRITE\_USN\_CLOSE\_RECORD**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                        | Generates a record in the update sequence number (USN) change journal stream for the input file.<br/>                                                                                                                                                               |
| [**IOCTL\_VOLUME\_GET\_GPT\_ATTRIBUTES**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_volume_get_gpt_attributes?branch=master)<br/>                                                  | Retrieves the attributes for a volume.<br/> To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with the following parameters.<br/>                                                                                      |
| [**IOCTL\_VOLUME\_GET\_VOLUME\_DISK\_EXTENTS**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_volume_get_volume_disk_extents?branch=master)<br/>                                       | Retrieves the physical location of a specified volume on one or more disks.<br/>                                                                                                                                                                                    |
| [**IOCTL\_VOLUME\_IS\_CLUSTERED**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_volume_is_clustered?branch=master)<br/>                                                               | Determines whether the specified volume is clustered.<br/>                                                                                                                                                                                                          |
| [**IOCTL\_VOLUME\_IS\_CSV**](ioctl-volume-is-csv.md)<br/>                                                                           | Determines whether a volume is a CSV volume.<br/>                                                                                                                                                                                                                   |
| [**IOCTL\_VOLUME\_OFFLINE**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_volume_offline?branch=master)<br/>                                                                          | Takes a volume offline.<br/>                                                                                                                                                                                                                                        |
| [**IOCTL\_VOLUME\_ONLINE**](/windows/win32/WinIoCtl/ni-winioctl-ioctl_volume_online?branch=master)<br/>                                                                            | Brings a volume online.<br/>                                                                                                                                                                                                                                        |



 

The following control codes are used with [change journals](change-journals.md).

-   [**FSCTL\_CREATE\_USN\_JOURNAL**](/windows/win32/WinIoCtl/?branch=master)
-   [**FSCTL\_DELETE\_USN\_JOURNAL**](/windows/win32/WinIoCtl/?branch=master)
-   [**FSCTL\_ENUM\_USN\_DATA**](/windows/win32/WinIoCtl/?branch=master)
-   [**FSCTL\_MARK\_HANDLE**](/windows/win32/WinIoCtl/?branch=master)
-   [**FSCTL\_QUERY\_USN\_JOURNAL**](/windows/win32/WinIoCtl/?branch=master)
-   [**FSCTL\_READ\_FILE\_USN\_DATA**](/windows/win32/WinIoCtl/?branch=master)
-   [**FSCTL\_READ\_USN\_JOURNAL**](/windows/win32/WinIoCtl/?branch=master)
-   [**FSCTL\_WRITE\_USN\_CLOSE\_RECORD**](/windows/win32/WinIoCtl/?branch=master)

The following are [defragmentation](defragmenting-files.md) control codes.

-   [**FSCTL\_GET\_RETRIEVAL\_POINTER\_BASE**](/windows/win32/WinIoCtl/?branch=master)
-   [**FSCTL\_GET\_RETRIEVAL\_POINTERS**](/windows/win32/WinIoCtl/?branch=master)
-   [**FSCTL\_GET\_VOLUME\_BITMAP**](/windows/win32/WinIoCtl/?branch=master)
-   [**FSCTL\_LOOKUP\_STREAM\_FROM\_CLUSTER**](/windows/win32/WinIoCtl/?branch=master)
-   [**FSCTL\_MOVE\_FILE**](/windows/win32/WinIoCtl/?branch=master)
-   [**FSCTL\_QUERY\_REGION\_INFO**](/windows/win32/WinIoctl/?branch=master)
-   [**FSCTL\_QUERY\_USN\_JOURNAL**](/windows/win32/WinIoCtl/?branch=master)

## Related topics

<dl> <dt>

[Directory Management Control Codes](directory-management-control-codes.md)
</dt> <dt>

[File Management Control Codes](file-management-control-codes.md)
</dt> </dl>

 

 




